# SNMP MIB module (SENSORBOX-WIFI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/sensorebox_43498/SENSORBOX-WIFI-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:57:10 2025
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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sensorbox = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43498)
)
if mibBuilder.loadTexts:
    sensorbox.setRevisions(
        ("2016-09-15 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SbTemperatureTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-400, 1250),
    )



class SbAddressTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class SbUmidityTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class SbStatus(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
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



class SbStatusRelay(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
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
          ("reset", 2))
    )



class SbStatusTamper(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("close", 0),
          ("open", 1))
    )



class SbACVoltage(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )



class SbDCVoltage(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )



class SbDCOffsetAdjustment(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )



class Sb420maTChundredths(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 2000),
    )



class Sb420maTCbits(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )



class SbResetTimeTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )



class SbAcVoltageValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 400),
    )



class SbFreqValue(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 80),
    )



class SbCurrentValue(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-1"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )



class SbPowerFactorValue(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )



class SbPowerValue(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-2"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )



# MIB Managed Objects in the order of their OIDs

_SbModules_ObjectIdentity = ObjectIdentity
sbModules = _SbModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1)
)
_SbModTemp_ObjectIdentity = ObjectIdentity
sbModTemp = _SbModTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1)
)
_SbTempP1_01_ObjectIdentity = ObjectIdentity
sbTempP1_01 = _SbTempP1_01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 1)
)
_SbModTempStatusP1_01_Type = SbStatus
_SbModTempStatusP1_01_Object = MibScalar
sbModTempStatusP1_01 = _SbModTempStatusP1_01_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 1, 1),
    _SbModTempStatusP1_01_Type()
)
sbModTempStatusP1_01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTempStatusP1_01.setStatus("current")
_SbModTempAddressP1_01_Type = SbAddressTC
_SbModTempAddressP1_01_Object = MibScalar
sbModTempAddressP1_01 = _SbModTempAddressP1_01_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 1, 2),
    _SbModTempAddressP1_01_Type()
)
sbModTempAddressP1_01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTempAddressP1_01.setStatus("current")
_SbModTempValueP1_01_Type = SbTemperatureTC
_SbModTempValueP1_01_Object = MibScalar
sbModTempValueP1_01 = _SbModTempValueP1_01_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 1, 3),
    _SbModTempValueP1_01_Type()
)
sbModTempValueP1_01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTempValueP1_01.setStatus("current")
_SbModTempAlarmMinP1_01_Type = SbTemperatureTC
_SbModTempAlarmMinP1_01_Object = MibScalar
sbModTempAlarmMinP1_01 = _SbModTempAlarmMinP1_01_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 1, 4),
    _SbModTempAlarmMinP1_01_Type()
)
sbModTempAlarmMinP1_01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTempAlarmMinP1_01.setStatus("current")
_SbModTempAlarmMaxP1_01_Type = SbTemperatureTC
_SbModTempAlarmMaxP1_01_Object = MibScalar
sbModTempAlarmMaxP1_01 = _SbModTempAlarmMaxP1_01_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 1, 5),
    _SbModTempAlarmMaxP1_01_Type()
)
sbModTempAlarmMaxP1_01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTempAlarmMaxP1_01.setStatus("current")
_SbTempP1_02_ObjectIdentity = ObjectIdentity
sbTempP1_02 = _SbTempP1_02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 2)
)
_SbModTempStatusP1_02_Type = SbStatus
_SbModTempStatusP1_02_Object = MibScalar
sbModTempStatusP1_02 = _SbModTempStatusP1_02_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 2, 1),
    _SbModTempStatusP1_02_Type()
)
sbModTempStatusP1_02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTempStatusP1_02.setStatus("current")
_SbModTempAddressP1_02_Type = SbAddressTC
_SbModTempAddressP1_02_Object = MibScalar
sbModTempAddressP1_02 = _SbModTempAddressP1_02_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 2, 2),
    _SbModTempAddressP1_02_Type()
)
sbModTempAddressP1_02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTempAddressP1_02.setStatus("current")
_SbModTempValueP1_02_Type = SbTemperatureTC
_SbModTempValueP1_02_Object = MibScalar
sbModTempValueP1_02 = _SbModTempValueP1_02_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 2, 3),
    _SbModTempValueP1_02_Type()
)
sbModTempValueP1_02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTempValueP1_02.setStatus("current")
_SbModTempAlarmMinP1_02_Type = SbTemperatureTC
_SbModTempAlarmMinP1_02_Object = MibScalar
sbModTempAlarmMinP1_02 = _SbModTempAlarmMinP1_02_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 2, 4),
    _SbModTempAlarmMinP1_02_Type()
)
sbModTempAlarmMinP1_02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTempAlarmMinP1_02.setStatus("current")
_SbModTempAlarmMaxP1_02_Type = SbTemperatureTC
_SbModTempAlarmMaxP1_02_Object = MibScalar
sbModTempAlarmMaxP1_02 = _SbModTempAlarmMaxP1_02_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 2, 5),
    _SbModTempAlarmMaxP1_02_Type()
)
sbModTempAlarmMaxP1_02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTempAlarmMaxP1_02.setStatus("current")
_SbTempP1_03_ObjectIdentity = ObjectIdentity
sbTempP1_03 = _SbTempP1_03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 3)
)
_SbModTempStatusP1_03_Type = SbStatus
_SbModTempStatusP1_03_Object = MibScalar
sbModTempStatusP1_03 = _SbModTempStatusP1_03_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 3, 1),
    _SbModTempStatusP1_03_Type()
)
sbModTempStatusP1_03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTempStatusP1_03.setStatus("current")
_SbModTempAddressP1_03_Type = SbAddressTC
_SbModTempAddressP1_03_Object = MibScalar
sbModTempAddressP1_03 = _SbModTempAddressP1_03_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 3, 2),
    _SbModTempAddressP1_03_Type()
)
sbModTempAddressP1_03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTempAddressP1_03.setStatus("current")
_SbModTempValueP1_03_Type = SbTemperatureTC
_SbModTempValueP1_03_Object = MibScalar
sbModTempValueP1_03 = _SbModTempValueP1_03_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 3, 3),
    _SbModTempValueP1_03_Type()
)
sbModTempValueP1_03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTempValueP1_03.setStatus("current")
_SbModTempAlarmMinP1_03_Type = SbTemperatureTC
_SbModTempAlarmMinP1_03_Object = MibScalar
sbModTempAlarmMinP1_03 = _SbModTempAlarmMinP1_03_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 3, 4),
    _SbModTempAlarmMinP1_03_Type()
)
sbModTempAlarmMinP1_03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTempAlarmMinP1_03.setStatus("current")
_SbModTempAlarmMaxP1_03_Type = SbTemperatureTC
_SbModTempAlarmMaxP1_03_Object = MibScalar
sbModTempAlarmMaxP1_03 = _SbModTempAlarmMaxP1_03_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 3, 5),
    _SbModTempAlarmMaxP1_03_Type()
)
sbModTempAlarmMaxP1_03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTempAlarmMaxP1_03.setStatus("current")
_SbTempP1_04_ObjectIdentity = ObjectIdentity
sbTempP1_04 = _SbTempP1_04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 4)
)
_SbModTempStatusP1_04_Type = SbStatus
_SbModTempStatusP1_04_Object = MibScalar
sbModTempStatusP1_04 = _SbModTempStatusP1_04_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 4, 1),
    _SbModTempStatusP1_04_Type()
)
sbModTempStatusP1_04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTempStatusP1_04.setStatus("current")
_SbModTempAddressP1_04_Type = SbAddressTC
_SbModTempAddressP1_04_Object = MibScalar
sbModTempAddressP1_04 = _SbModTempAddressP1_04_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 4, 2),
    _SbModTempAddressP1_04_Type()
)
sbModTempAddressP1_04.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTempAddressP1_04.setStatus("current")
_SbModTempValueP1_04_Type = SbTemperatureTC
_SbModTempValueP1_04_Object = MibScalar
sbModTempValueP1_04 = _SbModTempValueP1_04_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 4, 3),
    _SbModTempValueP1_04_Type()
)
sbModTempValueP1_04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTempValueP1_04.setStatus("current")
_SbModTempAlarmMinP1_04_Type = SbTemperatureTC
_SbModTempAlarmMinP1_04_Object = MibScalar
sbModTempAlarmMinP1_04 = _SbModTempAlarmMinP1_04_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 4, 4),
    _SbModTempAlarmMinP1_04_Type()
)
sbModTempAlarmMinP1_04.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTempAlarmMinP1_04.setStatus("current")
_SbModTempAlarmMaxP1_04_Type = SbTemperatureTC
_SbModTempAlarmMaxP1_04_Object = MibScalar
sbModTempAlarmMaxP1_04 = _SbModTempAlarmMaxP1_04_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 4, 5),
    _SbModTempAlarmMaxP1_04_Type()
)
sbModTempAlarmMaxP1_04.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTempAlarmMaxP1_04.setStatus("current")
_SbTempP2_01_ObjectIdentity = ObjectIdentity
sbTempP2_01 = _SbTempP2_01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 5)
)
_SbModTempStatusP2_01_Type = SbStatus
_SbModTempStatusP2_01_Object = MibScalar
sbModTempStatusP2_01 = _SbModTempStatusP2_01_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 5, 1),
    _SbModTempStatusP2_01_Type()
)
sbModTempStatusP2_01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTempStatusP2_01.setStatus("current")
_SbModTempAddressP2_01_Type = SbAddressTC
_SbModTempAddressP2_01_Object = MibScalar
sbModTempAddressP2_01 = _SbModTempAddressP2_01_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 5, 2),
    _SbModTempAddressP2_01_Type()
)
sbModTempAddressP2_01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTempAddressP2_01.setStatus("current")
_SbModTempValueP2_01_Type = SbTemperatureTC
_SbModTempValueP2_01_Object = MibScalar
sbModTempValueP2_01 = _SbModTempValueP2_01_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 5, 3),
    _SbModTempValueP2_01_Type()
)
sbModTempValueP2_01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTempValueP2_01.setStatus("current")
_SbModTempAlarmMinP2_01_Type = SbTemperatureTC
_SbModTempAlarmMinP2_01_Object = MibScalar
sbModTempAlarmMinP2_01 = _SbModTempAlarmMinP2_01_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 5, 4),
    _SbModTempAlarmMinP2_01_Type()
)
sbModTempAlarmMinP2_01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTempAlarmMinP2_01.setStatus("current")
_SbModTempAlarmMaxP2_01_Type = SbTemperatureTC
_SbModTempAlarmMaxP2_01_Object = MibScalar
sbModTempAlarmMaxP2_01 = _SbModTempAlarmMaxP2_01_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 5, 5),
    _SbModTempAlarmMaxP2_01_Type()
)
sbModTempAlarmMaxP2_01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTempAlarmMaxP2_01.setStatus("current")
_SbTempP2_02_ObjectIdentity = ObjectIdentity
sbTempP2_02 = _SbTempP2_02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 6)
)
_SbModTempStatusP2_02_Type = SbStatus
_SbModTempStatusP2_02_Object = MibScalar
sbModTempStatusP2_02 = _SbModTempStatusP2_02_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 6, 1),
    _SbModTempStatusP2_02_Type()
)
sbModTempStatusP2_02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTempStatusP2_02.setStatus("current")
_SbModTempAddressP2_02_Type = SbAddressTC
_SbModTempAddressP2_02_Object = MibScalar
sbModTempAddressP2_02 = _SbModTempAddressP2_02_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 6, 2),
    _SbModTempAddressP2_02_Type()
)
sbModTempAddressP2_02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTempAddressP2_02.setStatus("current")
_SbModTempValueP2_02_Type = SbTemperatureTC
_SbModTempValueP2_02_Object = MibScalar
sbModTempValueP2_02 = _SbModTempValueP2_02_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 6, 3),
    _SbModTempValueP2_02_Type()
)
sbModTempValueP2_02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTempValueP2_02.setStatus("current")
_SbModTempAlarmMinP2_02_Type = SbTemperatureTC
_SbModTempAlarmMinP2_02_Object = MibScalar
sbModTempAlarmMinP2_02 = _SbModTempAlarmMinP2_02_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 6, 4),
    _SbModTempAlarmMinP2_02_Type()
)
sbModTempAlarmMinP2_02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTempAlarmMinP2_02.setStatus("current")
_SbModTempAlarmMaxP2_02_Type = SbTemperatureTC
_SbModTempAlarmMaxP2_02_Object = MibScalar
sbModTempAlarmMaxP2_02 = _SbModTempAlarmMaxP2_02_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 6, 5),
    _SbModTempAlarmMaxP2_02_Type()
)
sbModTempAlarmMaxP2_02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTempAlarmMaxP2_02.setStatus("current")
_SbTempP2_03_ObjectIdentity = ObjectIdentity
sbTempP2_03 = _SbTempP2_03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 7)
)
_SbModTempStatusP2_03_Type = SbStatus
_SbModTempStatusP2_03_Object = MibScalar
sbModTempStatusP2_03 = _SbModTempStatusP2_03_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 7, 1),
    _SbModTempStatusP2_03_Type()
)
sbModTempStatusP2_03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTempStatusP2_03.setStatus("current")
_SbModTempAddressP2_03_Type = SbAddressTC
_SbModTempAddressP2_03_Object = MibScalar
sbModTempAddressP2_03 = _SbModTempAddressP2_03_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 7, 2),
    _SbModTempAddressP2_03_Type()
)
sbModTempAddressP2_03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTempAddressP2_03.setStatus("current")
_SbModTempValueP2_03_Type = SbTemperatureTC
_SbModTempValueP2_03_Object = MibScalar
sbModTempValueP2_03 = _SbModTempValueP2_03_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 7, 3),
    _SbModTempValueP2_03_Type()
)
sbModTempValueP2_03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTempValueP2_03.setStatus("current")
_SbModTempAlarmMinP2_03_Type = SbTemperatureTC
_SbModTempAlarmMinP2_03_Object = MibScalar
sbModTempAlarmMinP2_03 = _SbModTempAlarmMinP2_03_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 7, 4),
    _SbModTempAlarmMinP2_03_Type()
)
sbModTempAlarmMinP2_03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTempAlarmMinP2_03.setStatus("current")
_SbModTempAlarmMaxP2_03_Type = SbTemperatureTC
_SbModTempAlarmMaxP2_03_Object = MibScalar
sbModTempAlarmMaxP2_03 = _SbModTempAlarmMaxP2_03_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 7, 5),
    _SbModTempAlarmMaxP2_03_Type()
)
sbModTempAlarmMaxP2_03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTempAlarmMaxP2_03.setStatus("current")
_SbTempP2_04_ObjectIdentity = ObjectIdentity
sbTempP2_04 = _SbTempP2_04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 8)
)
_SbModTempStatusP2_04_Type = SbStatus
_SbModTempStatusP2_04_Object = MibScalar
sbModTempStatusP2_04 = _SbModTempStatusP2_04_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 8, 1),
    _SbModTempStatusP2_04_Type()
)
sbModTempStatusP2_04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTempStatusP2_04.setStatus("current")
_SbModTempAddressP2_04_Type = SbAddressTC
_SbModTempAddressP2_04_Object = MibScalar
sbModTempAddressP2_04 = _SbModTempAddressP2_04_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 8, 2),
    _SbModTempAddressP2_04_Type()
)
sbModTempAddressP2_04.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTempAddressP2_04.setStatus("current")
_SbModTempValueP2_04_Type = SbTemperatureTC
_SbModTempValueP2_04_Object = MibScalar
sbModTempValueP2_04 = _SbModTempValueP2_04_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 8, 3),
    _SbModTempValueP2_04_Type()
)
sbModTempValueP2_04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTempValueP2_04.setStatus("current")
_SbModTempAlarmMinP2_04_Type = SbTemperatureTC
_SbModTempAlarmMinP2_04_Object = MibScalar
sbModTempAlarmMinP2_04 = _SbModTempAlarmMinP2_04_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 8, 4),
    _SbModTempAlarmMinP2_04_Type()
)
sbModTempAlarmMinP2_04.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTempAlarmMinP2_04.setStatus("current")
_SbModTempAlarmMaxP2_04_Type = SbTemperatureTC
_SbModTempAlarmMaxP2_04_Object = MibScalar
sbModTempAlarmMaxP2_04 = _SbModTempAlarmMaxP2_04_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 1, 8, 5),
    _SbModTempAlarmMaxP2_04_Type()
)
sbModTempAlarmMaxP2_04.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTempAlarmMaxP2_04.setStatus("current")
_SbModTempHum_ObjectIdentity = ObjectIdentity
sbModTempHum = _SbModTempHum_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2)
)
_SbTempHumP1_ObjectIdentity = ObjectIdentity
sbTempHumP1 = _SbTempHumP1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 1)
)
_SbModTHStatus_P1_Type = SbStatus
_SbModTHStatus_P1_Object = MibScalar
sbModTHStatus_P1 = _SbModTHStatus_P1_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 1, 1),
    _SbModTHStatus_P1_Type()
)
sbModTHStatus_P1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTHStatus_P1.setStatus("current")
_SbModTHValueTemp_P1_Type = SbTemperatureTC
_SbModTHValueTemp_P1_Object = MibScalar
sbModTHValueTemp_P1 = _SbModTHValueTemp_P1_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 1, 2),
    _SbModTHValueTemp_P1_Type()
)
sbModTHValueTemp_P1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTHValueTemp_P1.setStatus("current")
_SbModTHAlarmTempMin_P1_Type = SbTemperatureTC
_SbModTHAlarmTempMin_P1_Object = MibScalar
sbModTHAlarmTempMin_P1 = _SbModTHAlarmTempMin_P1_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 1, 3),
    _SbModTHAlarmTempMin_P1_Type()
)
sbModTHAlarmTempMin_P1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTHAlarmTempMin_P1.setStatus("current")
_SbModTHAlarmTempMax_P1_Type = SbTemperatureTC
_SbModTHAlarmTempMax_P1_Object = MibScalar
sbModTHAlarmTempMax_P1 = _SbModTHAlarmTempMax_P1_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 1, 4),
    _SbModTHAlarmTempMax_P1_Type()
)
sbModTHAlarmTempMax_P1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTHAlarmTempMax_P1.setStatus("current")
_SbModTHValueHum_P1_Type = SbUmidityTC
_SbModTHValueHum_P1_Object = MibScalar
sbModTHValueHum_P1 = _SbModTHValueHum_P1_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 1, 5),
    _SbModTHValueHum_P1_Type()
)
sbModTHValueHum_P1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTHValueHum_P1.setStatus("current")
_SbModTHAlarmHumMin_P1_Type = SbUmidityTC
_SbModTHAlarmHumMin_P1_Object = MibScalar
sbModTHAlarmHumMin_P1 = _SbModTHAlarmHumMin_P1_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 1, 6),
    _SbModTHAlarmHumMin_P1_Type()
)
sbModTHAlarmHumMin_P1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTHAlarmHumMin_P1.setStatus("current")
_SbModTHAlarmHumMax_P1_Type = SbUmidityTC
_SbModTHAlarmHumMax_P1_Object = MibScalar
sbModTHAlarmHumMax_P1 = _SbModTHAlarmHumMax_P1_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 1, 7),
    _SbModTHAlarmHumMax_P1_Type()
)
sbModTHAlarmHumMax_P1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTHAlarmHumMax_P1.setStatus("current")
_SbTempHumP2_ObjectIdentity = ObjectIdentity
sbTempHumP2 = _SbTempHumP2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 2)
)
_SbModTHStatus_P2_Type = SbStatus
_SbModTHStatus_P2_Object = MibScalar
sbModTHStatus_P2 = _SbModTHStatus_P2_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 2, 1),
    _SbModTHStatus_P2_Type()
)
sbModTHStatus_P2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTHStatus_P2.setStatus("current")
_SbModTHValueTemp_P2_Type = SbTemperatureTC
_SbModTHValueTemp_P2_Object = MibScalar
sbModTHValueTemp_P2 = _SbModTHValueTemp_P2_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 2, 2),
    _SbModTHValueTemp_P2_Type()
)
sbModTHValueTemp_P2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTHValueTemp_P2.setStatus("current")
_SbModTHAlarmTempMin_P2_Type = SbTemperatureTC
_SbModTHAlarmTempMin_P2_Object = MibScalar
sbModTHAlarmTempMin_P2 = _SbModTHAlarmTempMin_P2_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 2, 3),
    _SbModTHAlarmTempMin_P2_Type()
)
sbModTHAlarmTempMin_P2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTHAlarmTempMin_P2.setStatus("current")
_SbModTHAlarmTempMax_P2_Type = SbTemperatureTC
_SbModTHAlarmTempMax_P2_Object = MibScalar
sbModTHAlarmTempMax_P2 = _SbModTHAlarmTempMax_P2_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 2, 4),
    _SbModTHAlarmTempMax_P2_Type()
)
sbModTHAlarmTempMax_P2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTHAlarmTempMax_P2.setStatus("current")
_SbModTHValueHum_P2_Type = SbUmidityTC
_SbModTHValueHum_P2_Object = MibScalar
sbModTHValueHum_P2 = _SbModTHValueHum_P2_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 2, 5),
    _SbModTHValueHum_P2_Type()
)
sbModTHValueHum_P2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTHValueHum_P2.setStatus("current")
_SbModTHAlarmHumMin_P2_Type = SbUmidityTC
_SbModTHAlarmHumMin_P2_Object = MibScalar
sbModTHAlarmHumMin_P2 = _SbModTHAlarmHumMin_P2_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 2, 6),
    _SbModTHAlarmHumMin_P2_Type()
)
sbModTHAlarmHumMin_P2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTHAlarmHumMin_P2.setStatus("current")
_SbModTHAlarmHumMax_P2_Type = SbUmidityTC
_SbModTHAlarmHumMax_P2_Object = MibScalar
sbModTHAlarmHumMax_P2 = _SbModTHAlarmHumMax_P2_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 2, 7),
    _SbModTHAlarmHumMax_P2_Type()
)
sbModTHAlarmHumMax_P2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTHAlarmHumMax_P2.setStatus("current")
_SbTempHumExtern01_ObjectIdentity = ObjectIdentity
sbTempHumExtern01 = _SbTempHumExtern01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 3)
)
_SbModTHStatus_Ext01_Type = SbStatus
_SbModTHStatus_Ext01_Object = MibScalar
sbModTHStatus_Ext01 = _SbModTHStatus_Ext01_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 3, 1),
    _SbModTHStatus_Ext01_Type()
)
sbModTHStatus_Ext01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTHStatus_Ext01.setStatus("current")
_SbModTHValueTemp_Ext01_Type = SbTemperatureTC
_SbModTHValueTemp_Ext01_Object = MibScalar
sbModTHValueTemp_Ext01 = _SbModTHValueTemp_Ext01_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 3, 2),
    _SbModTHValueTemp_Ext01_Type()
)
sbModTHValueTemp_Ext01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTHValueTemp_Ext01.setStatus("current")
_SbModTHAlarmTempMin_Ext01_Type = SbTemperatureTC
_SbModTHAlarmTempMin_Ext01_Object = MibScalar
sbModTHAlarmTempMin_Ext01 = _SbModTHAlarmTempMin_Ext01_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 3, 3),
    _SbModTHAlarmTempMin_Ext01_Type()
)
sbModTHAlarmTempMin_Ext01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTHAlarmTempMin_Ext01.setStatus("current")
_SbModTHAlarmTempMax_Ext01_Type = SbTemperatureTC
_SbModTHAlarmTempMax_Ext01_Object = MibScalar
sbModTHAlarmTempMax_Ext01 = _SbModTHAlarmTempMax_Ext01_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 3, 4),
    _SbModTHAlarmTempMax_Ext01_Type()
)
sbModTHAlarmTempMax_Ext01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTHAlarmTempMax_Ext01.setStatus("current")
_SbModTHValueHum_Ext01_Type = SbUmidityTC
_SbModTHValueHum_Ext01_Object = MibScalar
sbModTHValueHum_Ext01 = _SbModTHValueHum_Ext01_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 3, 5),
    _SbModTHValueHum_Ext01_Type()
)
sbModTHValueHum_Ext01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTHValueHum_Ext01.setStatus("current")
_SbModTHAlarmHumMin_Ext01_Type = SbUmidityTC
_SbModTHAlarmHumMin_Ext01_Object = MibScalar
sbModTHAlarmHumMin_Ext01 = _SbModTHAlarmHumMin_Ext01_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 3, 6),
    _SbModTHAlarmHumMin_Ext01_Type()
)
sbModTHAlarmHumMin_Ext01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTHAlarmHumMin_Ext01.setStatus("current")
_SbModTHAlarmHumMax_Ext01_Type = SbUmidityTC
_SbModTHAlarmHumMax_Ext01_Object = MibScalar
sbModTHAlarmHumMax_Ext01 = _SbModTHAlarmHumMax_Ext01_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 3, 7),
    _SbModTHAlarmHumMax_Ext01_Type()
)
sbModTHAlarmHumMax_Ext01.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTHAlarmHumMax_Ext01.setStatus("current")
_SbTempHumExtern02_ObjectIdentity = ObjectIdentity
sbTempHumExtern02 = _SbTempHumExtern02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 4)
)
_SbModTHStatus_Ext02_Type = SbStatus
_SbModTHStatus_Ext02_Object = MibScalar
sbModTHStatus_Ext02 = _SbModTHStatus_Ext02_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 4, 1),
    _SbModTHStatus_Ext02_Type()
)
sbModTHStatus_Ext02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTHStatus_Ext02.setStatus("current")
_SbModTHValueTemp_Ext02_Type = SbTemperatureTC
_SbModTHValueTemp_Ext02_Object = MibScalar
sbModTHValueTemp_Ext02 = _SbModTHValueTemp_Ext02_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 4, 2),
    _SbModTHValueTemp_Ext02_Type()
)
sbModTHValueTemp_Ext02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTHValueTemp_Ext02.setStatus("current")
_SbModTHAlarmTempMin_Ext02_Type = SbTemperatureTC
_SbModTHAlarmTempMin_Ext02_Object = MibScalar
sbModTHAlarmTempMin_Ext02 = _SbModTHAlarmTempMin_Ext02_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 4, 3),
    _SbModTHAlarmTempMin_Ext02_Type()
)
sbModTHAlarmTempMin_Ext02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTHAlarmTempMin_Ext02.setStatus("current")
_SbModTHAlarmTempMax_Ext02_Type = SbTemperatureTC
_SbModTHAlarmTempMax_Ext02_Object = MibScalar
sbModTHAlarmTempMax_Ext02 = _SbModTHAlarmTempMax_Ext02_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 4, 4),
    _SbModTHAlarmTempMax_Ext02_Type()
)
sbModTHAlarmTempMax_Ext02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTHAlarmTempMax_Ext02.setStatus("current")
_SbModTHValueHum_Ext02_Type = SbUmidityTC
_SbModTHValueHum_Ext02_Object = MibScalar
sbModTHValueHum_Ext02 = _SbModTHValueHum_Ext02_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 4, 5),
    _SbModTHValueHum_Ext02_Type()
)
sbModTHValueHum_Ext02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTHValueHum_Ext02.setStatus("current")
_SbModTHAlarmHumMin_Ext02_Type = SbUmidityTC
_SbModTHAlarmHumMin_Ext02_Object = MibScalar
sbModTHAlarmHumMin_Ext02 = _SbModTHAlarmHumMin_Ext02_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 4, 6),
    _SbModTHAlarmHumMin_Ext02_Type()
)
sbModTHAlarmHumMin_Ext02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTHAlarmHumMin_Ext02.setStatus("current")
_SbModTHAlarmHumMax_Ext02_Type = SbUmidityTC
_SbModTHAlarmHumMax_Ext02_Object = MibScalar
sbModTHAlarmHumMax_Ext02 = _SbModTHAlarmHumMax_Ext02_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 4, 7),
    _SbModTHAlarmHumMax_Ext02_Type()
)
sbModTHAlarmHumMax_Ext02.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTHAlarmHumMax_Ext02.setStatus("current")
_SbTempHumExtern03_ObjectIdentity = ObjectIdentity
sbTempHumExtern03 = _SbTempHumExtern03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 5)
)
_SbModTHStatus_Ext03_Type = SbStatus
_SbModTHStatus_Ext03_Object = MibScalar
sbModTHStatus_Ext03 = _SbModTHStatus_Ext03_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 5, 1),
    _SbModTHStatus_Ext03_Type()
)
sbModTHStatus_Ext03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTHStatus_Ext03.setStatus("current")
_SbModTHValueTemp_Ext03_Type = SbTemperatureTC
_SbModTHValueTemp_Ext03_Object = MibScalar
sbModTHValueTemp_Ext03 = _SbModTHValueTemp_Ext03_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 5, 2),
    _SbModTHValueTemp_Ext03_Type()
)
sbModTHValueTemp_Ext03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTHValueTemp_Ext03.setStatus("current")
_SbModTHAlarmTempMin_Ext03_Type = SbTemperatureTC
_SbModTHAlarmTempMin_Ext03_Object = MibScalar
sbModTHAlarmTempMin_Ext03 = _SbModTHAlarmTempMin_Ext03_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 5, 3),
    _SbModTHAlarmTempMin_Ext03_Type()
)
sbModTHAlarmTempMin_Ext03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTHAlarmTempMin_Ext03.setStatus("current")
_SbModTHAlarmTempMax_Ext03_Type = SbTemperatureTC
_SbModTHAlarmTempMax_Ext03_Object = MibScalar
sbModTHAlarmTempMax_Ext03 = _SbModTHAlarmTempMax_Ext03_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 5, 4),
    _SbModTHAlarmTempMax_Ext03_Type()
)
sbModTHAlarmTempMax_Ext03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTHAlarmTempMax_Ext03.setStatus("current")
_SbModTHValueHum_Ext03_Type = SbUmidityTC
_SbModTHValueHum_Ext03_Object = MibScalar
sbModTHValueHum_Ext03 = _SbModTHValueHum_Ext03_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 5, 5),
    _SbModTHValueHum_Ext03_Type()
)
sbModTHValueHum_Ext03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTHValueHum_Ext03.setStatus("current")
_SbModTHAlarmHumMin_Ext03_Type = SbUmidityTC
_SbModTHAlarmHumMin_Ext03_Object = MibScalar
sbModTHAlarmHumMin_Ext03 = _SbModTHAlarmHumMin_Ext03_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 5, 6),
    _SbModTHAlarmHumMin_Ext03_Type()
)
sbModTHAlarmHumMin_Ext03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTHAlarmHumMin_Ext03.setStatus("current")
_SbModTHAlarmHumMax_Ext03_Type = SbUmidityTC
_SbModTHAlarmHumMax_Ext03_Object = MibScalar
sbModTHAlarmHumMax_Ext03 = _SbModTHAlarmHumMax_Ext03_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 5, 7),
    _SbModTHAlarmHumMax_Ext03_Type()
)
sbModTHAlarmHumMax_Ext03.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTHAlarmHumMax_Ext03.setStatus("current")
_SbTempHumExtern04_ObjectIdentity = ObjectIdentity
sbTempHumExtern04 = _SbTempHumExtern04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 6)
)
_SbModTHStatus_Ext04_Type = SbStatus
_SbModTHStatus_Ext04_Object = MibScalar
sbModTHStatus_Ext04 = _SbModTHStatus_Ext04_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 6, 1),
    _SbModTHStatus_Ext04_Type()
)
sbModTHStatus_Ext04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTHStatus_Ext04.setStatus("current")
_SbModTHValueTemp_Ext04_Type = SbTemperatureTC
_SbModTHValueTemp_Ext04_Object = MibScalar
sbModTHValueTemp_Ext04 = _SbModTHValueTemp_Ext04_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 6, 2),
    _SbModTHValueTemp_Ext04_Type()
)
sbModTHValueTemp_Ext04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTHValueTemp_Ext04.setStatus("current")
_SbModTHAlarmTempMin_Ext04_Type = SbTemperatureTC
_SbModTHAlarmTempMin_Ext04_Object = MibScalar
sbModTHAlarmTempMin_Ext04 = _SbModTHAlarmTempMin_Ext04_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 6, 3),
    _SbModTHAlarmTempMin_Ext04_Type()
)
sbModTHAlarmTempMin_Ext04.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTHAlarmTempMin_Ext04.setStatus("current")
_SbModTHAlarmTempMax_Ext04_Type = SbTemperatureTC
_SbModTHAlarmTempMax_Ext04_Object = MibScalar
sbModTHAlarmTempMax_Ext04 = _SbModTHAlarmTempMax_Ext04_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 6, 4),
    _SbModTHAlarmTempMax_Ext04_Type()
)
sbModTHAlarmTempMax_Ext04.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTHAlarmTempMax_Ext04.setStatus("current")
_SbModTHValueHum_Ext04_Type = SbUmidityTC
_SbModTHValueHum_Ext04_Object = MibScalar
sbModTHValueHum_Ext04 = _SbModTHValueHum_Ext04_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 6, 5),
    _SbModTHValueHum_Ext04_Type()
)
sbModTHValueHum_Ext04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTHValueHum_Ext04.setStatus("current")
_SbModTHAlarmHumMin_Ext04_Type = SbUmidityTC
_SbModTHAlarmHumMin_Ext04_Object = MibScalar
sbModTHAlarmHumMin_Ext04 = _SbModTHAlarmHumMin_Ext04_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 6, 6),
    _SbModTHAlarmHumMin_Ext04_Type()
)
sbModTHAlarmHumMin_Ext04.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTHAlarmHumMin_Ext04.setStatus("current")
_SbModTHAlarmHumMax_Ext04_Type = SbUmidityTC
_SbModTHAlarmHumMax_Ext04_Object = MibScalar
sbModTHAlarmHumMax_Ext04 = _SbModTHAlarmHumMax_Ext04_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 2, 6, 7),
    _SbModTHAlarmHumMax_Ext04_Type()
)
sbModTHAlarmHumMax_Ext04.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModTHAlarmHumMax_Ext04.setStatus("current")
_SbModAC_ObjectIdentity = ObjectIdentity
sbModAC = _SbModAC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 3)
)
_SbModAC01_ObjectIdentity = ObjectIdentity
sbModAC01 = _SbModAC01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 3, 1)
)
_SbModAC01Status_Type = SbStatus
_SbModAC01Status_Object = MibScalar
sbModAC01Status = _SbModAC01Status_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 3, 1, 1),
    _SbModAC01Status_Type()
)
sbModAC01Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModAC01Status.setStatus("current")
_SbModAC01Value_Type = SbACVoltage
_SbModAC01Value_Object = MibScalar
sbModAC01Value = _SbModAC01Value_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 3, 1, 2),
    _SbModAC01Value_Type()
)
sbModAC01Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModAC01Value.setStatus("current")
_SbModAC01AlarmMin_Type = SbACVoltage
_SbModAC01AlarmMin_Object = MibScalar
sbModAC01AlarmMin = _SbModAC01AlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 3, 1, 3),
    _SbModAC01AlarmMin_Type()
)
sbModAC01AlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModAC01AlarmMin.setStatus("current")
_SbModAC01AlarmMax_Type = SbACVoltage
_SbModAC01AlarmMax_Object = MibScalar
sbModAC01AlarmMax = _SbModAC01AlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 3, 1, 4),
    _SbModAC01AlarmMax_Type()
)
sbModAC01AlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModAC01AlarmMax.setStatus("current")
_SbModAC02_ObjectIdentity = ObjectIdentity
sbModAC02 = _SbModAC02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 3, 2)
)
_SbModAC02Status_Type = SbStatus
_SbModAC02Status_Object = MibScalar
sbModAC02Status = _SbModAC02Status_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 3, 2, 1),
    _SbModAC02Status_Type()
)
sbModAC02Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModAC02Status.setStatus("current")
_SbModAC02Value_Type = SbACVoltage
_SbModAC02Value_Object = MibScalar
sbModAC02Value = _SbModAC02Value_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 3, 2, 2),
    _SbModAC02Value_Type()
)
sbModAC02Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModAC02Value.setStatus("current")
_SbModAC02AlarmMin_Type = SbACVoltage
_SbModAC02AlarmMin_Object = MibScalar
sbModAC02AlarmMin = _SbModAC02AlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 3, 2, 3),
    _SbModAC02AlarmMin_Type()
)
sbModAC02AlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModAC02AlarmMin.setStatus("current")
_SbModAC02AlarmMax_Type = SbACVoltage
_SbModAC02AlarmMax_Object = MibScalar
sbModAC02AlarmMax = _SbModAC02AlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 3, 2, 4),
    _SbModAC02AlarmMax_Type()
)
sbModAC02AlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModAC02AlarmMax.setStatus("current")
_SbModAC03_ObjectIdentity = ObjectIdentity
sbModAC03 = _SbModAC03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 3, 3)
)
_SbModAC03Status_Type = SbStatus
_SbModAC03Status_Object = MibScalar
sbModAC03Status = _SbModAC03Status_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 3, 3, 1),
    _SbModAC03Status_Type()
)
sbModAC03Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModAC03Status.setStatus("current")
_SbModAC03Value_Type = SbACVoltage
_SbModAC03Value_Object = MibScalar
sbModAC03Value = _SbModAC03Value_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 3, 3, 2),
    _SbModAC03Value_Type()
)
sbModAC03Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModAC03Value.setStatus("current")
_SbModAC03AlarmMin_Type = SbACVoltage
_SbModAC03AlarmMin_Object = MibScalar
sbModAC03AlarmMin = _SbModAC03AlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 3, 3, 3),
    _SbModAC03AlarmMin_Type()
)
sbModAC03AlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModAC03AlarmMin.setStatus("current")
_SbModAC03AlarmMax_Type = SbACVoltage
_SbModAC03AlarmMax_Object = MibScalar
sbModAC03AlarmMax = _SbModAC03AlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 3, 3, 4),
    _SbModAC03AlarmMax_Type()
)
sbModAC03AlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModAC03AlarmMax.setStatus("current")
_SbModACAIO_ObjectIdentity = ObjectIdentity
sbModACAIO = _SbModACAIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 3, 4)
)
_SbModACAIOStatus_Type = SbStatus
_SbModACAIOStatus_Object = MibScalar
sbModACAIOStatus = _SbModACAIOStatus_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 3, 4, 1),
    _SbModACAIOStatus_Type()
)
sbModACAIOStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModACAIOStatus.setStatus("current")
_SbModACAIOValue_Type = SbACVoltage
_SbModACAIOValue_Object = MibScalar
sbModACAIOValue = _SbModACAIOValue_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 3, 4, 2),
    _SbModACAIOValue_Type()
)
sbModACAIOValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModACAIOValue.setStatus("current")
_SbModACAIOAlarmMin_Type = SbACVoltage
_SbModACAIOAlarmMin_Object = MibScalar
sbModACAIOAlarmMin = _SbModACAIOAlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 3, 4, 3),
    _SbModACAIOAlarmMin_Type()
)
sbModACAIOAlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModACAIOAlarmMin.setStatus("current")
_SbModACAIOAlarmMax_Type = SbACVoltage
_SbModACAIOAlarmMax_Object = MibScalar
sbModACAIOAlarmMax = _SbModACAIOAlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 3, 4, 4),
    _SbModACAIOAlarmMax_Type()
)
sbModACAIOAlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModACAIOAlarmMax.setStatus("current")
_SbModDC_ObjectIdentity = ObjectIdentity
sbModDC = _SbModDC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 4)
)
_SbModDC01_ObjectIdentity = ObjectIdentity
sbModDC01 = _SbModDC01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 4, 1)
)
_SbModDC01Status_Type = SbStatus
_SbModDC01Status_Object = MibScalar
sbModDC01Status = _SbModDC01Status_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 4, 1, 1),
    _SbModDC01Status_Type()
)
sbModDC01Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModDC01Status.setStatus("current")
_SbModDC01Value_Type = SbDCVoltage
_SbModDC01Value_Object = MibScalar
sbModDC01Value = _SbModDC01Value_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 4, 1, 2),
    _SbModDC01Value_Type()
)
sbModDC01Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModDC01Value.setStatus("current")
_SbModDC01AlarmMin_Type = SbDCVoltage
_SbModDC01AlarmMin_Object = MibScalar
sbModDC01AlarmMin = _SbModDC01AlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 4, 1, 3),
    _SbModDC01AlarmMin_Type()
)
sbModDC01AlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModDC01AlarmMin.setStatus("current")
_SbModDC01AlarmMax_Type = SbDCVoltage
_SbModDC01AlarmMax_Object = MibScalar
sbModDC01AlarmMax = _SbModDC01AlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 4, 1, 4),
    _SbModDC01AlarmMax_Type()
)
sbModDC01AlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModDC01AlarmMax.setStatus("current")
_SbModDC01OffsetAdjustment_Type = SbDCOffsetAdjustment
_SbModDC01OffsetAdjustment_Object = MibScalar
sbModDC01OffsetAdjustment = _SbModDC01OffsetAdjustment_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 4, 1, 5),
    _SbModDC01OffsetAdjustment_Type()
)
sbModDC01OffsetAdjustment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModDC01OffsetAdjustment.setStatus("current")
_SbModDC02_ObjectIdentity = ObjectIdentity
sbModDC02 = _SbModDC02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 4, 2)
)
_SbModDC02Status_Type = SbStatus
_SbModDC02Status_Object = MibScalar
sbModDC02Status = _SbModDC02Status_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 4, 2, 1),
    _SbModDC02Status_Type()
)
sbModDC02Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModDC02Status.setStatus("current")
_SbModDC02Value_Type = SbDCVoltage
_SbModDC02Value_Object = MibScalar
sbModDC02Value = _SbModDC02Value_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 4, 2, 2),
    _SbModDC02Value_Type()
)
sbModDC02Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModDC02Value.setStatus("current")
_SbModDC02AlarmMin_Type = SbDCVoltage
_SbModDC02AlarmMin_Object = MibScalar
sbModDC02AlarmMin = _SbModDC02AlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 4, 2, 3),
    _SbModDC02AlarmMin_Type()
)
sbModDC02AlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModDC02AlarmMin.setStatus("current")
_SbModDC02AlarmMax_Type = SbDCVoltage
_SbModDC02AlarmMax_Object = MibScalar
sbModDC02AlarmMax = _SbModDC02AlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 4, 2, 4),
    _SbModDC02AlarmMax_Type()
)
sbModDC02AlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModDC02AlarmMax.setStatus("current")
_SbModDC02OffsetAdjustment_Type = SbDCOffsetAdjustment
_SbModDC02OffsetAdjustment_Object = MibScalar
sbModDC02OffsetAdjustment = _SbModDC02OffsetAdjustment_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 4, 2, 5),
    _SbModDC02OffsetAdjustment_Type()
)
sbModDC02OffsetAdjustment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModDC02OffsetAdjustment.setStatus("current")
_SbModDC03_ObjectIdentity = ObjectIdentity
sbModDC03 = _SbModDC03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 4, 3)
)
_SbModDC03Status_Type = SbStatus
_SbModDC03Status_Object = MibScalar
sbModDC03Status = _SbModDC03Status_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 4, 3, 1),
    _SbModDC03Status_Type()
)
sbModDC03Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModDC03Status.setStatus("current")
_SbModDC03Value_Type = SbDCVoltage
_SbModDC03Value_Object = MibScalar
sbModDC03Value = _SbModDC03Value_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 4, 3, 2),
    _SbModDC03Value_Type()
)
sbModDC03Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModDC03Value.setStatus("current")
_SbModDC03AlarmMin_Type = SbDCVoltage
_SbModDC03AlarmMin_Object = MibScalar
sbModDC03AlarmMin = _SbModDC03AlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 4, 3, 3),
    _SbModDC03AlarmMin_Type()
)
sbModDC03AlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModDC03AlarmMin.setStatus("current")
_SbModDC03AlarmMax_Type = SbDCVoltage
_SbModDC03AlarmMax_Object = MibScalar
sbModDC03AlarmMax = _SbModDC03AlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 4, 3, 4),
    _SbModDC03AlarmMax_Type()
)
sbModDC03AlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModDC03AlarmMax.setStatus("current")
_SbModDC03OffsetAdjustment_Type = SbDCOffsetAdjustment
_SbModDC03OffsetAdjustment_Object = MibScalar
sbModDC03OffsetAdjustment = _SbModDC03OffsetAdjustment_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 4, 3, 5),
    _SbModDC03OffsetAdjustment_Type()
)
sbModDC03OffsetAdjustment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModDC03OffsetAdjustment.setStatus("current")
_SbModDC04_ObjectIdentity = ObjectIdentity
sbModDC04 = _SbModDC04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 4, 4)
)
_SbModDC04Status_Type = SbStatus
_SbModDC04Status_Object = MibScalar
sbModDC04Status = _SbModDC04Status_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 4, 4, 1),
    _SbModDC04Status_Type()
)
sbModDC04Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModDC04Status.setStatus("current")
_SbModDC04Value_Type = SbDCVoltage
_SbModDC04Value_Object = MibScalar
sbModDC04Value = _SbModDC04Value_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 4, 4, 2),
    _SbModDC04Value_Type()
)
sbModDC04Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModDC04Value.setStatus("current")
_SbModDC04AlarmMin_Type = SbDCVoltage
_SbModDC04AlarmMin_Object = MibScalar
sbModDC04AlarmMin = _SbModDC04AlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 4, 4, 3),
    _SbModDC04AlarmMin_Type()
)
sbModDC04AlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModDC04AlarmMin.setStatus("current")
_SbModDC04AlarmMax_Type = SbDCVoltage
_SbModDC04AlarmMax_Object = MibScalar
sbModDC04AlarmMax = _SbModDC04AlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 4, 4, 4),
    _SbModDC04AlarmMax_Type()
)
sbModDC04AlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModDC04AlarmMax.setStatus("current")
_SbModDC04OffsetAdjustment_Type = SbDCOffsetAdjustment
_SbModDC04OffsetAdjustment_Object = MibScalar
sbModDC04OffsetAdjustment = _SbModDC04OffsetAdjustment_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 4, 4, 5),
    _SbModDC04OffsetAdjustment_Type()
)
sbModDC04OffsetAdjustment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbModDC04OffsetAdjustment.setStatus("current")
_SbModTamper_ObjectIdentity = ObjectIdentity
sbModTamper = _SbModTamper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 5)
)
_SbModTamperExtern_ObjectIdentity = ObjectIdentity
sbModTamperExtern = _SbModTamperExtern_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 5, 1)
)
_SbModTamperExternStatus_Type = SbStatus
_SbModTamperExternStatus_Object = MibScalar
sbModTamperExternStatus = _SbModTamperExternStatus_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 5, 1, 1),
    _SbModTamperExternStatus_Type()
)
sbModTamperExternStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTamperExternStatus.setStatus("current")
_SbTamperExtern01Status_Type = SbStatusTamper
_SbTamperExtern01Status_Object = MibScalar
sbTamperExtern01Status = _SbTamperExtern01Status_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 5, 1, 2),
    _SbTamperExtern01Status_Type()
)
sbTamperExtern01Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbTamperExtern01Status.setStatus("current")
_SbTamperExtern02Status_Type = SbStatusTamper
_SbTamperExtern02Status_Object = MibScalar
sbTamperExtern02Status = _SbTamperExtern02Status_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 5, 1, 3),
    _SbTamperExtern02Status_Type()
)
sbTamperExtern02Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbTamperExtern02Status.setStatus("current")
_SbTamperExtern03Status_Type = SbStatusTamper
_SbTamperExtern03Status_Object = MibScalar
sbTamperExtern03Status = _SbTamperExtern03Status_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 5, 1, 4),
    _SbTamperExtern03Status_Type()
)
sbTamperExtern03Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbTamperExtern03Status.setStatus("current")
_SbTamperExtern04Status_Type = SbStatusTamper
_SbTamperExtern04Status_Object = MibScalar
sbTamperExtern04Status = _SbTamperExtern04Status_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 5, 1, 5),
    _SbTamperExtern04Status_Type()
)
sbTamperExtern04Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbTamperExtern04Status.setStatus("current")
_SbTamperExtern05Status_Type = SbStatusTamper
_SbTamperExtern05Status_Object = MibScalar
sbTamperExtern05Status = _SbTamperExtern05Status_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 5, 1, 6),
    _SbTamperExtern05Status_Type()
)
sbTamperExtern05Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbTamperExtern05Status.setStatus("current")
_SbTamperExtern06Status_Type = SbStatusTamper
_SbTamperExtern06Status_Object = MibScalar
sbTamperExtern06Status = _SbTamperExtern06Status_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 5, 1, 7),
    _SbTamperExtern06Status_Type()
)
sbTamperExtern06Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbTamperExtern06Status.setStatus("current")
_SbTamperExtern07Status_Type = SbStatusTamper
_SbTamperExtern07Status_Object = MibScalar
sbTamperExtern07Status = _SbTamperExtern07Status_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 5, 1, 8),
    _SbTamperExtern07Status_Type()
)
sbTamperExtern07Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbTamperExtern07Status.setStatus("current")
_SbTamperExtern08Status_Type = SbStatusTamper
_SbTamperExtern08Status_Object = MibScalar
sbTamperExtern08Status = _SbTamperExtern08Status_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 5, 1, 9),
    _SbTamperExtern08Status_Type()
)
sbTamperExtern08Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbTamperExtern08Status.setStatus("current")
_SbModTamperAIO_ObjectIdentity = ObjectIdentity
sbModTamperAIO = _SbModTamperAIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 5, 2)
)
_SbModTamperAIOStatus_Type = SbStatus
_SbModTamperAIOStatus_Object = MibScalar
sbModTamperAIOStatus = _SbModTamperAIOStatus_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 5, 2, 1),
    _SbModTamperAIOStatus_Type()
)
sbModTamperAIOStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModTamperAIOStatus.setStatus("current")
_SbTamperAIO01Status_Type = SbStatusTamper
_SbTamperAIO01Status_Object = MibScalar
sbTamperAIO01Status = _SbTamperAIO01Status_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 5, 2, 2),
    _SbTamperAIO01Status_Type()
)
sbTamperAIO01Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbTamperAIO01Status.setStatus("current")
_SbTamperAIO02Status_Type = SbStatusTamper
_SbTamperAIO02Status_Object = MibScalar
sbTamperAIO02Status = _SbTamperAIO02Status_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 5, 2, 3),
    _SbTamperAIO02Status_Type()
)
sbTamperAIO02Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbTamperAIO02Status.setStatus("current")
_SbTamperAIO03Status_Type = SbStatusTamper
_SbTamperAIO03Status_Object = MibScalar
sbTamperAIO03Status = _SbTamperAIO03Status_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 5, 2, 4),
    _SbTamperAIO03Status_Type()
)
sbTamperAIO03Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbTamperAIO03Status.setStatus("current")
_SbTamperAIO04Status_Type = SbStatusTamper
_SbTamperAIO04Status_Object = MibScalar
sbTamperAIO04Status = _SbTamperAIO04Status_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 5, 2, 5),
    _SbTamperAIO04Status_Type()
)
sbTamperAIO04Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbTamperAIO04Status.setStatus("current")
_SbModRelay_ObjectIdentity = ObjectIdentity
sbModRelay = _SbModRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 6)
)
_SbModRelayExtern_ObjectIdentity = ObjectIdentity
sbModRelayExtern = _SbModRelayExtern_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 6, 1)
)
_SbModRelayExternStatus_Type = SbStatus
_SbModRelayExternStatus_Object = MibScalar
sbModRelayExternStatus = _SbModRelayExternStatus_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 6, 1, 1),
    _SbModRelayExternStatus_Type()
)
sbModRelayExternStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModRelayExternStatus.setStatus("current")
_SbRelayExtern01Status_Type = SbStatusRelay
_SbRelayExtern01Status_Object = MibScalar
sbRelayExtern01Status = _SbRelayExtern01Status_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 6, 1, 2),
    _SbRelayExtern01Status_Type()
)
sbRelayExtern01Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbRelayExtern01Status.setStatus("current")
_SbRelayExtern02Status_Type = SbStatusRelay
_SbRelayExtern02Status_Object = MibScalar
sbRelayExtern02Status = _SbRelayExtern02Status_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 6, 1, 3),
    _SbRelayExtern02Status_Type()
)
sbRelayExtern02Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbRelayExtern02Status.setStatus("current")
_SbRelayExtern03Status_Type = SbStatusRelay
_SbRelayExtern03Status_Object = MibScalar
sbRelayExtern03Status = _SbRelayExtern03Status_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 6, 1, 4),
    _SbRelayExtern03Status_Type()
)
sbRelayExtern03Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbRelayExtern03Status.setStatus("current")
_SbRelayExternResetTime_Type = SbResetTimeTC
_SbRelayExternResetTime_Object = MibScalar
sbRelayExternResetTime = _SbRelayExternResetTime_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 6, 1, 5),
    _SbRelayExternResetTime_Type()
)
sbRelayExternResetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbRelayExternResetTime.setStatus("current")
_SbModRelayAIO_ObjectIdentity = ObjectIdentity
sbModRelayAIO = _SbModRelayAIO_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 6, 2)
)
_SbModRelayAIOStatus_Type = SbStatus
_SbModRelayAIOStatus_Object = MibScalar
sbModRelayAIOStatus = _SbModRelayAIOStatus_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 6, 2, 1),
    _SbModRelayAIOStatus_Type()
)
sbModRelayAIOStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbModRelayAIOStatus.setStatus("current")
_SbRelayAIO01Status_Type = SbStatusRelay
_SbRelayAIO01Status_Object = MibScalar
sbRelayAIO01Status = _SbRelayAIO01Status_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 6, 2, 2),
    _SbRelayAIO01Status_Type()
)
sbRelayAIO01Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbRelayAIO01Status.setStatus("current")
_SbRelayAIO02Status_Type = SbStatusRelay
_SbRelayAIO02Status_Object = MibScalar
sbRelayAIO02Status = _SbRelayAIO02Status_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 6, 2, 3),
    _SbRelayAIO02Status_Type()
)
sbRelayAIO02Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbRelayAIO02Status.setStatus("current")
_SbRelayAIO03Status_Type = SbStatusRelay
_SbRelayAIO03Status_Object = MibScalar
sbRelayAIO03Status = _SbRelayAIO03Status_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 6, 2, 4),
    _SbRelayAIO03Status_Type()
)
sbRelayAIO03Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbRelayAIO03Status.setStatus("current")
_SbRelayAIOResetTime_Type = SbResetTimeTC
_SbRelayAIOResetTime_Object = MibScalar
sbRelayAIOResetTime = _SbRelayAIOResetTime_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 6, 2, 5),
    _SbRelayAIOResetTime_Type()
)
sbRelayAIOResetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbRelayAIOResetTime.setStatus("current")
_SbMod420ma_ObjectIdentity = ObjectIdentity
sbMod420ma = _SbMod420ma_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 7)
)
_SbMod420maValues_ObjectIdentity = ObjectIdentity
sbMod420maValues = _SbMod420maValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 7, 1)
)
_SbMod420maStatus_Type = SbStatus
_SbMod420maStatus_Object = MibScalar
sbMod420maStatus = _SbMod420maStatus_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 7, 1, 1),
    _SbMod420maStatus_Type()
)
sbMod420maStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbMod420maStatus.setStatus("current")
_SbMod420maS1Value_Type = Sb420maTChundredths
_SbMod420maS1Value_Object = MibScalar
sbMod420maS1Value = _SbMod420maS1Value_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 7, 1, 2),
    _SbMod420maS1Value_Type()
)
sbMod420maS1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbMod420maS1Value.setStatus("current")
_SbMod420maS1Value11Bits_Type = Sb420maTCbits
_SbMod420maS1Value11Bits_Object = MibScalar
sbMod420maS1Value11Bits = _SbMod420maS1Value11Bits_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 7, 1, 3),
    _SbMod420maS1Value11Bits_Type()
)
sbMod420maS1Value11Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbMod420maS1Value11Bits.setStatus("current")
_SbMod420maS2Value_Type = Sb420maTChundredths
_SbMod420maS2Value_Object = MibScalar
sbMod420maS2Value = _SbMod420maS2Value_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 7, 1, 4),
    _SbMod420maS2Value_Type()
)
sbMod420maS2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbMod420maS2Value.setStatus("current")
_SbMod420maS2Value11Bits_Type = Sb420maTCbits
_SbMod420maS2Value11Bits_Object = MibScalar
sbMod420maS2Value11Bits = _SbMod420maS2Value11Bits_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 7, 1, 5),
    _SbMod420maS2Value11Bits_Type()
)
sbMod420maS2Value11Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbMod420maS2Value11Bits.setStatus("current")
_SbMod420maS3Value_Type = Sb420maTChundredths
_SbMod420maS3Value_Object = MibScalar
sbMod420maS3Value = _SbMod420maS3Value_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 7, 1, 6),
    _SbMod420maS3Value_Type()
)
sbMod420maS3Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbMod420maS3Value.setStatus("current")
_SbMod420maS3Value11Bits_Type = Sb420maTCbits
_SbMod420maS3Value11Bits_Object = MibScalar
sbMod420maS3Value11Bits = _SbMod420maS3Value11Bits_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 7, 1, 7),
    _SbMod420maS3Value11Bits_Type()
)
sbMod420maS3Value11Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbMod420maS3Value11Bits.setStatus("current")
_SbMod420maS4Value_Type = Sb420maTChundredths
_SbMod420maS4Value_Object = MibScalar
sbMod420maS4Value = _SbMod420maS4Value_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 7, 1, 8),
    _SbMod420maS4Value_Type()
)
sbMod420maS4Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbMod420maS4Value.setStatus("current")
_SbMod420maS4Value11Bits_Type = Sb420maTCbits
_SbMod420maS4Value11Bits_Object = MibScalar
sbMod420maS4Value11Bits = _SbMod420maS4Value11Bits_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 7, 1, 9),
    _SbMod420maS4Value11Bits_Type()
)
sbMod420maS4Value11Bits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbMod420maS4Value11Bits.setStatus("current")
_SbMod420maAlarm_ObjectIdentity = ObjectIdentity
sbMod420maAlarm = _SbMod420maAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 7, 2)
)
_SbMod420maS1AlarmMin_Type = Sb420maTChundredths
_SbMod420maS1AlarmMin_Object = MibScalar
sbMod420maS1AlarmMin = _SbMod420maS1AlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 7, 2, 1),
    _SbMod420maS1AlarmMin_Type()
)
sbMod420maS1AlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbMod420maS1AlarmMin.setStatus("current")
_SbMod420maS1AlarmMax_Type = Sb420maTChundredths
_SbMod420maS1AlarmMax_Object = MibScalar
sbMod420maS1AlarmMax = _SbMod420maS1AlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 7, 2, 2),
    _SbMod420maS1AlarmMax_Type()
)
sbMod420maS1AlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbMod420maS1AlarmMax.setStatus("current")
_SbMod420maS2AlarmMin_Type = Sb420maTChundredths
_SbMod420maS2AlarmMin_Object = MibScalar
sbMod420maS2AlarmMin = _SbMod420maS2AlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 7, 2, 3),
    _SbMod420maS2AlarmMin_Type()
)
sbMod420maS2AlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbMod420maS2AlarmMin.setStatus("current")
_SbMod420maS2AlarmMax_Type = Sb420maTChundredths
_SbMod420maS2AlarmMax_Object = MibScalar
sbMod420maS2AlarmMax = _SbMod420maS2AlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 7, 2, 4),
    _SbMod420maS2AlarmMax_Type()
)
sbMod420maS2AlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbMod420maS2AlarmMax.setStatus("current")
_SbMod420maS3AlarmMin_Type = Sb420maTChundredths
_SbMod420maS3AlarmMin_Object = MibScalar
sbMod420maS3AlarmMin = _SbMod420maS3AlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 7, 2, 5),
    _SbMod420maS3AlarmMin_Type()
)
sbMod420maS3AlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbMod420maS3AlarmMin.setStatus("current")
_SbMod420maS3AlarmMax_Type = Sb420maTChundredths
_SbMod420maS3AlarmMax_Object = MibScalar
sbMod420maS3AlarmMax = _SbMod420maS3AlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 7, 2, 6),
    _SbMod420maS3AlarmMax_Type()
)
sbMod420maS3AlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbMod420maS3AlarmMax.setStatus("current")
_SbMod420maS4AlarmMin_Type = Sb420maTChundredths
_SbMod420maS4AlarmMin_Object = MibScalar
sbMod420maS4AlarmMin = _SbMod420maS4AlarmMin_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 7, 2, 7),
    _SbMod420maS4AlarmMin_Type()
)
sbMod420maS4AlarmMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbMod420maS4AlarmMin.setStatus("current")
_SbMod420maS4AlarmMax_Type = Sb420maTChundredths
_SbMod420maS4AlarmMax_Object = MibScalar
sbMod420maS4AlarmMax = _SbMod420maS4AlarmMax_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 7, 2, 8),
    _SbMod420maS4AlarmMax_Type()
)
sbMod420maS4AlarmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbMod420maS4AlarmMax.setStatus("current")
_SbPowerWifi_ObjectIdentity = ObjectIdentity
sbPowerWifi = _SbPowerWifi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8)
)
_SbPowerWifiPhase1_ObjectIdentity = ObjectIdentity
sbPowerWifiPhase1 = _SbPowerWifiPhase1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 1)
)
_SbPowerWifiPhase1Voltage_Type = SbAcVoltageValue
_SbPowerWifiPhase1Voltage_Object = MibScalar
sbPowerWifiPhase1Voltage = _SbPowerWifiPhase1Voltage_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 1, 1),
    _SbPowerWifiPhase1Voltage_Type()
)
sbPowerWifiPhase1Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase1Voltage.setStatus("current")
_SbPowerWifiPhase1Current_Type = SbCurrentValue
_SbPowerWifiPhase1Current_Object = MibScalar
sbPowerWifiPhase1Current = _SbPowerWifiPhase1Current_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 1, 2),
    _SbPowerWifiPhase1Current_Type()
)
sbPowerWifiPhase1Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase1Current.setStatus("current")
_SbPowerWifiPhase1PowerFactor_Type = SbPowerFactorValue
_SbPowerWifiPhase1PowerFactor_Object = MibScalar
sbPowerWifiPhase1PowerFactor = _SbPowerWifiPhase1PowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 1, 3),
    _SbPowerWifiPhase1PowerFactor_Type()
)
sbPowerWifiPhase1PowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase1PowerFactor.setStatus("current")
_SbPowerWifiPhase1Frequency_Type = SbFreqValue
_SbPowerWifiPhase1Frequency_Object = MibScalar
sbPowerWifiPhase1Frequency = _SbPowerWifiPhase1Frequency_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 1, 4),
    _SbPowerWifiPhase1Frequency_Type()
)
sbPowerWifiPhase1Frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase1Frequency.setStatus("current")
_SbPowerWifiPhase1Power_Type = SbPowerValue
_SbPowerWifiPhase1Power_Object = MibScalar
sbPowerWifiPhase1Power = _SbPowerWifiPhase1Power_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 1, 5),
    _SbPowerWifiPhase1Power_Type()
)
sbPowerWifiPhase1Power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase1Power.setStatus("current")
_SbPowerWifiPhase1Temperature_Type = SbTemperatureTC
_SbPowerWifiPhase1Temperature_Object = MibScalar
sbPowerWifiPhase1Temperature = _SbPowerWifiPhase1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 1, 6),
    _SbPowerWifiPhase1Temperature_Type()
)
sbPowerWifiPhase1Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase1Temperature.setStatus("current")
_SbPowerWifiPhase1MimMaxValues_ObjectIdentity = ObjectIdentity
sbPowerWifiPhase1MimMaxValues = _SbPowerWifiPhase1MimMaxValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 1, 7)
)
_SbPowerWifiMaxPhase1Voltage_Type = SbAcVoltageValue
_SbPowerWifiMaxPhase1Voltage_Object = MibScalar
sbPowerWifiMaxPhase1Voltage = _SbPowerWifiMaxPhase1Voltage_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 1, 7, 1),
    _SbPowerWifiMaxPhase1Voltage_Type()
)
sbPowerWifiMaxPhase1Voltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMaxPhase1Voltage.setStatus("current")
_SbPowerWifiMinPhase1Voltage_Type = SbAcVoltageValue
_SbPowerWifiMinPhase1Voltage_Object = MibScalar
sbPowerWifiMinPhase1Voltage = _SbPowerWifiMinPhase1Voltage_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 1, 7, 2),
    _SbPowerWifiMinPhase1Voltage_Type()
)
sbPowerWifiMinPhase1Voltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMinPhase1Voltage.setStatus("current")
_SbPowerWifiMaxPhase1Current_Type = SbCurrentValue
_SbPowerWifiMaxPhase1Current_Object = MibScalar
sbPowerWifiMaxPhase1Current = _SbPowerWifiMaxPhase1Current_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 1, 7, 3),
    _SbPowerWifiMaxPhase1Current_Type()
)
sbPowerWifiMaxPhase1Current.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMaxPhase1Current.setStatus("current")
_SbPowerWifiMinPhase1Current_Type = SbCurrentValue
_SbPowerWifiMinPhase1Current_Object = MibScalar
sbPowerWifiMinPhase1Current = _SbPowerWifiMinPhase1Current_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 1, 7, 4),
    _SbPowerWifiMinPhase1Current_Type()
)
sbPowerWifiMinPhase1Current.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMinPhase1Current.setStatus("current")
_SbPowerWifiMaxPhase1PowerFactor_Type = SbPowerFactorValue
_SbPowerWifiMaxPhase1PowerFactor_Object = MibScalar
sbPowerWifiMaxPhase1PowerFactor = _SbPowerWifiMaxPhase1PowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 1, 7, 5),
    _SbPowerWifiMaxPhase1PowerFactor_Type()
)
sbPowerWifiMaxPhase1PowerFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMaxPhase1PowerFactor.setStatus("current")
_SbPowerWifiMinPhase1PowerFactor_Type = SbPowerFactorValue
_SbPowerWifiMinPhase1PowerFactor_Object = MibScalar
sbPowerWifiMinPhase1PowerFactor = _SbPowerWifiMinPhase1PowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 1, 7, 6),
    _SbPowerWifiMinPhase1PowerFactor_Type()
)
sbPowerWifiMinPhase1PowerFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMinPhase1PowerFactor.setStatus("current")
_SbPowerWifiMaxPhase1Frequency_Type = SbFreqValue
_SbPowerWifiMaxPhase1Frequency_Object = MibScalar
sbPowerWifiMaxPhase1Frequency = _SbPowerWifiMaxPhase1Frequency_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 1, 7, 7),
    _SbPowerWifiMaxPhase1Frequency_Type()
)
sbPowerWifiMaxPhase1Frequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMaxPhase1Frequency.setStatus("current")
_SbPowerWifiMinPhase1Frequency_Type = SbFreqValue
_SbPowerWifiMinPhase1Frequency_Object = MibScalar
sbPowerWifiMinPhase1Frequency = _SbPowerWifiMinPhase1Frequency_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 1, 7, 8),
    _SbPowerWifiMinPhase1Frequency_Type()
)
sbPowerWifiMinPhase1Frequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMinPhase1Frequency.setStatus("current")
_SbPowerWifiMaxPhase1Temperature_Type = SbTemperatureTC
_SbPowerWifiMaxPhase1Temperature_Object = MibScalar
sbPowerWifiMaxPhase1Temperature = _SbPowerWifiMaxPhase1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 1, 7, 9),
    _SbPowerWifiMaxPhase1Temperature_Type()
)
sbPowerWifiMaxPhase1Temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMaxPhase1Temperature.setStatus("current")
_SbPowerWifiMinPhase1Temperature_Type = SbTemperatureTC
_SbPowerWifiMinPhase1Temperature_Object = MibScalar
sbPowerWifiMinPhase1Temperature = _SbPowerWifiMinPhase1Temperature_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 1, 7, 10),
    _SbPowerWifiMinPhase1Temperature_Type()
)
sbPowerWifiMinPhase1Temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMinPhase1Temperature.setStatus("current")
_SbPowerWifiPhase2_ObjectIdentity = ObjectIdentity
sbPowerWifiPhase2 = _SbPowerWifiPhase2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 2)
)
_SbPowerWifiPhase2Voltage_Type = SbAcVoltageValue
_SbPowerWifiPhase2Voltage_Object = MibScalar
sbPowerWifiPhase2Voltage = _SbPowerWifiPhase2Voltage_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 2, 1),
    _SbPowerWifiPhase2Voltage_Type()
)
sbPowerWifiPhase2Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase2Voltage.setStatus("current")
_SbPowerWifiPhase2Current_Type = SbCurrentValue
_SbPowerWifiPhase2Current_Object = MibScalar
sbPowerWifiPhase2Current = _SbPowerWifiPhase2Current_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 2, 2),
    _SbPowerWifiPhase2Current_Type()
)
sbPowerWifiPhase2Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase2Current.setStatus("current")
_SbPowerWifiPhase2PowerFactor_Type = SbPowerFactorValue
_SbPowerWifiPhase2PowerFactor_Object = MibScalar
sbPowerWifiPhase2PowerFactor = _SbPowerWifiPhase2PowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 2, 3),
    _SbPowerWifiPhase2PowerFactor_Type()
)
sbPowerWifiPhase2PowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase2PowerFactor.setStatus("current")
_SbPowerWifiPhase2Frequency_Type = SbFreqValue
_SbPowerWifiPhase2Frequency_Object = MibScalar
sbPowerWifiPhase2Frequency = _SbPowerWifiPhase2Frequency_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 2, 4),
    _SbPowerWifiPhase2Frequency_Type()
)
sbPowerWifiPhase2Frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase2Frequency.setStatus("current")
_SbPowerWifiPhase2Power_Type = SbPowerValue
_SbPowerWifiPhase2Power_Object = MibScalar
sbPowerWifiPhase2Power = _SbPowerWifiPhase2Power_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 2, 5),
    _SbPowerWifiPhase2Power_Type()
)
sbPowerWifiPhase2Power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase2Power.setStatus("current")
_SbPowerWifiPhase2Temperature_Type = SbTemperatureTC
_SbPowerWifiPhase2Temperature_Object = MibScalar
sbPowerWifiPhase2Temperature = _SbPowerWifiPhase2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 2, 6),
    _SbPowerWifiPhase2Temperature_Type()
)
sbPowerWifiPhase2Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase2Temperature.setStatus("current")
_SbPowerWifiPhase2MimMaxValues_ObjectIdentity = ObjectIdentity
sbPowerWifiPhase2MimMaxValues = _SbPowerWifiPhase2MimMaxValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 2, 7)
)
_SbPowerWifiMaxPhase2Voltage_Type = SbAcVoltageValue
_SbPowerWifiMaxPhase2Voltage_Object = MibScalar
sbPowerWifiMaxPhase2Voltage = _SbPowerWifiMaxPhase2Voltage_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 2, 7, 1),
    _SbPowerWifiMaxPhase2Voltage_Type()
)
sbPowerWifiMaxPhase2Voltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMaxPhase2Voltage.setStatus("current")
_SbPowerWifiMinPhase2Voltage_Type = SbAcVoltageValue
_SbPowerWifiMinPhase2Voltage_Object = MibScalar
sbPowerWifiMinPhase2Voltage = _SbPowerWifiMinPhase2Voltage_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 2, 7, 2),
    _SbPowerWifiMinPhase2Voltage_Type()
)
sbPowerWifiMinPhase2Voltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMinPhase2Voltage.setStatus("current")
_SbPowerWifiMaxPhase2Current_Type = SbCurrentValue
_SbPowerWifiMaxPhase2Current_Object = MibScalar
sbPowerWifiMaxPhase2Current = _SbPowerWifiMaxPhase2Current_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 2, 7, 3),
    _SbPowerWifiMaxPhase2Current_Type()
)
sbPowerWifiMaxPhase2Current.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMaxPhase2Current.setStatus("current")
_SbPowerWifiMinPhase2Current_Type = SbCurrentValue
_SbPowerWifiMinPhase2Current_Object = MibScalar
sbPowerWifiMinPhase2Current = _SbPowerWifiMinPhase2Current_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 2, 7, 4),
    _SbPowerWifiMinPhase2Current_Type()
)
sbPowerWifiMinPhase2Current.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMinPhase2Current.setStatus("current")
_SbPowerWifiMaxPhase2PowerFactor_Type = SbPowerFactorValue
_SbPowerWifiMaxPhase2PowerFactor_Object = MibScalar
sbPowerWifiMaxPhase2PowerFactor = _SbPowerWifiMaxPhase2PowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 2, 7, 5),
    _SbPowerWifiMaxPhase2PowerFactor_Type()
)
sbPowerWifiMaxPhase2PowerFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMaxPhase2PowerFactor.setStatus("current")
_SbPowerWifiMinPhase2PowerFactor_Type = SbPowerFactorValue
_SbPowerWifiMinPhase2PowerFactor_Object = MibScalar
sbPowerWifiMinPhase2PowerFactor = _SbPowerWifiMinPhase2PowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 2, 7, 6),
    _SbPowerWifiMinPhase2PowerFactor_Type()
)
sbPowerWifiMinPhase2PowerFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMinPhase2PowerFactor.setStatus("current")
_SbPowerWifiMaxPhase2Frequency_Type = SbFreqValue
_SbPowerWifiMaxPhase2Frequency_Object = MibScalar
sbPowerWifiMaxPhase2Frequency = _SbPowerWifiMaxPhase2Frequency_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 2, 7, 7),
    _SbPowerWifiMaxPhase2Frequency_Type()
)
sbPowerWifiMaxPhase2Frequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMaxPhase2Frequency.setStatus("current")
_SbPowerWifiMinPhase2Frequency_Type = SbFreqValue
_SbPowerWifiMinPhase2Frequency_Object = MibScalar
sbPowerWifiMinPhase2Frequency = _SbPowerWifiMinPhase2Frequency_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 2, 7, 8),
    _SbPowerWifiMinPhase2Frequency_Type()
)
sbPowerWifiMinPhase2Frequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMinPhase2Frequency.setStatus("current")
_SbPowerWifiMaxPhase2Temperature_Type = SbTemperatureTC
_SbPowerWifiMaxPhase2Temperature_Object = MibScalar
sbPowerWifiMaxPhase2Temperature = _SbPowerWifiMaxPhase2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 2, 7, 9),
    _SbPowerWifiMaxPhase2Temperature_Type()
)
sbPowerWifiMaxPhase2Temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMaxPhase2Temperature.setStatus("current")
_SbPowerWifiMinPhase2Temperature_Type = SbTemperatureTC
_SbPowerWifiMinPhase2Temperature_Object = MibScalar
sbPowerWifiMinPhase2Temperature = _SbPowerWifiMinPhase2Temperature_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 2, 7, 10),
    _SbPowerWifiMinPhase2Temperature_Type()
)
sbPowerWifiMinPhase2Temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMinPhase2Temperature.setStatus("current")
_SbPowerWifiPhase3_ObjectIdentity = ObjectIdentity
sbPowerWifiPhase3 = _SbPowerWifiPhase3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 3)
)
_SbPowerWifiPhase3Voltage_Type = SbAcVoltageValue
_SbPowerWifiPhase3Voltage_Object = MibScalar
sbPowerWifiPhase3Voltage = _SbPowerWifiPhase3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 3, 1),
    _SbPowerWifiPhase3Voltage_Type()
)
sbPowerWifiPhase3Voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase3Voltage.setStatus("current")
_SbPowerWifiPhase3Current_Type = SbCurrentValue
_SbPowerWifiPhase3Current_Object = MibScalar
sbPowerWifiPhase3Current = _SbPowerWifiPhase3Current_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 3, 2),
    _SbPowerWifiPhase3Current_Type()
)
sbPowerWifiPhase3Current.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase3Current.setStatus("current")
_SbPowerWifiPhase3PowerFactor_Type = SbPowerFactorValue
_SbPowerWifiPhase3PowerFactor_Object = MibScalar
sbPowerWifiPhase3PowerFactor = _SbPowerWifiPhase3PowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 3, 3),
    _SbPowerWifiPhase3PowerFactor_Type()
)
sbPowerWifiPhase3PowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase3PowerFactor.setStatus("current")
_SbPowerWifiPhase3Frequency_Type = SbFreqValue
_SbPowerWifiPhase3Frequency_Object = MibScalar
sbPowerWifiPhase3Frequency = _SbPowerWifiPhase3Frequency_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 3, 4),
    _SbPowerWifiPhase3Frequency_Type()
)
sbPowerWifiPhase3Frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase3Frequency.setStatus("current")
_SbPowerWifiPhase3Power_Type = SbPowerValue
_SbPowerWifiPhase3Power_Object = MibScalar
sbPowerWifiPhase3Power = _SbPowerWifiPhase3Power_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 3, 5),
    _SbPowerWifiPhase3Power_Type()
)
sbPowerWifiPhase3Power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase3Power.setStatus("current")
_SbPowerWifiPhase3Temperature_Type = SbTemperatureTC
_SbPowerWifiPhase3Temperature_Object = MibScalar
sbPowerWifiPhase3Temperature = _SbPowerWifiPhase3Temperature_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 3, 6),
    _SbPowerWifiPhase3Temperature_Type()
)
sbPowerWifiPhase3Temperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase3Temperature.setStatus("current")
_SbPowerWifiPhase3MimMaxValues_ObjectIdentity = ObjectIdentity
sbPowerWifiPhase3MimMaxValues = _SbPowerWifiPhase3MimMaxValues_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 3, 7)
)
_SbPowerWifiMaxPhase3Voltage_Type = SbAcVoltageValue
_SbPowerWifiMaxPhase3Voltage_Object = MibScalar
sbPowerWifiMaxPhase3Voltage = _SbPowerWifiMaxPhase3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 3, 7, 1),
    _SbPowerWifiMaxPhase3Voltage_Type()
)
sbPowerWifiMaxPhase3Voltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMaxPhase3Voltage.setStatus("current")
_SbPowerWifiMinPhase3Voltage_Type = SbAcVoltageValue
_SbPowerWifiMinPhase3Voltage_Object = MibScalar
sbPowerWifiMinPhase3Voltage = _SbPowerWifiMinPhase3Voltage_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 3, 7, 2),
    _SbPowerWifiMinPhase3Voltage_Type()
)
sbPowerWifiMinPhase3Voltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMinPhase3Voltage.setStatus("current")
_SbPowerWifiMaxPhase3Current_Type = SbCurrentValue
_SbPowerWifiMaxPhase3Current_Object = MibScalar
sbPowerWifiMaxPhase3Current = _SbPowerWifiMaxPhase3Current_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 3, 7, 3),
    _SbPowerWifiMaxPhase3Current_Type()
)
sbPowerWifiMaxPhase3Current.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMaxPhase3Current.setStatus("current")
_SbPowerWifiMinPhase3Current_Type = SbCurrentValue
_SbPowerWifiMinPhase3Current_Object = MibScalar
sbPowerWifiMinPhase3Current = _SbPowerWifiMinPhase3Current_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 3, 7, 4),
    _SbPowerWifiMinPhase3Current_Type()
)
sbPowerWifiMinPhase3Current.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMinPhase3Current.setStatus("current")
_SbPowerWifiMaxPhase3PowerFactor_Type = SbPowerFactorValue
_SbPowerWifiMaxPhase3PowerFactor_Object = MibScalar
sbPowerWifiMaxPhase3PowerFactor = _SbPowerWifiMaxPhase3PowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 3, 7, 5),
    _SbPowerWifiMaxPhase3PowerFactor_Type()
)
sbPowerWifiMaxPhase3PowerFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMaxPhase3PowerFactor.setStatus("current")
_SbPowerWifiMinPhase3PowerFactor_Type = SbPowerFactorValue
_SbPowerWifiMinPhase3PowerFactor_Object = MibScalar
sbPowerWifiMinPhase3PowerFactor = _SbPowerWifiMinPhase3PowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 3, 7, 6),
    _SbPowerWifiMinPhase3PowerFactor_Type()
)
sbPowerWifiMinPhase3PowerFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMinPhase3PowerFactor.setStatus("current")
_SbPowerWifiMaxPhase3Frequency_Type = SbFreqValue
_SbPowerWifiMaxPhase3Frequency_Object = MibScalar
sbPowerWifiMaxPhase3Frequency = _SbPowerWifiMaxPhase3Frequency_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 3, 7, 7),
    _SbPowerWifiMaxPhase3Frequency_Type()
)
sbPowerWifiMaxPhase3Frequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMaxPhase3Frequency.setStatus("current")
_SbPowerWifiMinPhase3Frequency_Type = SbFreqValue
_SbPowerWifiMinPhase3Frequency_Object = MibScalar
sbPowerWifiMinPhase3Frequency = _SbPowerWifiMinPhase3Frequency_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 3, 7, 8),
    _SbPowerWifiMinPhase3Frequency_Type()
)
sbPowerWifiMinPhase3Frequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMinPhase3Frequency.setStatus("current")
_SbPowerWifiMaxPhase3Temperature_Type = SbTemperatureTC
_SbPowerWifiMaxPhase3Temperature_Object = MibScalar
sbPowerWifiMaxPhase3Temperature = _SbPowerWifiMaxPhase3Temperature_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 3, 7, 9),
    _SbPowerWifiMaxPhase3Temperature_Type()
)
sbPowerWifiMaxPhase3Temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMaxPhase3Temperature.setStatus("current")
_SbPowerWifiMinPhase3Temperature_Type = SbTemperatureTC
_SbPowerWifiMinPhase3Temperature_Object = MibScalar
sbPowerWifiMinPhase3Temperature = _SbPowerWifiMinPhase3Temperature_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 3, 7, 10),
    _SbPowerWifiMinPhase3Temperature_Type()
)
sbPowerWifiMinPhase3Temperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbPowerWifiMinPhase3Temperature.setStatus("current")
_SbPowerWifiValuesTables_ObjectIdentity = ObjectIdentity
sbPowerWifiValuesTables = _SbPowerWifiValuesTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4)
)
_SbPowerTablePhase1_Object = MibTable
sbPowerTablePhase1 = _SbPowerTablePhase1_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4, 1)
)
if mibBuilder.loadTexts:
    sbPowerTablePhase1.setStatus("current")
_SbPowerTable1Entry_Object = MibTableRow
sbPowerTable1Entry = _SbPowerTable1Entry_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4, 1, 1)
)
sbPowerTable1Entry.setIndexNames(
    (0, "SENSORBOX-WIFI-MIB", "sbPowerIndex1"),
)
if mibBuilder.loadTexts:
    sbPowerTable1Entry.setStatus("current")
_SbPowerWifiPhase1TbVoltage_Type = SbAcVoltageValue
_SbPowerWifiPhase1TbVoltage_Object = MibTableColumn
sbPowerWifiPhase1TbVoltage = _SbPowerWifiPhase1TbVoltage_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4, 1, 1, 1),
    _SbPowerWifiPhase1TbVoltage_Type()
)
sbPowerWifiPhase1TbVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase1TbVoltage.setStatus("current")
_SbPowerWifiPhase1TbCurrent_Type = SbCurrentValue
_SbPowerWifiPhase1TbCurrent_Object = MibTableColumn
sbPowerWifiPhase1TbCurrent = _SbPowerWifiPhase1TbCurrent_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4, 1, 1, 2),
    _SbPowerWifiPhase1TbCurrent_Type()
)
sbPowerWifiPhase1TbCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase1TbCurrent.setStatus("current")
_SbPowerWifiPhase1TbPowerFactor_Type = SbPowerFactorValue
_SbPowerWifiPhase1TbPowerFactor_Object = MibTableColumn
sbPowerWifiPhase1TbPowerFactor = _SbPowerWifiPhase1TbPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4, 1, 1, 3),
    _SbPowerWifiPhase1TbPowerFactor_Type()
)
sbPowerWifiPhase1TbPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase1TbPowerFactor.setStatus("current")
_SbPowerWifiPhase1TbFrequency_Type = SbFreqValue
_SbPowerWifiPhase1TbFrequency_Object = MibTableColumn
sbPowerWifiPhase1TbFrequency = _SbPowerWifiPhase1TbFrequency_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4, 1, 1, 4),
    _SbPowerWifiPhase1TbFrequency_Type()
)
sbPowerWifiPhase1TbFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase1TbFrequency.setStatus("current")
_SbPowerWifiPhase1TbPower_Type = SbPowerValue
_SbPowerWifiPhase1TbPower_Object = MibTableColumn
sbPowerWifiPhase1TbPower = _SbPowerWifiPhase1TbPower_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4, 1, 1, 5),
    _SbPowerWifiPhase1TbPower_Type()
)
sbPowerWifiPhase1TbPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase1TbPower.setStatus("current")
_SbPowerWifiPhase1TbTemperature_Type = SbTemperatureTC
_SbPowerWifiPhase1TbTemperature_Object = MibTableColumn
sbPowerWifiPhase1TbTemperature = _SbPowerWifiPhase1TbTemperature_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4, 1, 1, 6),
    _SbPowerWifiPhase1TbTemperature_Type()
)
sbPowerWifiPhase1TbTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase1TbTemperature.setStatus("current")


class _SbPowerIndex1_Type(Integer32):
    """Custom type sbPowerIndex1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SbPowerIndex1_Type.__name__ = "Integer32"
_SbPowerIndex1_Object = MibTableColumn
sbPowerIndex1 = _SbPowerIndex1_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4, 1, 1, 7),
    _SbPowerIndex1_Type()
)
sbPowerIndex1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sbPowerIndex1.setStatus("current")
_SbPowerTablePhase2_Object = MibTable
sbPowerTablePhase2 = _SbPowerTablePhase2_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4, 2)
)
if mibBuilder.loadTexts:
    sbPowerTablePhase2.setStatus("current")
_SbPowerTable2Entry_Object = MibTableRow
sbPowerTable2Entry = _SbPowerTable2Entry_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4, 2, 1)
)
sbPowerTable2Entry.setIndexNames(
    (0, "SENSORBOX-WIFI-MIB", "sbPowerIndex2"),
)
if mibBuilder.loadTexts:
    sbPowerTable2Entry.setStatus("current")
_SbPowerWifiPhase2TbVoltage_Type = SbAcVoltageValue
_SbPowerWifiPhase2TbVoltage_Object = MibTableColumn
sbPowerWifiPhase2TbVoltage = _SbPowerWifiPhase2TbVoltage_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4, 2, 1, 1),
    _SbPowerWifiPhase2TbVoltage_Type()
)
sbPowerWifiPhase2TbVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase2TbVoltage.setStatus("current")
_SbPowerWifiPhase2TbCurrent_Type = SbCurrentValue
_SbPowerWifiPhase2TbCurrent_Object = MibTableColumn
sbPowerWifiPhase2TbCurrent = _SbPowerWifiPhase2TbCurrent_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4, 2, 1, 2),
    _SbPowerWifiPhase2TbCurrent_Type()
)
sbPowerWifiPhase2TbCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase2TbCurrent.setStatus("current")
_SbPowerWifiPhase2TbPowerFactor_Type = SbPowerFactorValue
_SbPowerWifiPhase2TbPowerFactor_Object = MibTableColumn
sbPowerWifiPhase2TbPowerFactor = _SbPowerWifiPhase2TbPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4, 2, 1, 3),
    _SbPowerWifiPhase2TbPowerFactor_Type()
)
sbPowerWifiPhase2TbPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase2TbPowerFactor.setStatus("current")
_SbPowerWifiPhase2TbFrequency_Type = SbFreqValue
_SbPowerWifiPhase2TbFrequency_Object = MibTableColumn
sbPowerWifiPhase2TbFrequency = _SbPowerWifiPhase2TbFrequency_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4, 2, 1, 4),
    _SbPowerWifiPhase2TbFrequency_Type()
)
sbPowerWifiPhase2TbFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase2TbFrequency.setStatus("current")
_SbPowerWifiPhase2TbPower_Type = SbPowerValue
_SbPowerWifiPhase2TbPower_Object = MibTableColumn
sbPowerWifiPhase2TbPower = _SbPowerWifiPhase2TbPower_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4, 2, 1, 5),
    _SbPowerWifiPhase2TbPower_Type()
)
sbPowerWifiPhase2TbPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase2TbPower.setStatus("current")
_SbPowerWifiPhase2TbTemperature_Type = SbTemperatureTC
_SbPowerWifiPhase2TbTemperature_Object = MibTableColumn
sbPowerWifiPhase2TbTemperature = _SbPowerWifiPhase2TbTemperature_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4, 2, 1, 6),
    _SbPowerWifiPhase2TbTemperature_Type()
)
sbPowerWifiPhase2TbTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase2TbTemperature.setStatus("current")


class _SbPowerIndex2_Type(Integer32):
    """Custom type sbPowerIndex2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SbPowerIndex2_Type.__name__ = "Integer32"
_SbPowerIndex2_Object = MibTableColumn
sbPowerIndex2 = _SbPowerIndex2_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4, 2, 1, 7),
    _SbPowerIndex2_Type()
)
sbPowerIndex2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sbPowerIndex2.setStatus("current")
_SbPowerTablePhase3_Object = MibTable
sbPowerTablePhase3 = _SbPowerTablePhase3_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4, 3)
)
if mibBuilder.loadTexts:
    sbPowerTablePhase3.setStatus("current")
_SbPowerTable3Entry_Object = MibTableRow
sbPowerTable3Entry = _SbPowerTable3Entry_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4, 3, 1)
)
sbPowerTable3Entry.setIndexNames(
    (0, "SENSORBOX-WIFI-MIB", "sbPowerIndex3"),
)
if mibBuilder.loadTexts:
    sbPowerTable3Entry.setStatus("current")
_SbPowerWifiPhase3TbVoltage_Type = SbAcVoltageValue
_SbPowerWifiPhase3TbVoltage_Object = MibTableColumn
sbPowerWifiPhase3TbVoltage = _SbPowerWifiPhase3TbVoltage_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4, 3, 1, 1),
    _SbPowerWifiPhase3TbVoltage_Type()
)
sbPowerWifiPhase3TbVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase3TbVoltage.setStatus("current")
_SbPowerWifiPhase3TbCurrent_Type = SbCurrentValue
_SbPowerWifiPhase3TbCurrent_Object = MibTableColumn
sbPowerWifiPhase3TbCurrent = _SbPowerWifiPhase3TbCurrent_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4, 3, 1, 2),
    _SbPowerWifiPhase3TbCurrent_Type()
)
sbPowerWifiPhase3TbCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase3TbCurrent.setStatus("current")
_SbPowerWifiPhase3TbPowerFactor_Type = SbPowerFactorValue
_SbPowerWifiPhase3TbPowerFactor_Object = MibTableColumn
sbPowerWifiPhase3TbPowerFactor = _SbPowerWifiPhase3TbPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4, 3, 1, 3),
    _SbPowerWifiPhase3TbPowerFactor_Type()
)
sbPowerWifiPhase3TbPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase3TbPowerFactor.setStatus("current")
_SbPowerWifiPhase3TbFrequency_Type = SbFreqValue
_SbPowerWifiPhase3TbFrequency_Object = MibTableColumn
sbPowerWifiPhase3TbFrequency = _SbPowerWifiPhase3TbFrequency_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4, 3, 1, 4),
    _SbPowerWifiPhase3TbFrequency_Type()
)
sbPowerWifiPhase3TbFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase3TbFrequency.setStatus("current")
_SbPowerWifiPhase3TbPower_Type = SbPowerValue
_SbPowerWifiPhase3TbPower_Object = MibTableColumn
sbPowerWifiPhase3TbPower = _SbPowerWifiPhase3TbPower_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4, 3, 1, 5),
    _SbPowerWifiPhase3TbPower_Type()
)
sbPowerWifiPhase3TbPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase3TbPower.setStatus("current")
_SbPowerWifiPhase3TbTemperature_Type = SbTemperatureTC
_SbPowerWifiPhase3TbTemperature_Object = MibTableColumn
sbPowerWifiPhase3TbTemperature = _SbPowerWifiPhase3TbTemperature_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4, 3, 1, 6),
    _SbPowerWifiPhase3TbTemperature_Type()
)
sbPowerWifiPhase3TbTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbPowerWifiPhase3TbTemperature.setStatus("current")


class _SbPowerIndex3_Type(Integer32):
    """Custom type sbPowerIndex3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SbPowerIndex3_Type.__name__ = "Integer32"
_SbPowerIndex3_Object = MibTableColumn
sbPowerIndex3 = _SbPowerIndex3_Object(
    (1, 3, 6, 1, 4, 1, 43498, 1, 8, 4, 3, 1, 7),
    _SbPowerIndex3_Type()
)
sbPowerIndex3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sbPowerIndex3.setStatus("current")
_SbConfig_ObjectIdentity = ObjectIdentity
sbConfig = _SbConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 2)
)
_SbNetwork_ObjectIdentity = ObjectIdentity
sbNetwork = _SbNetwork_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 2, 1)
)
_SbMainSSID_Type = OctetString
_SbMainSSID_Object = MibScalar
sbMainSSID = _SbMainSSID_Object(
    (1, 3, 6, 1, 4, 1, 43498, 2, 1, 1),
    _SbMainSSID_Type()
)
sbMainSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbMainSSID.setStatus("current")
_SbBackupSSID_Type = OctetString
_SbBackupSSID_Object = MibScalar
sbBackupSSID = _SbBackupSSID_Object(
    (1, 3, 6, 1, 4, 1, 43498, 2, 1, 2),
    _SbBackupSSID_Type()
)
sbBackupSSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbBackupSSID.setStatus("current")
_SbWatchdog_ObjectIdentity = ObjectIdentity
sbWatchdog = _SbWatchdog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 2, 2)
)
_SbWatchdogAloneRelay_Type = SbStatus
_SbWatchdogAloneRelay_Object = MibScalar
sbWatchdogAloneRelay = _SbWatchdogAloneRelay_Object(
    (1, 3, 6, 1, 4, 1, 43498, 2, 2, 1),
    _SbWatchdogAloneRelay_Type()
)
sbWatchdogAloneRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbWatchdogAloneRelay.setStatus("current")
_SbWatchdogRelay1_Type = SbStatus
_SbWatchdogRelay1_Object = MibScalar
sbWatchdogRelay1 = _SbWatchdogRelay1_Object(
    (1, 3, 6, 1, 4, 1, 43498, 2, 2, 2),
    _SbWatchdogRelay1_Type()
)
sbWatchdogRelay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbWatchdogRelay1.setStatus("current")
_SbOthers_ObjectIdentity = ObjectIdentity
sbOthers = _SbOthers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 2, 3)
)
_SbAutoUpdate_Type = SbStatus
_SbAutoUpdate_Object = MibScalar
sbAutoUpdate = _SbAutoUpdate_Object(
    (1, 3, 6, 1, 4, 1, 43498, 2, 3, 1),
    _SbAutoUpdate_Type()
)
sbAutoUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbAutoUpdate.setStatus("current")
_SbNotifications_ObjectIdentity = ObjectIdentity
sbNotifications = _SbNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43498, 3)
)

# Managed Objects groups


# Notification objects

sbModNotifierStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 43498, 3, 1)
)
if mibBuilder.loadTexts:
    sbModNotifierStatus.setStatus(
        "current"
    )

sbModNotifierValueMin = NotificationType(
    (1, 3, 6, 1, 4, 1, 43498, 3, 2)
)
if mibBuilder.loadTexts:
    sbModNotifierValueMin.setStatus(
        "current"
    )

sbModNotifierValueMax = NotificationType(
    (1, 3, 6, 1, 4, 1, 43498, 3, 3)
)
if mibBuilder.loadTexts:
    sbModNotifierValueMax.setStatus(
        "current"
    )

sbModNotifierStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 43498, 3, 4)
)
if mibBuilder.loadTexts:
    sbModNotifierStateChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SENSORBOX-WIFI-MIB",
    **{"SbTemperatureTC": SbTemperatureTC,
       "SbAddressTC": SbAddressTC,
       "SbUmidityTC": SbUmidityTC,
       "SbStatus": SbStatus,
       "SbStatusRelay": SbStatusRelay,
       "SbStatusTamper": SbStatusTamper,
       "SbACVoltage": SbACVoltage,
       "SbDCVoltage": SbDCVoltage,
       "SbDCOffsetAdjustment": SbDCOffsetAdjustment,
       "Sb420maTChundredths": Sb420maTChundredths,
       "Sb420maTCbits": Sb420maTCbits,
       "SbResetTimeTC": SbResetTimeTC,
       "SbAcVoltageValue": SbAcVoltageValue,
       "SbFreqValue": SbFreqValue,
       "SbCurrentValue": SbCurrentValue,
       "SbPowerFactorValue": SbPowerFactorValue,
       "SbPowerValue": SbPowerValue,
       "sensorbox": sensorbox,
       "sbModules": sbModules,
       "sbModTemp": sbModTemp,
       "sbTempP1_01": sbTempP1_01,
       "sbModTempStatusP1_01": sbModTempStatusP1_01,
       "sbModTempAddressP1_01": sbModTempAddressP1_01,
       "sbModTempValueP1_01": sbModTempValueP1_01,
       "sbModTempAlarmMinP1_01": sbModTempAlarmMinP1_01,
       "sbModTempAlarmMaxP1_01": sbModTempAlarmMaxP1_01,
       "sbTempP1_02": sbTempP1_02,
       "sbModTempStatusP1_02": sbModTempStatusP1_02,
       "sbModTempAddressP1_02": sbModTempAddressP1_02,
       "sbModTempValueP1_02": sbModTempValueP1_02,
       "sbModTempAlarmMinP1_02": sbModTempAlarmMinP1_02,
       "sbModTempAlarmMaxP1_02": sbModTempAlarmMaxP1_02,
       "sbTempP1_03": sbTempP1_03,
       "sbModTempStatusP1_03": sbModTempStatusP1_03,
       "sbModTempAddressP1_03": sbModTempAddressP1_03,
       "sbModTempValueP1_03": sbModTempValueP1_03,
       "sbModTempAlarmMinP1_03": sbModTempAlarmMinP1_03,
       "sbModTempAlarmMaxP1_03": sbModTempAlarmMaxP1_03,
       "sbTempP1_04": sbTempP1_04,
       "sbModTempStatusP1_04": sbModTempStatusP1_04,
       "sbModTempAddressP1_04": sbModTempAddressP1_04,
       "sbModTempValueP1_04": sbModTempValueP1_04,
       "sbModTempAlarmMinP1_04": sbModTempAlarmMinP1_04,
       "sbModTempAlarmMaxP1_04": sbModTempAlarmMaxP1_04,
       "sbTempP2_01": sbTempP2_01,
       "sbModTempStatusP2_01": sbModTempStatusP2_01,
       "sbModTempAddressP2_01": sbModTempAddressP2_01,
       "sbModTempValueP2_01": sbModTempValueP2_01,
       "sbModTempAlarmMinP2_01": sbModTempAlarmMinP2_01,
       "sbModTempAlarmMaxP2_01": sbModTempAlarmMaxP2_01,
       "sbTempP2_02": sbTempP2_02,
       "sbModTempStatusP2_02": sbModTempStatusP2_02,
       "sbModTempAddressP2_02": sbModTempAddressP2_02,
       "sbModTempValueP2_02": sbModTempValueP2_02,
       "sbModTempAlarmMinP2_02": sbModTempAlarmMinP2_02,
       "sbModTempAlarmMaxP2_02": sbModTempAlarmMaxP2_02,
       "sbTempP2_03": sbTempP2_03,
       "sbModTempStatusP2_03": sbModTempStatusP2_03,
       "sbModTempAddressP2_03": sbModTempAddressP2_03,
       "sbModTempValueP2_03": sbModTempValueP2_03,
       "sbModTempAlarmMinP2_03": sbModTempAlarmMinP2_03,
       "sbModTempAlarmMaxP2_03": sbModTempAlarmMaxP2_03,
       "sbTempP2_04": sbTempP2_04,
       "sbModTempStatusP2_04": sbModTempStatusP2_04,
       "sbModTempAddressP2_04": sbModTempAddressP2_04,
       "sbModTempValueP2_04": sbModTempValueP2_04,
       "sbModTempAlarmMinP2_04": sbModTempAlarmMinP2_04,
       "sbModTempAlarmMaxP2_04": sbModTempAlarmMaxP2_04,
       "sbModTempHum": sbModTempHum,
       "sbTempHumP1": sbTempHumP1,
       "sbModTHStatus_P1": sbModTHStatus_P1,
       "sbModTHValueTemp_P1": sbModTHValueTemp_P1,
       "sbModTHAlarmTempMin_P1": sbModTHAlarmTempMin_P1,
       "sbModTHAlarmTempMax_P1": sbModTHAlarmTempMax_P1,
       "sbModTHValueHum_P1": sbModTHValueHum_P1,
       "sbModTHAlarmHumMin_P1": sbModTHAlarmHumMin_P1,
       "sbModTHAlarmHumMax_P1": sbModTHAlarmHumMax_P1,
       "sbTempHumP2": sbTempHumP2,
       "sbModTHStatus_P2": sbModTHStatus_P2,
       "sbModTHValueTemp_P2": sbModTHValueTemp_P2,
       "sbModTHAlarmTempMin_P2": sbModTHAlarmTempMin_P2,
       "sbModTHAlarmTempMax_P2": sbModTHAlarmTempMax_P2,
       "sbModTHValueHum_P2": sbModTHValueHum_P2,
       "sbModTHAlarmHumMin_P2": sbModTHAlarmHumMin_P2,
       "sbModTHAlarmHumMax_P2": sbModTHAlarmHumMax_P2,
       "sbTempHumExtern01": sbTempHumExtern01,
       "sbModTHStatus_Ext01": sbModTHStatus_Ext01,
       "sbModTHValueTemp_Ext01": sbModTHValueTemp_Ext01,
       "sbModTHAlarmTempMin_Ext01": sbModTHAlarmTempMin_Ext01,
       "sbModTHAlarmTempMax_Ext01": sbModTHAlarmTempMax_Ext01,
       "sbModTHValueHum_Ext01": sbModTHValueHum_Ext01,
       "sbModTHAlarmHumMin_Ext01": sbModTHAlarmHumMin_Ext01,
       "sbModTHAlarmHumMax_Ext01": sbModTHAlarmHumMax_Ext01,
       "sbTempHumExtern02": sbTempHumExtern02,
       "sbModTHStatus_Ext02": sbModTHStatus_Ext02,
       "sbModTHValueTemp_Ext02": sbModTHValueTemp_Ext02,
       "sbModTHAlarmTempMin_Ext02": sbModTHAlarmTempMin_Ext02,
       "sbModTHAlarmTempMax_Ext02": sbModTHAlarmTempMax_Ext02,
       "sbModTHValueHum_Ext02": sbModTHValueHum_Ext02,
       "sbModTHAlarmHumMin_Ext02": sbModTHAlarmHumMin_Ext02,
       "sbModTHAlarmHumMax_Ext02": sbModTHAlarmHumMax_Ext02,
       "sbTempHumExtern03": sbTempHumExtern03,
       "sbModTHStatus_Ext03": sbModTHStatus_Ext03,
       "sbModTHValueTemp_Ext03": sbModTHValueTemp_Ext03,
       "sbModTHAlarmTempMin_Ext03": sbModTHAlarmTempMin_Ext03,
       "sbModTHAlarmTempMax_Ext03": sbModTHAlarmTempMax_Ext03,
       "sbModTHValueHum_Ext03": sbModTHValueHum_Ext03,
       "sbModTHAlarmHumMin_Ext03": sbModTHAlarmHumMin_Ext03,
       "sbModTHAlarmHumMax_Ext03": sbModTHAlarmHumMax_Ext03,
       "sbTempHumExtern04": sbTempHumExtern04,
       "sbModTHStatus_Ext04": sbModTHStatus_Ext04,
       "sbModTHValueTemp_Ext04": sbModTHValueTemp_Ext04,
       "sbModTHAlarmTempMin_Ext04": sbModTHAlarmTempMin_Ext04,
       "sbModTHAlarmTempMax_Ext04": sbModTHAlarmTempMax_Ext04,
       "sbModTHValueHum_Ext04": sbModTHValueHum_Ext04,
       "sbModTHAlarmHumMin_Ext04": sbModTHAlarmHumMin_Ext04,
       "sbModTHAlarmHumMax_Ext04": sbModTHAlarmHumMax_Ext04,
       "sbModAC": sbModAC,
       "sbModAC01": sbModAC01,
       "sbModAC01Status": sbModAC01Status,
       "sbModAC01Value": sbModAC01Value,
       "sbModAC01AlarmMin": sbModAC01AlarmMin,
       "sbModAC01AlarmMax": sbModAC01AlarmMax,
       "sbModAC02": sbModAC02,
       "sbModAC02Status": sbModAC02Status,
       "sbModAC02Value": sbModAC02Value,
       "sbModAC02AlarmMin": sbModAC02AlarmMin,
       "sbModAC02AlarmMax": sbModAC02AlarmMax,
       "sbModAC03": sbModAC03,
       "sbModAC03Status": sbModAC03Status,
       "sbModAC03Value": sbModAC03Value,
       "sbModAC03AlarmMin": sbModAC03AlarmMin,
       "sbModAC03AlarmMax": sbModAC03AlarmMax,
       "sbModACAIO": sbModACAIO,
       "sbModACAIOStatus": sbModACAIOStatus,
       "sbModACAIOValue": sbModACAIOValue,
       "sbModACAIOAlarmMin": sbModACAIOAlarmMin,
       "sbModACAIOAlarmMax": sbModACAIOAlarmMax,
       "sbModDC": sbModDC,
       "sbModDC01": sbModDC01,
       "sbModDC01Status": sbModDC01Status,
       "sbModDC01Value": sbModDC01Value,
       "sbModDC01AlarmMin": sbModDC01AlarmMin,
       "sbModDC01AlarmMax": sbModDC01AlarmMax,
       "sbModDC01OffsetAdjustment": sbModDC01OffsetAdjustment,
       "sbModDC02": sbModDC02,
       "sbModDC02Status": sbModDC02Status,
       "sbModDC02Value": sbModDC02Value,
       "sbModDC02AlarmMin": sbModDC02AlarmMin,
       "sbModDC02AlarmMax": sbModDC02AlarmMax,
       "sbModDC02OffsetAdjustment": sbModDC02OffsetAdjustment,
       "sbModDC03": sbModDC03,
       "sbModDC03Status": sbModDC03Status,
       "sbModDC03Value": sbModDC03Value,
       "sbModDC03AlarmMin": sbModDC03AlarmMin,
       "sbModDC03AlarmMax": sbModDC03AlarmMax,
       "sbModDC03OffsetAdjustment": sbModDC03OffsetAdjustment,
       "sbModDC04": sbModDC04,
       "sbModDC04Status": sbModDC04Status,
       "sbModDC04Value": sbModDC04Value,
       "sbModDC04AlarmMin": sbModDC04AlarmMin,
       "sbModDC04AlarmMax": sbModDC04AlarmMax,
       "sbModDC04OffsetAdjustment": sbModDC04OffsetAdjustment,
       "sbModTamper": sbModTamper,
       "sbModTamperExtern": sbModTamperExtern,
       "sbModTamperExternStatus": sbModTamperExternStatus,
       "sbTamperExtern01Status": sbTamperExtern01Status,
       "sbTamperExtern02Status": sbTamperExtern02Status,
       "sbTamperExtern03Status": sbTamperExtern03Status,
       "sbTamperExtern04Status": sbTamperExtern04Status,
       "sbTamperExtern05Status": sbTamperExtern05Status,
       "sbTamperExtern06Status": sbTamperExtern06Status,
       "sbTamperExtern07Status": sbTamperExtern07Status,
       "sbTamperExtern08Status": sbTamperExtern08Status,
       "sbModTamperAIO": sbModTamperAIO,
       "sbModTamperAIOStatus": sbModTamperAIOStatus,
       "sbTamperAIO01Status": sbTamperAIO01Status,
       "sbTamperAIO02Status": sbTamperAIO02Status,
       "sbTamperAIO03Status": sbTamperAIO03Status,
       "sbTamperAIO04Status": sbTamperAIO04Status,
       "sbModRelay": sbModRelay,
       "sbModRelayExtern": sbModRelayExtern,
       "sbModRelayExternStatus": sbModRelayExternStatus,
       "sbRelayExtern01Status": sbRelayExtern01Status,
       "sbRelayExtern02Status": sbRelayExtern02Status,
       "sbRelayExtern03Status": sbRelayExtern03Status,
       "sbRelayExternResetTime": sbRelayExternResetTime,
       "sbModRelayAIO": sbModRelayAIO,
       "sbModRelayAIOStatus": sbModRelayAIOStatus,
       "sbRelayAIO01Status": sbRelayAIO01Status,
       "sbRelayAIO02Status": sbRelayAIO02Status,
       "sbRelayAIO03Status": sbRelayAIO03Status,
       "sbRelayAIOResetTime": sbRelayAIOResetTime,
       "sbMod420ma": sbMod420ma,
       "sbMod420maValues": sbMod420maValues,
       "sbMod420maStatus": sbMod420maStatus,
       "sbMod420maS1Value": sbMod420maS1Value,
       "sbMod420maS1Value11Bits": sbMod420maS1Value11Bits,
       "sbMod420maS2Value": sbMod420maS2Value,
       "sbMod420maS2Value11Bits": sbMod420maS2Value11Bits,
       "sbMod420maS3Value": sbMod420maS3Value,
       "sbMod420maS3Value11Bits": sbMod420maS3Value11Bits,
       "sbMod420maS4Value": sbMod420maS4Value,
       "sbMod420maS4Value11Bits": sbMod420maS4Value11Bits,
       "sbMod420maAlarm": sbMod420maAlarm,
       "sbMod420maS1AlarmMin": sbMod420maS1AlarmMin,
       "sbMod420maS1AlarmMax": sbMod420maS1AlarmMax,
       "sbMod420maS2AlarmMin": sbMod420maS2AlarmMin,
       "sbMod420maS2AlarmMax": sbMod420maS2AlarmMax,
       "sbMod420maS3AlarmMin": sbMod420maS3AlarmMin,
       "sbMod420maS3AlarmMax": sbMod420maS3AlarmMax,
       "sbMod420maS4AlarmMin": sbMod420maS4AlarmMin,
       "sbMod420maS4AlarmMax": sbMod420maS4AlarmMax,
       "sbPowerWifi": sbPowerWifi,
       "sbPowerWifiPhase1": sbPowerWifiPhase1,
       "sbPowerWifiPhase1Voltage": sbPowerWifiPhase1Voltage,
       "sbPowerWifiPhase1Current": sbPowerWifiPhase1Current,
       "sbPowerWifiPhase1PowerFactor": sbPowerWifiPhase1PowerFactor,
       "sbPowerWifiPhase1Frequency": sbPowerWifiPhase1Frequency,
       "sbPowerWifiPhase1Power": sbPowerWifiPhase1Power,
       "sbPowerWifiPhase1Temperature": sbPowerWifiPhase1Temperature,
       "sbPowerWifiPhase1MimMaxValues": sbPowerWifiPhase1MimMaxValues,
       "sbPowerWifiMaxPhase1Voltage": sbPowerWifiMaxPhase1Voltage,
       "sbPowerWifiMinPhase1Voltage": sbPowerWifiMinPhase1Voltage,
       "sbPowerWifiMaxPhase1Current": sbPowerWifiMaxPhase1Current,
       "sbPowerWifiMinPhase1Current": sbPowerWifiMinPhase1Current,
       "sbPowerWifiMaxPhase1PowerFactor": sbPowerWifiMaxPhase1PowerFactor,
       "sbPowerWifiMinPhase1PowerFactor": sbPowerWifiMinPhase1PowerFactor,
       "sbPowerWifiMaxPhase1Frequency": sbPowerWifiMaxPhase1Frequency,
       "sbPowerWifiMinPhase1Frequency": sbPowerWifiMinPhase1Frequency,
       "sbPowerWifiMaxPhase1Temperature": sbPowerWifiMaxPhase1Temperature,
       "sbPowerWifiMinPhase1Temperature": sbPowerWifiMinPhase1Temperature,
       "sbPowerWifiPhase2": sbPowerWifiPhase2,
       "sbPowerWifiPhase2Voltage": sbPowerWifiPhase2Voltage,
       "sbPowerWifiPhase2Current": sbPowerWifiPhase2Current,
       "sbPowerWifiPhase2PowerFactor": sbPowerWifiPhase2PowerFactor,
       "sbPowerWifiPhase2Frequency": sbPowerWifiPhase2Frequency,
       "sbPowerWifiPhase2Power": sbPowerWifiPhase2Power,
       "sbPowerWifiPhase2Temperature": sbPowerWifiPhase2Temperature,
       "sbPowerWifiPhase2MimMaxValues": sbPowerWifiPhase2MimMaxValues,
       "sbPowerWifiMaxPhase2Voltage": sbPowerWifiMaxPhase2Voltage,
       "sbPowerWifiMinPhase2Voltage": sbPowerWifiMinPhase2Voltage,
       "sbPowerWifiMaxPhase2Current": sbPowerWifiMaxPhase2Current,
       "sbPowerWifiMinPhase2Current": sbPowerWifiMinPhase2Current,
       "sbPowerWifiMaxPhase2PowerFactor": sbPowerWifiMaxPhase2PowerFactor,
       "sbPowerWifiMinPhase2PowerFactor": sbPowerWifiMinPhase2PowerFactor,
       "sbPowerWifiMaxPhase2Frequency": sbPowerWifiMaxPhase2Frequency,
       "sbPowerWifiMinPhase2Frequency": sbPowerWifiMinPhase2Frequency,
       "sbPowerWifiMaxPhase2Temperature": sbPowerWifiMaxPhase2Temperature,
       "sbPowerWifiMinPhase2Temperature": sbPowerWifiMinPhase2Temperature,
       "sbPowerWifiPhase3": sbPowerWifiPhase3,
       "sbPowerWifiPhase3Voltage": sbPowerWifiPhase3Voltage,
       "sbPowerWifiPhase3Current": sbPowerWifiPhase3Current,
       "sbPowerWifiPhase3PowerFactor": sbPowerWifiPhase3PowerFactor,
       "sbPowerWifiPhase3Frequency": sbPowerWifiPhase3Frequency,
       "sbPowerWifiPhase3Power": sbPowerWifiPhase3Power,
       "sbPowerWifiPhase3Temperature": sbPowerWifiPhase3Temperature,
       "sbPowerWifiPhase3MimMaxValues": sbPowerWifiPhase3MimMaxValues,
       "sbPowerWifiMaxPhase3Voltage": sbPowerWifiMaxPhase3Voltage,
       "sbPowerWifiMinPhase3Voltage": sbPowerWifiMinPhase3Voltage,
       "sbPowerWifiMaxPhase3Current": sbPowerWifiMaxPhase3Current,
       "sbPowerWifiMinPhase3Current": sbPowerWifiMinPhase3Current,
       "sbPowerWifiMaxPhase3PowerFactor": sbPowerWifiMaxPhase3PowerFactor,
       "sbPowerWifiMinPhase3PowerFactor": sbPowerWifiMinPhase3PowerFactor,
       "sbPowerWifiMaxPhase3Frequency": sbPowerWifiMaxPhase3Frequency,
       "sbPowerWifiMinPhase3Frequency": sbPowerWifiMinPhase3Frequency,
       "sbPowerWifiMaxPhase3Temperature": sbPowerWifiMaxPhase3Temperature,
       "sbPowerWifiMinPhase3Temperature": sbPowerWifiMinPhase3Temperature,
       "sbPowerWifiValuesTables": sbPowerWifiValuesTables,
       "sbPowerTablePhase1": sbPowerTablePhase1,
       "sbPowerTable1Entry": sbPowerTable1Entry,
       "sbPowerWifiPhase1TbVoltage": sbPowerWifiPhase1TbVoltage,
       "sbPowerWifiPhase1TbCurrent": sbPowerWifiPhase1TbCurrent,
       "sbPowerWifiPhase1TbPowerFactor": sbPowerWifiPhase1TbPowerFactor,
       "sbPowerWifiPhase1TbFrequency": sbPowerWifiPhase1TbFrequency,
       "sbPowerWifiPhase1TbPower": sbPowerWifiPhase1TbPower,
       "sbPowerWifiPhase1TbTemperature": sbPowerWifiPhase1TbTemperature,
       "sbPowerIndex1": sbPowerIndex1,
       "sbPowerTablePhase2": sbPowerTablePhase2,
       "sbPowerTable2Entry": sbPowerTable2Entry,
       "sbPowerWifiPhase2TbVoltage": sbPowerWifiPhase2TbVoltage,
       "sbPowerWifiPhase2TbCurrent": sbPowerWifiPhase2TbCurrent,
       "sbPowerWifiPhase2TbPowerFactor": sbPowerWifiPhase2TbPowerFactor,
       "sbPowerWifiPhase2TbFrequency": sbPowerWifiPhase2TbFrequency,
       "sbPowerWifiPhase2TbPower": sbPowerWifiPhase2TbPower,
       "sbPowerWifiPhase2TbTemperature": sbPowerWifiPhase2TbTemperature,
       "sbPowerIndex2": sbPowerIndex2,
       "sbPowerTablePhase3": sbPowerTablePhase3,
       "sbPowerTable3Entry": sbPowerTable3Entry,
       "sbPowerWifiPhase3TbVoltage": sbPowerWifiPhase3TbVoltage,
       "sbPowerWifiPhase3TbCurrent": sbPowerWifiPhase3TbCurrent,
       "sbPowerWifiPhase3TbPowerFactor": sbPowerWifiPhase3TbPowerFactor,
       "sbPowerWifiPhase3TbFrequency": sbPowerWifiPhase3TbFrequency,
       "sbPowerWifiPhase3TbPower": sbPowerWifiPhase3TbPower,
       "sbPowerWifiPhase3TbTemperature": sbPowerWifiPhase3TbTemperature,
       "sbPowerIndex3": sbPowerIndex3,
       "sbConfig": sbConfig,
       "sbNetwork": sbNetwork,
       "sbMainSSID": sbMainSSID,
       "sbBackupSSID": sbBackupSSID,
       "sbWatchdog": sbWatchdog,
       "sbWatchdogAloneRelay": sbWatchdogAloneRelay,
       "sbWatchdogRelay1": sbWatchdogRelay1,
       "sbOthers": sbOthers,
       "sbAutoUpdate": sbAutoUpdate,
       "sbNotifications": sbNotifications,
       "sbModNotifierStatus": sbModNotifierStatus,
       "sbModNotifierValueMin": sbModNotifierValueMin,
       "sbModNotifierValueMax": sbModNotifierValueMax,
       "sbModNotifierStateChanged": sbModNotifierStateChanged}
)
