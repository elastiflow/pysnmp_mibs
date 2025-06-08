# SNMP MIB module (KAM-PRO) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kentix_37954/KAM-PRO.mib
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
_Alarmmanager_pro_ObjectIdentity = ObjectIdentity
alarmmanager_pro = _Alarmmanager_pro_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1)
)
_State_ObjectIdentity = ObjectIdentity
state = _State_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 1)
)


class _Alarm1_Type(Integer32):
    """Custom type alarm1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarm1_Type.__name__ = "Integer32"
_Alarm1_Object = MibScalar
alarm1 = _Alarm1_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 1, 4),
    _Alarm1_Type()
)
alarm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarm1.setStatus("mandatory")


class _Alarm2_Type(Integer32):
    """Custom type alarm2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarm2_Type.__name__ = "Integer32"
_Alarm2_Object = MibScalar
alarm2 = _Alarm2_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 1, 5),
    _Alarm2_Type()
)
alarm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarm2.setStatus("mandatory")


class _Serverstate_Type(Integer32):
    """Custom type serverstate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Serverstate_Type.__name__ = "Integer32"
_Serverstate_Object = MibScalar
serverstate = _Serverstate_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 1, 6),
    _Serverstate_Type()
)
serverstate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverstate.setStatus("mandatory")


class _Sensorcommunication_Type(Integer32):
    """Custom type sensorcommunication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sensorcommunication_Type.__name__ = "Integer32"
_Sensorcommunication_Object = MibScalar
sensorcommunication = _Sensorcommunication_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 1, 7),
    _Sensorcommunication_Type()
)
sensorcommunication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorcommunication.setStatus("mandatory")


class _Extalarm_Type(Integer32):
    """Custom type extalarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Extalarm_Type.__name__ = "Integer32"
_Extalarm_Object = MibScalar
extalarm = _Extalarm_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 1, 8),
    _Extalarm_Type()
)
extalarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extalarm.setStatus("mandatory")


class _Extarmed_Type(Integer32):
    """Custom type extarmed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Extarmed_Type.__name__ = "Integer32"
_Extarmed_Object = MibScalar
extarmed = _Extarmed_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 1, 9),
    _Extarmed_Type()
)
extarmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extarmed.setStatus("mandatory")


class _Extpower_Type(Integer32):
    """Custom type extpower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Extpower_Type.__name__ = "Integer32"
_Extpower_Object = MibScalar
extpower = _Extpower_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 1, 10),
    _Extpower_Type()
)
extpower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extpower.setStatus("mandatory")


class _Sabotage_Type(Integer32):
    """Custom type sabotage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Sabotage_Type.__name__ = "Integer32"
_Sabotage_Object = MibScalar
sabotage = _Sabotage_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 1, 11),
    _Sabotage_Type()
)
sabotage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sabotage.setStatus("mandatory")


class _Gsmsignal_Type(Integer32):
    """Custom type gsmsignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Gsmsignal_Type.__name__ = "Integer32"
_Gsmsignal_Object = MibScalar
gsmsignal = _Gsmsignal_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 1, 12),
    _Gsmsignal_Type()
)
gsmsignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmsignal.setStatus("mandatory")


class _Gsmok_Type(Integer32):
    """Custom type gsmok based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_Gsmok_Type.__name__ = "Integer32"
_Gsmok_Object = MibScalar
gsmok = _Gsmok_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 1, 13),
    _Gsmok_Type()
)
gsmok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gsmok.setStatus("mandatory")


class _Systemarmed_Type(Integer32):
    """Custom type systemarmed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Systemarmed_Type.__name__ = "Integer32"
_Systemarmed_Object = MibScalar
systemarmed = _Systemarmed_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 1, 14),
    _Systemarmed_Type()
)
systemarmed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    systemarmed.setStatus("mandatory")


class _Alarmtemp_Type(Integer32):
    """Custom type alarmtemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmtemp_Type.__name__ = "Integer32"
_Alarmtemp_Object = MibScalar
alarmtemp = _Alarmtemp_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 1, 15),
    _Alarmtemp_Type()
)
alarmtemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmtemp.setStatus("mandatory")


class _Alarmhum_Type(Integer32):
    """Custom type alarmhum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmhum_Type.__name__ = "Integer32"
_Alarmhum_Object = MibScalar
alarmhum = _Alarmhum_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 1, 16),
    _Alarmhum_Type()
)
alarmhum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmhum.setStatus("mandatory")


class _Alarmdewpoint_Type(Integer32):
    """Custom type alarmdewpoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmdewpoint_Type.__name__ = "Integer32"
_Alarmdewpoint_Object = MibScalar
alarmdewpoint = _Alarmdewpoint_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 1, 17),
    _Alarmdewpoint_Type()
)
alarmdewpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmdewpoint.setStatus("mandatory")


class _Alarmco_Type(Integer32):
    """Custom type alarmco based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmco_Type.__name__ = "Integer32"
_Alarmco_Object = MibScalar
alarmco = _Alarmco_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 1, 18),
    _Alarmco_Type()
)
alarmco.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmco.setStatus("mandatory")
_Multisensors_ObjectIdentity = ObjectIdentity
multisensors = _Multisensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2)
)
_Multisensor01_ObjectIdentity = ObjectIdentity
multisensor01 = _Multisensor01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 1)
)
_Sensorname01_Type = DisplayString
_Sensorname01_Object = MibScalar
sensorname01 = _Sensorname01_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 1, 1),
    _Sensorname01_Type()
)
sensorname01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname01.setStatus("mandatory")


class _Temperature01_Type(Integer32):
    """Custom type temperature01 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature01_Type.__name__ = "Integer32"
_Temperature01_Object = MibScalar
temperature01 = _Temperature01_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 1, 2),
    _Temperature01_Type()
)
temperature01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature01.setStatus("mandatory")


class _Humidity01_Type(Integer32):
    """Custom type humidity01 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity01_Type.__name__ = "Integer32"
_Humidity01_Object = MibScalar
humidity01 = _Humidity01_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 1, 3),
    _Humidity01_Type()
)
humidity01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity01.setStatus("mandatory")


class _Dewpoint01_Type(Integer32):
    """Custom type dewpoint01 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint01_Type.__name__ = "Integer32"
_Dewpoint01_Object = MibScalar
dewpoint01 = _Dewpoint01_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 1, 4),
    _Dewpoint01_Type()
)
dewpoint01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint01.setStatus("mandatory")


class _Co01_Type(Integer32):
    """Custom type co01 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co01_Type.__name__ = "Integer32"
_Co01_Object = MibScalar
co01 = _Co01_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 1, 5),
    _Co01_Type()
)
co01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co01.setStatus("mandatory")


class _Motion01_Type(Integer32):
    """Custom type motion01 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion01_Type.__name__ = "Integer32"
_Motion01_Object = MibScalar
motion01 = _Motion01_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 1, 6),
    _Motion01_Type()
)
motion01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion01.setStatus("mandatory")


class _Digitalin101_Type(Integer32):
    """Custom type digitalin101 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin101_Type.__name__ = "Integer32"
_Digitalin101_Object = MibScalar
digitalin101 = _Digitalin101_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 1, 7),
    _Digitalin101_Type()
)
digitalin101.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin101.setStatus("mandatory")


class _Digitalin201_Type(Integer32):
    """Custom type digitalin201 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin201_Type.__name__ = "Integer32"
_Digitalin201_Object = MibScalar
digitalin201 = _Digitalin201_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 1, 8),
    _Digitalin201_Type()
)
digitalin201.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin201.setStatus("mandatory")


class _Digitalout201_Type(Integer32):
    """Custom type digitalout201 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout201_Type.__name__ = "Integer32"
_Digitalout201_Object = MibScalar
digitalout201 = _Digitalout201_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 1, 9),
    _Digitalout201_Type()
)
digitalout201.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout201.setStatus("mandatory")


class _ComError01_Type(Integer32):
    """Custom type comError01 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError01_Type.__name__ = "Integer32"
_ComError01_Object = MibScalar
comError01 = _ComError01_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 1, 10),
    _ComError01_Type()
)
comError01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError01.setStatus("mandatory")
_Multisensor02_ObjectIdentity = ObjectIdentity
multisensor02 = _Multisensor02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 2)
)
_Sensorname02_Type = DisplayString
_Sensorname02_Object = MibScalar
sensorname02 = _Sensorname02_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 2, 1),
    _Sensorname02_Type()
)
sensorname02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname02.setStatus("mandatory")


class _Temperature02_Type(Integer32):
    """Custom type temperature02 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature02_Type.__name__ = "Integer32"
_Temperature02_Object = MibScalar
temperature02 = _Temperature02_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 2, 2),
    _Temperature02_Type()
)
temperature02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature02.setStatus("mandatory")


class _Humidity02_Type(Integer32):
    """Custom type humidity02 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity02_Type.__name__ = "Integer32"
_Humidity02_Object = MibScalar
humidity02 = _Humidity02_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 2, 3),
    _Humidity02_Type()
)
humidity02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity02.setStatus("mandatory")


class _Dewpoint02_Type(Integer32):
    """Custom type dewpoint02 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint02_Type.__name__ = "Integer32"
_Dewpoint02_Object = MibScalar
dewpoint02 = _Dewpoint02_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 2, 4),
    _Dewpoint02_Type()
)
dewpoint02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint02.setStatus("mandatory")


class _Co02_Type(Integer32):
    """Custom type co02 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co02_Type.__name__ = "Integer32"
_Co02_Object = MibScalar
co02 = _Co02_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 2, 5),
    _Co02_Type()
)
co02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co02.setStatus("mandatory")


class _Motion02_Type(Integer32):
    """Custom type motion02 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion02_Type.__name__ = "Integer32"
_Motion02_Object = MibScalar
motion02 = _Motion02_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 2, 6),
    _Motion02_Type()
)
motion02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion02.setStatus("mandatory")


class _Digitalin102_Type(Integer32):
    """Custom type digitalin102 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin102_Type.__name__ = "Integer32"
_Digitalin102_Object = MibScalar
digitalin102 = _Digitalin102_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 2, 7),
    _Digitalin102_Type()
)
digitalin102.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin102.setStatus("mandatory")


class _Digitalin202_Type(Integer32):
    """Custom type digitalin202 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin202_Type.__name__ = "Integer32"
_Digitalin202_Object = MibScalar
digitalin202 = _Digitalin202_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 2, 8),
    _Digitalin202_Type()
)
digitalin202.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin202.setStatus("mandatory")


class _Digitalout202_Type(Integer32):
    """Custom type digitalout202 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout202_Type.__name__ = "Integer32"
_Digitalout202_Object = MibScalar
digitalout202 = _Digitalout202_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 2, 9),
    _Digitalout202_Type()
)
digitalout202.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout202.setStatus("mandatory")


class _ComError02_Type(Integer32):
    """Custom type comError02 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError02_Type.__name__ = "Integer32"
_ComError02_Object = MibScalar
comError02 = _ComError02_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 2, 10),
    _ComError02_Type()
)
comError02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError02.setStatus("mandatory")
_Multisensor03_ObjectIdentity = ObjectIdentity
multisensor03 = _Multisensor03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 3)
)
_Sensorname03_Type = DisplayString
_Sensorname03_Object = MibScalar
sensorname03 = _Sensorname03_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 3, 1),
    _Sensorname03_Type()
)
sensorname03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname03.setStatus("mandatory")


class _Temperature03_Type(Integer32):
    """Custom type temperature03 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature03_Type.__name__ = "Integer32"
_Temperature03_Object = MibScalar
temperature03 = _Temperature03_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 3, 2),
    _Temperature03_Type()
)
temperature03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature03.setStatus("mandatory")


class _Humidity03_Type(Integer32):
    """Custom type humidity03 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity03_Type.__name__ = "Integer32"
_Humidity03_Object = MibScalar
humidity03 = _Humidity03_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 3, 3),
    _Humidity03_Type()
)
humidity03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity03.setStatus("mandatory")


class _Dewpoint03_Type(Integer32):
    """Custom type dewpoint03 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint03_Type.__name__ = "Integer32"
_Dewpoint03_Object = MibScalar
dewpoint03 = _Dewpoint03_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 3, 4),
    _Dewpoint03_Type()
)
dewpoint03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint03.setStatus("mandatory")


class _Co03_Type(Integer32):
    """Custom type co03 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co03_Type.__name__ = "Integer32"
_Co03_Object = MibScalar
co03 = _Co03_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 3, 5),
    _Co03_Type()
)
co03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co03.setStatus("mandatory")


class _Motion03_Type(Integer32):
    """Custom type motion03 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion03_Type.__name__ = "Integer32"
_Motion03_Object = MibScalar
motion03 = _Motion03_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 3, 6),
    _Motion03_Type()
)
motion03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion03.setStatus("mandatory")


class _Digitalin103_Type(Integer32):
    """Custom type digitalin103 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin103_Type.__name__ = "Integer32"
_Digitalin103_Object = MibScalar
digitalin103 = _Digitalin103_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 3, 7),
    _Digitalin103_Type()
)
digitalin103.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin103.setStatus("mandatory")


class _Digitalin203_Type(Integer32):
    """Custom type digitalin203 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin203_Type.__name__ = "Integer32"
_Digitalin203_Object = MibScalar
digitalin203 = _Digitalin203_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 3, 8),
    _Digitalin203_Type()
)
digitalin203.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin203.setStatus("mandatory")


class _Digitalout203_Type(Integer32):
    """Custom type digitalout203 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout203_Type.__name__ = "Integer32"
_Digitalout203_Object = MibScalar
digitalout203 = _Digitalout203_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 3, 9),
    _Digitalout203_Type()
)
digitalout203.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout203.setStatus("mandatory")


class _ComError03_Type(Integer32):
    """Custom type comError03 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError03_Type.__name__ = "Integer32"
_ComError03_Object = MibScalar
comError03 = _ComError03_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 3, 10),
    _ComError03_Type()
)
comError03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError03.setStatus("mandatory")
_Multisensor04_ObjectIdentity = ObjectIdentity
multisensor04 = _Multisensor04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 4)
)
_Sensorname04_Type = DisplayString
_Sensorname04_Object = MibScalar
sensorname04 = _Sensorname04_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 4, 1),
    _Sensorname04_Type()
)
sensorname04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname04.setStatus("mandatory")


class _Temperature04_Type(Integer32):
    """Custom type temperature04 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature04_Type.__name__ = "Integer32"
_Temperature04_Object = MibScalar
temperature04 = _Temperature04_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 4, 2),
    _Temperature04_Type()
)
temperature04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature04.setStatus("mandatory")


class _Humidity04_Type(Integer32):
    """Custom type humidity04 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity04_Type.__name__ = "Integer32"
_Humidity04_Object = MibScalar
humidity04 = _Humidity04_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 4, 3),
    _Humidity04_Type()
)
humidity04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity04.setStatus("mandatory")


class _Dewpoint04_Type(Integer32):
    """Custom type dewpoint04 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint04_Type.__name__ = "Integer32"
_Dewpoint04_Object = MibScalar
dewpoint04 = _Dewpoint04_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 4, 4),
    _Dewpoint04_Type()
)
dewpoint04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint04.setStatus("mandatory")


class _Co04_Type(Integer32):
    """Custom type co04 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co04_Type.__name__ = "Integer32"
_Co04_Object = MibScalar
co04 = _Co04_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 4, 5),
    _Co04_Type()
)
co04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co04.setStatus("mandatory")


class _Motion04_Type(Integer32):
    """Custom type motion04 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion04_Type.__name__ = "Integer32"
_Motion04_Object = MibScalar
motion04 = _Motion04_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 4, 6),
    _Motion04_Type()
)
motion04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion04.setStatus("mandatory")


class _Digitalin104_Type(Integer32):
    """Custom type digitalin104 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin104_Type.__name__ = "Integer32"
_Digitalin104_Object = MibScalar
digitalin104 = _Digitalin104_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 4, 7),
    _Digitalin104_Type()
)
digitalin104.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin104.setStatus("mandatory")


class _Digitalin204_Type(Integer32):
    """Custom type digitalin204 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin204_Type.__name__ = "Integer32"
_Digitalin204_Object = MibScalar
digitalin204 = _Digitalin204_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 4, 8),
    _Digitalin204_Type()
)
digitalin204.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin204.setStatus("mandatory")


class _Digitalout204_Type(Integer32):
    """Custom type digitalout204 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout204_Type.__name__ = "Integer32"
_Digitalout204_Object = MibScalar
digitalout204 = _Digitalout204_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 4, 9),
    _Digitalout204_Type()
)
digitalout204.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout204.setStatus("mandatory")


class _ComError04_Type(Integer32):
    """Custom type comError04 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError04_Type.__name__ = "Integer32"
_ComError04_Object = MibScalar
comError04 = _ComError04_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 4, 10),
    _ComError04_Type()
)
comError04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError04.setStatus("mandatory")
_Multisensor05_ObjectIdentity = ObjectIdentity
multisensor05 = _Multisensor05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 5)
)
_Sensorname05_Type = DisplayString
_Sensorname05_Object = MibScalar
sensorname05 = _Sensorname05_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 5, 1),
    _Sensorname05_Type()
)
sensorname05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname05.setStatus("mandatory")


class _Temperature05_Type(Integer32):
    """Custom type temperature05 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature05_Type.__name__ = "Integer32"
_Temperature05_Object = MibScalar
temperature05 = _Temperature05_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 5, 2),
    _Temperature05_Type()
)
temperature05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature05.setStatus("mandatory")


class _Humidity05_Type(Integer32):
    """Custom type humidity05 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity05_Type.__name__ = "Integer32"
_Humidity05_Object = MibScalar
humidity05 = _Humidity05_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 5, 3),
    _Humidity05_Type()
)
humidity05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity05.setStatus("mandatory")


class _Dewpoint05_Type(Integer32):
    """Custom type dewpoint05 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint05_Type.__name__ = "Integer32"
_Dewpoint05_Object = MibScalar
dewpoint05 = _Dewpoint05_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 5, 4),
    _Dewpoint05_Type()
)
dewpoint05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint05.setStatus("mandatory")


class _Co05_Type(Integer32):
    """Custom type co05 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co05_Type.__name__ = "Integer32"
_Co05_Object = MibScalar
co05 = _Co05_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 5, 5),
    _Co05_Type()
)
co05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co05.setStatus("mandatory")


class _Motion05_Type(Integer32):
    """Custom type motion05 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion05_Type.__name__ = "Integer32"
_Motion05_Object = MibScalar
motion05 = _Motion05_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 5, 6),
    _Motion05_Type()
)
motion05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion05.setStatus("mandatory")


class _Digitalin105_Type(Integer32):
    """Custom type digitalin105 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin105_Type.__name__ = "Integer32"
_Digitalin105_Object = MibScalar
digitalin105 = _Digitalin105_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 5, 7),
    _Digitalin105_Type()
)
digitalin105.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin105.setStatus("mandatory")


class _Digitalin205_Type(Integer32):
    """Custom type digitalin205 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin205_Type.__name__ = "Integer32"
_Digitalin205_Object = MibScalar
digitalin205 = _Digitalin205_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 5, 8),
    _Digitalin205_Type()
)
digitalin205.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin205.setStatus("mandatory")


class _Digitalout205_Type(Integer32):
    """Custom type digitalout205 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout205_Type.__name__ = "Integer32"
_Digitalout205_Object = MibScalar
digitalout205 = _Digitalout205_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 5, 9),
    _Digitalout205_Type()
)
digitalout205.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout205.setStatus("mandatory")


class _ComError05_Type(Integer32):
    """Custom type comError05 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError05_Type.__name__ = "Integer32"
_ComError05_Object = MibScalar
comError05 = _ComError05_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 5, 10),
    _ComError05_Type()
)
comError05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError05.setStatus("mandatory")
_Multisensor06_ObjectIdentity = ObjectIdentity
multisensor06 = _Multisensor06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 6)
)
_Sensorname06_Type = DisplayString
_Sensorname06_Object = MibScalar
sensorname06 = _Sensorname06_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 6, 1),
    _Sensorname06_Type()
)
sensorname06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname06.setStatus("mandatory")


class _Temperature06_Type(Integer32):
    """Custom type temperature06 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature06_Type.__name__ = "Integer32"
_Temperature06_Object = MibScalar
temperature06 = _Temperature06_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 6, 2),
    _Temperature06_Type()
)
temperature06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature06.setStatus("mandatory")


class _Humidity06_Type(Integer32):
    """Custom type humidity06 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity06_Type.__name__ = "Integer32"
_Humidity06_Object = MibScalar
humidity06 = _Humidity06_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 6, 3),
    _Humidity06_Type()
)
humidity06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity06.setStatus("mandatory")


class _Dewpoint06_Type(Integer32):
    """Custom type dewpoint06 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint06_Type.__name__ = "Integer32"
_Dewpoint06_Object = MibScalar
dewpoint06 = _Dewpoint06_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 6, 4),
    _Dewpoint06_Type()
)
dewpoint06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint06.setStatus("mandatory")


class _Co06_Type(Integer32):
    """Custom type co06 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co06_Type.__name__ = "Integer32"
_Co06_Object = MibScalar
co06 = _Co06_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 6, 5),
    _Co06_Type()
)
co06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co06.setStatus("mandatory")


class _Motion06_Type(Integer32):
    """Custom type motion06 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion06_Type.__name__ = "Integer32"
_Motion06_Object = MibScalar
motion06 = _Motion06_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 6, 6),
    _Motion06_Type()
)
motion06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion06.setStatus("mandatory")


class _Digitalin106_Type(Integer32):
    """Custom type digitalin106 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin106_Type.__name__ = "Integer32"
_Digitalin106_Object = MibScalar
digitalin106 = _Digitalin106_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 6, 7),
    _Digitalin106_Type()
)
digitalin106.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin106.setStatus("mandatory")


class _Digitalin206_Type(Integer32):
    """Custom type digitalin206 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin206_Type.__name__ = "Integer32"
_Digitalin206_Object = MibScalar
digitalin206 = _Digitalin206_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 6, 8),
    _Digitalin206_Type()
)
digitalin206.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin206.setStatus("mandatory")


class _Digitalout206_Type(Integer32):
    """Custom type digitalout206 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout206_Type.__name__ = "Integer32"
_Digitalout206_Object = MibScalar
digitalout206 = _Digitalout206_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 6, 9),
    _Digitalout206_Type()
)
digitalout206.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout206.setStatus("mandatory")


class _ComError06_Type(Integer32):
    """Custom type comError06 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError06_Type.__name__ = "Integer32"
_ComError06_Object = MibScalar
comError06 = _ComError06_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 6, 10),
    _ComError06_Type()
)
comError06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError06.setStatus("mandatory")
_Multisensor07_ObjectIdentity = ObjectIdentity
multisensor07 = _Multisensor07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 7)
)
_Sensorname07_Type = DisplayString
_Sensorname07_Object = MibScalar
sensorname07 = _Sensorname07_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 7, 1),
    _Sensorname07_Type()
)
sensorname07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname07.setStatus("mandatory")


class _Temperature07_Type(Integer32):
    """Custom type temperature07 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature07_Type.__name__ = "Integer32"
_Temperature07_Object = MibScalar
temperature07 = _Temperature07_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 7, 2),
    _Temperature07_Type()
)
temperature07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature07.setStatus("mandatory")


class _Humidity07_Type(Integer32):
    """Custom type humidity07 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity07_Type.__name__ = "Integer32"
_Humidity07_Object = MibScalar
humidity07 = _Humidity07_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 7, 3),
    _Humidity07_Type()
)
humidity07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity07.setStatus("mandatory")


class _Dewpoint07_Type(Integer32):
    """Custom type dewpoint07 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint07_Type.__name__ = "Integer32"
_Dewpoint07_Object = MibScalar
dewpoint07 = _Dewpoint07_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 7, 4),
    _Dewpoint07_Type()
)
dewpoint07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint07.setStatus("mandatory")


class _Co07_Type(Integer32):
    """Custom type co07 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co07_Type.__name__ = "Integer32"
_Co07_Object = MibScalar
co07 = _Co07_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 7, 5),
    _Co07_Type()
)
co07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co07.setStatus("mandatory")


class _Motion07_Type(Integer32):
    """Custom type motion07 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion07_Type.__name__ = "Integer32"
_Motion07_Object = MibScalar
motion07 = _Motion07_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 7, 6),
    _Motion07_Type()
)
motion07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion07.setStatus("mandatory")


class _Digitalin107_Type(Integer32):
    """Custom type digitalin107 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin107_Type.__name__ = "Integer32"
_Digitalin107_Object = MibScalar
digitalin107 = _Digitalin107_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 7, 7),
    _Digitalin107_Type()
)
digitalin107.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin107.setStatus("mandatory")


class _Digitalin207_Type(Integer32):
    """Custom type digitalin207 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin207_Type.__name__ = "Integer32"
_Digitalin207_Object = MibScalar
digitalin207 = _Digitalin207_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 7, 8),
    _Digitalin207_Type()
)
digitalin207.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin207.setStatus("mandatory")


class _Digitalout207_Type(Integer32):
    """Custom type digitalout207 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout207_Type.__name__ = "Integer32"
_Digitalout207_Object = MibScalar
digitalout207 = _Digitalout207_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 7, 9),
    _Digitalout207_Type()
)
digitalout207.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout207.setStatus("mandatory")


class _ComError07_Type(Integer32):
    """Custom type comError07 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError07_Type.__name__ = "Integer32"
_ComError07_Object = MibScalar
comError07 = _ComError07_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 7, 10),
    _ComError07_Type()
)
comError07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError07.setStatus("mandatory")
_Multisensor08_ObjectIdentity = ObjectIdentity
multisensor08 = _Multisensor08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 8)
)
_Sensorname08_Type = DisplayString
_Sensorname08_Object = MibScalar
sensorname08 = _Sensorname08_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 8, 1),
    _Sensorname08_Type()
)
sensorname08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname08.setStatus("mandatory")


class _Temperature08_Type(Integer32):
    """Custom type temperature08 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature08_Type.__name__ = "Integer32"
_Temperature08_Object = MibScalar
temperature08 = _Temperature08_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 8, 2),
    _Temperature08_Type()
)
temperature08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature08.setStatus("mandatory")


class _Humidity08_Type(Integer32):
    """Custom type humidity08 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity08_Type.__name__ = "Integer32"
_Humidity08_Object = MibScalar
humidity08 = _Humidity08_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 8, 3),
    _Humidity08_Type()
)
humidity08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity08.setStatus("mandatory")


class _Dewpoint08_Type(Integer32):
    """Custom type dewpoint08 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint08_Type.__name__ = "Integer32"
_Dewpoint08_Object = MibScalar
dewpoint08 = _Dewpoint08_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 8, 4),
    _Dewpoint08_Type()
)
dewpoint08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint08.setStatus("mandatory")


class _Co08_Type(Integer32):
    """Custom type co08 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co08_Type.__name__ = "Integer32"
_Co08_Object = MibScalar
co08 = _Co08_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 8, 5),
    _Co08_Type()
)
co08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co08.setStatus("mandatory")


class _Motion08_Type(Integer32):
    """Custom type motion08 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion08_Type.__name__ = "Integer32"
_Motion08_Object = MibScalar
motion08 = _Motion08_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 8, 6),
    _Motion08_Type()
)
motion08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion08.setStatus("mandatory")


class _Digitalin108_Type(Integer32):
    """Custom type digitalin108 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin108_Type.__name__ = "Integer32"
_Digitalin108_Object = MibScalar
digitalin108 = _Digitalin108_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 8, 7),
    _Digitalin108_Type()
)
digitalin108.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin108.setStatus("mandatory")


class _Digitalin208_Type(Integer32):
    """Custom type digitalin208 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin208_Type.__name__ = "Integer32"
_Digitalin208_Object = MibScalar
digitalin208 = _Digitalin208_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 8, 8),
    _Digitalin208_Type()
)
digitalin208.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin208.setStatus("mandatory")


class _Digitalout208_Type(Integer32):
    """Custom type digitalout208 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout208_Type.__name__ = "Integer32"
_Digitalout208_Object = MibScalar
digitalout208 = _Digitalout208_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 8, 9),
    _Digitalout208_Type()
)
digitalout208.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout208.setStatus("mandatory")


class _ComError08_Type(Integer32):
    """Custom type comError08 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError08_Type.__name__ = "Integer32"
_ComError08_Object = MibScalar
comError08 = _ComError08_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 8, 10),
    _ComError08_Type()
)
comError08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError08.setStatus("mandatory")
_Multisensor09_ObjectIdentity = ObjectIdentity
multisensor09 = _Multisensor09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 9)
)
_Sensorname09_Type = DisplayString
_Sensorname09_Object = MibScalar
sensorname09 = _Sensorname09_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 9, 1),
    _Sensorname09_Type()
)
sensorname09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname09.setStatus("mandatory")


class _Temperature09_Type(Integer32):
    """Custom type temperature09 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature09_Type.__name__ = "Integer32"
_Temperature09_Object = MibScalar
temperature09 = _Temperature09_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 9, 2),
    _Temperature09_Type()
)
temperature09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature09.setStatus("mandatory")


class _Humidity09_Type(Integer32):
    """Custom type humidity09 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity09_Type.__name__ = "Integer32"
_Humidity09_Object = MibScalar
humidity09 = _Humidity09_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 9, 3),
    _Humidity09_Type()
)
humidity09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity09.setStatus("mandatory")


class _Dewpoint09_Type(Integer32):
    """Custom type dewpoint09 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint09_Type.__name__ = "Integer32"
_Dewpoint09_Object = MibScalar
dewpoint09 = _Dewpoint09_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 9, 4),
    _Dewpoint09_Type()
)
dewpoint09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint09.setStatus("mandatory")


class _Co09_Type(Integer32):
    """Custom type co09 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co09_Type.__name__ = "Integer32"
_Co09_Object = MibScalar
co09 = _Co09_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 9, 5),
    _Co09_Type()
)
co09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co09.setStatus("mandatory")


class _Motion09_Type(Integer32):
    """Custom type motion09 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion09_Type.__name__ = "Integer32"
_Motion09_Object = MibScalar
motion09 = _Motion09_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 9, 6),
    _Motion09_Type()
)
motion09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion09.setStatus("mandatory")


class _Digitalin109_Type(Integer32):
    """Custom type digitalin109 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin109_Type.__name__ = "Integer32"
_Digitalin109_Object = MibScalar
digitalin109 = _Digitalin109_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 9, 7),
    _Digitalin109_Type()
)
digitalin109.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin109.setStatus("mandatory")


class _Digitalin209_Type(Integer32):
    """Custom type digitalin209 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin209_Type.__name__ = "Integer32"
_Digitalin209_Object = MibScalar
digitalin209 = _Digitalin209_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 9, 8),
    _Digitalin209_Type()
)
digitalin209.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin209.setStatus("mandatory")


class _Digitalout209_Type(Integer32):
    """Custom type digitalout209 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout209_Type.__name__ = "Integer32"
_Digitalout209_Object = MibScalar
digitalout209 = _Digitalout209_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 9, 9),
    _Digitalout209_Type()
)
digitalout209.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout209.setStatus("mandatory")


class _ComError09_Type(Integer32):
    """Custom type comError09 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError09_Type.__name__ = "Integer32"
_ComError09_Object = MibScalar
comError09 = _ComError09_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 9, 10),
    _ComError09_Type()
)
comError09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError09.setStatus("mandatory")
_Multisensor10_ObjectIdentity = ObjectIdentity
multisensor10 = _Multisensor10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 10)
)
_Sensorname10_Type = DisplayString
_Sensorname10_Object = MibScalar
sensorname10 = _Sensorname10_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 10, 1),
    _Sensorname10_Type()
)
sensorname10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname10.setStatus("mandatory")


class _Temperature10_Type(Integer32):
    """Custom type temperature10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature10_Type.__name__ = "Integer32"
_Temperature10_Object = MibScalar
temperature10 = _Temperature10_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 10, 2),
    _Temperature10_Type()
)
temperature10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature10.setStatus("mandatory")


class _Humidity10_Type(Integer32):
    """Custom type humidity10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity10_Type.__name__ = "Integer32"
_Humidity10_Object = MibScalar
humidity10 = _Humidity10_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 10, 3),
    _Humidity10_Type()
)
humidity10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity10.setStatus("mandatory")


class _Dewpoint10_Type(Integer32):
    """Custom type dewpoint10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint10_Type.__name__ = "Integer32"
_Dewpoint10_Object = MibScalar
dewpoint10 = _Dewpoint10_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 10, 4),
    _Dewpoint10_Type()
)
dewpoint10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint10.setStatus("mandatory")


class _Co10_Type(Integer32):
    """Custom type co10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co10_Type.__name__ = "Integer32"
_Co10_Object = MibScalar
co10 = _Co10_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 10, 5),
    _Co10_Type()
)
co10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co10.setStatus("mandatory")


class _Motion10_Type(Integer32):
    """Custom type motion10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion10_Type.__name__ = "Integer32"
_Motion10_Object = MibScalar
motion10 = _Motion10_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 10, 6),
    _Motion10_Type()
)
motion10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion10.setStatus("mandatory")


class _Digitalin110_Type(Integer32):
    """Custom type digitalin110 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin110_Type.__name__ = "Integer32"
_Digitalin110_Object = MibScalar
digitalin110 = _Digitalin110_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 10, 7),
    _Digitalin110_Type()
)
digitalin110.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin110.setStatus("mandatory")


class _Digitalin210_Type(Integer32):
    """Custom type digitalin210 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin210_Type.__name__ = "Integer32"
_Digitalin210_Object = MibScalar
digitalin210 = _Digitalin210_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 10, 8),
    _Digitalin210_Type()
)
digitalin210.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin210.setStatus("mandatory")


class _Digitalout210_Type(Integer32):
    """Custom type digitalout210 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout210_Type.__name__ = "Integer32"
_Digitalout210_Object = MibScalar
digitalout210 = _Digitalout210_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 10, 9),
    _Digitalout210_Type()
)
digitalout210.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout210.setStatus("mandatory")


class _ComError10_Type(Integer32):
    """Custom type comError10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError10_Type.__name__ = "Integer32"
_ComError10_Object = MibScalar
comError10 = _ComError10_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 10, 10),
    _ComError10_Type()
)
comError10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError10.setStatus("mandatory")
_Multisensor11_ObjectIdentity = ObjectIdentity
multisensor11 = _Multisensor11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 11)
)
_Sensorname11_Type = DisplayString
_Sensorname11_Object = MibScalar
sensorname11 = _Sensorname11_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 11, 1),
    _Sensorname11_Type()
)
sensorname11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname11.setStatus("mandatory")


class _Temperature11_Type(Integer32):
    """Custom type temperature11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature11_Type.__name__ = "Integer32"
_Temperature11_Object = MibScalar
temperature11 = _Temperature11_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 11, 2),
    _Temperature11_Type()
)
temperature11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature11.setStatus("mandatory")


class _Humidity11_Type(Integer32):
    """Custom type humidity11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity11_Type.__name__ = "Integer32"
_Humidity11_Object = MibScalar
humidity11 = _Humidity11_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 11, 3),
    _Humidity11_Type()
)
humidity11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity11.setStatus("mandatory")


class _Dewpoint11_Type(Integer32):
    """Custom type dewpoint11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint11_Type.__name__ = "Integer32"
_Dewpoint11_Object = MibScalar
dewpoint11 = _Dewpoint11_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 11, 4),
    _Dewpoint11_Type()
)
dewpoint11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint11.setStatus("mandatory")


class _Co11_Type(Integer32):
    """Custom type co11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co11_Type.__name__ = "Integer32"
_Co11_Object = MibScalar
co11 = _Co11_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 11, 5),
    _Co11_Type()
)
co11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co11.setStatus("mandatory")


class _Motion11_Type(Integer32):
    """Custom type motion11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion11_Type.__name__ = "Integer32"
_Motion11_Object = MibScalar
motion11 = _Motion11_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 11, 6),
    _Motion11_Type()
)
motion11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion11.setStatus("mandatory")


class _Digitalin111_Type(Integer32):
    """Custom type digitalin111 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin111_Type.__name__ = "Integer32"
_Digitalin111_Object = MibScalar
digitalin111 = _Digitalin111_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 11, 7),
    _Digitalin111_Type()
)
digitalin111.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin111.setStatus("mandatory")


class _Digitalin211_Type(Integer32):
    """Custom type digitalin211 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin211_Type.__name__ = "Integer32"
_Digitalin211_Object = MibScalar
digitalin211 = _Digitalin211_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 11, 8),
    _Digitalin211_Type()
)
digitalin211.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin211.setStatus("mandatory")


class _Digitalout211_Type(Integer32):
    """Custom type digitalout211 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout211_Type.__name__ = "Integer32"
_Digitalout211_Object = MibScalar
digitalout211 = _Digitalout211_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 11, 9),
    _Digitalout211_Type()
)
digitalout211.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout211.setStatus("mandatory")


class _ComError11_Type(Integer32):
    """Custom type comError11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError11_Type.__name__ = "Integer32"
_ComError11_Object = MibScalar
comError11 = _ComError11_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 11, 10),
    _ComError11_Type()
)
comError11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError11.setStatus("mandatory")
_Multisensor12_ObjectIdentity = ObjectIdentity
multisensor12 = _Multisensor12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 12)
)
_Sensorname12_Type = DisplayString
_Sensorname12_Object = MibScalar
sensorname12 = _Sensorname12_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 12, 1),
    _Sensorname12_Type()
)
sensorname12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname12.setStatus("mandatory")


class _Temperature12_Type(Integer32):
    """Custom type temperature12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature12_Type.__name__ = "Integer32"
_Temperature12_Object = MibScalar
temperature12 = _Temperature12_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 12, 2),
    _Temperature12_Type()
)
temperature12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature12.setStatus("mandatory")


class _Humidity12_Type(Integer32):
    """Custom type humidity12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity12_Type.__name__ = "Integer32"
_Humidity12_Object = MibScalar
humidity12 = _Humidity12_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 12, 3),
    _Humidity12_Type()
)
humidity12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity12.setStatus("mandatory")


class _Dewpoint12_Type(Integer32):
    """Custom type dewpoint12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint12_Type.__name__ = "Integer32"
_Dewpoint12_Object = MibScalar
dewpoint12 = _Dewpoint12_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 12, 4),
    _Dewpoint12_Type()
)
dewpoint12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint12.setStatus("mandatory")


class _Co12_Type(Integer32):
    """Custom type co12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co12_Type.__name__ = "Integer32"
_Co12_Object = MibScalar
co12 = _Co12_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 12, 5),
    _Co12_Type()
)
co12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co12.setStatus("mandatory")


class _Motion12_Type(Integer32):
    """Custom type motion12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion12_Type.__name__ = "Integer32"
_Motion12_Object = MibScalar
motion12 = _Motion12_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 12, 6),
    _Motion12_Type()
)
motion12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion12.setStatus("mandatory")


class _Digitalin112_Type(Integer32):
    """Custom type digitalin112 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin112_Type.__name__ = "Integer32"
_Digitalin112_Object = MibScalar
digitalin112 = _Digitalin112_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 12, 7),
    _Digitalin112_Type()
)
digitalin112.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin112.setStatus("mandatory")


class _Digitalin212_Type(Integer32):
    """Custom type digitalin212 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin212_Type.__name__ = "Integer32"
_Digitalin212_Object = MibScalar
digitalin212 = _Digitalin212_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 12, 8),
    _Digitalin212_Type()
)
digitalin212.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin212.setStatus("mandatory")


class _Digitalout212_Type(Integer32):
    """Custom type digitalout212 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout212_Type.__name__ = "Integer32"
_Digitalout212_Object = MibScalar
digitalout212 = _Digitalout212_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 12, 9),
    _Digitalout212_Type()
)
digitalout212.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout212.setStatus("mandatory")


class _ComError12_Type(Integer32):
    """Custom type comError12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError12_Type.__name__ = "Integer32"
_ComError12_Object = MibScalar
comError12 = _ComError12_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 12, 10),
    _ComError12_Type()
)
comError12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError12.setStatus("mandatory")
_Multisensor13_ObjectIdentity = ObjectIdentity
multisensor13 = _Multisensor13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 13)
)
_Sensorname13_Type = DisplayString
_Sensorname13_Object = MibScalar
sensorname13 = _Sensorname13_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 13, 1),
    _Sensorname13_Type()
)
sensorname13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname13.setStatus("mandatory")


class _Temperature13_Type(Integer32):
    """Custom type temperature13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature13_Type.__name__ = "Integer32"
_Temperature13_Object = MibScalar
temperature13 = _Temperature13_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 13, 2),
    _Temperature13_Type()
)
temperature13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature13.setStatus("mandatory")


class _Humidity13_Type(Integer32):
    """Custom type humidity13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity13_Type.__name__ = "Integer32"
_Humidity13_Object = MibScalar
humidity13 = _Humidity13_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 13, 3),
    _Humidity13_Type()
)
humidity13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity13.setStatus("mandatory")


class _Dewpoint13_Type(Integer32):
    """Custom type dewpoint13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint13_Type.__name__ = "Integer32"
_Dewpoint13_Object = MibScalar
dewpoint13 = _Dewpoint13_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 13, 4),
    _Dewpoint13_Type()
)
dewpoint13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint13.setStatus("mandatory")


class _Co13_Type(Integer32):
    """Custom type co13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co13_Type.__name__ = "Integer32"
_Co13_Object = MibScalar
co13 = _Co13_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 13, 5),
    _Co13_Type()
)
co13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co13.setStatus("mandatory")


class _Motion13_Type(Integer32):
    """Custom type motion13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion13_Type.__name__ = "Integer32"
_Motion13_Object = MibScalar
motion13 = _Motion13_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 13, 6),
    _Motion13_Type()
)
motion13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion13.setStatus("mandatory")


class _Digitalin113_Type(Integer32):
    """Custom type digitalin113 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin113_Type.__name__ = "Integer32"
_Digitalin113_Object = MibScalar
digitalin113 = _Digitalin113_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 13, 7),
    _Digitalin113_Type()
)
digitalin113.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin113.setStatus("mandatory")


class _Digitalin213_Type(Integer32):
    """Custom type digitalin213 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin213_Type.__name__ = "Integer32"
_Digitalin213_Object = MibScalar
digitalin213 = _Digitalin213_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 13, 8),
    _Digitalin213_Type()
)
digitalin213.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin213.setStatus("mandatory")


class _Digitalout213_Type(Integer32):
    """Custom type digitalout213 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout213_Type.__name__ = "Integer32"
_Digitalout213_Object = MibScalar
digitalout213 = _Digitalout213_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 13, 9),
    _Digitalout213_Type()
)
digitalout213.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout213.setStatus("mandatory")


class _ComError13_Type(Integer32):
    """Custom type comError13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError13_Type.__name__ = "Integer32"
_ComError13_Object = MibScalar
comError13 = _ComError13_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 13, 10),
    _ComError13_Type()
)
comError13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError13.setStatus("mandatory")
_Multisensor14_ObjectIdentity = ObjectIdentity
multisensor14 = _Multisensor14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 14)
)
_Sensorname14_Type = DisplayString
_Sensorname14_Object = MibScalar
sensorname14 = _Sensorname14_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 14, 1),
    _Sensorname14_Type()
)
sensorname14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname14.setStatus("mandatory")


class _Temperature14_Type(Integer32):
    """Custom type temperature14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature14_Type.__name__ = "Integer32"
_Temperature14_Object = MibScalar
temperature14 = _Temperature14_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 14, 2),
    _Temperature14_Type()
)
temperature14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature14.setStatus("mandatory")


class _Humidity14_Type(Integer32):
    """Custom type humidity14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity14_Type.__name__ = "Integer32"
_Humidity14_Object = MibScalar
humidity14 = _Humidity14_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 14, 3),
    _Humidity14_Type()
)
humidity14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity14.setStatus("mandatory")


class _Dewpoint14_Type(Integer32):
    """Custom type dewpoint14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint14_Type.__name__ = "Integer32"
_Dewpoint14_Object = MibScalar
dewpoint14 = _Dewpoint14_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 14, 4),
    _Dewpoint14_Type()
)
dewpoint14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint14.setStatus("mandatory")


class _Co14_Type(Integer32):
    """Custom type co14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co14_Type.__name__ = "Integer32"
_Co14_Object = MibScalar
co14 = _Co14_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 14, 5),
    _Co14_Type()
)
co14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co14.setStatus("mandatory")


class _Motion14_Type(Integer32):
    """Custom type motion14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion14_Type.__name__ = "Integer32"
_Motion14_Object = MibScalar
motion14 = _Motion14_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 14, 6),
    _Motion14_Type()
)
motion14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion14.setStatus("mandatory")


class _Digitalin114_Type(Integer32):
    """Custom type digitalin114 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin114_Type.__name__ = "Integer32"
_Digitalin114_Object = MibScalar
digitalin114 = _Digitalin114_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 14, 7),
    _Digitalin114_Type()
)
digitalin114.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin114.setStatus("mandatory")


class _Digitalin214_Type(Integer32):
    """Custom type digitalin214 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin214_Type.__name__ = "Integer32"
_Digitalin214_Object = MibScalar
digitalin214 = _Digitalin214_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 14, 8),
    _Digitalin214_Type()
)
digitalin214.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin214.setStatus("mandatory")


class _Digitalout214_Type(Integer32):
    """Custom type digitalout214 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout214_Type.__name__ = "Integer32"
_Digitalout214_Object = MibScalar
digitalout214 = _Digitalout214_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 14, 9),
    _Digitalout214_Type()
)
digitalout214.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout214.setStatus("mandatory")


class _ComError14_Type(Integer32):
    """Custom type comError14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError14_Type.__name__ = "Integer32"
_ComError14_Object = MibScalar
comError14 = _ComError14_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 14, 10),
    _ComError14_Type()
)
comError14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError14.setStatus("mandatory")
_Multisensor15_ObjectIdentity = ObjectIdentity
multisensor15 = _Multisensor15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 15)
)
_Sensorname15_Type = DisplayString
_Sensorname15_Object = MibScalar
sensorname15 = _Sensorname15_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 15, 1),
    _Sensorname15_Type()
)
sensorname15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname15.setStatus("mandatory")


class _Temperature15_Type(Integer32):
    """Custom type temperature15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature15_Type.__name__ = "Integer32"
_Temperature15_Object = MibScalar
temperature15 = _Temperature15_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 15, 2),
    _Temperature15_Type()
)
temperature15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature15.setStatus("mandatory")


class _Humidity15_Type(Integer32):
    """Custom type humidity15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity15_Type.__name__ = "Integer32"
_Humidity15_Object = MibScalar
humidity15 = _Humidity15_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 15, 3),
    _Humidity15_Type()
)
humidity15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity15.setStatus("mandatory")


class _Dewpoint15_Type(Integer32):
    """Custom type dewpoint15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint15_Type.__name__ = "Integer32"
_Dewpoint15_Object = MibScalar
dewpoint15 = _Dewpoint15_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 15, 4),
    _Dewpoint15_Type()
)
dewpoint15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint15.setStatus("mandatory")


class _Co15_Type(Integer32):
    """Custom type co15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co15_Type.__name__ = "Integer32"
_Co15_Object = MibScalar
co15 = _Co15_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 15, 5),
    _Co15_Type()
)
co15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co15.setStatus("mandatory")


class _Motion15_Type(Integer32):
    """Custom type motion15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion15_Type.__name__ = "Integer32"
_Motion15_Object = MibScalar
motion15 = _Motion15_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 15, 6),
    _Motion15_Type()
)
motion15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion15.setStatus("mandatory")


class _Digitalin115_Type(Integer32):
    """Custom type digitalin115 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin115_Type.__name__ = "Integer32"
_Digitalin115_Object = MibScalar
digitalin115 = _Digitalin115_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 15, 7),
    _Digitalin115_Type()
)
digitalin115.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin115.setStatus("mandatory")


class _Digitalin215_Type(Integer32):
    """Custom type digitalin215 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin215_Type.__name__ = "Integer32"
_Digitalin215_Object = MibScalar
digitalin215 = _Digitalin215_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 15, 8),
    _Digitalin215_Type()
)
digitalin215.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin215.setStatus("mandatory")


class _Digitalout215_Type(Integer32):
    """Custom type digitalout215 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout215_Type.__name__ = "Integer32"
_Digitalout215_Object = MibScalar
digitalout215 = _Digitalout215_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 15, 9),
    _Digitalout215_Type()
)
digitalout215.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout215.setStatus("mandatory")


class _ComError15_Type(Integer32):
    """Custom type comError15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError15_Type.__name__ = "Integer32"
_ComError15_Object = MibScalar
comError15 = _ComError15_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 15, 10),
    _ComError15_Type()
)
comError15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError15.setStatus("mandatory")
_Multisensor16_ObjectIdentity = ObjectIdentity
multisensor16 = _Multisensor16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 16)
)
_Sensorname16_Type = DisplayString
_Sensorname16_Object = MibScalar
sensorname16 = _Sensorname16_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 16, 1),
    _Sensorname16_Type()
)
sensorname16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname16.setStatus("mandatory")


class _Temperature16_Type(Integer32):
    """Custom type temperature16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature16_Type.__name__ = "Integer32"
_Temperature16_Object = MibScalar
temperature16 = _Temperature16_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 16, 2),
    _Temperature16_Type()
)
temperature16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature16.setStatus("mandatory")


class _Humidity16_Type(Integer32):
    """Custom type humidity16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity16_Type.__name__ = "Integer32"
_Humidity16_Object = MibScalar
humidity16 = _Humidity16_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 16, 3),
    _Humidity16_Type()
)
humidity16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity16.setStatus("mandatory")


class _Dewpoint16_Type(Integer32):
    """Custom type dewpoint16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint16_Type.__name__ = "Integer32"
_Dewpoint16_Object = MibScalar
dewpoint16 = _Dewpoint16_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 16, 4),
    _Dewpoint16_Type()
)
dewpoint16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint16.setStatus("mandatory")


class _Co16_Type(Integer32):
    """Custom type co16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co16_Type.__name__ = "Integer32"
_Co16_Object = MibScalar
co16 = _Co16_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 16, 5),
    _Co16_Type()
)
co16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co16.setStatus("mandatory")


class _Motion16_Type(Integer32):
    """Custom type motion16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion16_Type.__name__ = "Integer32"
_Motion16_Object = MibScalar
motion16 = _Motion16_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 16, 6),
    _Motion16_Type()
)
motion16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion16.setStatus("mandatory")


class _Digitalin116_Type(Integer32):
    """Custom type digitalin116 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin116_Type.__name__ = "Integer32"
_Digitalin116_Object = MibScalar
digitalin116 = _Digitalin116_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 16, 7),
    _Digitalin116_Type()
)
digitalin116.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin116.setStatus("mandatory")


class _Digitalin216_Type(Integer32):
    """Custom type digitalin216 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin216_Type.__name__ = "Integer32"
_Digitalin216_Object = MibScalar
digitalin216 = _Digitalin216_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 16, 8),
    _Digitalin216_Type()
)
digitalin216.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin216.setStatus("mandatory")


class _Digitalout216_Type(Integer32):
    """Custom type digitalout216 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout216_Type.__name__ = "Integer32"
_Digitalout216_Object = MibScalar
digitalout216 = _Digitalout216_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 16, 9),
    _Digitalout216_Type()
)
digitalout216.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout216.setStatus("mandatory")


class _ComError16_Type(Integer32):
    """Custom type comError16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError16_Type.__name__ = "Integer32"
_ComError16_Object = MibScalar
comError16 = _ComError16_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 16, 10),
    _ComError16_Type()
)
comError16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError16.setStatus("mandatory")
_Multisensor17_ObjectIdentity = ObjectIdentity
multisensor17 = _Multisensor17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 17)
)
_Sensorname17_Type = DisplayString
_Sensorname17_Object = MibScalar
sensorname17 = _Sensorname17_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 17, 1),
    _Sensorname17_Type()
)
sensorname17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname17.setStatus("mandatory")


class _Temperature17_Type(Integer32):
    """Custom type temperature17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature17_Type.__name__ = "Integer32"
_Temperature17_Object = MibScalar
temperature17 = _Temperature17_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 17, 2),
    _Temperature17_Type()
)
temperature17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature17.setStatus("mandatory")


class _Humidity17_Type(Integer32):
    """Custom type humidity17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity17_Type.__name__ = "Integer32"
_Humidity17_Object = MibScalar
humidity17 = _Humidity17_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 17, 3),
    _Humidity17_Type()
)
humidity17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity17.setStatus("mandatory")


class _Dewpoint17_Type(Integer32):
    """Custom type dewpoint17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint17_Type.__name__ = "Integer32"
_Dewpoint17_Object = MibScalar
dewpoint17 = _Dewpoint17_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 17, 4),
    _Dewpoint17_Type()
)
dewpoint17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint17.setStatus("mandatory")


class _Co17_Type(Integer32):
    """Custom type co17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co17_Type.__name__ = "Integer32"
_Co17_Object = MibScalar
co17 = _Co17_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 17, 5),
    _Co17_Type()
)
co17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co17.setStatus("mandatory")


class _Motion17_Type(Integer32):
    """Custom type motion17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion17_Type.__name__ = "Integer32"
_Motion17_Object = MibScalar
motion17 = _Motion17_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 17, 6),
    _Motion17_Type()
)
motion17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion17.setStatus("mandatory")


class _Digitalin117_Type(Integer32):
    """Custom type digitalin117 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin117_Type.__name__ = "Integer32"
_Digitalin117_Object = MibScalar
digitalin117 = _Digitalin117_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 17, 7),
    _Digitalin117_Type()
)
digitalin117.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin117.setStatus("mandatory")


class _Digitalin217_Type(Integer32):
    """Custom type digitalin217 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin217_Type.__name__ = "Integer32"
_Digitalin217_Object = MibScalar
digitalin217 = _Digitalin217_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 17, 8),
    _Digitalin217_Type()
)
digitalin217.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin217.setStatus("mandatory")


class _Digitalout217_Type(Integer32):
    """Custom type digitalout217 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout217_Type.__name__ = "Integer32"
_Digitalout217_Object = MibScalar
digitalout217 = _Digitalout217_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 17, 9),
    _Digitalout217_Type()
)
digitalout217.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout217.setStatus("mandatory")


class _ComError17_Type(Integer32):
    """Custom type comError17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError17_Type.__name__ = "Integer32"
_ComError17_Object = MibScalar
comError17 = _ComError17_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 17, 10),
    _ComError17_Type()
)
comError17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError17.setStatus("mandatory")
_Multisensor18_ObjectIdentity = ObjectIdentity
multisensor18 = _Multisensor18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 18)
)
_Sensorname18_Type = DisplayString
_Sensorname18_Object = MibScalar
sensorname18 = _Sensorname18_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 18, 1),
    _Sensorname18_Type()
)
sensorname18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname18.setStatus("mandatory")


class _Temperature18_Type(Integer32):
    """Custom type temperature18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature18_Type.__name__ = "Integer32"
_Temperature18_Object = MibScalar
temperature18 = _Temperature18_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 18, 2),
    _Temperature18_Type()
)
temperature18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature18.setStatus("mandatory")


class _Humidity18_Type(Integer32):
    """Custom type humidity18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity18_Type.__name__ = "Integer32"
_Humidity18_Object = MibScalar
humidity18 = _Humidity18_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 18, 3),
    _Humidity18_Type()
)
humidity18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity18.setStatus("mandatory")


class _Dewpoint18_Type(Integer32):
    """Custom type dewpoint18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint18_Type.__name__ = "Integer32"
_Dewpoint18_Object = MibScalar
dewpoint18 = _Dewpoint18_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 18, 4),
    _Dewpoint18_Type()
)
dewpoint18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint18.setStatus("mandatory")


class _Co18_Type(Integer32):
    """Custom type co18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co18_Type.__name__ = "Integer32"
_Co18_Object = MibScalar
co18 = _Co18_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 18, 5),
    _Co18_Type()
)
co18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co18.setStatus("mandatory")


class _Motion18_Type(Integer32):
    """Custom type motion18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion18_Type.__name__ = "Integer32"
_Motion18_Object = MibScalar
motion18 = _Motion18_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 18, 6),
    _Motion18_Type()
)
motion18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion18.setStatus("mandatory")


class _Digitalin118_Type(Integer32):
    """Custom type digitalin118 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin118_Type.__name__ = "Integer32"
_Digitalin118_Object = MibScalar
digitalin118 = _Digitalin118_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 18, 7),
    _Digitalin118_Type()
)
digitalin118.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin118.setStatus("mandatory")


class _Digitalin218_Type(Integer32):
    """Custom type digitalin218 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin218_Type.__name__ = "Integer32"
_Digitalin218_Object = MibScalar
digitalin218 = _Digitalin218_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 18, 8),
    _Digitalin218_Type()
)
digitalin218.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin218.setStatus("mandatory")


class _Digitalout218_Type(Integer32):
    """Custom type digitalout218 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout218_Type.__name__ = "Integer32"
_Digitalout218_Object = MibScalar
digitalout218 = _Digitalout218_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 18, 9),
    _Digitalout218_Type()
)
digitalout218.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout218.setStatus("mandatory")


class _ComError18_Type(Integer32):
    """Custom type comError18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError18_Type.__name__ = "Integer32"
_ComError18_Object = MibScalar
comError18 = _ComError18_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 18, 10),
    _ComError18_Type()
)
comError18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError18.setStatus("mandatory")
_Multisensor19_ObjectIdentity = ObjectIdentity
multisensor19 = _Multisensor19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 19)
)
_Sensorname19_Type = DisplayString
_Sensorname19_Object = MibScalar
sensorname19 = _Sensorname19_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 19, 1),
    _Sensorname19_Type()
)
sensorname19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname19.setStatus("mandatory")


class _Temperature19_Type(Integer32):
    """Custom type temperature19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature19_Type.__name__ = "Integer32"
_Temperature19_Object = MibScalar
temperature19 = _Temperature19_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 19, 2),
    _Temperature19_Type()
)
temperature19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature19.setStatus("mandatory")


class _Humidity19_Type(Integer32):
    """Custom type humidity19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity19_Type.__name__ = "Integer32"
_Humidity19_Object = MibScalar
humidity19 = _Humidity19_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 19, 3),
    _Humidity19_Type()
)
humidity19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity19.setStatus("mandatory")


class _Dewpoint19_Type(Integer32):
    """Custom type dewpoint19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint19_Type.__name__ = "Integer32"
_Dewpoint19_Object = MibScalar
dewpoint19 = _Dewpoint19_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 19, 4),
    _Dewpoint19_Type()
)
dewpoint19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint19.setStatus("mandatory")


class _Co19_Type(Integer32):
    """Custom type co19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co19_Type.__name__ = "Integer32"
_Co19_Object = MibScalar
co19 = _Co19_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 19, 5),
    _Co19_Type()
)
co19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co19.setStatus("mandatory")


class _Motion19_Type(Integer32):
    """Custom type motion19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion19_Type.__name__ = "Integer32"
_Motion19_Object = MibScalar
motion19 = _Motion19_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 19, 6),
    _Motion19_Type()
)
motion19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion19.setStatus("mandatory")


class _Digitalin119_Type(Integer32):
    """Custom type digitalin119 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin119_Type.__name__ = "Integer32"
_Digitalin119_Object = MibScalar
digitalin119 = _Digitalin119_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 19, 7),
    _Digitalin119_Type()
)
digitalin119.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin119.setStatus("mandatory")


class _Digitalin219_Type(Integer32):
    """Custom type digitalin219 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin219_Type.__name__ = "Integer32"
_Digitalin219_Object = MibScalar
digitalin219 = _Digitalin219_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 19, 8),
    _Digitalin219_Type()
)
digitalin219.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin219.setStatus("mandatory")


class _Digitalout219_Type(Integer32):
    """Custom type digitalout219 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout219_Type.__name__ = "Integer32"
_Digitalout219_Object = MibScalar
digitalout219 = _Digitalout219_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 19, 9),
    _Digitalout219_Type()
)
digitalout219.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout219.setStatus("mandatory")


class _ComError19_Type(Integer32):
    """Custom type comError19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError19_Type.__name__ = "Integer32"
_ComError19_Object = MibScalar
comError19 = _ComError19_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 19, 10),
    _ComError19_Type()
)
comError19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError19.setStatus("mandatory")
_Multisensor20_ObjectIdentity = ObjectIdentity
multisensor20 = _Multisensor20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 20)
)
_Sensorname20_Type = DisplayString
_Sensorname20_Object = MibScalar
sensorname20 = _Sensorname20_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 20, 1),
    _Sensorname20_Type()
)
sensorname20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname20.setStatus("mandatory")


class _Temperature20_Type(Integer32):
    """Custom type temperature20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature20_Type.__name__ = "Integer32"
_Temperature20_Object = MibScalar
temperature20 = _Temperature20_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 20, 2),
    _Temperature20_Type()
)
temperature20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature20.setStatus("mandatory")


class _Humidity20_Type(Integer32):
    """Custom type humidity20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity20_Type.__name__ = "Integer32"
_Humidity20_Object = MibScalar
humidity20 = _Humidity20_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 20, 3),
    _Humidity20_Type()
)
humidity20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity20.setStatus("mandatory")


class _Dewpoint20_Type(Integer32):
    """Custom type dewpoint20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint20_Type.__name__ = "Integer32"
_Dewpoint20_Object = MibScalar
dewpoint20 = _Dewpoint20_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 20, 4),
    _Dewpoint20_Type()
)
dewpoint20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint20.setStatus("mandatory")


class _Co20_Type(Integer32):
    """Custom type co20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co20_Type.__name__ = "Integer32"
_Co20_Object = MibScalar
co20 = _Co20_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 20, 5),
    _Co20_Type()
)
co20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co20.setStatus("mandatory")


class _Motion20_Type(Integer32):
    """Custom type motion20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion20_Type.__name__ = "Integer32"
_Motion20_Object = MibScalar
motion20 = _Motion20_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 20, 6),
    _Motion20_Type()
)
motion20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion20.setStatus("mandatory")


class _Digitalin120_Type(Integer32):
    """Custom type digitalin120 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin120_Type.__name__ = "Integer32"
_Digitalin120_Object = MibScalar
digitalin120 = _Digitalin120_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 20, 7),
    _Digitalin120_Type()
)
digitalin120.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin120.setStatus("mandatory")


class _Digitalin220_Type(Integer32):
    """Custom type digitalin220 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin220_Type.__name__ = "Integer32"
_Digitalin220_Object = MibScalar
digitalin220 = _Digitalin220_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 20, 8),
    _Digitalin220_Type()
)
digitalin220.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin220.setStatus("mandatory")


class _Digitalout220_Type(Integer32):
    """Custom type digitalout220 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout220_Type.__name__ = "Integer32"
_Digitalout220_Object = MibScalar
digitalout220 = _Digitalout220_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 20, 9),
    _Digitalout220_Type()
)
digitalout220.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout220.setStatus("mandatory")


class _ComError20_Type(Integer32):
    """Custom type comError20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError20_Type.__name__ = "Integer32"
_ComError20_Object = MibScalar
comError20 = _ComError20_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 20, 10),
    _ComError20_Type()
)
comError20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError20.setStatus("mandatory")
_Multisensor21_ObjectIdentity = ObjectIdentity
multisensor21 = _Multisensor21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 21)
)
_Sensorname21_Type = DisplayString
_Sensorname21_Object = MibScalar
sensorname21 = _Sensorname21_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 21, 1),
    _Sensorname21_Type()
)
sensorname21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname21.setStatus("mandatory")


class _Temperature21_Type(Integer32):
    """Custom type temperature21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature21_Type.__name__ = "Integer32"
_Temperature21_Object = MibScalar
temperature21 = _Temperature21_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 21, 2),
    _Temperature21_Type()
)
temperature21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature21.setStatus("mandatory")


class _Humidity21_Type(Integer32):
    """Custom type humidity21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity21_Type.__name__ = "Integer32"
_Humidity21_Object = MibScalar
humidity21 = _Humidity21_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 21, 3),
    _Humidity21_Type()
)
humidity21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity21.setStatus("mandatory")


class _Dewpoint21_Type(Integer32):
    """Custom type dewpoint21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint21_Type.__name__ = "Integer32"
_Dewpoint21_Object = MibScalar
dewpoint21 = _Dewpoint21_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 21, 4),
    _Dewpoint21_Type()
)
dewpoint21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint21.setStatus("mandatory")


class _Co21_Type(Integer32):
    """Custom type co21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co21_Type.__name__ = "Integer32"
_Co21_Object = MibScalar
co21 = _Co21_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 21, 5),
    _Co21_Type()
)
co21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co21.setStatus("mandatory")


class _Motion21_Type(Integer32):
    """Custom type motion21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion21_Type.__name__ = "Integer32"
_Motion21_Object = MibScalar
motion21 = _Motion21_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 21, 6),
    _Motion21_Type()
)
motion21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion21.setStatus("mandatory")


class _Digitalin121_Type(Integer32):
    """Custom type digitalin121 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin121_Type.__name__ = "Integer32"
_Digitalin121_Object = MibScalar
digitalin121 = _Digitalin121_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 21, 7),
    _Digitalin121_Type()
)
digitalin121.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin121.setStatus("mandatory")


class _Digitalin221_Type(Integer32):
    """Custom type digitalin221 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin221_Type.__name__ = "Integer32"
_Digitalin221_Object = MibScalar
digitalin221 = _Digitalin221_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 21, 8),
    _Digitalin221_Type()
)
digitalin221.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin221.setStatus("mandatory")


class _Digitalout221_Type(Integer32):
    """Custom type digitalout221 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout221_Type.__name__ = "Integer32"
_Digitalout221_Object = MibScalar
digitalout221 = _Digitalout221_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 21, 9),
    _Digitalout221_Type()
)
digitalout221.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout221.setStatus("mandatory")


class _ComError21_Type(Integer32):
    """Custom type comError21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError21_Type.__name__ = "Integer32"
_ComError21_Object = MibScalar
comError21 = _ComError21_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 21, 10),
    _ComError21_Type()
)
comError21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError21.setStatus("mandatory")
_Multisensor22_ObjectIdentity = ObjectIdentity
multisensor22 = _Multisensor22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 22)
)
_Sensorname22_Type = DisplayString
_Sensorname22_Object = MibScalar
sensorname22 = _Sensorname22_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 22, 1),
    _Sensorname22_Type()
)
sensorname22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname22.setStatus("mandatory")


class _Temperature22_Type(Integer32):
    """Custom type temperature22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature22_Type.__name__ = "Integer32"
_Temperature22_Object = MibScalar
temperature22 = _Temperature22_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 22, 2),
    _Temperature22_Type()
)
temperature22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature22.setStatus("mandatory")


class _Humidity22_Type(Integer32):
    """Custom type humidity22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity22_Type.__name__ = "Integer32"
_Humidity22_Object = MibScalar
humidity22 = _Humidity22_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 22, 3),
    _Humidity22_Type()
)
humidity22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity22.setStatus("mandatory")


class _Dewpoint22_Type(Integer32):
    """Custom type dewpoint22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint22_Type.__name__ = "Integer32"
_Dewpoint22_Object = MibScalar
dewpoint22 = _Dewpoint22_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 22, 4),
    _Dewpoint22_Type()
)
dewpoint22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint22.setStatus("mandatory")


class _Co22_Type(Integer32):
    """Custom type co22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co22_Type.__name__ = "Integer32"
_Co22_Object = MibScalar
co22 = _Co22_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 22, 5),
    _Co22_Type()
)
co22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co22.setStatus("mandatory")


class _Motion22_Type(Integer32):
    """Custom type motion22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion22_Type.__name__ = "Integer32"
_Motion22_Object = MibScalar
motion22 = _Motion22_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 22, 6),
    _Motion22_Type()
)
motion22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion22.setStatus("mandatory")


class _Digitalin122_Type(Integer32):
    """Custom type digitalin122 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin122_Type.__name__ = "Integer32"
_Digitalin122_Object = MibScalar
digitalin122 = _Digitalin122_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 22, 7),
    _Digitalin122_Type()
)
digitalin122.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin122.setStatus("mandatory")


class _Digitalin222_Type(Integer32):
    """Custom type digitalin222 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin222_Type.__name__ = "Integer32"
_Digitalin222_Object = MibScalar
digitalin222 = _Digitalin222_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 22, 8),
    _Digitalin222_Type()
)
digitalin222.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin222.setStatus("mandatory")


class _Digitalout222_Type(Integer32):
    """Custom type digitalout222 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout222_Type.__name__ = "Integer32"
_Digitalout222_Object = MibScalar
digitalout222 = _Digitalout222_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 22, 9),
    _Digitalout222_Type()
)
digitalout222.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout222.setStatus("mandatory")


class _ComError22_Type(Integer32):
    """Custom type comError22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError22_Type.__name__ = "Integer32"
_ComError22_Object = MibScalar
comError22 = _ComError22_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 22, 10),
    _ComError22_Type()
)
comError22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError22.setStatus("mandatory")
_Multisensor23_ObjectIdentity = ObjectIdentity
multisensor23 = _Multisensor23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 23)
)
_Sensorname23_Type = DisplayString
_Sensorname23_Object = MibScalar
sensorname23 = _Sensorname23_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 23, 1),
    _Sensorname23_Type()
)
sensorname23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname23.setStatus("mandatory")


class _Temperature23_Type(Integer32):
    """Custom type temperature23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature23_Type.__name__ = "Integer32"
_Temperature23_Object = MibScalar
temperature23 = _Temperature23_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 23, 2),
    _Temperature23_Type()
)
temperature23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature23.setStatus("mandatory")


class _Humidity23_Type(Integer32):
    """Custom type humidity23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity23_Type.__name__ = "Integer32"
_Humidity23_Object = MibScalar
humidity23 = _Humidity23_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 23, 3),
    _Humidity23_Type()
)
humidity23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity23.setStatus("mandatory")


class _Dewpoint23_Type(Integer32):
    """Custom type dewpoint23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint23_Type.__name__ = "Integer32"
_Dewpoint23_Object = MibScalar
dewpoint23 = _Dewpoint23_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 23, 4),
    _Dewpoint23_Type()
)
dewpoint23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint23.setStatus("mandatory")


class _Co23_Type(Integer32):
    """Custom type co23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co23_Type.__name__ = "Integer32"
_Co23_Object = MibScalar
co23 = _Co23_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 23, 5),
    _Co23_Type()
)
co23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co23.setStatus("mandatory")


class _Motion23_Type(Integer32):
    """Custom type motion23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion23_Type.__name__ = "Integer32"
_Motion23_Object = MibScalar
motion23 = _Motion23_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 23, 6),
    _Motion23_Type()
)
motion23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion23.setStatus("mandatory")


class _Digitalin123_Type(Integer32):
    """Custom type digitalin123 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin123_Type.__name__ = "Integer32"
_Digitalin123_Object = MibScalar
digitalin123 = _Digitalin123_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 23, 7),
    _Digitalin123_Type()
)
digitalin123.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin123.setStatus("mandatory")


class _Digitalin223_Type(Integer32):
    """Custom type digitalin223 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin223_Type.__name__ = "Integer32"
_Digitalin223_Object = MibScalar
digitalin223 = _Digitalin223_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 23, 8),
    _Digitalin223_Type()
)
digitalin223.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin223.setStatus("mandatory")


class _Digitalout223_Type(Integer32):
    """Custom type digitalout223 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout223_Type.__name__ = "Integer32"
_Digitalout223_Object = MibScalar
digitalout223 = _Digitalout223_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 23, 9),
    _Digitalout223_Type()
)
digitalout223.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout223.setStatus("mandatory")


class _ComError23_Type(Integer32):
    """Custom type comError23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError23_Type.__name__ = "Integer32"
_ComError23_Object = MibScalar
comError23 = _ComError23_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 23, 10),
    _ComError23_Type()
)
comError23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError23.setStatus("mandatory")
_Multisensor24_ObjectIdentity = ObjectIdentity
multisensor24 = _Multisensor24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 24)
)
_Sensorname24_Type = DisplayString
_Sensorname24_Object = MibScalar
sensorname24 = _Sensorname24_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 24, 1),
    _Sensorname24_Type()
)
sensorname24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname24.setStatus("mandatory")


class _Temperature24_Type(Integer32):
    """Custom type temperature24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature24_Type.__name__ = "Integer32"
_Temperature24_Object = MibScalar
temperature24 = _Temperature24_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 24, 2),
    _Temperature24_Type()
)
temperature24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature24.setStatus("mandatory")


class _Humidity24_Type(Integer32):
    """Custom type humidity24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity24_Type.__name__ = "Integer32"
_Humidity24_Object = MibScalar
humidity24 = _Humidity24_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 24, 3),
    _Humidity24_Type()
)
humidity24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity24.setStatus("mandatory")


class _Dewpoint24_Type(Integer32):
    """Custom type dewpoint24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint24_Type.__name__ = "Integer32"
_Dewpoint24_Object = MibScalar
dewpoint24 = _Dewpoint24_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 24, 4),
    _Dewpoint24_Type()
)
dewpoint24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint24.setStatus("mandatory")


class _Co24_Type(Integer32):
    """Custom type co24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co24_Type.__name__ = "Integer32"
_Co24_Object = MibScalar
co24 = _Co24_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 24, 5),
    _Co24_Type()
)
co24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co24.setStatus("mandatory")


class _Motion24_Type(Integer32):
    """Custom type motion24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion24_Type.__name__ = "Integer32"
_Motion24_Object = MibScalar
motion24 = _Motion24_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 24, 6),
    _Motion24_Type()
)
motion24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion24.setStatus("mandatory")


class _Digitalin124_Type(Integer32):
    """Custom type digitalin124 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin124_Type.__name__ = "Integer32"
_Digitalin124_Object = MibScalar
digitalin124 = _Digitalin124_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 24, 7),
    _Digitalin124_Type()
)
digitalin124.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin124.setStatus("mandatory")


class _Digitalin224_Type(Integer32):
    """Custom type digitalin224 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin224_Type.__name__ = "Integer32"
_Digitalin224_Object = MibScalar
digitalin224 = _Digitalin224_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 24, 8),
    _Digitalin224_Type()
)
digitalin224.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin224.setStatus("mandatory")


class _Digitalout224_Type(Integer32):
    """Custom type digitalout224 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout224_Type.__name__ = "Integer32"
_Digitalout224_Object = MibScalar
digitalout224 = _Digitalout224_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 24, 9),
    _Digitalout224_Type()
)
digitalout224.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout224.setStatus("mandatory")


class _ComError24_Type(Integer32):
    """Custom type comError24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError24_Type.__name__ = "Integer32"
_ComError24_Object = MibScalar
comError24 = _ComError24_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 24, 10),
    _ComError24_Type()
)
comError24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError24.setStatus("mandatory")
_Multisensor25_ObjectIdentity = ObjectIdentity
multisensor25 = _Multisensor25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 25)
)
_Sensorname25_Type = DisplayString
_Sensorname25_Object = MibScalar
sensorname25 = _Sensorname25_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 25, 1),
    _Sensorname25_Type()
)
sensorname25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname25.setStatus("mandatory")


class _Temperature25_Type(Integer32):
    """Custom type temperature25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature25_Type.__name__ = "Integer32"
_Temperature25_Object = MibScalar
temperature25 = _Temperature25_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 25, 2),
    _Temperature25_Type()
)
temperature25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature25.setStatus("mandatory")


class _Humidity25_Type(Integer32):
    """Custom type humidity25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity25_Type.__name__ = "Integer32"
_Humidity25_Object = MibScalar
humidity25 = _Humidity25_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 25, 3),
    _Humidity25_Type()
)
humidity25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity25.setStatus("mandatory")


class _Dewpoint25_Type(Integer32):
    """Custom type dewpoint25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint25_Type.__name__ = "Integer32"
_Dewpoint25_Object = MibScalar
dewpoint25 = _Dewpoint25_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 25, 4),
    _Dewpoint25_Type()
)
dewpoint25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint25.setStatus("mandatory")


class _Co25_Type(Integer32):
    """Custom type co25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co25_Type.__name__ = "Integer32"
_Co25_Object = MibScalar
co25 = _Co25_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 25, 5),
    _Co25_Type()
)
co25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co25.setStatus("mandatory")


class _Motion25_Type(Integer32):
    """Custom type motion25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion25_Type.__name__ = "Integer32"
_Motion25_Object = MibScalar
motion25 = _Motion25_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 25, 6),
    _Motion25_Type()
)
motion25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion25.setStatus("mandatory")


class _Digitalin125_Type(Integer32):
    """Custom type digitalin125 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin125_Type.__name__ = "Integer32"
_Digitalin125_Object = MibScalar
digitalin125 = _Digitalin125_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 25, 7),
    _Digitalin125_Type()
)
digitalin125.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin125.setStatus("mandatory")


class _Digitalin225_Type(Integer32):
    """Custom type digitalin225 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin225_Type.__name__ = "Integer32"
_Digitalin225_Object = MibScalar
digitalin225 = _Digitalin225_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 25, 8),
    _Digitalin225_Type()
)
digitalin225.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin225.setStatus("mandatory")


class _Digitalout225_Type(Integer32):
    """Custom type digitalout225 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout225_Type.__name__ = "Integer32"
_Digitalout225_Object = MibScalar
digitalout225 = _Digitalout225_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 25, 9),
    _Digitalout225_Type()
)
digitalout225.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout225.setStatus("mandatory")


class _ComError25_Type(Integer32):
    """Custom type comError25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError25_Type.__name__ = "Integer32"
_ComError25_Object = MibScalar
comError25 = _ComError25_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 25, 10),
    _ComError25_Type()
)
comError25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError25.setStatus("mandatory")
_Multisensor26_ObjectIdentity = ObjectIdentity
multisensor26 = _Multisensor26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 26)
)
_Sensorname26_Type = DisplayString
_Sensorname26_Object = MibScalar
sensorname26 = _Sensorname26_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 26, 1),
    _Sensorname26_Type()
)
sensorname26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname26.setStatus("mandatory")


class _Temperature26_Type(Integer32):
    """Custom type temperature26 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature26_Type.__name__ = "Integer32"
_Temperature26_Object = MibScalar
temperature26 = _Temperature26_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 26, 2),
    _Temperature26_Type()
)
temperature26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature26.setStatus("mandatory")


class _Humidity26_Type(Integer32):
    """Custom type humidity26 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity26_Type.__name__ = "Integer32"
_Humidity26_Object = MibScalar
humidity26 = _Humidity26_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 26, 3),
    _Humidity26_Type()
)
humidity26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity26.setStatus("mandatory")


class _Dewpoint26_Type(Integer32):
    """Custom type dewpoint26 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint26_Type.__name__ = "Integer32"
_Dewpoint26_Object = MibScalar
dewpoint26 = _Dewpoint26_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 26, 4),
    _Dewpoint26_Type()
)
dewpoint26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint26.setStatus("mandatory")


class _Co26_Type(Integer32):
    """Custom type co26 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co26_Type.__name__ = "Integer32"
_Co26_Object = MibScalar
co26 = _Co26_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 26, 5),
    _Co26_Type()
)
co26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co26.setStatus("mandatory")


class _Motion26_Type(Integer32):
    """Custom type motion26 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion26_Type.__name__ = "Integer32"
_Motion26_Object = MibScalar
motion26 = _Motion26_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 26, 6),
    _Motion26_Type()
)
motion26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion26.setStatus("mandatory")


class _Digitalin126_Type(Integer32):
    """Custom type digitalin126 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin126_Type.__name__ = "Integer32"
_Digitalin126_Object = MibScalar
digitalin126 = _Digitalin126_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 26, 7),
    _Digitalin126_Type()
)
digitalin126.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin126.setStatus("mandatory")


class _Digitalin226_Type(Integer32):
    """Custom type digitalin226 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin226_Type.__name__ = "Integer32"
_Digitalin226_Object = MibScalar
digitalin226 = _Digitalin226_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 26, 8),
    _Digitalin226_Type()
)
digitalin226.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin226.setStatus("mandatory")


class _Digitalout226_Type(Integer32):
    """Custom type digitalout226 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout226_Type.__name__ = "Integer32"
_Digitalout226_Object = MibScalar
digitalout226 = _Digitalout226_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 26, 9),
    _Digitalout226_Type()
)
digitalout226.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout226.setStatus("mandatory")


class _ComError26_Type(Integer32):
    """Custom type comError26 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError26_Type.__name__ = "Integer32"
_ComError26_Object = MibScalar
comError26 = _ComError26_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 26, 10),
    _ComError26_Type()
)
comError26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError26.setStatus("mandatory")
_Multisensor27_ObjectIdentity = ObjectIdentity
multisensor27 = _Multisensor27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 27)
)
_Sensorname27_Type = DisplayString
_Sensorname27_Object = MibScalar
sensorname27 = _Sensorname27_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 27, 1),
    _Sensorname27_Type()
)
sensorname27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname27.setStatus("mandatory")


class _Temperature27_Type(Integer32):
    """Custom type temperature27 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature27_Type.__name__ = "Integer32"
_Temperature27_Object = MibScalar
temperature27 = _Temperature27_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 27, 2),
    _Temperature27_Type()
)
temperature27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature27.setStatus("mandatory")


class _Humidity27_Type(Integer32):
    """Custom type humidity27 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity27_Type.__name__ = "Integer32"
_Humidity27_Object = MibScalar
humidity27 = _Humidity27_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 27, 3),
    _Humidity27_Type()
)
humidity27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity27.setStatus("mandatory")


class _Dewpoint27_Type(Integer32):
    """Custom type dewpoint27 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint27_Type.__name__ = "Integer32"
_Dewpoint27_Object = MibScalar
dewpoint27 = _Dewpoint27_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 27, 4),
    _Dewpoint27_Type()
)
dewpoint27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint27.setStatus("mandatory")


class _Co27_Type(Integer32):
    """Custom type co27 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co27_Type.__name__ = "Integer32"
_Co27_Object = MibScalar
co27 = _Co27_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 27, 5),
    _Co27_Type()
)
co27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co27.setStatus("mandatory")


class _Motion27_Type(Integer32):
    """Custom type motion27 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion27_Type.__name__ = "Integer32"
_Motion27_Object = MibScalar
motion27 = _Motion27_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 27, 6),
    _Motion27_Type()
)
motion27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion27.setStatus("mandatory")


class _Digitalin127_Type(Integer32):
    """Custom type digitalin127 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin127_Type.__name__ = "Integer32"
_Digitalin127_Object = MibScalar
digitalin127 = _Digitalin127_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 27, 7),
    _Digitalin127_Type()
)
digitalin127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin127.setStatus("mandatory")


class _Digitalin227_Type(Integer32):
    """Custom type digitalin227 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin227_Type.__name__ = "Integer32"
_Digitalin227_Object = MibScalar
digitalin227 = _Digitalin227_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 27, 8),
    _Digitalin227_Type()
)
digitalin227.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin227.setStatus("mandatory")


class _Digitalout227_Type(Integer32):
    """Custom type digitalout227 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout227_Type.__name__ = "Integer32"
_Digitalout227_Object = MibScalar
digitalout227 = _Digitalout227_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 27, 9),
    _Digitalout227_Type()
)
digitalout227.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout227.setStatus("mandatory")


class _ComError27_Type(Integer32):
    """Custom type comError27 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError27_Type.__name__ = "Integer32"
_ComError27_Object = MibScalar
comError27 = _ComError27_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 27, 10),
    _ComError27_Type()
)
comError27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError27.setStatus("mandatory")
_Multisensor28_ObjectIdentity = ObjectIdentity
multisensor28 = _Multisensor28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 28)
)
_Sensorname28_Type = DisplayString
_Sensorname28_Object = MibScalar
sensorname28 = _Sensorname28_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 28, 1),
    _Sensorname28_Type()
)
sensorname28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname28.setStatus("mandatory")


class _Temperature28_Type(Integer32):
    """Custom type temperature28 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature28_Type.__name__ = "Integer32"
_Temperature28_Object = MibScalar
temperature28 = _Temperature28_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 28, 2),
    _Temperature28_Type()
)
temperature28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature28.setStatus("mandatory")


class _Humidity28_Type(Integer32):
    """Custom type humidity28 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity28_Type.__name__ = "Integer32"
_Humidity28_Object = MibScalar
humidity28 = _Humidity28_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 28, 3),
    _Humidity28_Type()
)
humidity28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity28.setStatus("mandatory")


class _Dewpoint28_Type(Integer32):
    """Custom type dewpoint28 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint28_Type.__name__ = "Integer32"
_Dewpoint28_Object = MibScalar
dewpoint28 = _Dewpoint28_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 28, 4),
    _Dewpoint28_Type()
)
dewpoint28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint28.setStatus("mandatory")


class _Co28_Type(Integer32):
    """Custom type co28 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co28_Type.__name__ = "Integer32"
_Co28_Object = MibScalar
co28 = _Co28_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 28, 5),
    _Co28_Type()
)
co28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co28.setStatus("mandatory")


class _Motion28_Type(Integer32):
    """Custom type motion28 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion28_Type.__name__ = "Integer32"
_Motion28_Object = MibScalar
motion28 = _Motion28_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 28, 6),
    _Motion28_Type()
)
motion28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion28.setStatus("mandatory")


class _Digitalin128_Type(Integer32):
    """Custom type digitalin128 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin128_Type.__name__ = "Integer32"
_Digitalin128_Object = MibScalar
digitalin128 = _Digitalin128_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 28, 7),
    _Digitalin128_Type()
)
digitalin128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin128.setStatus("mandatory")


class _Digitalin228_Type(Integer32):
    """Custom type digitalin228 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin228_Type.__name__ = "Integer32"
_Digitalin228_Object = MibScalar
digitalin228 = _Digitalin228_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 28, 8),
    _Digitalin228_Type()
)
digitalin228.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin228.setStatus("mandatory")


class _Digitalout228_Type(Integer32):
    """Custom type digitalout228 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout228_Type.__name__ = "Integer32"
_Digitalout228_Object = MibScalar
digitalout228 = _Digitalout228_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 28, 9),
    _Digitalout228_Type()
)
digitalout228.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout228.setStatus("mandatory")


class _ComError28_Type(Integer32):
    """Custom type comError28 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError28_Type.__name__ = "Integer32"
_ComError28_Object = MibScalar
comError28 = _ComError28_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 28, 10),
    _ComError28_Type()
)
comError28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError28.setStatus("mandatory")
_Multisensor29_ObjectIdentity = ObjectIdentity
multisensor29 = _Multisensor29_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 29)
)
_Sensorname29_Type = DisplayString
_Sensorname29_Object = MibScalar
sensorname29 = _Sensorname29_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 29, 1),
    _Sensorname29_Type()
)
sensorname29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname29.setStatus("mandatory")


class _Temperature29_Type(Integer32):
    """Custom type temperature29 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature29_Type.__name__ = "Integer32"
_Temperature29_Object = MibScalar
temperature29 = _Temperature29_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 29, 2),
    _Temperature29_Type()
)
temperature29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature29.setStatus("mandatory")


class _Humidity29_Type(Integer32):
    """Custom type humidity29 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity29_Type.__name__ = "Integer32"
_Humidity29_Object = MibScalar
humidity29 = _Humidity29_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 29, 3),
    _Humidity29_Type()
)
humidity29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity29.setStatus("mandatory")


class _Dewpoint29_Type(Integer32):
    """Custom type dewpoint29 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint29_Type.__name__ = "Integer32"
_Dewpoint29_Object = MibScalar
dewpoint29 = _Dewpoint29_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 29, 4),
    _Dewpoint29_Type()
)
dewpoint29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint29.setStatus("mandatory")


class _Co29_Type(Integer32):
    """Custom type co29 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co29_Type.__name__ = "Integer32"
_Co29_Object = MibScalar
co29 = _Co29_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 29, 5),
    _Co29_Type()
)
co29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co29.setStatus("mandatory")


class _Motion29_Type(Integer32):
    """Custom type motion29 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion29_Type.__name__ = "Integer32"
_Motion29_Object = MibScalar
motion29 = _Motion29_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 29, 6),
    _Motion29_Type()
)
motion29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion29.setStatus("mandatory")


class _Digitalin129_Type(Integer32):
    """Custom type digitalin129 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin129_Type.__name__ = "Integer32"
_Digitalin129_Object = MibScalar
digitalin129 = _Digitalin129_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 29, 7),
    _Digitalin129_Type()
)
digitalin129.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin129.setStatus("mandatory")


class _Digitalin229_Type(Integer32):
    """Custom type digitalin229 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin229_Type.__name__ = "Integer32"
_Digitalin229_Object = MibScalar
digitalin229 = _Digitalin229_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 29, 8),
    _Digitalin229_Type()
)
digitalin229.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin229.setStatus("mandatory")


class _Digitalout229_Type(Integer32):
    """Custom type digitalout229 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout229_Type.__name__ = "Integer32"
_Digitalout229_Object = MibScalar
digitalout229 = _Digitalout229_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 29, 9),
    _Digitalout229_Type()
)
digitalout229.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout229.setStatus("mandatory")


class _ComError29_Type(Integer32):
    """Custom type comError29 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError29_Type.__name__ = "Integer32"
_ComError29_Object = MibScalar
comError29 = _ComError29_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 29, 10),
    _ComError29_Type()
)
comError29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError29.setStatus("mandatory")
_Multisensor30_ObjectIdentity = ObjectIdentity
multisensor30 = _Multisensor30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 30)
)
_Sensorname30_Type = DisplayString
_Sensorname30_Object = MibScalar
sensorname30 = _Sensorname30_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 30, 1),
    _Sensorname30_Type()
)
sensorname30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname30.setStatus("mandatory")


class _Temperature30_Type(Integer32):
    """Custom type temperature30 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature30_Type.__name__ = "Integer32"
_Temperature30_Object = MibScalar
temperature30 = _Temperature30_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 30, 2),
    _Temperature30_Type()
)
temperature30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature30.setStatus("mandatory")


class _Humidity30_Type(Integer32):
    """Custom type humidity30 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity30_Type.__name__ = "Integer32"
_Humidity30_Object = MibScalar
humidity30 = _Humidity30_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 30, 3),
    _Humidity30_Type()
)
humidity30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity30.setStatus("mandatory")


class _Dewpoint30_Type(Integer32):
    """Custom type dewpoint30 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint30_Type.__name__ = "Integer32"
_Dewpoint30_Object = MibScalar
dewpoint30 = _Dewpoint30_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 30, 4),
    _Dewpoint30_Type()
)
dewpoint30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint30.setStatus("mandatory")


class _Co30_Type(Integer32):
    """Custom type co30 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co30_Type.__name__ = "Integer32"
_Co30_Object = MibScalar
co30 = _Co30_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 30, 5),
    _Co30_Type()
)
co30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co30.setStatus("mandatory")


class _Motion30_Type(Integer32):
    """Custom type motion30 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion30_Type.__name__ = "Integer32"
_Motion30_Object = MibScalar
motion30 = _Motion30_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 30, 6),
    _Motion30_Type()
)
motion30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion30.setStatus("mandatory")


class _Digitalin130_Type(Integer32):
    """Custom type digitalin130 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin130_Type.__name__ = "Integer32"
_Digitalin130_Object = MibScalar
digitalin130 = _Digitalin130_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 30, 7),
    _Digitalin130_Type()
)
digitalin130.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin130.setStatus("mandatory")


class _Digitalin230_Type(Integer32):
    """Custom type digitalin230 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin230_Type.__name__ = "Integer32"
_Digitalin230_Object = MibScalar
digitalin230 = _Digitalin230_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 30, 8),
    _Digitalin230_Type()
)
digitalin230.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin230.setStatus("mandatory")


class _Digitalout230_Type(Integer32):
    """Custom type digitalout230 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout230_Type.__name__ = "Integer32"
_Digitalout230_Object = MibScalar
digitalout230 = _Digitalout230_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 30, 9),
    _Digitalout230_Type()
)
digitalout230.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout230.setStatus("mandatory")


class _ComError30_Type(Integer32):
    """Custom type comError30 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError30_Type.__name__ = "Integer32"
_ComError30_Object = MibScalar
comError30 = _ComError30_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 30, 10),
    _ComError30_Type()
)
comError30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError30.setStatus("mandatory")
_Multisensor31_ObjectIdentity = ObjectIdentity
multisensor31 = _Multisensor31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 31)
)
_Sensorname31_Type = DisplayString
_Sensorname31_Object = MibScalar
sensorname31 = _Sensorname31_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 31, 1),
    _Sensorname31_Type()
)
sensorname31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname31.setStatus("mandatory")


class _Temperature31_Type(Integer32):
    """Custom type temperature31 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature31_Type.__name__ = "Integer32"
_Temperature31_Object = MibScalar
temperature31 = _Temperature31_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 31, 2),
    _Temperature31_Type()
)
temperature31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature31.setStatus("mandatory")


class _Humidity31_Type(Integer32):
    """Custom type humidity31 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity31_Type.__name__ = "Integer32"
_Humidity31_Object = MibScalar
humidity31 = _Humidity31_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 31, 3),
    _Humidity31_Type()
)
humidity31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity31.setStatus("mandatory")


class _Dewpoint31_Type(Integer32):
    """Custom type dewpoint31 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint31_Type.__name__ = "Integer32"
_Dewpoint31_Object = MibScalar
dewpoint31 = _Dewpoint31_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 31, 4),
    _Dewpoint31_Type()
)
dewpoint31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint31.setStatus("mandatory")


class _Co31_Type(Integer32):
    """Custom type co31 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co31_Type.__name__ = "Integer32"
_Co31_Object = MibScalar
co31 = _Co31_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 31, 5),
    _Co31_Type()
)
co31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co31.setStatus("mandatory")


class _Motion31_Type(Integer32):
    """Custom type motion31 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion31_Type.__name__ = "Integer32"
_Motion31_Object = MibScalar
motion31 = _Motion31_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 31, 6),
    _Motion31_Type()
)
motion31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion31.setStatus("mandatory")


class _Digitalin131_Type(Integer32):
    """Custom type digitalin131 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin131_Type.__name__ = "Integer32"
_Digitalin131_Object = MibScalar
digitalin131 = _Digitalin131_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 31, 7),
    _Digitalin131_Type()
)
digitalin131.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin131.setStatus("mandatory")


class _Digitalin231_Type(Integer32):
    """Custom type digitalin231 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin231_Type.__name__ = "Integer32"
_Digitalin231_Object = MibScalar
digitalin231 = _Digitalin231_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 31, 8),
    _Digitalin231_Type()
)
digitalin231.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin231.setStatus("mandatory")


class _Digitalout231_Type(Integer32):
    """Custom type digitalout231 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout231_Type.__name__ = "Integer32"
_Digitalout231_Object = MibScalar
digitalout231 = _Digitalout231_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 31, 9),
    _Digitalout231_Type()
)
digitalout231.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout231.setStatus("mandatory")


class _ComError31_Type(Integer32):
    """Custom type comError31 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError31_Type.__name__ = "Integer32"
_ComError31_Object = MibScalar
comError31 = _ComError31_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 31, 10),
    _ComError31_Type()
)
comError31.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError31.setStatus("mandatory")
_Multisensor32_ObjectIdentity = ObjectIdentity
multisensor32 = _Multisensor32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 32)
)
_Sensorname32_Type = DisplayString
_Sensorname32_Object = MibScalar
sensorname32 = _Sensorname32_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 32, 1),
    _Sensorname32_Type()
)
sensorname32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname32.setStatus("mandatory")


class _Temperature32_Type(Integer32):
    """Custom type temperature32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature32_Type.__name__ = "Integer32"
_Temperature32_Object = MibScalar
temperature32 = _Temperature32_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 32, 2),
    _Temperature32_Type()
)
temperature32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature32.setStatus("mandatory")


class _Humidity32_Type(Integer32):
    """Custom type humidity32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity32_Type.__name__ = "Integer32"
_Humidity32_Object = MibScalar
humidity32 = _Humidity32_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 32, 3),
    _Humidity32_Type()
)
humidity32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity32.setStatus("mandatory")


class _Dewpoint32_Type(Integer32):
    """Custom type dewpoint32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint32_Type.__name__ = "Integer32"
_Dewpoint32_Object = MibScalar
dewpoint32 = _Dewpoint32_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 32, 4),
    _Dewpoint32_Type()
)
dewpoint32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint32.setStatus("mandatory")


class _Co32_Type(Integer32):
    """Custom type co32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co32_Type.__name__ = "Integer32"
_Co32_Object = MibScalar
co32 = _Co32_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 32, 5),
    _Co32_Type()
)
co32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co32.setStatus("mandatory")


class _Motion32_Type(Integer32):
    """Custom type motion32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion32_Type.__name__ = "Integer32"
_Motion32_Object = MibScalar
motion32 = _Motion32_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 32, 6),
    _Motion32_Type()
)
motion32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion32.setStatus("mandatory")


class _Digitalin132_Type(Integer32):
    """Custom type digitalin132 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin132_Type.__name__ = "Integer32"
_Digitalin132_Object = MibScalar
digitalin132 = _Digitalin132_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 32, 7),
    _Digitalin132_Type()
)
digitalin132.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin132.setStatus("mandatory")


class _Digitalin232_Type(Integer32):
    """Custom type digitalin232 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin232_Type.__name__ = "Integer32"
_Digitalin232_Object = MibScalar
digitalin232 = _Digitalin232_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 32, 8),
    _Digitalin232_Type()
)
digitalin232.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin232.setStatus("mandatory")


class _Digitalout232_Type(Integer32):
    """Custom type digitalout232 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout232_Type.__name__ = "Integer32"
_Digitalout232_Object = MibScalar
digitalout232 = _Digitalout232_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 32, 9),
    _Digitalout232_Type()
)
digitalout232.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout232.setStatus("mandatory")


class _ComError32_Type(Integer32):
    """Custom type comError32 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError32_Type.__name__ = "Integer32"
_ComError32_Object = MibScalar
comError32 = _ComError32_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 32, 10),
    _ComError32_Type()
)
comError32.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError32.setStatus("mandatory")
_Multisensor33_ObjectIdentity = ObjectIdentity
multisensor33 = _Multisensor33_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 33)
)
_Sensorname33_Type = DisplayString
_Sensorname33_Object = MibScalar
sensorname33 = _Sensorname33_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 33, 1),
    _Sensorname33_Type()
)
sensorname33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname33.setStatus("mandatory")


class _Temperature33_Type(Integer32):
    """Custom type temperature33 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature33_Type.__name__ = "Integer32"
_Temperature33_Object = MibScalar
temperature33 = _Temperature33_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 33, 2),
    _Temperature33_Type()
)
temperature33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature33.setStatus("mandatory")


class _Humidity33_Type(Integer32):
    """Custom type humidity33 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity33_Type.__name__ = "Integer32"
_Humidity33_Object = MibScalar
humidity33 = _Humidity33_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 33, 3),
    _Humidity33_Type()
)
humidity33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity33.setStatus("mandatory")


class _Dewpoint33_Type(Integer32):
    """Custom type dewpoint33 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint33_Type.__name__ = "Integer32"
_Dewpoint33_Object = MibScalar
dewpoint33 = _Dewpoint33_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 33, 4),
    _Dewpoint33_Type()
)
dewpoint33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint33.setStatus("mandatory")


class _Co33_Type(Integer32):
    """Custom type co33 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co33_Type.__name__ = "Integer32"
_Co33_Object = MibScalar
co33 = _Co33_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 33, 5),
    _Co33_Type()
)
co33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co33.setStatus("mandatory")


class _Motion33_Type(Integer32):
    """Custom type motion33 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion33_Type.__name__ = "Integer32"
_Motion33_Object = MibScalar
motion33 = _Motion33_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 33, 6),
    _Motion33_Type()
)
motion33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion33.setStatus("mandatory")


class _Digitalin133_Type(Integer32):
    """Custom type digitalin133 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin133_Type.__name__ = "Integer32"
_Digitalin133_Object = MibScalar
digitalin133 = _Digitalin133_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 33, 7),
    _Digitalin133_Type()
)
digitalin133.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin133.setStatus("mandatory")


class _Digitalin233_Type(Integer32):
    """Custom type digitalin233 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin233_Type.__name__ = "Integer32"
_Digitalin233_Object = MibScalar
digitalin233 = _Digitalin233_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 33, 8),
    _Digitalin233_Type()
)
digitalin233.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin233.setStatus("mandatory")


class _Digitalout233_Type(Integer32):
    """Custom type digitalout233 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout233_Type.__name__ = "Integer32"
_Digitalout233_Object = MibScalar
digitalout233 = _Digitalout233_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 33, 9),
    _Digitalout233_Type()
)
digitalout233.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout233.setStatus("mandatory")


class _ComError33_Type(Integer32):
    """Custom type comError33 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError33_Type.__name__ = "Integer32"
_ComError33_Object = MibScalar
comError33 = _ComError33_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 33, 10),
    _ComError33_Type()
)
comError33.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError33.setStatus("mandatory")
_Multisensor34_ObjectIdentity = ObjectIdentity
multisensor34 = _Multisensor34_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 34)
)
_Sensorname34_Type = DisplayString
_Sensorname34_Object = MibScalar
sensorname34 = _Sensorname34_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 34, 1),
    _Sensorname34_Type()
)
sensorname34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname34.setStatus("mandatory")


class _Temperature34_Type(Integer32):
    """Custom type temperature34 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature34_Type.__name__ = "Integer32"
_Temperature34_Object = MibScalar
temperature34 = _Temperature34_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 34, 2),
    _Temperature34_Type()
)
temperature34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature34.setStatus("mandatory")


class _Humidity34_Type(Integer32):
    """Custom type humidity34 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity34_Type.__name__ = "Integer32"
_Humidity34_Object = MibScalar
humidity34 = _Humidity34_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 34, 3),
    _Humidity34_Type()
)
humidity34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity34.setStatus("mandatory")


class _Dewpoint34_Type(Integer32):
    """Custom type dewpoint34 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint34_Type.__name__ = "Integer32"
_Dewpoint34_Object = MibScalar
dewpoint34 = _Dewpoint34_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 34, 4),
    _Dewpoint34_Type()
)
dewpoint34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint34.setStatus("mandatory")


class _Co34_Type(Integer32):
    """Custom type co34 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co34_Type.__name__ = "Integer32"
_Co34_Object = MibScalar
co34 = _Co34_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 34, 5),
    _Co34_Type()
)
co34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co34.setStatus("mandatory")


class _Motion34_Type(Integer32):
    """Custom type motion34 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion34_Type.__name__ = "Integer32"
_Motion34_Object = MibScalar
motion34 = _Motion34_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 34, 6),
    _Motion34_Type()
)
motion34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion34.setStatus("mandatory")


class _Digitalin134_Type(Integer32):
    """Custom type digitalin134 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin134_Type.__name__ = "Integer32"
_Digitalin134_Object = MibScalar
digitalin134 = _Digitalin134_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 34, 7),
    _Digitalin134_Type()
)
digitalin134.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin134.setStatus("mandatory")


class _Digitalin234_Type(Integer32):
    """Custom type digitalin234 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin234_Type.__name__ = "Integer32"
_Digitalin234_Object = MibScalar
digitalin234 = _Digitalin234_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 34, 8),
    _Digitalin234_Type()
)
digitalin234.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin234.setStatus("mandatory")


class _Digitalout234_Type(Integer32):
    """Custom type digitalout234 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout234_Type.__name__ = "Integer32"
_Digitalout234_Object = MibScalar
digitalout234 = _Digitalout234_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 34, 9),
    _Digitalout234_Type()
)
digitalout234.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout234.setStatus("mandatory")


class _ComError34_Type(Integer32):
    """Custom type comError34 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError34_Type.__name__ = "Integer32"
_ComError34_Object = MibScalar
comError34 = _ComError34_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 34, 10),
    _ComError34_Type()
)
comError34.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError34.setStatus("mandatory")
_Multisensor35_ObjectIdentity = ObjectIdentity
multisensor35 = _Multisensor35_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 35)
)
_Sensorname35_Type = DisplayString
_Sensorname35_Object = MibScalar
sensorname35 = _Sensorname35_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 35, 1),
    _Sensorname35_Type()
)
sensorname35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname35.setStatus("mandatory")


class _Temperature35_Type(Integer32):
    """Custom type temperature35 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature35_Type.__name__ = "Integer32"
_Temperature35_Object = MibScalar
temperature35 = _Temperature35_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 35, 2),
    _Temperature35_Type()
)
temperature35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature35.setStatus("mandatory")


class _Humidity35_Type(Integer32):
    """Custom type humidity35 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity35_Type.__name__ = "Integer32"
_Humidity35_Object = MibScalar
humidity35 = _Humidity35_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 35, 3),
    _Humidity35_Type()
)
humidity35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity35.setStatus("mandatory")


class _Dewpoint35_Type(Integer32):
    """Custom type dewpoint35 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint35_Type.__name__ = "Integer32"
_Dewpoint35_Object = MibScalar
dewpoint35 = _Dewpoint35_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 35, 4),
    _Dewpoint35_Type()
)
dewpoint35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint35.setStatus("mandatory")


class _Co35_Type(Integer32):
    """Custom type co35 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co35_Type.__name__ = "Integer32"
_Co35_Object = MibScalar
co35 = _Co35_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 35, 5),
    _Co35_Type()
)
co35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co35.setStatus("mandatory")


class _Motion35_Type(Integer32):
    """Custom type motion35 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion35_Type.__name__ = "Integer32"
_Motion35_Object = MibScalar
motion35 = _Motion35_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 35, 6),
    _Motion35_Type()
)
motion35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion35.setStatus("mandatory")


class _Digitalin135_Type(Integer32):
    """Custom type digitalin135 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin135_Type.__name__ = "Integer32"
_Digitalin135_Object = MibScalar
digitalin135 = _Digitalin135_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 35, 7),
    _Digitalin135_Type()
)
digitalin135.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin135.setStatus("mandatory")


class _Digitalin235_Type(Integer32):
    """Custom type digitalin235 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin235_Type.__name__ = "Integer32"
_Digitalin235_Object = MibScalar
digitalin235 = _Digitalin235_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 35, 8),
    _Digitalin235_Type()
)
digitalin235.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin235.setStatus("mandatory")


class _Digitalout235_Type(Integer32):
    """Custom type digitalout235 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout235_Type.__name__ = "Integer32"
_Digitalout235_Object = MibScalar
digitalout235 = _Digitalout235_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 35, 9),
    _Digitalout235_Type()
)
digitalout235.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout235.setStatus("mandatory")


class _ComError35_Type(Integer32):
    """Custom type comError35 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError35_Type.__name__ = "Integer32"
_ComError35_Object = MibScalar
comError35 = _ComError35_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 35, 10),
    _ComError35_Type()
)
comError35.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError35.setStatus("mandatory")
_Multisensor36_ObjectIdentity = ObjectIdentity
multisensor36 = _Multisensor36_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 36)
)
_Sensorname36_Type = DisplayString
_Sensorname36_Object = MibScalar
sensorname36 = _Sensorname36_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 36, 1),
    _Sensorname36_Type()
)
sensorname36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname36.setStatus("mandatory")


class _Temperature36_Type(Integer32):
    """Custom type temperature36 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature36_Type.__name__ = "Integer32"
_Temperature36_Object = MibScalar
temperature36 = _Temperature36_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 36, 2),
    _Temperature36_Type()
)
temperature36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature36.setStatus("mandatory")


class _Humidity36_Type(Integer32):
    """Custom type humidity36 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity36_Type.__name__ = "Integer32"
_Humidity36_Object = MibScalar
humidity36 = _Humidity36_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 36, 3),
    _Humidity36_Type()
)
humidity36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity36.setStatus("mandatory")


class _Dewpoint36_Type(Integer32):
    """Custom type dewpoint36 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint36_Type.__name__ = "Integer32"
_Dewpoint36_Object = MibScalar
dewpoint36 = _Dewpoint36_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 36, 4),
    _Dewpoint36_Type()
)
dewpoint36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint36.setStatus("mandatory")


class _Co36_Type(Integer32):
    """Custom type co36 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co36_Type.__name__ = "Integer32"
_Co36_Object = MibScalar
co36 = _Co36_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 36, 5),
    _Co36_Type()
)
co36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co36.setStatus("mandatory")


class _Motion36_Type(Integer32):
    """Custom type motion36 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion36_Type.__name__ = "Integer32"
_Motion36_Object = MibScalar
motion36 = _Motion36_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 36, 6),
    _Motion36_Type()
)
motion36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion36.setStatus("mandatory")


class _Digitalin136_Type(Integer32):
    """Custom type digitalin136 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin136_Type.__name__ = "Integer32"
_Digitalin136_Object = MibScalar
digitalin136 = _Digitalin136_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 36, 7),
    _Digitalin136_Type()
)
digitalin136.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin136.setStatus("mandatory")


class _Digitalin236_Type(Integer32):
    """Custom type digitalin236 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin236_Type.__name__ = "Integer32"
_Digitalin236_Object = MibScalar
digitalin236 = _Digitalin236_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 36, 8),
    _Digitalin236_Type()
)
digitalin236.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin236.setStatus("mandatory")


class _Digitalout236_Type(Integer32):
    """Custom type digitalout236 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout236_Type.__name__ = "Integer32"
_Digitalout236_Object = MibScalar
digitalout236 = _Digitalout236_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 36, 9),
    _Digitalout236_Type()
)
digitalout236.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout236.setStatus("mandatory")


class _ComError36_Type(Integer32):
    """Custom type comError36 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError36_Type.__name__ = "Integer32"
_ComError36_Object = MibScalar
comError36 = _ComError36_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 36, 10),
    _ComError36_Type()
)
comError36.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError36.setStatus("mandatory")
_Multisensor37_ObjectIdentity = ObjectIdentity
multisensor37 = _Multisensor37_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 37)
)
_Sensorname37_Type = DisplayString
_Sensorname37_Object = MibScalar
sensorname37 = _Sensorname37_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 37, 1),
    _Sensorname37_Type()
)
sensorname37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname37.setStatus("mandatory")


class _Temperature37_Type(Integer32):
    """Custom type temperature37 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature37_Type.__name__ = "Integer32"
_Temperature37_Object = MibScalar
temperature37 = _Temperature37_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 37, 2),
    _Temperature37_Type()
)
temperature37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature37.setStatus("mandatory")


class _Humidity37_Type(Integer32):
    """Custom type humidity37 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity37_Type.__name__ = "Integer32"
_Humidity37_Object = MibScalar
humidity37 = _Humidity37_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 37, 3),
    _Humidity37_Type()
)
humidity37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity37.setStatus("mandatory")


class _Dewpoint37_Type(Integer32):
    """Custom type dewpoint37 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint37_Type.__name__ = "Integer32"
_Dewpoint37_Object = MibScalar
dewpoint37 = _Dewpoint37_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 37, 4),
    _Dewpoint37_Type()
)
dewpoint37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint37.setStatus("mandatory")


class _Co37_Type(Integer32):
    """Custom type co37 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co37_Type.__name__ = "Integer32"
_Co37_Object = MibScalar
co37 = _Co37_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 37, 5),
    _Co37_Type()
)
co37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co37.setStatus("mandatory")


class _Motion37_Type(Integer32):
    """Custom type motion37 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion37_Type.__name__ = "Integer32"
_Motion37_Object = MibScalar
motion37 = _Motion37_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 37, 6),
    _Motion37_Type()
)
motion37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion37.setStatus("mandatory")


class _Digitalin137_Type(Integer32):
    """Custom type digitalin137 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin137_Type.__name__ = "Integer32"
_Digitalin137_Object = MibScalar
digitalin137 = _Digitalin137_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 37, 7),
    _Digitalin137_Type()
)
digitalin137.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin137.setStatus("mandatory")


class _Digitalin237_Type(Integer32):
    """Custom type digitalin237 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin237_Type.__name__ = "Integer32"
_Digitalin237_Object = MibScalar
digitalin237 = _Digitalin237_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 37, 8),
    _Digitalin237_Type()
)
digitalin237.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin237.setStatus("mandatory")


class _Digitalout237_Type(Integer32):
    """Custom type digitalout237 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout237_Type.__name__ = "Integer32"
_Digitalout237_Object = MibScalar
digitalout237 = _Digitalout237_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 37, 9),
    _Digitalout237_Type()
)
digitalout237.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout237.setStatus("mandatory")


class _ComError37_Type(Integer32):
    """Custom type comError37 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError37_Type.__name__ = "Integer32"
_ComError37_Object = MibScalar
comError37 = _ComError37_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 37, 10),
    _ComError37_Type()
)
comError37.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError37.setStatus("mandatory")
_Multisensor38_ObjectIdentity = ObjectIdentity
multisensor38 = _Multisensor38_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 38)
)
_Sensorname38_Type = DisplayString
_Sensorname38_Object = MibScalar
sensorname38 = _Sensorname38_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 38, 1),
    _Sensorname38_Type()
)
sensorname38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname38.setStatus("mandatory")


class _Temperature38_Type(Integer32):
    """Custom type temperature38 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature38_Type.__name__ = "Integer32"
_Temperature38_Object = MibScalar
temperature38 = _Temperature38_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 38, 2),
    _Temperature38_Type()
)
temperature38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature38.setStatus("mandatory")


class _Humidity38_Type(Integer32):
    """Custom type humidity38 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity38_Type.__name__ = "Integer32"
_Humidity38_Object = MibScalar
humidity38 = _Humidity38_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 38, 3),
    _Humidity38_Type()
)
humidity38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity38.setStatus("mandatory")


class _Dewpoint38_Type(Integer32):
    """Custom type dewpoint38 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint38_Type.__name__ = "Integer32"
_Dewpoint38_Object = MibScalar
dewpoint38 = _Dewpoint38_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 38, 4),
    _Dewpoint38_Type()
)
dewpoint38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint38.setStatus("mandatory")


class _Co38_Type(Integer32):
    """Custom type co38 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co38_Type.__name__ = "Integer32"
_Co38_Object = MibScalar
co38 = _Co38_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 38, 5),
    _Co38_Type()
)
co38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co38.setStatus("mandatory")


class _Motion38_Type(Integer32):
    """Custom type motion38 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion38_Type.__name__ = "Integer32"
_Motion38_Object = MibScalar
motion38 = _Motion38_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 38, 6),
    _Motion38_Type()
)
motion38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion38.setStatus("mandatory")


class _Digitalin138_Type(Integer32):
    """Custom type digitalin138 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin138_Type.__name__ = "Integer32"
_Digitalin138_Object = MibScalar
digitalin138 = _Digitalin138_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 38, 7),
    _Digitalin138_Type()
)
digitalin138.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin138.setStatus("mandatory")


class _Digitalin238_Type(Integer32):
    """Custom type digitalin238 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin238_Type.__name__ = "Integer32"
_Digitalin238_Object = MibScalar
digitalin238 = _Digitalin238_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 38, 8),
    _Digitalin238_Type()
)
digitalin238.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin238.setStatus("mandatory")


class _Digitalout238_Type(Integer32):
    """Custom type digitalout238 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout238_Type.__name__ = "Integer32"
_Digitalout238_Object = MibScalar
digitalout238 = _Digitalout238_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 38, 9),
    _Digitalout238_Type()
)
digitalout238.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout238.setStatus("mandatory")


class _ComError38_Type(Integer32):
    """Custom type comError38 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError38_Type.__name__ = "Integer32"
_ComError38_Object = MibScalar
comError38 = _ComError38_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 38, 10),
    _ComError38_Type()
)
comError38.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError38.setStatus("mandatory")
_Multisensor39_ObjectIdentity = ObjectIdentity
multisensor39 = _Multisensor39_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 39)
)
_Sensorname39_Type = DisplayString
_Sensorname39_Object = MibScalar
sensorname39 = _Sensorname39_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 39, 1),
    _Sensorname39_Type()
)
sensorname39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname39.setStatus("mandatory")


class _Temperature39_Type(Integer32):
    """Custom type temperature39 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature39_Type.__name__ = "Integer32"
_Temperature39_Object = MibScalar
temperature39 = _Temperature39_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 39, 2),
    _Temperature39_Type()
)
temperature39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature39.setStatus("mandatory")


class _Humidity39_Type(Integer32):
    """Custom type humidity39 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity39_Type.__name__ = "Integer32"
_Humidity39_Object = MibScalar
humidity39 = _Humidity39_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 39, 3),
    _Humidity39_Type()
)
humidity39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity39.setStatus("mandatory")


class _Dewpoint39_Type(Integer32):
    """Custom type dewpoint39 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint39_Type.__name__ = "Integer32"
_Dewpoint39_Object = MibScalar
dewpoint39 = _Dewpoint39_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 39, 4),
    _Dewpoint39_Type()
)
dewpoint39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint39.setStatus("mandatory")


class _Co39_Type(Integer32):
    """Custom type co39 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co39_Type.__name__ = "Integer32"
_Co39_Object = MibScalar
co39 = _Co39_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 39, 5),
    _Co39_Type()
)
co39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co39.setStatus("mandatory")


class _Motion39_Type(Integer32):
    """Custom type motion39 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion39_Type.__name__ = "Integer32"
_Motion39_Object = MibScalar
motion39 = _Motion39_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 39, 6),
    _Motion39_Type()
)
motion39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion39.setStatus("mandatory")


class _Digitalin139_Type(Integer32):
    """Custom type digitalin139 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin139_Type.__name__ = "Integer32"
_Digitalin139_Object = MibScalar
digitalin139 = _Digitalin139_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 39, 7),
    _Digitalin139_Type()
)
digitalin139.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin139.setStatus("mandatory")


class _Digitalin239_Type(Integer32):
    """Custom type digitalin239 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin239_Type.__name__ = "Integer32"
_Digitalin239_Object = MibScalar
digitalin239 = _Digitalin239_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 39, 8),
    _Digitalin239_Type()
)
digitalin239.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin239.setStatus("mandatory")


class _Digitalout239_Type(Integer32):
    """Custom type digitalout239 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout239_Type.__name__ = "Integer32"
_Digitalout239_Object = MibScalar
digitalout239 = _Digitalout239_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 39, 9),
    _Digitalout239_Type()
)
digitalout239.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout239.setStatus("mandatory")


class _ComError39_Type(Integer32):
    """Custom type comError39 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError39_Type.__name__ = "Integer32"
_ComError39_Object = MibScalar
comError39 = _ComError39_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 39, 10),
    _ComError39_Type()
)
comError39.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError39.setStatus("mandatory")
_Multisensor40_ObjectIdentity = ObjectIdentity
multisensor40 = _Multisensor40_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 40)
)
_Sensorname40_Type = DisplayString
_Sensorname40_Object = MibScalar
sensorname40 = _Sensorname40_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 40, 1),
    _Sensorname40_Type()
)
sensorname40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname40.setStatus("mandatory")


class _Temperature40_Type(Integer32):
    """Custom type temperature40 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature40_Type.__name__ = "Integer32"
_Temperature40_Object = MibScalar
temperature40 = _Temperature40_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 40, 2),
    _Temperature40_Type()
)
temperature40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature40.setStatus("mandatory")


class _Humidity40_Type(Integer32):
    """Custom type humidity40 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity40_Type.__name__ = "Integer32"
_Humidity40_Object = MibScalar
humidity40 = _Humidity40_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 40, 3),
    _Humidity40_Type()
)
humidity40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity40.setStatus("mandatory")


class _Dewpoint40_Type(Integer32):
    """Custom type dewpoint40 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint40_Type.__name__ = "Integer32"
_Dewpoint40_Object = MibScalar
dewpoint40 = _Dewpoint40_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 40, 4),
    _Dewpoint40_Type()
)
dewpoint40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint40.setStatus("mandatory")


class _Co40_Type(Integer32):
    """Custom type co40 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co40_Type.__name__ = "Integer32"
_Co40_Object = MibScalar
co40 = _Co40_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 40, 5),
    _Co40_Type()
)
co40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co40.setStatus("mandatory")


class _Motion40_Type(Integer32):
    """Custom type motion40 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion40_Type.__name__ = "Integer32"
_Motion40_Object = MibScalar
motion40 = _Motion40_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 40, 6),
    _Motion40_Type()
)
motion40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion40.setStatus("mandatory")


class _Digitalin140_Type(Integer32):
    """Custom type digitalin140 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin140_Type.__name__ = "Integer32"
_Digitalin140_Object = MibScalar
digitalin140 = _Digitalin140_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 40, 7),
    _Digitalin140_Type()
)
digitalin140.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin140.setStatus("mandatory")


class _Digitalin240_Type(Integer32):
    """Custom type digitalin240 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin240_Type.__name__ = "Integer32"
_Digitalin240_Object = MibScalar
digitalin240 = _Digitalin240_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 40, 8),
    _Digitalin240_Type()
)
digitalin240.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin240.setStatus("mandatory")


class _Digitalout240_Type(Integer32):
    """Custom type digitalout240 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout240_Type.__name__ = "Integer32"
_Digitalout240_Object = MibScalar
digitalout240 = _Digitalout240_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 40, 9),
    _Digitalout240_Type()
)
digitalout240.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout240.setStatus("mandatory")


class _ComError40_Type(Integer32):
    """Custom type comError40 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError40_Type.__name__ = "Integer32"
_ComError40_Object = MibScalar
comError40 = _ComError40_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 40, 10),
    _ComError40_Type()
)
comError40.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError40.setStatus("mandatory")
_Multisensor41_ObjectIdentity = ObjectIdentity
multisensor41 = _Multisensor41_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 41)
)
_Sensorname41_Type = DisplayString
_Sensorname41_Object = MibScalar
sensorname41 = _Sensorname41_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 41, 1),
    _Sensorname41_Type()
)
sensorname41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname41.setStatus("mandatory")


class _Temperature41_Type(Integer32):
    """Custom type temperature41 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature41_Type.__name__ = "Integer32"
_Temperature41_Object = MibScalar
temperature41 = _Temperature41_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 41, 2),
    _Temperature41_Type()
)
temperature41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature41.setStatus("mandatory")


class _Humidity41_Type(Integer32):
    """Custom type humidity41 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity41_Type.__name__ = "Integer32"
_Humidity41_Object = MibScalar
humidity41 = _Humidity41_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 41, 3),
    _Humidity41_Type()
)
humidity41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity41.setStatus("mandatory")


class _Dewpoint41_Type(Integer32):
    """Custom type dewpoint41 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint41_Type.__name__ = "Integer32"
_Dewpoint41_Object = MibScalar
dewpoint41 = _Dewpoint41_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 41, 4),
    _Dewpoint41_Type()
)
dewpoint41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint41.setStatus("mandatory")


class _Co41_Type(Integer32):
    """Custom type co41 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co41_Type.__name__ = "Integer32"
_Co41_Object = MibScalar
co41 = _Co41_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 41, 5),
    _Co41_Type()
)
co41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co41.setStatus("mandatory")


class _Motion41_Type(Integer32):
    """Custom type motion41 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion41_Type.__name__ = "Integer32"
_Motion41_Object = MibScalar
motion41 = _Motion41_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 41, 6),
    _Motion41_Type()
)
motion41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion41.setStatus("mandatory")


class _Digitalin141_Type(Integer32):
    """Custom type digitalin141 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin141_Type.__name__ = "Integer32"
_Digitalin141_Object = MibScalar
digitalin141 = _Digitalin141_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 41, 7),
    _Digitalin141_Type()
)
digitalin141.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin141.setStatus("mandatory")


class _Digitalin241_Type(Integer32):
    """Custom type digitalin241 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin241_Type.__name__ = "Integer32"
_Digitalin241_Object = MibScalar
digitalin241 = _Digitalin241_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 41, 8),
    _Digitalin241_Type()
)
digitalin241.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin241.setStatus("mandatory")


class _Digitalout241_Type(Integer32):
    """Custom type digitalout241 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout241_Type.__name__ = "Integer32"
_Digitalout241_Object = MibScalar
digitalout241 = _Digitalout241_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 41, 9),
    _Digitalout241_Type()
)
digitalout241.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout241.setStatus("mandatory")


class _ComError41_Type(Integer32):
    """Custom type comError41 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError41_Type.__name__ = "Integer32"
_ComError41_Object = MibScalar
comError41 = _ComError41_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 41, 10),
    _ComError41_Type()
)
comError41.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError41.setStatus("mandatory")
_Multisensor42_ObjectIdentity = ObjectIdentity
multisensor42 = _Multisensor42_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 42)
)
_Sensorname42_Type = DisplayString
_Sensorname42_Object = MibScalar
sensorname42 = _Sensorname42_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 42, 1),
    _Sensorname42_Type()
)
sensorname42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname42.setStatus("mandatory")


class _Temperature42_Type(Integer32):
    """Custom type temperature42 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature42_Type.__name__ = "Integer32"
_Temperature42_Object = MibScalar
temperature42 = _Temperature42_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 42, 2),
    _Temperature42_Type()
)
temperature42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature42.setStatus("mandatory")


class _Humidity42_Type(Integer32):
    """Custom type humidity42 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity42_Type.__name__ = "Integer32"
_Humidity42_Object = MibScalar
humidity42 = _Humidity42_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 42, 3),
    _Humidity42_Type()
)
humidity42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity42.setStatus("mandatory")


class _Dewpoint42_Type(Integer32):
    """Custom type dewpoint42 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint42_Type.__name__ = "Integer32"
_Dewpoint42_Object = MibScalar
dewpoint42 = _Dewpoint42_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 42, 4),
    _Dewpoint42_Type()
)
dewpoint42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint42.setStatus("mandatory")


class _Co42_Type(Integer32):
    """Custom type co42 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co42_Type.__name__ = "Integer32"
_Co42_Object = MibScalar
co42 = _Co42_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 42, 5),
    _Co42_Type()
)
co42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co42.setStatus("mandatory")


class _Motion42_Type(Integer32):
    """Custom type motion42 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion42_Type.__name__ = "Integer32"
_Motion42_Object = MibScalar
motion42 = _Motion42_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 42, 6),
    _Motion42_Type()
)
motion42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion42.setStatus("mandatory")


class _Digitalin142_Type(Integer32):
    """Custom type digitalin142 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin142_Type.__name__ = "Integer32"
_Digitalin142_Object = MibScalar
digitalin142 = _Digitalin142_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 42, 7),
    _Digitalin142_Type()
)
digitalin142.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin142.setStatus("mandatory")


class _Digitalin242_Type(Integer32):
    """Custom type digitalin242 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin242_Type.__name__ = "Integer32"
_Digitalin242_Object = MibScalar
digitalin242 = _Digitalin242_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 42, 8),
    _Digitalin242_Type()
)
digitalin242.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin242.setStatus("mandatory")


class _Digitalout242_Type(Integer32):
    """Custom type digitalout242 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout242_Type.__name__ = "Integer32"
_Digitalout242_Object = MibScalar
digitalout242 = _Digitalout242_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 42, 9),
    _Digitalout242_Type()
)
digitalout242.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout242.setStatus("mandatory")


class _ComError42_Type(Integer32):
    """Custom type comError42 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError42_Type.__name__ = "Integer32"
_ComError42_Object = MibScalar
comError42 = _ComError42_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 42, 10),
    _ComError42_Type()
)
comError42.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError42.setStatus("mandatory")
_Multisensor43_ObjectIdentity = ObjectIdentity
multisensor43 = _Multisensor43_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 43)
)
_Sensorname43_Type = DisplayString
_Sensorname43_Object = MibScalar
sensorname43 = _Sensorname43_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 43, 1),
    _Sensorname43_Type()
)
sensorname43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname43.setStatus("mandatory")


class _Temperature43_Type(Integer32):
    """Custom type temperature43 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature43_Type.__name__ = "Integer32"
_Temperature43_Object = MibScalar
temperature43 = _Temperature43_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 43, 2),
    _Temperature43_Type()
)
temperature43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature43.setStatus("mandatory")


class _Humidity43_Type(Integer32):
    """Custom type humidity43 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity43_Type.__name__ = "Integer32"
_Humidity43_Object = MibScalar
humidity43 = _Humidity43_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 43, 3),
    _Humidity43_Type()
)
humidity43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity43.setStatus("mandatory")


class _Dewpoint43_Type(Integer32):
    """Custom type dewpoint43 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint43_Type.__name__ = "Integer32"
_Dewpoint43_Object = MibScalar
dewpoint43 = _Dewpoint43_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 43, 4),
    _Dewpoint43_Type()
)
dewpoint43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint43.setStatus("mandatory")


class _Co43_Type(Integer32):
    """Custom type co43 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co43_Type.__name__ = "Integer32"
_Co43_Object = MibScalar
co43 = _Co43_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 43, 5),
    _Co43_Type()
)
co43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co43.setStatus("mandatory")


class _Motion43_Type(Integer32):
    """Custom type motion43 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion43_Type.__name__ = "Integer32"
_Motion43_Object = MibScalar
motion43 = _Motion43_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 43, 6),
    _Motion43_Type()
)
motion43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion43.setStatus("mandatory")


class _Digitalin143_Type(Integer32):
    """Custom type digitalin143 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin143_Type.__name__ = "Integer32"
_Digitalin143_Object = MibScalar
digitalin143 = _Digitalin143_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 43, 7),
    _Digitalin143_Type()
)
digitalin143.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin143.setStatus("mandatory")


class _Digitalin243_Type(Integer32):
    """Custom type digitalin243 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin243_Type.__name__ = "Integer32"
_Digitalin243_Object = MibScalar
digitalin243 = _Digitalin243_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 43, 8),
    _Digitalin243_Type()
)
digitalin243.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin243.setStatus("mandatory")


class _Digitalout243_Type(Integer32):
    """Custom type digitalout243 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout243_Type.__name__ = "Integer32"
_Digitalout243_Object = MibScalar
digitalout243 = _Digitalout243_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 43, 9),
    _Digitalout243_Type()
)
digitalout243.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout243.setStatus("mandatory")


class _ComError43_Type(Integer32):
    """Custom type comError43 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError43_Type.__name__ = "Integer32"
_ComError43_Object = MibScalar
comError43 = _ComError43_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 43, 10),
    _ComError43_Type()
)
comError43.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError43.setStatus("mandatory")
_Multisensor44_ObjectIdentity = ObjectIdentity
multisensor44 = _Multisensor44_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 44)
)
_Sensorname44_Type = DisplayString
_Sensorname44_Object = MibScalar
sensorname44 = _Sensorname44_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 44, 1),
    _Sensorname44_Type()
)
sensorname44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname44.setStatus("mandatory")


class _Temperature44_Type(Integer32):
    """Custom type temperature44 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature44_Type.__name__ = "Integer32"
_Temperature44_Object = MibScalar
temperature44 = _Temperature44_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 44, 2),
    _Temperature44_Type()
)
temperature44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature44.setStatus("mandatory")


class _Humidity44_Type(Integer32):
    """Custom type humidity44 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity44_Type.__name__ = "Integer32"
_Humidity44_Object = MibScalar
humidity44 = _Humidity44_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 44, 3),
    _Humidity44_Type()
)
humidity44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity44.setStatus("mandatory")


class _Dewpoint44_Type(Integer32):
    """Custom type dewpoint44 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint44_Type.__name__ = "Integer32"
_Dewpoint44_Object = MibScalar
dewpoint44 = _Dewpoint44_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 44, 4),
    _Dewpoint44_Type()
)
dewpoint44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint44.setStatus("mandatory")


class _Co44_Type(Integer32):
    """Custom type co44 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co44_Type.__name__ = "Integer32"
_Co44_Object = MibScalar
co44 = _Co44_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 44, 5),
    _Co44_Type()
)
co44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co44.setStatus("mandatory")


class _Motion44_Type(Integer32):
    """Custom type motion44 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion44_Type.__name__ = "Integer32"
_Motion44_Object = MibScalar
motion44 = _Motion44_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 44, 6),
    _Motion44_Type()
)
motion44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion44.setStatus("mandatory")


class _Digitalin144_Type(Integer32):
    """Custom type digitalin144 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin144_Type.__name__ = "Integer32"
_Digitalin144_Object = MibScalar
digitalin144 = _Digitalin144_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 44, 7),
    _Digitalin144_Type()
)
digitalin144.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin144.setStatus("mandatory")


class _Digitalin244_Type(Integer32):
    """Custom type digitalin244 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin244_Type.__name__ = "Integer32"
_Digitalin244_Object = MibScalar
digitalin244 = _Digitalin244_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 44, 8),
    _Digitalin244_Type()
)
digitalin244.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin244.setStatus("mandatory")


class _Digitalout244_Type(Integer32):
    """Custom type digitalout244 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout244_Type.__name__ = "Integer32"
_Digitalout244_Object = MibScalar
digitalout244 = _Digitalout244_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 44, 9),
    _Digitalout244_Type()
)
digitalout244.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout244.setStatus("mandatory")


class _ComError44_Type(Integer32):
    """Custom type comError44 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError44_Type.__name__ = "Integer32"
_ComError44_Object = MibScalar
comError44 = _ComError44_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 44, 10),
    _ComError44_Type()
)
comError44.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError44.setStatus("mandatory")
_Multisensor45_ObjectIdentity = ObjectIdentity
multisensor45 = _Multisensor45_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 45)
)
_Sensorname45_Type = DisplayString
_Sensorname45_Object = MibScalar
sensorname45 = _Sensorname45_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 45, 1),
    _Sensorname45_Type()
)
sensorname45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname45.setStatus("mandatory")


class _Temperature45_Type(Integer32):
    """Custom type temperature45 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature45_Type.__name__ = "Integer32"
_Temperature45_Object = MibScalar
temperature45 = _Temperature45_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 45, 2),
    _Temperature45_Type()
)
temperature45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature45.setStatus("mandatory")


class _Humidity45_Type(Integer32):
    """Custom type humidity45 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity45_Type.__name__ = "Integer32"
_Humidity45_Object = MibScalar
humidity45 = _Humidity45_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 45, 3),
    _Humidity45_Type()
)
humidity45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity45.setStatus("mandatory")


class _Dewpoint45_Type(Integer32):
    """Custom type dewpoint45 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint45_Type.__name__ = "Integer32"
_Dewpoint45_Object = MibScalar
dewpoint45 = _Dewpoint45_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 45, 4),
    _Dewpoint45_Type()
)
dewpoint45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint45.setStatus("mandatory")


class _Co45_Type(Integer32):
    """Custom type co45 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co45_Type.__name__ = "Integer32"
_Co45_Object = MibScalar
co45 = _Co45_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 45, 5),
    _Co45_Type()
)
co45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co45.setStatus("mandatory")


class _Motion45_Type(Integer32):
    """Custom type motion45 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion45_Type.__name__ = "Integer32"
_Motion45_Object = MibScalar
motion45 = _Motion45_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 45, 6),
    _Motion45_Type()
)
motion45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion45.setStatus("mandatory")


class _Digitalin145_Type(Integer32):
    """Custom type digitalin145 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin145_Type.__name__ = "Integer32"
_Digitalin145_Object = MibScalar
digitalin145 = _Digitalin145_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 45, 7),
    _Digitalin145_Type()
)
digitalin145.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin145.setStatus("mandatory")


class _Digitalin245_Type(Integer32):
    """Custom type digitalin245 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin245_Type.__name__ = "Integer32"
_Digitalin245_Object = MibScalar
digitalin245 = _Digitalin245_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 45, 8),
    _Digitalin245_Type()
)
digitalin245.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin245.setStatus("mandatory")


class _Digitalout245_Type(Integer32):
    """Custom type digitalout245 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout245_Type.__name__ = "Integer32"
_Digitalout245_Object = MibScalar
digitalout245 = _Digitalout245_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 45, 9),
    _Digitalout245_Type()
)
digitalout245.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout245.setStatus("mandatory")


class _ComError45_Type(Integer32):
    """Custom type comError45 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError45_Type.__name__ = "Integer32"
_ComError45_Object = MibScalar
comError45 = _ComError45_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 45, 10),
    _ComError45_Type()
)
comError45.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError45.setStatus("mandatory")
_Multisensor46_ObjectIdentity = ObjectIdentity
multisensor46 = _Multisensor46_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 46)
)
_Sensorname46_Type = DisplayString
_Sensorname46_Object = MibScalar
sensorname46 = _Sensorname46_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 46, 1),
    _Sensorname46_Type()
)
sensorname46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname46.setStatus("mandatory")


class _Temperature46_Type(Integer32):
    """Custom type temperature46 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature46_Type.__name__ = "Integer32"
_Temperature46_Object = MibScalar
temperature46 = _Temperature46_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 46, 2),
    _Temperature46_Type()
)
temperature46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature46.setStatus("mandatory")


class _Humidity46_Type(Integer32):
    """Custom type humidity46 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity46_Type.__name__ = "Integer32"
_Humidity46_Object = MibScalar
humidity46 = _Humidity46_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 46, 3),
    _Humidity46_Type()
)
humidity46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity46.setStatus("mandatory")


class _Dewpoint46_Type(Integer32):
    """Custom type dewpoint46 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint46_Type.__name__ = "Integer32"
_Dewpoint46_Object = MibScalar
dewpoint46 = _Dewpoint46_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 46, 4),
    _Dewpoint46_Type()
)
dewpoint46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint46.setStatus("mandatory")


class _Co46_Type(Integer32):
    """Custom type co46 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co46_Type.__name__ = "Integer32"
_Co46_Object = MibScalar
co46 = _Co46_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 46, 5),
    _Co46_Type()
)
co46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co46.setStatus("mandatory")


class _Motion46_Type(Integer32):
    """Custom type motion46 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion46_Type.__name__ = "Integer32"
_Motion46_Object = MibScalar
motion46 = _Motion46_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 46, 6),
    _Motion46_Type()
)
motion46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion46.setStatus("mandatory")


class _Digitalin146_Type(Integer32):
    """Custom type digitalin146 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin146_Type.__name__ = "Integer32"
_Digitalin146_Object = MibScalar
digitalin146 = _Digitalin146_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 46, 7),
    _Digitalin146_Type()
)
digitalin146.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin146.setStatus("mandatory")


class _Digitalin246_Type(Integer32):
    """Custom type digitalin246 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin246_Type.__name__ = "Integer32"
_Digitalin246_Object = MibScalar
digitalin246 = _Digitalin246_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 46, 8),
    _Digitalin246_Type()
)
digitalin246.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin246.setStatus("mandatory")


class _Digitalout246_Type(Integer32):
    """Custom type digitalout246 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout246_Type.__name__ = "Integer32"
_Digitalout246_Object = MibScalar
digitalout246 = _Digitalout246_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 46, 9),
    _Digitalout246_Type()
)
digitalout246.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout246.setStatus("mandatory")


class _ComError46_Type(Integer32):
    """Custom type comError46 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError46_Type.__name__ = "Integer32"
_ComError46_Object = MibScalar
comError46 = _ComError46_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 46, 10),
    _ComError46_Type()
)
comError46.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError46.setStatus("mandatory")
_Multisensor47_ObjectIdentity = ObjectIdentity
multisensor47 = _Multisensor47_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 47)
)
_Sensorname47_Type = DisplayString
_Sensorname47_Object = MibScalar
sensorname47 = _Sensorname47_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 47, 1),
    _Sensorname47_Type()
)
sensorname47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname47.setStatus("mandatory")


class _Temperature47_Type(Integer32):
    """Custom type temperature47 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature47_Type.__name__ = "Integer32"
_Temperature47_Object = MibScalar
temperature47 = _Temperature47_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 47, 2),
    _Temperature47_Type()
)
temperature47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature47.setStatus("mandatory")


class _Humidity47_Type(Integer32):
    """Custom type humidity47 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity47_Type.__name__ = "Integer32"
_Humidity47_Object = MibScalar
humidity47 = _Humidity47_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 47, 3),
    _Humidity47_Type()
)
humidity47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity47.setStatus("mandatory")


class _Dewpoint47_Type(Integer32):
    """Custom type dewpoint47 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint47_Type.__name__ = "Integer32"
_Dewpoint47_Object = MibScalar
dewpoint47 = _Dewpoint47_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 47, 4),
    _Dewpoint47_Type()
)
dewpoint47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint47.setStatus("mandatory")


class _Co47_Type(Integer32):
    """Custom type co47 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co47_Type.__name__ = "Integer32"
_Co47_Object = MibScalar
co47 = _Co47_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 47, 5),
    _Co47_Type()
)
co47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co47.setStatus("mandatory")


class _Motion47_Type(Integer32):
    """Custom type motion47 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion47_Type.__name__ = "Integer32"
_Motion47_Object = MibScalar
motion47 = _Motion47_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 47, 6),
    _Motion47_Type()
)
motion47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion47.setStatus("mandatory")


class _Digitalin147_Type(Integer32):
    """Custom type digitalin147 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin147_Type.__name__ = "Integer32"
_Digitalin147_Object = MibScalar
digitalin147 = _Digitalin147_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 47, 7),
    _Digitalin147_Type()
)
digitalin147.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin147.setStatus("mandatory")


class _Digitalin247_Type(Integer32):
    """Custom type digitalin247 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin247_Type.__name__ = "Integer32"
_Digitalin247_Object = MibScalar
digitalin247 = _Digitalin247_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 47, 8),
    _Digitalin247_Type()
)
digitalin247.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin247.setStatus("mandatory")


class _Digitalout247_Type(Integer32):
    """Custom type digitalout247 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout247_Type.__name__ = "Integer32"
_Digitalout247_Object = MibScalar
digitalout247 = _Digitalout247_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 47, 9),
    _Digitalout247_Type()
)
digitalout247.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout247.setStatus("mandatory")


class _ComError47_Type(Integer32):
    """Custom type comError47 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError47_Type.__name__ = "Integer32"
_ComError47_Object = MibScalar
comError47 = _ComError47_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 47, 10),
    _ComError47_Type()
)
comError47.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError47.setStatus("mandatory")
_Multisensor48_ObjectIdentity = ObjectIdentity
multisensor48 = _Multisensor48_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 48)
)
_Sensorname48_Type = DisplayString
_Sensorname48_Object = MibScalar
sensorname48 = _Sensorname48_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 48, 1),
    _Sensorname48_Type()
)
sensorname48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname48.setStatus("mandatory")


class _Temperature48_Type(Integer32):
    """Custom type temperature48 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature48_Type.__name__ = "Integer32"
_Temperature48_Object = MibScalar
temperature48 = _Temperature48_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 48, 2),
    _Temperature48_Type()
)
temperature48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature48.setStatus("mandatory")


class _Humidity48_Type(Integer32):
    """Custom type humidity48 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity48_Type.__name__ = "Integer32"
_Humidity48_Object = MibScalar
humidity48 = _Humidity48_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 48, 3),
    _Humidity48_Type()
)
humidity48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity48.setStatus("mandatory")


class _Dewpoint48_Type(Integer32):
    """Custom type dewpoint48 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint48_Type.__name__ = "Integer32"
_Dewpoint48_Object = MibScalar
dewpoint48 = _Dewpoint48_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 48, 4),
    _Dewpoint48_Type()
)
dewpoint48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint48.setStatus("mandatory")


class _Co48_Type(Integer32):
    """Custom type co48 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co48_Type.__name__ = "Integer32"
_Co48_Object = MibScalar
co48 = _Co48_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 48, 5),
    _Co48_Type()
)
co48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co48.setStatus("mandatory")


class _Motion48_Type(Integer32):
    """Custom type motion48 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion48_Type.__name__ = "Integer32"
_Motion48_Object = MibScalar
motion48 = _Motion48_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 48, 6),
    _Motion48_Type()
)
motion48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion48.setStatus("mandatory")


class _Digitalin148_Type(Integer32):
    """Custom type digitalin148 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin148_Type.__name__ = "Integer32"
_Digitalin148_Object = MibScalar
digitalin148 = _Digitalin148_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 48, 7),
    _Digitalin148_Type()
)
digitalin148.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin148.setStatus("mandatory")


class _Digitalin248_Type(Integer32):
    """Custom type digitalin248 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin248_Type.__name__ = "Integer32"
_Digitalin248_Object = MibScalar
digitalin248 = _Digitalin248_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 48, 8),
    _Digitalin248_Type()
)
digitalin248.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin248.setStatus("mandatory")


class _Digitalout248_Type(Integer32):
    """Custom type digitalout248 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout248_Type.__name__ = "Integer32"
_Digitalout248_Object = MibScalar
digitalout248 = _Digitalout248_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 48, 9),
    _Digitalout248_Type()
)
digitalout248.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout248.setStatus("mandatory")


class _ComError48_Type(Integer32):
    """Custom type comError48 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError48_Type.__name__ = "Integer32"
_ComError48_Object = MibScalar
comError48 = _ComError48_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 48, 10),
    _ComError48_Type()
)
comError48.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError48.setStatus("mandatory")
_Multisensor49_ObjectIdentity = ObjectIdentity
multisensor49 = _Multisensor49_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 49)
)
_Sensorname49_Type = DisplayString
_Sensorname49_Object = MibScalar
sensorname49 = _Sensorname49_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 49, 1),
    _Sensorname49_Type()
)
sensorname49.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname49.setStatus("mandatory")


class _Temperature49_Type(Integer32):
    """Custom type temperature49 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature49_Type.__name__ = "Integer32"
_Temperature49_Object = MibScalar
temperature49 = _Temperature49_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 49, 2),
    _Temperature49_Type()
)
temperature49.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature49.setStatus("mandatory")


class _Humidity49_Type(Integer32):
    """Custom type humidity49 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity49_Type.__name__ = "Integer32"
_Humidity49_Object = MibScalar
humidity49 = _Humidity49_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 49, 3),
    _Humidity49_Type()
)
humidity49.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity49.setStatus("mandatory")


class _Dewpoint49_Type(Integer32):
    """Custom type dewpoint49 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint49_Type.__name__ = "Integer32"
_Dewpoint49_Object = MibScalar
dewpoint49 = _Dewpoint49_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 49, 4),
    _Dewpoint49_Type()
)
dewpoint49.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint49.setStatus("mandatory")


class _Co49_Type(Integer32):
    """Custom type co49 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co49_Type.__name__ = "Integer32"
_Co49_Object = MibScalar
co49 = _Co49_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 49, 5),
    _Co49_Type()
)
co49.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co49.setStatus("mandatory")


class _Motion49_Type(Integer32):
    """Custom type motion49 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion49_Type.__name__ = "Integer32"
_Motion49_Object = MibScalar
motion49 = _Motion49_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 49, 6),
    _Motion49_Type()
)
motion49.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion49.setStatus("mandatory")


class _Digitalin149_Type(Integer32):
    """Custom type digitalin149 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin149_Type.__name__ = "Integer32"
_Digitalin149_Object = MibScalar
digitalin149 = _Digitalin149_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 49, 7),
    _Digitalin149_Type()
)
digitalin149.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin149.setStatus("mandatory")


class _Digitalin249_Type(Integer32):
    """Custom type digitalin249 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin249_Type.__name__ = "Integer32"
_Digitalin249_Object = MibScalar
digitalin249 = _Digitalin249_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 49, 8),
    _Digitalin249_Type()
)
digitalin249.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin249.setStatus("mandatory")


class _Digitalout249_Type(Integer32):
    """Custom type digitalout249 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout249_Type.__name__ = "Integer32"
_Digitalout249_Object = MibScalar
digitalout249 = _Digitalout249_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 49, 9),
    _Digitalout249_Type()
)
digitalout249.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout249.setStatus("mandatory")


class _ComError49_Type(Integer32):
    """Custom type comError49 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError49_Type.__name__ = "Integer32"
_ComError49_Object = MibScalar
comError49 = _ComError49_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 49, 10),
    _ComError49_Type()
)
comError49.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError49.setStatus("mandatory")
_Multisensor50_ObjectIdentity = ObjectIdentity
multisensor50 = _Multisensor50_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 50)
)
_Sensorname50_Type = DisplayString
_Sensorname50_Object = MibScalar
sensorname50 = _Sensorname50_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 50, 1),
    _Sensorname50_Type()
)
sensorname50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname50.setStatus("mandatory")


class _Temperature50_Type(Integer32):
    """Custom type temperature50 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature50_Type.__name__ = "Integer32"
_Temperature50_Object = MibScalar
temperature50 = _Temperature50_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 50, 2),
    _Temperature50_Type()
)
temperature50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature50.setStatus("mandatory")


class _Humidity50_Type(Integer32):
    """Custom type humidity50 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity50_Type.__name__ = "Integer32"
_Humidity50_Object = MibScalar
humidity50 = _Humidity50_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 50, 3),
    _Humidity50_Type()
)
humidity50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity50.setStatus("mandatory")


class _Dewpoint50_Type(Integer32):
    """Custom type dewpoint50 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint50_Type.__name__ = "Integer32"
_Dewpoint50_Object = MibScalar
dewpoint50 = _Dewpoint50_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 50, 4),
    _Dewpoint50_Type()
)
dewpoint50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint50.setStatus("mandatory")


class _Co50_Type(Integer32):
    """Custom type co50 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co50_Type.__name__ = "Integer32"
_Co50_Object = MibScalar
co50 = _Co50_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 50, 5),
    _Co50_Type()
)
co50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co50.setStatus("mandatory")


class _Motion50_Type(Integer32):
    """Custom type motion50 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion50_Type.__name__ = "Integer32"
_Motion50_Object = MibScalar
motion50 = _Motion50_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 50, 6),
    _Motion50_Type()
)
motion50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion50.setStatus("mandatory")


class _Digitalin150_Type(Integer32):
    """Custom type digitalin150 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin150_Type.__name__ = "Integer32"
_Digitalin150_Object = MibScalar
digitalin150 = _Digitalin150_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 50, 7),
    _Digitalin150_Type()
)
digitalin150.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin150.setStatus("mandatory")


class _Digitalin250_Type(Integer32):
    """Custom type digitalin250 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin250_Type.__name__ = "Integer32"
_Digitalin250_Object = MibScalar
digitalin250 = _Digitalin250_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 50, 8),
    _Digitalin250_Type()
)
digitalin250.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin250.setStatus("mandatory")


class _Digitalout250_Type(Integer32):
    """Custom type digitalout250 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout250_Type.__name__ = "Integer32"
_Digitalout250_Object = MibScalar
digitalout250 = _Digitalout250_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 50, 9),
    _Digitalout250_Type()
)
digitalout250.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout250.setStatus("mandatory")


class _ComError50_Type(Integer32):
    """Custom type comError50 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError50_Type.__name__ = "Integer32"
_ComError50_Object = MibScalar
comError50 = _ComError50_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 50, 10),
    _ComError50_Type()
)
comError50.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError50.setStatus("mandatory")
_Multisensor51_ObjectIdentity = ObjectIdentity
multisensor51 = _Multisensor51_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 51)
)
_Sensorname51_Type = DisplayString
_Sensorname51_Object = MibScalar
sensorname51 = _Sensorname51_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 51, 1),
    _Sensorname51_Type()
)
sensorname51.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname51.setStatus("mandatory")


class _Temperature51_Type(Integer32):
    """Custom type temperature51 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature51_Type.__name__ = "Integer32"
_Temperature51_Object = MibScalar
temperature51 = _Temperature51_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 51, 2),
    _Temperature51_Type()
)
temperature51.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature51.setStatus("mandatory")


class _Humidity51_Type(Integer32):
    """Custom type humidity51 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity51_Type.__name__ = "Integer32"
_Humidity51_Object = MibScalar
humidity51 = _Humidity51_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 51, 3),
    _Humidity51_Type()
)
humidity51.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity51.setStatus("mandatory")


class _Dewpoint51_Type(Integer32):
    """Custom type dewpoint51 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint51_Type.__name__ = "Integer32"
_Dewpoint51_Object = MibScalar
dewpoint51 = _Dewpoint51_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 51, 4),
    _Dewpoint51_Type()
)
dewpoint51.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint51.setStatus("mandatory")


class _Co51_Type(Integer32):
    """Custom type co51 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co51_Type.__name__ = "Integer32"
_Co51_Object = MibScalar
co51 = _Co51_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 51, 5),
    _Co51_Type()
)
co51.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co51.setStatus("mandatory")


class _Motion51_Type(Integer32):
    """Custom type motion51 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion51_Type.__name__ = "Integer32"
_Motion51_Object = MibScalar
motion51 = _Motion51_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 51, 6),
    _Motion51_Type()
)
motion51.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion51.setStatus("mandatory")


class _Digitalin151_Type(Integer32):
    """Custom type digitalin151 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin151_Type.__name__ = "Integer32"
_Digitalin151_Object = MibScalar
digitalin151 = _Digitalin151_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 51, 7),
    _Digitalin151_Type()
)
digitalin151.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin151.setStatus("mandatory")


class _Digitalin251_Type(Integer32):
    """Custom type digitalin251 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin251_Type.__name__ = "Integer32"
_Digitalin251_Object = MibScalar
digitalin251 = _Digitalin251_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 51, 8),
    _Digitalin251_Type()
)
digitalin251.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin251.setStatus("mandatory")


class _Digitalout251_Type(Integer32):
    """Custom type digitalout251 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout251_Type.__name__ = "Integer32"
_Digitalout251_Object = MibScalar
digitalout251 = _Digitalout251_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 51, 9),
    _Digitalout251_Type()
)
digitalout251.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout251.setStatus("mandatory")


class _ComError51_Type(Integer32):
    """Custom type comError51 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError51_Type.__name__ = "Integer32"
_ComError51_Object = MibScalar
comError51 = _ComError51_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 51, 10),
    _ComError51_Type()
)
comError51.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError51.setStatus("mandatory")
_Multisensor52_ObjectIdentity = ObjectIdentity
multisensor52 = _Multisensor52_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 52)
)
_Sensorname52_Type = DisplayString
_Sensorname52_Object = MibScalar
sensorname52 = _Sensorname52_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 52, 1),
    _Sensorname52_Type()
)
sensorname52.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname52.setStatus("mandatory")


class _Temperature52_Type(Integer32):
    """Custom type temperature52 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature52_Type.__name__ = "Integer32"
_Temperature52_Object = MibScalar
temperature52 = _Temperature52_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 52, 2),
    _Temperature52_Type()
)
temperature52.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature52.setStatus("mandatory")


class _Humidity52_Type(Integer32):
    """Custom type humidity52 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity52_Type.__name__ = "Integer32"
_Humidity52_Object = MibScalar
humidity52 = _Humidity52_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 52, 3),
    _Humidity52_Type()
)
humidity52.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity52.setStatus("mandatory")


class _Dewpoint52_Type(Integer32):
    """Custom type dewpoint52 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint52_Type.__name__ = "Integer32"
_Dewpoint52_Object = MibScalar
dewpoint52 = _Dewpoint52_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 52, 4),
    _Dewpoint52_Type()
)
dewpoint52.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint52.setStatus("mandatory")


class _Co52_Type(Integer32):
    """Custom type co52 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co52_Type.__name__ = "Integer32"
_Co52_Object = MibScalar
co52 = _Co52_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 52, 5),
    _Co52_Type()
)
co52.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co52.setStatus("mandatory")


class _Motion52_Type(Integer32):
    """Custom type motion52 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion52_Type.__name__ = "Integer32"
_Motion52_Object = MibScalar
motion52 = _Motion52_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 52, 6),
    _Motion52_Type()
)
motion52.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion52.setStatus("mandatory")


class _Digitalin152_Type(Integer32):
    """Custom type digitalin152 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin152_Type.__name__ = "Integer32"
_Digitalin152_Object = MibScalar
digitalin152 = _Digitalin152_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 52, 7),
    _Digitalin152_Type()
)
digitalin152.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin152.setStatus("mandatory")


class _Digitalin252_Type(Integer32):
    """Custom type digitalin252 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin252_Type.__name__ = "Integer32"
_Digitalin252_Object = MibScalar
digitalin252 = _Digitalin252_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 52, 8),
    _Digitalin252_Type()
)
digitalin252.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin252.setStatus("mandatory")


class _Digitalout252_Type(Integer32):
    """Custom type digitalout252 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout252_Type.__name__ = "Integer32"
_Digitalout252_Object = MibScalar
digitalout252 = _Digitalout252_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 52, 9),
    _Digitalout252_Type()
)
digitalout252.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout252.setStatus("mandatory")


class _ComError52_Type(Integer32):
    """Custom type comError52 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError52_Type.__name__ = "Integer32"
_ComError52_Object = MibScalar
comError52 = _ComError52_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 52, 10),
    _ComError52_Type()
)
comError52.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError52.setStatus("mandatory")
_Multisensor53_ObjectIdentity = ObjectIdentity
multisensor53 = _Multisensor53_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 53)
)
_Sensorname53_Type = DisplayString
_Sensorname53_Object = MibScalar
sensorname53 = _Sensorname53_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 53, 1),
    _Sensorname53_Type()
)
sensorname53.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname53.setStatus("mandatory")


class _Temperature53_Type(Integer32):
    """Custom type temperature53 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature53_Type.__name__ = "Integer32"
_Temperature53_Object = MibScalar
temperature53 = _Temperature53_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 53, 2),
    _Temperature53_Type()
)
temperature53.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature53.setStatus("mandatory")


class _Humidity53_Type(Integer32):
    """Custom type humidity53 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity53_Type.__name__ = "Integer32"
_Humidity53_Object = MibScalar
humidity53 = _Humidity53_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 53, 3),
    _Humidity53_Type()
)
humidity53.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity53.setStatus("mandatory")


class _Dewpoint53_Type(Integer32):
    """Custom type dewpoint53 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint53_Type.__name__ = "Integer32"
_Dewpoint53_Object = MibScalar
dewpoint53 = _Dewpoint53_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 53, 4),
    _Dewpoint53_Type()
)
dewpoint53.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint53.setStatus("mandatory")


class _Co53_Type(Integer32):
    """Custom type co53 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co53_Type.__name__ = "Integer32"
_Co53_Object = MibScalar
co53 = _Co53_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 53, 5),
    _Co53_Type()
)
co53.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co53.setStatus("mandatory")


class _Motion53_Type(Integer32):
    """Custom type motion53 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion53_Type.__name__ = "Integer32"
_Motion53_Object = MibScalar
motion53 = _Motion53_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 53, 6),
    _Motion53_Type()
)
motion53.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion53.setStatus("mandatory")


class _Digitalin153_Type(Integer32):
    """Custom type digitalin153 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin153_Type.__name__ = "Integer32"
_Digitalin153_Object = MibScalar
digitalin153 = _Digitalin153_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 53, 7),
    _Digitalin153_Type()
)
digitalin153.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin153.setStatus("mandatory")


class _Digitalin253_Type(Integer32):
    """Custom type digitalin253 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin253_Type.__name__ = "Integer32"
_Digitalin253_Object = MibScalar
digitalin253 = _Digitalin253_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 53, 8),
    _Digitalin253_Type()
)
digitalin253.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin253.setStatus("mandatory")


class _Digitalout253_Type(Integer32):
    """Custom type digitalout253 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout253_Type.__name__ = "Integer32"
_Digitalout253_Object = MibScalar
digitalout253 = _Digitalout253_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 53, 9),
    _Digitalout253_Type()
)
digitalout253.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout253.setStatus("mandatory")


class _ComError53_Type(Integer32):
    """Custom type comError53 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError53_Type.__name__ = "Integer32"
_ComError53_Object = MibScalar
comError53 = _ComError53_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 53, 10),
    _ComError53_Type()
)
comError53.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError53.setStatus("mandatory")
_Multisensor54_ObjectIdentity = ObjectIdentity
multisensor54 = _Multisensor54_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 54)
)
_Sensorname54_Type = DisplayString
_Sensorname54_Object = MibScalar
sensorname54 = _Sensorname54_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 54, 1),
    _Sensorname54_Type()
)
sensorname54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname54.setStatus("mandatory")


class _Temperature54_Type(Integer32):
    """Custom type temperature54 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature54_Type.__name__ = "Integer32"
_Temperature54_Object = MibScalar
temperature54 = _Temperature54_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 54, 2),
    _Temperature54_Type()
)
temperature54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature54.setStatus("mandatory")


class _Humidity54_Type(Integer32):
    """Custom type humidity54 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity54_Type.__name__ = "Integer32"
_Humidity54_Object = MibScalar
humidity54 = _Humidity54_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 54, 3),
    _Humidity54_Type()
)
humidity54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity54.setStatus("mandatory")


class _Dewpoint54_Type(Integer32):
    """Custom type dewpoint54 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint54_Type.__name__ = "Integer32"
_Dewpoint54_Object = MibScalar
dewpoint54 = _Dewpoint54_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 54, 4),
    _Dewpoint54_Type()
)
dewpoint54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint54.setStatus("mandatory")


class _Co54_Type(Integer32):
    """Custom type co54 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co54_Type.__name__ = "Integer32"
_Co54_Object = MibScalar
co54 = _Co54_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 54, 5),
    _Co54_Type()
)
co54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co54.setStatus("mandatory")


class _Motion54_Type(Integer32):
    """Custom type motion54 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion54_Type.__name__ = "Integer32"
_Motion54_Object = MibScalar
motion54 = _Motion54_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 54, 6),
    _Motion54_Type()
)
motion54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion54.setStatus("mandatory")


class _Digitalin154_Type(Integer32):
    """Custom type digitalin154 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin154_Type.__name__ = "Integer32"
_Digitalin154_Object = MibScalar
digitalin154 = _Digitalin154_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 54, 7),
    _Digitalin154_Type()
)
digitalin154.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin154.setStatus("mandatory")


class _Digitalin254_Type(Integer32):
    """Custom type digitalin254 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin254_Type.__name__ = "Integer32"
_Digitalin254_Object = MibScalar
digitalin254 = _Digitalin254_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 54, 8),
    _Digitalin254_Type()
)
digitalin254.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin254.setStatus("mandatory")


class _Digitalout254_Type(Integer32):
    """Custom type digitalout254 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout254_Type.__name__ = "Integer32"
_Digitalout254_Object = MibScalar
digitalout254 = _Digitalout254_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 54, 9),
    _Digitalout254_Type()
)
digitalout254.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout254.setStatus("mandatory")


class _ComError54_Type(Integer32):
    """Custom type comError54 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError54_Type.__name__ = "Integer32"
_ComError54_Object = MibScalar
comError54 = _ComError54_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 54, 10),
    _ComError54_Type()
)
comError54.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError54.setStatus("mandatory")
_Multisensor55_ObjectIdentity = ObjectIdentity
multisensor55 = _Multisensor55_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 55)
)
_Sensorname55_Type = DisplayString
_Sensorname55_Object = MibScalar
sensorname55 = _Sensorname55_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 55, 1),
    _Sensorname55_Type()
)
sensorname55.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname55.setStatus("mandatory")


class _Temperature55_Type(Integer32):
    """Custom type temperature55 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature55_Type.__name__ = "Integer32"
_Temperature55_Object = MibScalar
temperature55 = _Temperature55_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 55, 2),
    _Temperature55_Type()
)
temperature55.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature55.setStatus("mandatory")


class _Humidity55_Type(Integer32):
    """Custom type humidity55 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity55_Type.__name__ = "Integer32"
_Humidity55_Object = MibScalar
humidity55 = _Humidity55_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 55, 3),
    _Humidity55_Type()
)
humidity55.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity55.setStatus("mandatory")


class _Dewpoint55_Type(Integer32):
    """Custom type dewpoint55 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint55_Type.__name__ = "Integer32"
_Dewpoint55_Object = MibScalar
dewpoint55 = _Dewpoint55_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 55, 4),
    _Dewpoint55_Type()
)
dewpoint55.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint55.setStatus("mandatory")


class _Co55_Type(Integer32):
    """Custom type co55 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co55_Type.__name__ = "Integer32"
_Co55_Object = MibScalar
co55 = _Co55_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 55, 5),
    _Co55_Type()
)
co55.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co55.setStatus("mandatory")


class _Motion55_Type(Integer32):
    """Custom type motion55 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion55_Type.__name__ = "Integer32"
_Motion55_Object = MibScalar
motion55 = _Motion55_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 55, 6),
    _Motion55_Type()
)
motion55.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion55.setStatus("mandatory")


class _Digitalin155_Type(Integer32):
    """Custom type digitalin155 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin155_Type.__name__ = "Integer32"
_Digitalin155_Object = MibScalar
digitalin155 = _Digitalin155_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 55, 7),
    _Digitalin155_Type()
)
digitalin155.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin155.setStatus("mandatory")


class _Digitalin255_Type(Integer32):
    """Custom type digitalin255 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin255_Type.__name__ = "Integer32"
_Digitalin255_Object = MibScalar
digitalin255 = _Digitalin255_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 55, 8),
    _Digitalin255_Type()
)
digitalin255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin255.setStatus("mandatory")


class _Digitalout255_Type(Integer32):
    """Custom type digitalout255 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout255_Type.__name__ = "Integer32"
_Digitalout255_Object = MibScalar
digitalout255 = _Digitalout255_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 55, 9),
    _Digitalout255_Type()
)
digitalout255.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout255.setStatus("mandatory")


class _ComError55_Type(Integer32):
    """Custom type comError55 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError55_Type.__name__ = "Integer32"
_ComError55_Object = MibScalar
comError55 = _ComError55_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 55, 10),
    _ComError55_Type()
)
comError55.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError55.setStatus("mandatory")
_Multisensor56_ObjectIdentity = ObjectIdentity
multisensor56 = _Multisensor56_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 56)
)
_Sensorname56_Type = DisplayString
_Sensorname56_Object = MibScalar
sensorname56 = _Sensorname56_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 56, 1),
    _Sensorname56_Type()
)
sensorname56.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname56.setStatus("mandatory")


class _Temperature56_Type(Integer32):
    """Custom type temperature56 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature56_Type.__name__ = "Integer32"
_Temperature56_Object = MibScalar
temperature56 = _Temperature56_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 56, 2),
    _Temperature56_Type()
)
temperature56.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature56.setStatus("mandatory")


class _Humidity56_Type(Integer32):
    """Custom type humidity56 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity56_Type.__name__ = "Integer32"
_Humidity56_Object = MibScalar
humidity56 = _Humidity56_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 56, 3),
    _Humidity56_Type()
)
humidity56.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity56.setStatus("mandatory")


class _Dewpoint56_Type(Integer32):
    """Custom type dewpoint56 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint56_Type.__name__ = "Integer32"
_Dewpoint56_Object = MibScalar
dewpoint56 = _Dewpoint56_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 56, 4),
    _Dewpoint56_Type()
)
dewpoint56.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint56.setStatus("mandatory")


class _Co56_Type(Integer32):
    """Custom type co56 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co56_Type.__name__ = "Integer32"
_Co56_Object = MibScalar
co56 = _Co56_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 56, 5),
    _Co56_Type()
)
co56.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co56.setStatus("mandatory")


class _Motion56_Type(Integer32):
    """Custom type motion56 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion56_Type.__name__ = "Integer32"
_Motion56_Object = MibScalar
motion56 = _Motion56_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 56, 6),
    _Motion56_Type()
)
motion56.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion56.setStatus("mandatory")


class _Digitalin156_Type(Integer32):
    """Custom type digitalin156 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin156_Type.__name__ = "Integer32"
_Digitalin156_Object = MibScalar
digitalin156 = _Digitalin156_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 56, 7),
    _Digitalin156_Type()
)
digitalin156.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin156.setStatus("mandatory")


class _Digitalin256_Type(Integer32):
    """Custom type digitalin256 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin256_Type.__name__ = "Integer32"
_Digitalin256_Object = MibScalar
digitalin256 = _Digitalin256_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 56, 8),
    _Digitalin256_Type()
)
digitalin256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin256.setStatus("mandatory")


class _Digitalout256_Type(Integer32):
    """Custom type digitalout256 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout256_Type.__name__ = "Integer32"
_Digitalout256_Object = MibScalar
digitalout256 = _Digitalout256_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 56, 9),
    _Digitalout256_Type()
)
digitalout256.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout256.setStatus("mandatory")


class _ComError56_Type(Integer32):
    """Custom type comError56 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError56_Type.__name__ = "Integer32"
_ComError56_Object = MibScalar
comError56 = _ComError56_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 56, 10),
    _ComError56_Type()
)
comError56.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError56.setStatus("mandatory")
_Multisensor57_ObjectIdentity = ObjectIdentity
multisensor57 = _Multisensor57_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 57)
)
_Sensorname57_Type = DisplayString
_Sensorname57_Object = MibScalar
sensorname57 = _Sensorname57_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 57, 1),
    _Sensorname57_Type()
)
sensorname57.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname57.setStatus("mandatory")


class _Temperature57_Type(Integer32):
    """Custom type temperature57 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature57_Type.__name__ = "Integer32"
_Temperature57_Object = MibScalar
temperature57 = _Temperature57_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 57, 2),
    _Temperature57_Type()
)
temperature57.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature57.setStatus("mandatory")


class _Humidity57_Type(Integer32):
    """Custom type humidity57 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity57_Type.__name__ = "Integer32"
_Humidity57_Object = MibScalar
humidity57 = _Humidity57_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 57, 3),
    _Humidity57_Type()
)
humidity57.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity57.setStatus("mandatory")


class _Dewpoint57_Type(Integer32):
    """Custom type dewpoint57 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint57_Type.__name__ = "Integer32"
_Dewpoint57_Object = MibScalar
dewpoint57 = _Dewpoint57_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 57, 4),
    _Dewpoint57_Type()
)
dewpoint57.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint57.setStatus("mandatory")


class _Co57_Type(Integer32):
    """Custom type co57 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co57_Type.__name__ = "Integer32"
_Co57_Object = MibScalar
co57 = _Co57_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 57, 5),
    _Co57_Type()
)
co57.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co57.setStatus("mandatory")


class _Motion57_Type(Integer32):
    """Custom type motion57 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion57_Type.__name__ = "Integer32"
_Motion57_Object = MibScalar
motion57 = _Motion57_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 57, 6),
    _Motion57_Type()
)
motion57.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion57.setStatus("mandatory")


class _Digitalin157_Type(Integer32):
    """Custom type digitalin157 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin157_Type.__name__ = "Integer32"
_Digitalin157_Object = MibScalar
digitalin157 = _Digitalin157_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 57, 7),
    _Digitalin157_Type()
)
digitalin157.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin157.setStatus("mandatory")


class _Digitalin257_Type(Integer32):
    """Custom type digitalin257 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin257_Type.__name__ = "Integer32"
_Digitalin257_Object = MibScalar
digitalin257 = _Digitalin257_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 57, 8),
    _Digitalin257_Type()
)
digitalin257.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin257.setStatus("mandatory")


class _Digitalout257_Type(Integer32):
    """Custom type digitalout257 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout257_Type.__name__ = "Integer32"
_Digitalout257_Object = MibScalar
digitalout257 = _Digitalout257_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 57, 9),
    _Digitalout257_Type()
)
digitalout257.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout257.setStatus("mandatory")


class _ComError57_Type(Integer32):
    """Custom type comError57 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError57_Type.__name__ = "Integer32"
_ComError57_Object = MibScalar
comError57 = _ComError57_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 57, 10),
    _ComError57_Type()
)
comError57.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError57.setStatus("mandatory")
_Multisensor58_ObjectIdentity = ObjectIdentity
multisensor58 = _Multisensor58_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 58)
)
_Sensorname58_Type = DisplayString
_Sensorname58_Object = MibScalar
sensorname58 = _Sensorname58_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 58, 1),
    _Sensorname58_Type()
)
sensorname58.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname58.setStatus("mandatory")


class _Temperature58_Type(Integer32):
    """Custom type temperature58 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature58_Type.__name__ = "Integer32"
_Temperature58_Object = MibScalar
temperature58 = _Temperature58_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 58, 2),
    _Temperature58_Type()
)
temperature58.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature58.setStatus("mandatory")


class _Humidity58_Type(Integer32):
    """Custom type humidity58 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity58_Type.__name__ = "Integer32"
_Humidity58_Object = MibScalar
humidity58 = _Humidity58_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 58, 3),
    _Humidity58_Type()
)
humidity58.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity58.setStatus("mandatory")


class _Dewpoint58_Type(Integer32):
    """Custom type dewpoint58 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint58_Type.__name__ = "Integer32"
_Dewpoint58_Object = MibScalar
dewpoint58 = _Dewpoint58_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 58, 4),
    _Dewpoint58_Type()
)
dewpoint58.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint58.setStatus("mandatory")


class _Co58_Type(Integer32):
    """Custom type co58 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co58_Type.__name__ = "Integer32"
_Co58_Object = MibScalar
co58 = _Co58_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 58, 5),
    _Co58_Type()
)
co58.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co58.setStatus("mandatory")


class _Motion58_Type(Integer32):
    """Custom type motion58 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion58_Type.__name__ = "Integer32"
_Motion58_Object = MibScalar
motion58 = _Motion58_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 58, 6),
    _Motion58_Type()
)
motion58.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion58.setStatus("mandatory")


class _Digitalin158_Type(Integer32):
    """Custom type digitalin158 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin158_Type.__name__ = "Integer32"
_Digitalin158_Object = MibScalar
digitalin158 = _Digitalin158_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 58, 7),
    _Digitalin158_Type()
)
digitalin158.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin158.setStatus("mandatory")


class _Digitalin258_Type(Integer32):
    """Custom type digitalin258 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin258_Type.__name__ = "Integer32"
_Digitalin258_Object = MibScalar
digitalin258 = _Digitalin258_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 58, 8),
    _Digitalin258_Type()
)
digitalin258.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin258.setStatus("mandatory")


class _Digitalout258_Type(Integer32):
    """Custom type digitalout258 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout258_Type.__name__ = "Integer32"
_Digitalout258_Object = MibScalar
digitalout258 = _Digitalout258_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 58, 9),
    _Digitalout258_Type()
)
digitalout258.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout258.setStatus("mandatory")


class _ComError58_Type(Integer32):
    """Custom type comError58 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError58_Type.__name__ = "Integer32"
_ComError58_Object = MibScalar
comError58 = _ComError58_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 58, 10),
    _ComError58_Type()
)
comError58.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError58.setStatus("mandatory")
_Multisensor59_ObjectIdentity = ObjectIdentity
multisensor59 = _Multisensor59_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 59)
)
_Sensorname59_Type = DisplayString
_Sensorname59_Object = MibScalar
sensorname59 = _Sensorname59_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 59, 1),
    _Sensorname59_Type()
)
sensorname59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname59.setStatus("mandatory")


class _Temperature59_Type(Integer32):
    """Custom type temperature59 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature59_Type.__name__ = "Integer32"
_Temperature59_Object = MibScalar
temperature59 = _Temperature59_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 59, 2),
    _Temperature59_Type()
)
temperature59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature59.setStatus("mandatory")


class _Humidity59_Type(Integer32):
    """Custom type humidity59 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity59_Type.__name__ = "Integer32"
_Humidity59_Object = MibScalar
humidity59 = _Humidity59_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 59, 3),
    _Humidity59_Type()
)
humidity59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity59.setStatus("mandatory")


class _Dewpoint59_Type(Integer32):
    """Custom type dewpoint59 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint59_Type.__name__ = "Integer32"
_Dewpoint59_Object = MibScalar
dewpoint59 = _Dewpoint59_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 59, 4),
    _Dewpoint59_Type()
)
dewpoint59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint59.setStatus("mandatory")


class _Co59_Type(Integer32):
    """Custom type co59 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co59_Type.__name__ = "Integer32"
_Co59_Object = MibScalar
co59 = _Co59_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 59, 5),
    _Co59_Type()
)
co59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co59.setStatus("mandatory")


class _Motion59_Type(Integer32):
    """Custom type motion59 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion59_Type.__name__ = "Integer32"
_Motion59_Object = MibScalar
motion59 = _Motion59_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 59, 6),
    _Motion59_Type()
)
motion59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion59.setStatus("mandatory")


class _Digitalin159_Type(Integer32):
    """Custom type digitalin159 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin159_Type.__name__ = "Integer32"
_Digitalin159_Object = MibScalar
digitalin159 = _Digitalin159_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 59, 7),
    _Digitalin159_Type()
)
digitalin159.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin159.setStatus("mandatory")


class _Digitalin259_Type(Integer32):
    """Custom type digitalin259 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin259_Type.__name__ = "Integer32"
_Digitalin259_Object = MibScalar
digitalin259 = _Digitalin259_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 59, 8),
    _Digitalin259_Type()
)
digitalin259.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin259.setStatus("mandatory")


class _Digitalout259_Type(Integer32):
    """Custom type digitalout259 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout259_Type.__name__ = "Integer32"
_Digitalout259_Object = MibScalar
digitalout259 = _Digitalout259_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 59, 9),
    _Digitalout259_Type()
)
digitalout259.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout259.setStatus("mandatory")


class _ComError59_Type(Integer32):
    """Custom type comError59 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError59_Type.__name__ = "Integer32"
_ComError59_Object = MibScalar
comError59 = _ComError59_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 59, 10),
    _ComError59_Type()
)
comError59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError59.setStatus("mandatory")
_Multisensor60_ObjectIdentity = ObjectIdentity
multisensor60 = _Multisensor60_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 60)
)
_Sensorname60_Type = DisplayString
_Sensorname60_Object = MibScalar
sensorname60 = _Sensorname60_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 60, 1),
    _Sensorname60_Type()
)
sensorname60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname60.setStatus("mandatory")


class _Temperature60_Type(Integer32):
    """Custom type temperature60 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature60_Type.__name__ = "Integer32"
_Temperature60_Object = MibScalar
temperature60 = _Temperature60_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 60, 2),
    _Temperature60_Type()
)
temperature60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature60.setStatus("mandatory")


class _Humidity60_Type(Integer32):
    """Custom type humidity60 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity60_Type.__name__ = "Integer32"
_Humidity60_Object = MibScalar
humidity60 = _Humidity60_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 60, 3),
    _Humidity60_Type()
)
humidity60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity60.setStatus("mandatory")


class _Dewpoint60_Type(Integer32):
    """Custom type dewpoint60 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint60_Type.__name__ = "Integer32"
_Dewpoint60_Object = MibScalar
dewpoint60 = _Dewpoint60_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 60, 4),
    _Dewpoint60_Type()
)
dewpoint60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint60.setStatus("mandatory")


class _Co60_Type(Integer32):
    """Custom type co60 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co60_Type.__name__ = "Integer32"
_Co60_Object = MibScalar
co60 = _Co60_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 60, 5),
    _Co60_Type()
)
co60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co60.setStatus("mandatory")


class _Motion60_Type(Integer32):
    """Custom type motion60 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion60_Type.__name__ = "Integer32"
_Motion60_Object = MibScalar
motion60 = _Motion60_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 60, 6),
    _Motion60_Type()
)
motion60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion60.setStatus("mandatory")


class _Digitalin160_Type(Integer32):
    """Custom type digitalin160 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin160_Type.__name__ = "Integer32"
_Digitalin160_Object = MibScalar
digitalin160 = _Digitalin160_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 60, 7),
    _Digitalin160_Type()
)
digitalin160.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin160.setStatus("mandatory")


class _Digitalin260_Type(Integer32):
    """Custom type digitalin260 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin260_Type.__name__ = "Integer32"
_Digitalin260_Object = MibScalar
digitalin260 = _Digitalin260_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 60, 8),
    _Digitalin260_Type()
)
digitalin260.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin260.setStatus("mandatory")


class _Digitalout260_Type(Integer32):
    """Custom type digitalout260 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout260_Type.__name__ = "Integer32"
_Digitalout260_Object = MibScalar
digitalout260 = _Digitalout260_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 60, 9),
    _Digitalout260_Type()
)
digitalout260.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout260.setStatus("mandatory")


class _ComError60_Type(Integer32):
    """Custom type comError60 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError60_Type.__name__ = "Integer32"
_ComError60_Object = MibScalar
comError60 = _ComError60_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 60, 10),
    _ComError60_Type()
)
comError60.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError60.setStatus("mandatory")
_Multisensor61_ObjectIdentity = ObjectIdentity
multisensor61 = _Multisensor61_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 61)
)
_Sensorname61_Type = DisplayString
_Sensorname61_Object = MibScalar
sensorname61 = _Sensorname61_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 61, 1),
    _Sensorname61_Type()
)
sensorname61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname61.setStatus("mandatory")


class _Temperature61_Type(Integer32):
    """Custom type temperature61 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature61_Type.__name__ = "Integer32"
_Temperature61_Object = MibScalar
temperature61 = _Temperature61_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 61, 2),
    _Temperature61_Type()
)
temperature61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature61.setStatus("mandatory")


class _Humidity61_Type(Integer32):
    """Custom type humidity61 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity61_Type.__name__ = "Integer32"
_Humidity61_Object = MibScalar
humidity61 = _Humidity61_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 61, 3),
    _Humidity61_Type()
)
humidity61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity61.setStatus("mandatory")


class _Dewpoint61_Type(Integer32):
    """Custom type dewpoint61 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint61_Type.__name__ = "Integer32"
_Dewpoint61_Object = MibScalar
dewpoint61 = _Dewpoint61_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 61, 4),
    _Dewpoint61_Type()
)
dewpoint61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint61.setStatus("mandatory")


class _Co61_Type(Integer32):
    """Custom type co61 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co61_Type.__name__ = "Integer32"
_Co61_Object = MibScalar
co61 = _Co61_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 61, 5),
    _Co61_Type()
)
co61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co61.setStatus("mandatory")


class _Motion61_Type(Integer32):
    """Custom type motion61 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion61_Type.__name__ = "Integer32"
_Motion61_Object = MibScalar
motion61 = _Motion61_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 61, 6),
    _Motion61_Type()
)
motion61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion61.setStatus("mandatory")


class _Digitalin161_Type(Integer32):
    """Custom type digitalin161 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin161_Type.__name__ = "Integer32"
_Digitalin161_Object = MibScalar
digitalin161 = _Digitalin161_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 61, 7),
    _Digitalin161_Type()
)
digitalin161.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin161.setStatus("mandatory")


class _Digitalin261_Type(Integer32):
    """Custom type digitalin261 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin261_Type.__name__ = "Integer32"
_Digitalin261_Object = MibScalar
digitalin261 = _Digitalin261_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 61, 8),
    _Digitalin261_Type()
)
digitalin261.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin261.setStatus("mandatory")


class _Digitalout261_Type(Integer32):
    """Custom type digitalout261 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout261_Type.__name__ = "Integer32"
_Digitalout261_Object = MibScalar
digitalout261 = _Digitalout261_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 61, 9),
    _Digitalout261_Type()
)
digitalout261.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout261.setStatus("mandatory")


class _ComError61_Type(Integer32):
    """Custom type comError61 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError61_Type.__name__ = "Integer32"
_ComError61_Object = MibScalar
comError61 = _ComError61_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 61, 10),
    _ComError61_Type()
)
comError61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError61.setStatus("mandatory")
_Multisensor62_ObjectIdentity = ObjectIdentity
multisensor62 = _Multisensor62_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 62)
)
_Sensorname62_Type = DisplayString
_Sensorname62_Object = MibScalar
sensorname62 = _Sensorname62_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 62, 1),
    _Sensorname62_Type()
)
sensorname62.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname62.setStatus("mandatory")


class _Temperature62_Type(Integer32):
    """Custom type temperature62 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature62_Type.__name__ = "Integer32"
_Temperature62_Object = MibScalar
temperature62 = _Temperature62_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 62, 2),
    _Temperature62_Type()
)
temperature62.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature62.setStatus("mandatory")


class _Humidity62_Type(Integer32):
    """Custom type humidity62 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity62_Type.__name__ = "Integer32"
_Humidity62_Object = MibScalar
humidity62 = _Humidity62_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 62, 3),
    _Humidity62_Type()
)
humidity62.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity62.setStatus("mandatory")


class _Dewpoint62_Type(Integer32):
    """Custom type dewpoint62 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint62_Type.__name__ = "Integer32"
_Dewpoint62_Object = MibScalar
dewpoint62 = _Dewpoint62_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 62, 4),
    _Dewpoint62_Type()
)
dewpoint62.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint62.setStatus("mandatory")


class _Co62_Type(Integer32):
    """Custom type co62 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co62_Type.__name__ = "Integer32"
_Co62_Object = MibScalar
co62 = _Co62_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 62, 5),
    _Co62_Type()
)
co62.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co62.setStatus("mandatory")


class _Motion62_Type(Integer32):
    """Custom type motion62 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion62_Type.__name__ = "Integer32"
_Motion62_Object = MibScalar
motion62 = _Motion62_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 62, 6),
    _Motion62_Type()
)
motion62.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion62.setStatus("mandatory")


class _Digitalin162_Type(Integer32):
    """Custom type digitalin162 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin162_Type.__name__ = "Integer32"
_Digitalin162_Object = MibScalar
digitalin162 = _Digitalin162_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 62, 7),
    _Digitalin162_Type()
)
digitalin162.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin162.setStatus("mandatory")


class _Digitalin262_Type(Integer32):
    """Custom type digitalin262 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin262_Type.__name__ = "Integer32"
_Digitalin262_Object = MibScalar
digitalin262 = _Digitalin262_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 62, 8),
    _Digitalin262_Type()
)
digitalin262.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin262.setStatus("mandatory")


class _Digitalout262_Type(Integer32):
    """Custom type digitalout262 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout262_Type.__name__ = "Integer32"
_Digitalout262_Object = MibScalar
digitalout262 = _Digitalout262_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 62, 9),
    _Digitalout262_Type()
)
digitalout262.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout262.setStatus("mandatory")


class _ComError62_Type(Integer32):
    """Custom type comError62 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError62_Type.__name__ = "Integer32"
_ComError62_Object = MibScalar
comError62 = _ComError62_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 62, 10),
    _ComError62_Type()
)
comError62.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError62.setStatus("mandatory")
_Multisensor63_ObjectIdentity = ObjectIdentity
multisensor63 = _Multisensor63_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 63)
)
_Sensorname63_Type = DisplayString
_Sensorname63_Object = MibScalar
sensorname63 = _Sensorname63_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 63, 1),
    _Sensorname63_Type()
)
sensorname63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname63.setStatus("mandatory")


class _Temperature63_Type(Integer32):
    """Custom type temperature63 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature63_Type.__name__ = "Integer32"
_Temperature63_Object = MibScalar
temperature63 = _Temperature63_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 63, 2),
    _Temperature63_Type()
)
temperature63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature63.setStatus("mandatory")


class _Humidity63_Type(Integer32):
    """Custom type humidity63 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity63_Type.__name__ = "Integer32"
_Humidity63_Object = MibScalar
humidity63 = _Humidity63_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 63, 3),
    _Humidity63_Type()
)
humidity63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity63.setStatus("mandatory")


class _Dewpoint63_Type(Integer32):
    """Custom type dewpoint63 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint63_Type.__name__ = "Integer32"
_Dewpoint63_Object = MibScalar
dewpoint63 = _Dewpoint63_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 63, 4),
    _Dewpoint63_Type()
)
dewpoint63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint63.setStatus("mandatory")


class _Co63_Type(Integer32):
    """Custom type co63 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co63_Type.__name__ = "Integer32"
_Co63_Object = MibScalar
co63 = _Co63_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 63, 5),
    _Co63_Type()
)
co63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co63.setStatus("mandatory")


class _Motion63_Type(Integer32):
    """Custom type motion63 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion63_Type.__name__ = "Integer32"
_Motion63_Object = MibScalar
motion63 = _Motion63_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 63, 6),
    _Motion63_Type()
)
motion63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion63.setStatus("mandatory")


class _Digitalin163_Type(Integer32):
    """Custom type digitalin163 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin163_Type.__name__ = "Integer32"
_Digitalin163_Object = MibScalar
digitalin163 = _Digitalin163_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 63, 7),
    _Digitalin163_Type()
)
digitalin163.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin163.setStatus("mandatory")


class _Digitalin263_Type(Integer32):
    """Custom type digitalin263 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin263_Type.__name__ = "Integer32"
_Digitalin263_Object = MibScalar
digitalin263 = _Digitalin263_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 63, 8),
    _Digitalin263_Type()
)
digitalin263.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin263.setStatus("mandatory")


class _Digitalout263_Type(Integer32):
    """Custom type digitalout263 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout263_Type.__name__ = "Integer32"
_Digitalout263_Object = MibScalar
digitalout263 = _Digitalout263_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 63, 9),
    _Digitalout263_Type()
)
digitalout263.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout263.setStatus("mandatory")


class _ComError63_Type(Integer32):
    """Custom type comError63 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError63_Type.__name__ = "Integer32"
_ComError63_Object = MibScalar
comError63 = _ComError63_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 63, 10),
    _ComError63_Type()
)
comError63.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError63.setStatus("mandatory")
_Multisensor64_ObjectIdentity = ObjectIdentity
multisensor64 = _Multisensor64_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 64)
)
_Sensorname64_Type = DisplayString
_Sensorname64_Object = MibScalar
sensorname64 = _Sensorname64_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 64, 1),
    _Sensorname64_Type()
)
sensorname64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname64.setStatus("mandatory")


class _Temperature64_Type(Integer32):
    """Custom type temperature64 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature64_Type.__name__ = "Integer32"
_Temperature64_Object = MibScalar
temperature64 = _Temperature64_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 64, 2),
    _Temperature64_Type()
)
temperature64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature64.setStatus("mandatory")


class _Humidity64_Type(Integer32):
    """Custom type humidity64 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity64_Type.__name__ = "Integer32"
_Humidity64_Object = MibScalar
humidity64 = _Humidity64_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 64, 3),
    _Humidity64_Type()
)
humidity64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity64.setStatus("mandatory")


class _Dewpoint64_Type(Integer32):
    """Custom type dewpoint64 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint64_Type.__name__ = "Integer32"
_Dewpoint64_Object = MibScalar
dewpoint64 = _Dewpoint64_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 64, 4),
    _Dewpoint64_Type()
)
dewpoint64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint64.setStatus("mandatory")


class _Co64_Type(Integer32):
    """Custom type co64 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co64_Type.__name__ = "Integer32"
_Co64_Object = MibScalar
co64 = _Co64_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 64, 5),
    _Co64_Type()
)
co64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co64.setStatus("mandatory")


class _Motion64_Type(Integer32):
    """Custom type motion64 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion64_Type.__name__ = "Integer32"
_Motion64_Object = MibScalar
motion64 = _Motion64_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 64, 6),
    _Motion64_Type()
)
motion64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion64.setStatus("mandatory")


class _Digitalin164_Type(Integer32):
    """Custom type digitalin164 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin164_Type.__name__ = "Integer32"
_Digitalin164_Object = MibScalar
digitalin164 = _Digitalin164_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 64, 7),
    _Digitalin164_Type()
)
digitalin164.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin164.setStatus("mandatory")


class _Digitalin264_Type(Integer32):
    """Custom type digitalin264 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin264_Type.__name__ = "Integer32"
_Digitalin264_Object = MibScalar
digitalin264 = _Digitalin264_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 64, 8),
    _Digitalin264_Type()
)
digitalin264.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin264.setStatus("mandatory")


class _Digitalout264_Type(Integer32):
    """Custom type digitalout264 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout264_Type.__name__ = "Integer32"
_Digitalout264_Object = MibScalar
digitalout264 = _Digitalout264_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 64, 9),
    _Digitalout264_Type()
)
digitalout264.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout264.setStatus("mandatory")


class _ComError64_Type(Integer32):
    """Custom type comError64 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError64_Type.__name__ = "Integer32"
_ComError64_Object = MibScalar
comError64 = _ComError64_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 64, 10),
    _ComError64_Type()
)
comError64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError64.setStatus("mandatory")
_Multisensor65_ObjectIdentity = ObjectIdentity
multisensor65 = _Multisensor65_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 65)
)
_Sensorname65_Type = DisplayString
_Sensorname65_Object = MibScalar
sensorname65 = _Sensorname65_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 65, 1),
    _Sensorname65_Type()
)
sensorname65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname65.setStatus("mandatory")


class _Temperature65_Type(Integer32):
    """Custom type temperature65 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature65_Type.__name__ = "Integer32"
_Temperature65_Object = MibScalar
temperature65 = _Temperature65_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 65, 2),
    _Temperature65_Type()
)
temperature65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature65.setStatus("mandatory")


class _Humidity65_Type(Integer32):
    """Custom type humidity65 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity65_Type.__name__ = "Integer32"
_Humidity65_Object = MibScalar
humidity65 = _Humidity65_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 65, 3),
    _Humidity65_Type()
)
humidity65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity65.setStatus("mandatory")


class _Dewpoint65_Type(Integer32):
    """Custom type dewpoint65 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint65_Type.__name__ = "Integer32"
_Dewpoint65_Object = MibScalar
dewpoint65 = _Dewpoint65_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 65, 4),
    _Dewpoint65_Type()
)
dewpoint65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint65.setStatus("mandatory")


class _Co65_Type(Integer32):
    """Custom type co65 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co65_Type.__name__ = "Integer32"
_Co65_Object = MibScalar
co65 = _Co65_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 65, 5),
    _Co65_Type()
)
co65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co65.setStatus("mandatory")


class _Motion65_Type(Integer32):
    """Custom type motion65 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion65_Type.__name__ = "Integer32"
_Motion65_Object = MibScalar
motion65 = _Motion65_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 65, 6),
    _Motion65_Type()
)
motion65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion65.setStatus("mandatory")


class _Digitalin165_Type(Integer32):
    """Custom type digitalin165 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin165_Type.__name__ = "Integer32"
_Digitalin165_Object = MibScalar
digitalin165 = _Digitalin165_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 65, 7),
    _Digitalin165_Type()
)
digitalin165.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin165.setStatus("mandatory")


class _Digitalin265_Type(Integer32):
    """Custom type digitalin265 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin265_Type.__name__ = "Integer32"
_Digitalin265_Object = MibScalar
digitalin265 = _Digitalin265_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 65, 8),
    _Digitalin265_Type()
)
digitalin265.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin265.setStatus("mandatory")


class _Digitalout265_Type(Integer32):
    """Custom type digitalout265 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout265_Type.__name__ = "Integer32"
_Digitalout265_Object = MibScalar
digitalout265 = _Digitalout265_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 65, 9),
    _Digitalout265_Type()
)
digitalout265.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout265.setStatus("mandatory")


class _ComError65_Type(Integer32):
    """Custom type comError65 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError65_Type.__name__ = "Integer32"
_ComError65_Object = MibScalar
comError65 = _ComError65_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 65, 10),
    _ComError65_Type()
)
comError65.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError65.setStatus("mandatory")
_Multisensor66_ObjectIdentity = ObjectIdentity
multisensor66 = _Multisensor66_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 66)
)
_Sensorname66_Type = DisplayString
_Sensorname66_Object = MibScalar
sensorname66 = _Sensorname66_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 66, 1),
    _Sensorname66_Type()
)
sensorname66.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname66.setStatus("mandatory")


class _Temperature66_Type(Integer32):
    """Custom type temperature66 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature66_Type.__name__ = "Integer32"
_Temperature66_Object = MibScalar
temperature66 = _Temperature66_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 66, 2),
    _Temperature66_Type()
)
temperature66.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature66.setStatus("mandatory")


class _Humidity66_Type(Integer32):
    """Custom type humidity66 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity66_Type.__name__ = "Integer32"
_Humidity66_Object = MibScalar
humidity66 = _Humidity66_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 66, 3),
    _Humidity66_Type()
)
humidity66.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity66.setStatus("mandatory")


class _Dewpoint66_Type(Integer32):
    """Custom type dewpoint66 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint66_Type.__name__ = "Integer32"
_Dewpoint66_Object = MibScalar
dewpoint66 = _Dewpoint66_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 66, 4),
    _Dewpoint66_Type()
)
dewpoint66.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint66.setStatus("mandatory")


class _Co66_Type(Integer32):
    """Custom type co66 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co66_Type.__name__ = "Integer32"
_Co66_Object = MibScalar
co66 = _Co66_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 66, 5),
    _Co66_Type()
)
co66.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co66.setStatus("mandatory")


class _Motion66_Type(Integer32):
    """Custom type motion66 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion66_Type.__name__ = "Integer32"
_Motion66_Object = MibScalar
motion66 = _Motion66_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 66, 6),
    _Motion66_Type()
)
motion66.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion66.setStatus("mandatory")


class _Digitalin166_Type(Integer32):
    """Custom type digitalin166 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin166_Type.__name__ = "Integer32"
_Digitalin166_Object = MibScalar
digitalin166 = _Digitalin166_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 66, 7),
    _Digitalin166_Type()
)
digitalin166.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin166.setStatus("mandatory")


class _Digitalin266_Type(Integer32):
    """Custom type digitalin266 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin266_Type.__name__ = "Integer32"
_Digitalin266_Object = MibScalar
digitalin266 = _Digitalin266_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 66, 8),
    _Digitalin266_Type()
)
digitalin266.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin266.setStatus("mandatory")


class _Digitalout266_Type(Integer32):
    """Custom type digitalout266 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout266_Type.__name__ = "Integer32"
_Digitalout266_Object = MibScalar
digitalout266 = _Digitalout266_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 66, 9),
    _Digitalout266_Type()
)
digitalout266.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout266.setStatus("mandatory")


class _ComError66_Type(Integer32):
    """Custom type comError66 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError66_Type.__name__ = "Integer32"
_ComError66_Object = MibScalar
comError66 = _ComError66_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 66, 10),
    _ComError66_Type()
)
comError66.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError66.setStatus("mandatory")
_Multisensor67_ObjectIdentity = ObjectIdentity
multisensor67 = _Multisensor67_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 67)
)
_Sensorname67_Type = DisplayString
_Sensorname67_Object = MibScalar
sensorname67 = _Sensorname67_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 67, 1),
    _Sensorname67_Type()
)
sensorname67.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname67.setStatus("mandatory")


class _Temperature67_Type(Integer32):
    """Custom type temperature67 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature67_Type.__name__ = "Integer32"
_Temperature67_Object = MibScalar
temperature67 = _Temperature67_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 67, 2),
    _Temperature67_Type()
)
temperature67.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature67.setStatus("mandatory")


class _Humidity67_Type(Integer32):
    """Custom type humidity67 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity67_Type.__name__ = "Integer32"
_Humidity67_Object = MibScalar
humidity67 = _Humidity67_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 67, 3),
    _Humidity67_Type()
)
humidity67.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity67.setStatus("mandatory")


class _Dewpoint67_Type(Integer32):
    """Custom type dewpoint67 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint67_Type.__name__ = "Integer32"
_Dewpoint67_Object = MibScalar
dewpoint67 = _Dewpoint67_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 67, 4),
    _Dewpoint67_Type()
)
dewpoint67.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint67.setStatus("mandatory")


class _Co67_Type(Integer32):
    """Custom type co67 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co67_Type.__name__ = "Integer32"
_Co67_Object = MibScalar
co67 = _Co67_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 67, 5),
    _Co67_Type()
)
co67.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co67.setStatus("mandatory")


class _Motion67_Type(Integer32):
    """Custom type motion67 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion67_Type.__name__ = "Integer32"
_Motion67_Object = MibScalar
motion67 = _Motion67_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 67, 6),
    _Motion67_Type()
)
motion67.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion67.setStatus("mandatory")


class _Digitalin167_Type(Integer32):
    """Custom type digitalin167 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin167_Type.__name__ = "Integer32"
_Digitalin167_Object = MibScalar
digitalin167 = _Digitalin167_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 67, 7),
    _Digitalin167_Type()
)
digitalin167.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin167.setStatus("mandatory")


class _Digitalin267_Type(Integer32):
    """Custom type digitalin267 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin267_Type.__name__ = "Integer32"
_Digitalin267_Object = MibScalar
digitalin267 = _Digitalin267_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 67, 8),
    _Digitalin267_Type()
)
digitalin267.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin267.setStatus("mandatory")


class _Digitalout267_Type(Integer32):
    """Custom type digitalout267 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout267_Type.__name__ = "Integer32"
_Digitalout267_Object = MibScalar
digitalout267 = _Digitalout267_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 67, 9),
    _Digitalout267_Type()
)
digitalout267.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout267.setStatus("mandatory")


class _ComError67_Type(Integer32):
    """Custom type comError67 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError67_Type.__name__ = "Integer32"
_ComError67_Object = MibScalar
comError67 = _ComError67_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 67, 10),
    _ComError67_Type()
)
comError67.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError67.setStatus("mandatory")
_Multisensor68_ObjectIdentity = ObjectIdentity
multisensor68 = _Multisensor68_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 68)
)
_Sensorname68_Type = DisplayString
_Sensorname68_Object = MibScalar
sensorname68 = _Sensorname68_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 68, 1),
    _Sensorname68_Type()
)
sensorname68.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname68.setStatus("mandatory")


class _Temperature68_Type(Integer32):
    """Custom type temperature68 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature68_Type.__name__ = "Integer32"
_Temperature68_Object = MibScalar
temperature68 = _Temperature68_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 68, 2),
    _Temperature68_Type()
)
temperature68.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature68.setStatus("mandatory")


class _Humidity68_Type(Integer32):
    """Custom type humidity68 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity68_Type.__name__ = "Integer32"
_Humidity68_Object = MibScalar
humidity68 = _Humidity68_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 68, 3),
    _Humidity68_Type()
)
humidity68.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity68.setStatus("mandatory")


class _Dewpoint68_Type(Integer32):
    """Custom type dewpoint68 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint68_Type.__name__ = "Integer32"
_Dewpoint68_Object = MibScalar
dewpoint68 = _Dewpoint68_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 68, 4),
    _Dewpoint68_Type()
)
dewpoint68.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint68.setStatus("mandatory")


class _Co68_Type(Integer32):
    """Custom type co68 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co68_Type.__name__ = "Integer32"
_Co68_Object = MibScalar
co68 = _Co68_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 68, 5),
    _Co68_Type()
)
co68.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co68.setStatus("mandatory")


class _Motion68_Type(Integer32):
    """Custom type motion68 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion68_Type.__name__ = "Integer32"
_Motion68_Object = MibScalar
motion68 = _Motion68_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 68, 6),
    _Motion68_Type()
)
motion68.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion68.setStatus("mandatory")


class _Digitalin168_Type(Integer32):
    """Custom type digitalin168 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin168_Type.__name__ = "Integer32"
_Digitalin168_Object = MibScalar
digitalin168 = _Digitalin168_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 68, 7),
    _Digitalin168_Type()
)
digitalin168.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin168.setStatus("mandatory")


class _Digitalin268_Type(Integer32):
    """Custom type digitalin268 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin268_Type.__name__ = "Integer32"
_Digitalin268_Object = MibScalar
digitalin268 = _Digitalin268_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 68, 8),
    _Digitalin268_Type()
)
digitalin268.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin268.setStatus("mandatory")


class _Digitalout268_Type(Integer32):
    """Custom type digitalout268 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout268_Type.__name__ = "Integer32"
_Digitalout268_Object = MibScalar
digitalout268 = _Digitalout268_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 68, 9),
    _Digitalout268_Type()
)
digitalout268.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout268.setStatus("mandatory")


class _ComError68_Type(Integer32):
    """Custom type comError68 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError68_Type.__name__ = "Integer32"
_ComError68_Object = MibScalar
comError68 = _ComError68_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 68, 10),
    _ComError68_Type()
)
comError68.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError68.setStatus("mandatory")
_Multisensor69_ObjectIdentity = ObjectIdentity
multisensor69 = _Multisensor69_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 69)
)
_Sensorname69_Type = DisplayString
_Sensorname69_Object = MibScalar
sensorname69 = _Sensorname69_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 69, 1),
    _Sensorname69_Type()
)
sensorname69.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname69.setStatus("mandatory")


class _Temperature69_Type(Integer32):
    """Custom type temperature69 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature69_Type.__name__ = "Integer32"
_Temperature69_Object = MibScalar
temperature69 = _Temperature69_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 69, 2),
    _Temperature69_Type()
)
temperature69.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature69.setStatus("mandatory")


class _Humidity69_Type(Integer32):
    """Custom type humidity69 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity69_Type.__name__ = "Integer32"
_Humidity69_Object = MibScalar
humidity69 = _Humidity69_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 69, 3),
    _Humidity69_Type()
)
humidity69.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity69.setStatus("mandatory")


class _Dewpoint69_Type(Integer32):
    """Custom type dewpoint69 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint69_Type.__name__ = "Integer32"
_Dewpoint69_Object = MibScalar
dewpoint69 = _Dewpoint69_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 69, 4),
    _Dewpoint69_Type()
)
dewpoint69.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint69.setStatus("mandatory")


class _Co69_Type(Integer32):
    """Custom type co69 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co69_Type.__name__ = "Integer32"
_Co69_Object = MibScalar
co69 = _Co69_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 69, 5),
    _Co69_Type()
)
co69.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co69.setStatus("mandatory")


class _Motion69_Type(Integer32):
    """Custom type motion69 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion69_Type.__name__ = "Integer32"
_Motion69_Object = MibScalar
motion69 = _Motion69_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 69, 6),
    _Motion69_Type()
)
motion69.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion69.setStatus("mandatory")


class _Digitalin169_Type(Integer32):
    """Custom type digitalin169 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin169_Type.__name__ = "Integer32"
_Digitalin169_Object = MibScalar
digitalin169 = _Digitalin169_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 69, 7),
    _Digitalin169_Type()
)
digitalin169.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin169.setStatus("mandatory")


class _Digitalin269_Type(Integer32):
    """Custom type digitalin269 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin269_Type.__name__ = "Integer32"
_Digitalin269_Object = MibScalar
digitalin269 = _Digitalin269_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 69, 8),
    _Digitalin269_Type()
)
digitalin269.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin269.setStatus("mandatory")


class _Digitalout269_Type(Integer32):
    """Custom type digitalout269 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout269_Type.__name__ = "Integer32"
_Digitalout269_Object = MibScalar
digitalout269 = _Digitalout269_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 69, 9),
    _Digitalout269_Type()
)
digitalout269.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout269.setStatus("mandatory")


class _ComError69_Type(Integer32):
    """Custom type comError69 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError69_Type.__name__ = "Integer32"
_ComError69_Object = MibScalar
comError69 = _ComError69_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 69, 10),
    _ComError69_Type()
)
comError69.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError69.setStatus("mandatory")
_Multisensor70_ObjectIdentity = ObjectIdentity
multisensor70 = _Multisensor70_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 70)
)
_Sensorname70_Type = DisplayString
_Sensorname70_Object = MibScalar
sensorname70 = _Sensorname70_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 70, 1),
    _Sensorname70_Type()
)
sensorname70.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname70.setStatus("mandatory")


class _Temperature70_Type(Integer32):
    """Custom type temperature70 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature70_Type.__name__ = "Integer32"
_Temperature70_Object = MibScalar
temperature70 = _Temperature70_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 70, 2),
    _Temperature70_Type()
)
temperature70.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature70.setStatus("mandatory")


class _Humidity70_Type(Integer32):
    """Custom type humidity70 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity70_Type.__name__ = "Integer32"
_Humidity70_Object = MibScalar
humidity70 = _Humidity70_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 70, 3),
    _Humidity70_Type()
)
humidity70.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity70.setStatus("mandatory")


class _Dewpoint70_Type(Integer32):
    """Custom type dewpoint70 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint70_Type.__name__ = "Integer32"
_Dewpoint70_Object = MibScalar
dewpoint70 = _Dewpoint70_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 70, 4),
    _Dewpoint70_Type()
)
dewpoint70.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint70.setStatus("mandatory")


class _Co70_Type(Integer32):
    """Custom type co70 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co70_Type.__name__ = "Integer32"
_Co70_Object = MibScalar
co70 = _Co70_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 70, 5),
    _Co70_Type()
)
co70.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co70.setStatus("mandatory")


class _Motion70_Type(Integer32):
    """Custom type motion70 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion70_Type.__name__ = "Integer32"
_Motion70_Object = MibScalar
motion70 = _Motion70_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 70, 6),
    _Motion70_Type()
)
motion70.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion70.setStatus("mandatory")


class _Digitalin170_Type(Integer32):
    """Custom type digitalin170 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin170_Type.__name__ = "Integer32"
_Digitalin170_Object = MibScalar
digitalin170 = _Digitalin170_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 70, 7),
    _Digitalin170_Type()
)
digitalin170.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin170.setStatus("mandatory")


class _Digitalin270_Type(Integer32):
    """Custom type digitalin270 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin270_Type.__name__ = "Integer32"
_Digitalin270_Object = MibScalar
digitalin270 = _Digitalin270_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 70, 8),
    _Digitalin270_Type()
)
digitalin270.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin270.setStatus("mandatory")


class _Digitalout270_Type(Integer32):
    """Custom type digitalout270 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout270_Type.__name__ = "Integer32"
_Digitalout270_Object = MibScalar
digitalout270 = _Digitalout270_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 70, 9),
    _Digitalout270_Type()
)
digitalout270.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout270.setStatus("mandatory")


class _ComError70_Type(Integer32):
    """Custom type comError70 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError70_Type.__name__ = "Integer32"
_ComError70_Object = MibScalar
comError70 = _ComError70_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 70, 10),
    _ComError70_Type()
)
comError70.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError70.setStatus("mandatory")
_Multisensor71_ObjectIdentity = ObjectIdentity
multisensor71 = _Multisensor71_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 71)
)
_Sensorname71_Type = DisplayString
_Sensorname71_Object = MibScalar
sensorname71 = _Sensorname71_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 71, 1),
    _Sensorname71_Type()
)
sensorname71.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname71.setStatus("mandatory")


class _Temperature71_Type(Integer32):
    """Custom type temperature71 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature71_Type.__name__ = "Integer32"
_Temperature71_Object = MibScalar
temperature71 = _Temperature71_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 71, 2),
    _Temperature71_Type()
)
temperature71.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature71.setStatus("mandatory")


class _Humidity71_Type(Integer32):
    """Custom type humidity71 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity71_Type.__name__ = "Integer32"
_Humidity71_Object = MibScalar
humidity71 = _Humidity71_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 71, 3),
    _Humidity71_Type()
)
humidity71.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity71.setStatus("mandatory")


class _Dewpoint71_Type(Integer32):
    """Custom type dewpoint71 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint71_Type.__name__ = "Integer32"
_Dewpoint71_Object = MibScalar
dewpoint71 = _Dewpoint71_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 71, 4),
    _Dewpoint71_Type()
)
dewpoint71.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint71.setStatus("mandatory")


class _Co71_Type(Integer32):
    """Custom type co71 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co71_Type.__name__ = "Integer32"
_Co71_Object = MibScalar
co71 = _Co71_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 71, 5),
    _Co71_Type()
)
co71.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co71.setStatus("mandatory")


class _Motion71_Type(Integer32):
    """Custom type motion71 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion71_Type.__name__ = "Integer32"
_Motion71_Object = MibScalar
motion71 = _Motion71_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 71, 6),
    _Motion71_Type()
)
motion71.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion71.setStatus("mandatory")


class _Digitalin171_Type(Integer32):
    """Custom type digitalin171 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin171_Type.__name__ = "Integer32"
_Digitalin171_Object = MibScalar
digitalin171 = _Digitalin171_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 71, 7),
    _Digitalin171_Type()
)
digitalin171.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin171.setStatus("mandatory")


class _Digitalin271_Type(Integer32):
    """Custom type digitalin271 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin271_Type.__name__ = "Integer32"
_Digitalin271_Object = MibScalar
digitalin271 = _Digitalin271_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 71, 8),
    _Digitalin271_Type()
)
digitalin271.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin271.setStatus("mandatory")


class _Digitalout271_Type(Integer32):
    """Custom type digitalout271 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout271_Type.__name__ = "Integer32"
_Digitalout271_Object = MibScalar
digitalout271 = _Digitalout271_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 71, 9),
    _Digitalout271_Type()
)
digitalout271.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout271.setStatus("mandatory")


class _ComError71_Type(Integer32):
    """Custom type comError71 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError71_Type.__name__ = "Integer32"
_ComError71_Object = MibScalar
comError71 = _ComError71_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 71, 10),
    _ComError71_Type()
)
comError71.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError71.setStatus("mandatory")
_Multisensor72_ObjectIdentity = ObjectIdentity
multisensor72 = _Multisensor72_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 72)
)
_Sensorname72_Type = DisplayString
_Sensorname72_Object = MibScalar
sensorname72 = _Sensorname72_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 72, 1),
    _Sensorname72_Type()
)
sensorname72.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname72.setStatus("mandatory")


class _Temperature72_Type(Integer32):
    """Custom type temperature72 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature72_Type.__name__ = "Integer32"
_Temperature72_Object = MibScalar
temperature72 = _Temperature72_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 72, 2),
    _Temperature72_Type()
)
temperature72.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature72.setStatus("mandatory")


class _Humidity72_Type(Integer32):
    """Custom type humidity72 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity72_Type.__name__ = "Integer32"
_Humidity72_Object = MibScalar
humidity72 = _Humidity72_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 72, 3),
    _Humidity72_Type()
)
humidity72.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity72.setStatus("mandatory")


class _Dewpoint72_Type(Integer32):
    """Custom type dewpoint72 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint72_Type.__name__ = "Integer32"
_Dewpoint72_Object = MibScalar
dewpoint72 = _Dewpoint72_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 72, 4),
    _Dewpoint72_Type()
)
dewpoint72.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint72.setStatus("mandatory")


class _Co72_Type(Integer32):
    """Custom type co72 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co72_Type.__name__ = "Integer32"
_Co72_Object = MibScalar
co72 = _Co72_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 72, 5),
    _Co72_Type()
)
co72.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co72.setStatus("mandatory")


class _Motion72_Type(Integer32):
    """Custom type motion72 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion72_Type.__name__ = "Integer32"
_Motion72_Object = MibScalar
motion72 = _Motion72_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 72, 6),
    _Motion72_Type()
)
motion72.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion72.setStatus("mandatory")


class _Digitalin172_Type(Integer32):
    """Custom type digitalin172 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin172_Type.__name__ = "Integer32"
_Digitalin172_Object = MibScalar
digitalin172 = _Digitalin172_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 72, 7),
    _Digitalin172_Type()
)
digitalin172.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin172.setStatus("mandatory")


class _Digitalin272_Type(Integer32):
    """Custom type digitalin272 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin272_Type.__name__ = "Integer32"
_Digitalin272_Object = MibScalar
digitalin272 = _Digitalin272_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 72, 8),
    _Digitalin272_Type()
)
digitalin272.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin272.setStatus("mandatory")


class _Digitalout272_Type(Integer32):
    """Custom type digitalout272 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout272_Type.__name__ = "Integer32"
_Digitalout272_Object = MibScalar
digitalout272 = _Digitalout272_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 72, 9),
    _Digitalout272_Type()
)
digitalout272.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout272.setStatus("mandatory")


class _ComError72_Type(Integer32):
    """Custom type comError72 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError72_Type.__name__ = "Integer32"
_ComError72_Object = MibScalar
comError72 = _ComError72_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 72, 10),
    _ComError72_Type()
)
comError72.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError72.setStatus("mandatory")
_Multisensor73_ObjectIdentity = ObjectIdentity
multisensor73 = _Multisensor73_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 73)
)
_Sensorname73_Type = DisplayString
_Sensorname73_Object = MibScalar
sensorname73 = _Sensorname73_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 73, 1),
    _Sensorname73_Type()
)
sensorname73.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname73.setStatus("mandatory")


class _Temperature73_Type(Integer32):
    """Custom type temperature73 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature73_Type.__name__ = "Integer32"
_Temperature73_Object = MibScalar
temperature73 = _Temperature73_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 73, 2),
    _Temperature73_Type()
)
temperature73.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature73.setStatus("mandatory")


class _Humidity73_Type(Integer32):
    """Custom type humidity73 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity73_Type.__name__ = "Integer32"
_Humidity73_Object = MibScalar
humidity73 = _Humidity73_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 73, 3),
    _Humidity73_Type()
)
humidity73.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity73.setStatus("mandatory")


class _Dewpoint73_Type(Integer32):
    """Custom type dewpoint73 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint73_Type.__name__ = "Integer32"
_Dewpoint73_Object = MibScalar
dewpoint73 = _Dewpoint73_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 73, 4),
    _Dewpoint73_Type()
)
dewpoint73.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint73.setStatus("mandatory")


class _Co73_Type(Integer32):
    """Custom type co73 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co73_Type.__name__ = "Integer32"
_Co73_Object = MibScalar
co73 = _Co73_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 73, 5),
    _Co73_Type()
)
co73.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co73.setStatus("mandatory")


class _Motion73_Type(Integer32):
    """Custom type motion73 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion73_Type.__name__ = "Integer32"
_Motion73_Object = MibScalar
motion73 = _Motion73_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 73, 6),
    _Motion73_Type()
)
motion73.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion73.setStatus("mandatory")


class _Digitalin173_Type(Integer32):
    """Custom type digitalin173 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin173_Type.__name__ = "Integer32"
_Digitalin173_Object = MibScalar
digitalin173 = _Digitalin173_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 73, 7),
    _Digitalin173_Type()
)
digitalin173.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin173.setStatus("mandatory")


class _Digitalin273_Type(Integer32):
    """Custom type digitalin273 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin273_Type.__name__ = "Integer32"
_Digitalin273_Object = MibScalar
digitalin273 = _Digitalin273_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 73, 8),
    _Digitalin273_Type()
)
digitalin273.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin273.setStatus("mandatory")


class _Digitalout273_Type(Integer32):
    """Custom type digitalout273 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout273_Type.__name__ = "Integer32"
_Digitalout273_Object = MibScalar
digitalout273 = _Digitalout273_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 73, 9),
    _Digitalout273_Type()
)
digitalout273.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout273.setStatus("mandatory")


class _ComError73_Type(Integer32):
    """Custom type comError73 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError73_Type.__name__ = "Integer32"
_ComError73_Object = MibScalar
comError73 = _ComError73_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 73, 10),
    _ComError73_Type()
)
comError73.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError73.setStatus("mandatory")
_Multisensor74_ObjectIdentity = ObjectIdentity
multisensor74 = _Multisensor74_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 74)
)
_Sensorname74_Type = DisplayString
_Sensorname74_Object = MibScalar
sensorname74 = _Sensorname74_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 74, 1),
    _Sensorname74_Type()
)
sensorname74.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname74.setStatus("mandatory")


class _Temperature74_Type(Integer32):
    """Custom type temperature74 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature74_Type.__name__ = "Integer32"
_Temperature74_Object = MibScalar
temperature74 = _Temperature74_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 74, 2),
    _Temperature74_Type()
)
temperature74.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature74.setStatus("mandatory")


class _Humidity74_Type(Integer32):
    """Custom type humidity74 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity74_Type.__name__ = "Integer32"
_Humidity74_Object = MibScalar
humidity74 = _Humidity74_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 74, 3),
    _Humidity74_Type()
)
humidity74.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity74.setStatus("mandatory")


class _Dewpoint74_Type(Integer32):
    """Custom type dewpoint74 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint74_Type.__name__ = "Integer32"
_Dewpoint74_Object = MibScalar
dewpoint74 = _Dewpoint74_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 74, 4),
    _Dewpoint74_Type()
)
dewpoint74.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint74.setStatus("mandatory")


class _Co74_Type(Integer32):
    """Custom type co74 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co74_Type.__name__ = "Integer32"
_Co74_Object = MibScalar
co74 = _Co74_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 74, 5),
    _Co74_Type()
)
co74.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co74.setStatus("mandatory")


class _Motion74_Type(Integer32):
    """Custom type motion74 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion74_Type.__name__ = "Integer32"
_Motion74_Object = MibScalar
motion74 = _Motion74_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 74, 6),
    _Motion74_Type()
)
motion74.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion74.setStatus("mandatory")


class _Digitalin174_Type(Integer32):
    """Custom type digitalin174 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin174_Type.__name__ = "Integer32"
_Digitalin174_Object = MibScalar
digitalin174 = _Digitalin174_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 74, 7),
    _Digitalin174_Type()
)
digitalin174.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin174.setStatus("mandatory")


class _Digitalin274_Type(Integer32):
    """Custom type digitalin274 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin274_Type.__name__ = "Integer32"
_Digitalin274_Object = MibScalar
digitalin274 = _Digitalin274_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 74, 8),
    _Digitalin274_Type()
)
digitalin274.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin274.setStatus("mandatory")


class _Digitalout274_Type(Integer32):
    """Custom type digitalout274 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout274_Type.__name__ = "Integer32"
_Digitalout274_Object = MibScalar
digitalout274 = _Digitalout274_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 74, 9),
    _Digitalout274_Type()
)
digitalout274.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout274.setStatus("mandatory")


class _ComError74_Type(Integer32):
    """Custom type comError74 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError74_Type.__name__ = "Integer32"
_ComError74_Object = MibScalar
comError74 = _ComError74_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 74, 10),
    _ComError74_Type()
)
comError74.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError74.setStatus("mandatory")
_Multisensor75_ObjectIdentity = ObjectIdentity
multisensor75 = _Multisensor75_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 75)
)
_Sensorname75_Type = DisplayString
_Sensorname75_Object = MibScalar
sensorname75 = _Sensorname75_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 75, 1),
    _Sensorname75_Type()
)
sensorname75.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname75.setStatus("mandatory")


class _Temperature75_Type(Integer32):
    """Custom type temperature75 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature75_Type.__name__ = "Integer32"
_Temperature75_Object = MibScalar
temperature75 = _Temperature75_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 75, 2),
    _Temperature75_Type()
)
temperature75.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature75.setStatus("mandatory")


class _Humidity75_Type(Integer32):
    """Custom type humidity75 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity75_Type.__name__ = "Integer32"
_Humidity75_Object = MibScalar
humidity75 = _Humidity75_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 75, 3),
    _Humidity75_Type()
)
humidity75.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity75.setStatus("mandatory")


class _Dewpoint75_Type(Integer32):
    """Custom type dewpoint75 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint75_Type.__name__ = "Integer32"
_Dewpoint75_Object = MibScalar
dewpoint75 = _Dewpoint75_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 75, 4),
    _Dewpoint75_Type()
)
dewpoint75.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint75.setStatus("mandatory")


class _Co75_Type(Integer32):
    """Custom type co75 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co75_Type.__name__ = "Integer32"
_Co75_Object = MibScalar
co75 = _Co75_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 75, 5),
    _Co75_Type()
)
co75.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co75.setStatus("mandatory")


class _Motion75_Type(Integer32):
    """Custom type motion75 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion75_Type.__name__ = "Integer32"
_Motion75_Object = MibScalar
motion75 = _Motion75_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 75, 6),
    _Motion75_Type()
)
motion75.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion75.setStatus("mandatory")


class _Digitalin175_Type(Integer32):
    """Custom type digitalin175 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin175_Type.__name__ = "Integer32"
_Digitalin175_Object = MibScalar
digitalin175 = _Digitalin175_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 75, 7),
    _Digitalin175_Type()
)
digitalin175.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin175.setStatus("mandatory")


class _Digitalin275_Type(Integer32):
    """Custom type digitalin275 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin275_Type.__name__ = "Integer32"
_Digitalin275_Object = MibScalar
digitalin275 = _Digitalin275_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 75, 8),
    _Digitalin275_Type()
)
digitalin275.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin275.setStatus("mandatory")


class _Digitalout275_Type(Integer32):
    """Custom type digitalout275 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout275_Type.__name__ = "Integer32"
_Digitalout275_Object = MibScalar
digitalout275 = _Digitalout275_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 75, 9),
    _Digitalout275_Type()
)
digitalout275.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout275.setStatus("mandatory")


class _ComError75_Type(Integer32):
    """Custom type comError75 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError75_Type.__name__ = "Integer32"
_ComError75_Object = MibScalar
comError75 = _ComError75_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 75, 10),
    _ComError75_Type()
)
comError75.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError75.setStatus("mandatory")
_Multisensor76_ObjectIdentity = ObjectIdentity
multisensor76 = _Multisensor76_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 76)
)
_Sensorname76_Type = DisplayString
_Sensorname76_Object = MibScalar
sensorname76 = _Sensorname76_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 76, 1),
    _Sensorname76_Type()
)
sensorname76.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname76.setStatus("mandatory")


class _Temperature76_Type(Integer32):
    """Custom type temperature76 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature76_Type.__name__ = "Integer32"
_Temperature76_Object = MibScalar
temperature76 = _Temperature76_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 76, 2),
    _Temperature76_Type()
)
temperature76.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature76.setStatus("mandatory")


class _Humidity76_Type(Integer32):
    """Custom type humidity76 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity76_Type.__name__ = "Integer32"
_Humidity76_Object = MibScalar
humidity76 = _Humidity76_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 76, 3),
    _Humidity76_Type()
)
humidity76.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity76.setStatus("mandatory")


class _Dewpoint76_Type(Integer32):
    """Custom type dewpoint76 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint76_Type.__name__ = "Integer32"
_Dewpoint76_Object = MibScalar
dewpoint76 = _Dewpoint76_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 76, 4),
    _Dewpoint76_Type()
)
dewpoint76.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint76.setStatus("mandatory")


class _Co76_Type(Integer32):
    """Custom type co76 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co76_Type.__name__ = "Integer32"
_Co76_Object = MibScalar
co76 = _Co76_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 76, 5),
    _Co76_Type()
)
co76.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co76.setStatus("mandatory")


class _Motion76_Type(Integer32):
    """Custom type motion76 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion76_Type.__name__ = "Integer32"
_Motion76_Object = MibScalar
motion76 = _Motion76_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 76, 6),
    _Motion76_Type()
)
motion76.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion76.setStatus("mandatory")


class _Digitalin176_Type(Integer32):
    """Custom type digitalin176 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin176_Type.__name__ = "Integer32"
_Digitalin176_Object = MibScalar
digitalin176 = _Digitalin176_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 76, 7),
    _Digitalin176_Type()
)
digitalin176.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin176.setStatus("mandatory")


class _Digitalin276_Type(Integer32):
    """Custom type digitalin276 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin276_Type.__name__ = "Integer32"
_Digitalin276_Object = MibScalar
digitalin276 = _Digitalin276_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 76, 8),
    _Digitalin276_Type()
)
digitalin276.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin276.setStatus("mandatory")


class _Digitalout276_Type(Integer32):
    """Custom type digitalout276 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout276_Type.__name__ = "Integer32"
_Digitalout276_Object = MibScalar
digitalout276 = _Digitalout276_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 76, 9),
    _Digitalout276_Type()
)
digitalout276.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout276.setStatus("mandatory")


class _ComError76_Type(Integer32):
    """Custom type comError76 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError76_Type.__name__ = "Integer32"
_ComError76_Object = MibScalar
comError76 = _ComError76_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 76, 10),
    _ComError76_Type()
)
comError76.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError76.setStatus("mandatory")
_Multisensor77_ObjectIdentity = ObjectIdentity
multisensor77 = _Multisensor77_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 77)
)
_Sensorname77_Type = DisplayString
_Sensorname77_Object = MibScalar
sensorname77 = _Sensorname77_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 77, 1),
    _Sensorname77_Type()
)
sensorname77.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname77.setStatus("mandatory")


class _Temperature77_Type(Integer32):
    """Custom type temperature77 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature77_Type.__name__ = "Integer32"
_Temperature77_Object = MibScalar
temperature77 = _Temperature77_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 77, 2),
    _Temperature77_Type()
)
temperature77.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature77.setStatus("mandatory")


class _Humidity77_Type(Integer32):
    """Custom type humidity77 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity77_Type.__name__ = "Integer32"
_Humidity77_Object = MibScalar
humidity77 = _Humidity77_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 77, 3),
    _Humidity77_Type()
)
humidity77.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity77.setStatus("mandatory")


class _Dewpoint77_Type(Integer32):
    """Custom type dewpoint77 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint77_Type.__name__ = "Integer32"
_Dewpoint77_Object = MibScalar
dewpoint77 = _Dewpoint77_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 77, 4),
    _Dewpoint77_Type()
)
dewpoint77.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint77.setStatus("mandatory")


class _Co77_Type(Integer32):
    """Custom type co77 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co77_Type.__name__ = "Integer32"
_Co77_Object = MibScalar
co77 = _Co77_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 77, 5),
    _Co77_Type()
)
co77.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co77.setStatus("mandatory")


class _Motion77_Type(Integer32):
    """Custom type motion77 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion77_Type.__name__ = "Integer32"
_Motion77_Object = MibScalar
motion77 = _Motion77_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 77, 6),
    _Motion77_Type()
)
motion77.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion77.setStatus("mandatory")


class _Digitalin177_Type(Integer32):
    """Custom type digitalin177 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin177_Type.__name__ = "Integer32"
_Digitalin177_Object = MibScalar
digitalin177 = _Digitalin177_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 77, 7),
    _Digitalin177_Type()
)
digitalin177.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin177.setStatus("mandatory")


class _Digitalin277_Type(Integer32):
    """Custom type digitalin277 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin277_Type.__name__ = "Integer32"
_Digitalin277_Object = MibScalar
digitalin277 = _Digitalin277_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 77, 8),
    _Digitalin277_Type()
)
digitalin277.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin277.setStatus("mandatory")


class _Digitalout277_Type(Integer32):
    """Custom type digitalout277 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout277_Type.__name__ = "Integer32"
_Digitalout277_Object = MibScalar
digitalout277 = _Digitalout277_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 77, 9),
    _Digitalout277_Type()
)
digitalout277.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout277.setStatus("mandatory")


class _ComError77_Type(Integer32):
    """Custom type comError77 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError77_Type.__name__ = "Integer32"
_ComError77_Object = MibScalar
comError77 = _ComError77_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 77, 10),
    _ComError77_Type()
)
comError77.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError77.setStatus("mandatory")
_Multisensor78_ObjectIdentity = ObjectIdentity
multisensor78 = _Multisensor78_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 78)
)
_Sensorname78_Type = DisplayString
_Sensorname78_Object = MibScalar
sensorname78 = _Sensorname78_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 78, 1),
    _Sensorname78_Type()
)
sensorname78.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname78.setStatus("mandatory")


class _Temperature78_Type(Integer32):
    """Custom type temperature78 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature78_Type.__name__ = "Integer32"
_Temperature78_Object = MibScalar
temperature78 = _Temperature78_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 78, 2),
    _Temperature78_Type()
)
temperature78.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature78.setStatus("mandatory")


class _Humidity78_Type(Integer32):
    """Custom type humidity78 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity78_Type.__name__ = "Integer32"
_Humidity78_Object = MibScalar
humidity78 = _Humidity78_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 78, 3),
    _Humidity78_Type()
)
humidity78.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity78.setStatus("mandatory")


class _Dewpoint78_Type(Integer32):
    """Custom type dewpoint78 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint78_Type.__name__ = "Integer32"
_Dewpoint78_Object = MibScalar
dewpoint78 = _Dewpoint78_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 78, 4),
    _Dewpoint78_Type()
)
dewpoint78.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint78.setStatus("mandatory")


class _Co78_Type(Integer32):
    """Custom type co78 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co78_Type.__name__ = "Integer32"
_Co78_Object = MibScalar
co78 = _Co78_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 78, 5),
    _Co78_Type()
)
co78.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co78.setStatus("mandatory")


class _Motion78_Type(Integer32):
    """Custom type motion78 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion78_Type.__name__ = "Integer32"
_Motion78_Object = MibScalar
motion78 = _Motion78_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 78, 6),
    _Motion78_Type()
)
motion78.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion78.setStatus("mandatory")


class _Digitalin178_Type(Integer32):
    """Custom type digitalin178 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin178_Type.__name__ = "Integer32"
_Digitalin178_Object = MibScalar
digitalin178 = _Digitalin178_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 78, 7),
    _Digitalin178_Type()
)
digitalin178.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin178.setStatus("mandatory")


class _Digitalin278_Type(Integer32):
    """Custom type digitalin278 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin278_Type.__name__ = "Integer32"
_Digitalin278_Object = MibScalar
digitalin278 = _Digitalin278_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 78, 8),
    _Digitalin278_Type()
)
digitalin278.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin278.setStatus("mandatory")


class _Digitalout278_Type(Integer32):
    """Custom type digitalout278 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout278_Type.__name__ = "Integer32"
_Digitalout278_Object = MibScalar
digitalout278 = _Digitalout278_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 78, 9),
    _Digitalout278_Type()
)
digitalout278.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout278.setStatus("mandatory")


class _ComError78_Type(Integer32):
    """Custom type comError78 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError78_Type.__name__ = "Integer32"
_ComError78_Object = MibScalar
comError78 = _ComError78_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 78, 10),
    _ComError78_Type()
)
comError78.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError78.setStatus("mandatory")
_Multisensor79_ObjectIdentity = ObjectIdentity
multisensor79 = _Multisensor79_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 79)
)
_Sensorname79_Type = DisplayString
_Sensorname79_Object = MibScalar
sensorname79 = _Sensorname79_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 79, 1),
    _Sensorname79_Type()
)
sensorname79.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname79.setStatus("mandatory")


class _Temperature79_Type(Integer32):
    """Custom type temperature79 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature79_Type.__name__ = "Integer32"
_Temperature79_Object = MibScalar
temperature79 = _Temperature79_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 79, 2),
    _Temperature79_Type()
)
temperature79.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature79.setStatus("mandatory")


class _Humidity79_Type(Integer32):
    """Custom type humidity79 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity79_Type.__name__ = "Integer32"
_Humidity79_Object = MibScalar
humidity79 = _Humidity79_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 79, 3),
    _Humidity79_Type()
)
humidity79.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity79.setStatus("mandatory")


class _Dewpoint79_Type(Integer32):
    """Custom type dewpoint79 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint79_Type.__name__ = "Integer32"
_Dewpoint79_Object = MibScalar
dewpoint79 = _Dewpoint79_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 79, 4),
    _Dewpoint79_Type()
)
dewpoint79.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint79.setStatus("mandatory")


class _Co79_Type(Integer32):
    """Custom type co79 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co79_Type.__name__ = "Integer32"
_Co79_Object = MibScalar
co79 = _Co79_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 79, 5),
    _Co79_Type()
)
co79.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co79.setStatus("mandatory")


class _Motion79_Type(Integer32):
    """Custom type motion79 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion79_Type.__name__ = "Integer32"
_Motion79_Object = MibScalar
motion79 = _Motion79_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 79, 6),
    _Motion79_Type()
)
motion79.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion79.setStatus("mandatory")


class _Digitalin179_Type(Integer32):
    """Custom type digitalin179 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin179_Type.__name__ = "Integer32"
_Digitalin179_Object = MibScalar
digitalin179 = _Digitalin179_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 79, 7),
    _Digitalin179_Type()
)
digitalin179.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin179.setStatus("mandatory")


class _Digitalin279_Type(Integer32):
    """Custom type digitalin279 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin279_Type.__name__ = "Integer32"
_Digitalin279_Object = MibScalar
digitalin279 = _Digitalin279_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 79, 8),
    _Digitalin279_Type()
)
digitalin279.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin279.setStatus("mandatory")


class _Digitalout279_Type(Integer32):
    """Custom type digitalout279 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout279_Type.__name__ = "Integer32"
_Digitalout279_Object = MibScalar
digitalout279 = _Digitalout279_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 79, 9),
    _Digitalout279_Type()
)
digitalout279.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout279.setStatus("mandatory")


class _ComError79_Type(Integer32):
    """Custom type comError79 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError79_Type.__name__ = "Integer32"
_ComError79_Object = MibScalar
comError79 = _ComError79_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 79, 10),
    _ComError79_Type()
)
comError79.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError79.setStatus("mandatory")
_Multisensor80_ObjectIdentity = ObjectIdentity
multisensor80 = _Multisensor80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 80)
)
_Sensorname80_Type = DisplayString
_Sensorname80_Object = MibScalar
sensorname80 = _Sensorname80_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 80, 1),
    _Sensorname80_Type()
)
sensorname80.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname80.setStatus("mandatory")


class _Temperature80_Type(Integer32):
    """Custom type temperature80 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature80_Type.__name__ = "Integer32"
_Temperature80_Object = MibScalar
temperature80 = _Temperature80_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 80, 2),
    _Temperature80_Type()
)
temperature80.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature80.setStatus("mandatory")


class _Humidity80_Type(Integer32):
    """Custom type humidity80 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity80_Type.__name__ = "Integer32"
_Humidity80_Object = MibScalar
humidity80 = _Humidity80_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 80, 3),
    _Humidity80_Type()
)
humidity80.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity80.setStatus("mandatory")


class _Dewpoint80_Type(Integer32):
    """Custom type dewpoint80 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint80_Type.__name__ = "Integer32"
_Dewpoint80_Object = MibScalar
dewpoint80 = _Dewpoint80_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 80, 4),
    _Dewpoint80_Type()
)
dewpoint80.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint80.setStatus("mandatory")


class _Co80_Type(Integer32):
    """Custom type co80 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co80_Type.__name__ = "Integer32"
_Co80_Object = MibScalar
co80 = _Co80_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 80, 5),
    _Co80_Type()
)
co80.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co80.setStatus("mandatory")


class _Motion80_Type(Integer32):
    """Custom type motion80 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion80_Type.__name__ = "Integer32"
_Motion80_Object = MibScalar
motion80 = _Motion80_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 80, 6),
    _Motion80_Type()
)
motion80.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion80.setStatus("mandatory")


class _Digitalin180_Type(Integer32):
    """Custom type digitalin180 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin180_Type.__name__ = "Integer32"
_Digitalin180_Object = MibScalar
digitalin180 = _Digitalin180_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 80, 7),
    _Digitalin180_Type()
)
digitalin180.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin180.setStatus("mandatory")


class _Digitalin280_Type(Integer32):
    """Custom type digitalin280 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin280_Type.__name__ = "Integer32"
_Digitalin280_Object = MibScalar
digitalin280 = _Digitalin280_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 80, 8),
    _Digitalin280_Type()
)
digitalin280.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin280.setStatus("mandatory")


class _Digitalout280_Type(Integer32):
    """Custom type digitalout280 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout280_Type.__name__ = "Integer32"
_Digitalout280_Object = MibScalar
digitalout280 = _Digitalout280_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 80, 9),
    _Digitalout280_Type()
)
digitalout280.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout280.setStatus("mandatory")


class _ComError80_Type(Integer32):
    """Custom type comError80 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError80_Type.__name__ = "Integer32"
_ComError80_Object = MibScalar
comError80 = _ComError80_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 80, 10),
    _ComError80_Type()
)
comError80.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError80.setStatus("mandatory")
_Multisensor81_ObjectIdentity = ObjectIdentity
multisensor81 = _Multisensor81_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 81)
)
_Sensorname81_Type = DisplayString
_Sensorname81_Object = MibScalar
sensorname81 = _Sensorname81_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 81, 1),
    _Sensorname81_Type()
)
sensorname81.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname81.setStatus("mandatory")


class _Temperature81_Type(Integer32):
    """Custom type temperature81 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature81_Type.__name__ = "Integer32"
_Temperature81_Object = MibScalar
temperature81 = _Temperature81_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 81, 2),
    _Temperature81_Type()
)
temperature81.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature81.setStatus("mandatory")


class _Humidity81_Type(Integer32):
    """Custom type humidity81 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity81_Type.__name__ = "Integer32"
_Humidity81_Object = MibScalar
humidity81 = _Humidity81_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 81, 3),
    _Humidity81_Type()
)
humidity81.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity81.setStatus("mandatory")


class _Dewpoint81_Type(Integer32):
    """Custom type dewpoint81 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint81_Type.__name__ = "Integer32"
_Dewpoint81_Object = MibScalar
dewpoint81 = _Dewpoint81_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 81, 4),
    _Dewpoint81_Type()
)
dewpoint81.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint81.setStatus("mandatory")


class _Co81_Type(Integer32):
    """Custom type co81 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co81_Type.__name__ = "Integer32"
_Co81_Object = MibScalar
co81 = _Co81_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 81, 5),
    _Co81_Type()
)
co81.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co81.setStatus("mandatory")


class _Motion81_Type(Integer32):
    """Custom type motion81 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion81_Type.__name__ = "Integer32"
_Motion81_Object = MibScalar
motion81 = _Motion81_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 81, 6),
    _Motion81_Type()
)
motion81.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion81.setStatus("mandatory")


class _Digitalin181_Type(Integer32):
    """Custom type digitalin181 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin181_Type.__name__ = "Integer32"
_Digitalin181_Object = MibScalar
digitalin181 = _Digitalin181_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 81, 7),
    _Digitalin181_Type()
)
digitalin181.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin181.setStatus("mandatory")


class _Digitalin281_Type(Integer32):
    """Custom type digitalin281 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin281_Type.__name__ = "Integer32"
_Digitalin281_Object = MibScalar
digitalin281 = _Digitalin281_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 81, 8),
    _Digitalin281_Type()
)
digitalin281.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin281.setStatus("mandatory")


class _Digitalout281_Type(Integer32):
    """Custom type digitalout281 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout281_Type.__name__ = "Integer32"
_Digitalout281_Object = MibScalar
digitalout281 = _Digitalout281_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 81, 9),
    _Digitalout281_Type()
)
digitalout281.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout281.setStatus("mandatory")


class _ComError81_Type(Integer32):
    """Custom type comError81 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError81_Type.__name__ = "Integer32"
_ComError81_Object = MibScalar
comError81 = _ComError81_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 81, 10),
    _ComError81_Type()
)
comError81.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError81.setStatus("mandatory")
_Multisensor82_ObjectIdentity = ObjectIdentity
multisensor82 = _Multisensor82_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 82)
)
_Sensorname82_Type = DisplayString
_Sensorname82_Object = MibScalar
sensorname82 = _Sensorname82_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 82, 1),
    _Sensorname82_Type()
)
sensorname82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname82.setStatus("mandatory")


class _Temperature82_Type(Integer32):
    """Custom type temperature82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature82_Type.__name__ = "Integer32"
_Temperature82_Object = MibScalar
temperature82 = _Temperature82_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 82, 2),
    _Temperature82_Type()
)
temperature82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature82.setStatus("mandatory")


class _Humidity82_Type(Integer32):
    """Custom type humidity82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity82_Type.__name__ = "Integer32"
_Humidity82_Object = MibScalar
humidity82 = _Humidity82_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 82, 3),
    _Humidity82_Type()
)
humidity82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity82.setStatus("mandatory")


class _Dewpoint82_Type(Integer32):
    """Custom type dewpoint82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint82_Type.__name__ = "Integer32"
_Dewpoint82_Object = MibScalar
dewpoint82 = _Dewpoint82_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 82, 4),
    _Dewpoint82_Type()
)
dewpoint82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint82.setStatus("mandatory")


class _Co82_Type(Integer32):
    """Custom type co82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co82_Type.__name__ = "Integer32"
_Co82_Object = MibScalar
co82 = _Co82_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 82, 5),
    _Co82_Type()
)
co82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co82.setStatus("mandatory")


class _Motion82_Type(Integer32):
    """Custom type motion82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion82_Type.__name__ = "Integer32"
_Motion82_Object = MibScalar
motion82 = _Motion82_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 82, 6),
    _Motion82_Type()
)
motion82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion82.setStatus("mandatory")


class _Digitalin182_Type(Integer32):
    """Custom type digitalin182 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin182_Type.__name__ = "Integer32"
_Digitalin182_Object = MibScalar
digitalin182 = _Digitalin182_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 82, 7),
    _Digitalin182_Type()
)
digitalin182.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin182.setStatus("mandatory")


class _Digitalin282_Type(Integer32):
    """Custom type digitalin282 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin282_Type.__name__ = "Integer32"
_Digitalin282_Object = MibScalar
digitalin282 = _Digitalin282_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 82, 8),
    _Digitalin282_Type()
)
digitalin282.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin282.setStatus("mandatory")


class _Digitalout282_Type(Integer32):
    """Custom type digitalout282 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout282_Type.__name__ = "Integer32"
_Digitalout282_Object = MibScalar
digitalout282 = _Digitalout282_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 82, 9),
    _Digitalout282_Type()
)
digitalout282.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout282.setStatus("mandatory")


class _ComError82_Type(Integer32):
    """Custom type comError82 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError82_Type.__name__ = "Integer32"
_ComError82_Object = MibScalar
comError82 = _ComError82_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 82, 10),
    _ComError82_Type()
)
comError82.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError82.setStatus("mandatory")
_Multisensor83_ObjectIdentity = ObjectIdentity
multisensor83 = _Multisensor83_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 83)
)
_Sensorname83_Type = DisplayString
_Sensorname83_Object = MibScalar
sensorname83 = _Sensorname83_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 83, 1),
    _Sensorname83_Type()
)
sensorname83.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname83.setStatus("mandatory")


class _Temperature83_Type(Integer32):
    """Custom type temperature83 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature83_Type.__name__ = "Integer32"
_Temperature83_Object = MibScalar
temperature83 = _Temperature83_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 83, 2),
    _Temperature83_Type()
)
temperature83.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature83.setStatus("mandatory")


class _Humidity83_Type(Integer32):
    """Custom type humidity83 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity83_Type.__name__ = "Integer32"
_Humidity83_Object = MibScalar
humidity83 = _Humidity83_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 83, 3),
    _Humidity83_Type()
)
humidity83.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity83.setStatus("mandatory")


class _Dewpoint83_Type(Integer32):
    """Custom type dewpoint83 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint83_Type.__name__ = "Integer32"
_Dewpoint83_Object = MibScalar
dewpoint83 = _Dewpoint83_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 83, 4),
    _Dewpoint83_Type()
)
dewpoint83.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint83.setStatus("mandatory")


class _Co83_Type(Integer32):
    """Custom type co83 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co83_Type.__name__ = "Integer32"
_Co83_Object = MibScalar
co83 = _Co83_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 83, 5),
    _Co83_Type()
)
co83.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co83.setStatus("mandatory")


class _Motion83_Type(Integer32):
    """Custom type motion83 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion83_Type.__name__ = "Integer32"
_Motion83_Object = MibScalar
motion83 = _Motion83_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 83, 6),
    _Motion83_Type()
)
motion83.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion83.setStatus("mandatory")


class _Digitalin183_Type(Integer32):
    """Custom type digitalin183 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin183_Type.__name__ = "Integer32"
_Digitalin183_Object = MibScalar
digitalin183 = _Digitalin183_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 83, 7),
    _Digitalin183_Type()
)
digitalin183.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin183.setStatus("mandatory")


class _Digitalin283_Type(Integer32):
    """Custom type digitalin283 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin283_Type.__name__ = "Integer32"
_Digitalin283_Object = MibScalar
digitalin283 = _Digitalin283_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 83, 8),
    _Digitalin283_Type()
)
digitalin283.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin283.setStatus("mandatory")


class _Digitalout283_Type(Integer32):
    """Custom type digitalout283 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout283_Type.__name__ = "Integer32"
_Digitalout283_Object = MibScalar
digitalout283 = _Digitalout283_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 83, 9),
    _Digitalout283_Type()
)
digitalout283.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout283.setStatus("mandatory")


class _ComError83_Type(Integer32):
    """Custom type comError83 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError83_Type.__name__ = "Integer32"
_ComError83_Object = MibScalar
comError83 = _ComError83_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 83, 10),
    _ComError83_Type()
)
comError83.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError83.setStatus("mandatory")
_Multisensor84_ObjectIdentity = ObjectIdentity
multisensor84 = _Multisensor84_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 84)
)
_Sensorname84_Type = DisplayString
_Sensorname84_Object = MibScalar
sensorname84 = _Sensorname84_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 84, 1),
    _Sensorname84_Type()
)
sensorname84.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname84.setStatus("mandatory")


class _Temperature84_Type(Integer32):
    """Custom type temperature84 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature84_Type.__name__ = "Integer32"
_Temperature84_Object = MibScalar
temperature84 = _Temperature84_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 84, 2),
    _Temperature84_Type()
)
temperature84.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature84.setStatus("mandatory")


class _Humidity84_Type(Integer32):
    """Custom type humidity84 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity84_Type.__name__ = "Integer32"
_Humidity84_Object = MibScalar
humidity84 = _Humidity84_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 84, 3),
    _Humidity84_Type()
)
humidity84.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity84.setStatus("mandatory")


class _Dewpoint84_Type(Integer32):
    """Custom type dewpoint84 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint84_Type.__name__ = "Integer32"
_Dewpoint84_Object = MibScalar
dewpoint84 = _Dewpoint84_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 84, 4),
    _Dewpoint84_Type()
)
dewpoint84.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint84.setStatus("mandatory")


class _Co84_Type(Integer32):
    """Custom type co84 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co84_Type.__name__ = "Integer32"
_Co84_Object = MibScalar
co84 = _Co84_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 84, 5),
    _Co84_Type()
)
co84.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co84.setStatus("mandatory")


class _Motion84_Type(Integer32):
    """Custom type motion84 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion84_Type.__name__ = "Integer32"
_Motion84_Object = MibScalar
motion84 = _Motion84_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 84, 6),
    _Motion84_Type()
)
motion84.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion84.setStatus("mandatory")


class _Digitalin184_Type(Integer32):
    """Custom type digitalin184 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin184_Type.__name__ = "Integer32"
_Digitalin184_Object = MibScalar
digitalin184 = _Digitalin184_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 84, 7),
    _Digitalin184_Type()
)
digitalin184.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin184.setStatus("mandatory")


class _Digitalin284_Type(Integer32):
    """Custom type digitalin284 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin284_Type.__name__ = "Integer32"
_Digitalin284_Object = MibScalar
digitalin284 = _Digitalin284_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 84, 8),
    _Digitalin284_Type()
)
digitalin284.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin284.setStatus("mandatory")


class _Digitalout284_Type(Integer32):
    """Custom type digitalout284 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout284_Type.__name__ = "Integer32"
_Digitalout284_Object = MibScalar
digitalout284 = _Digitalout284_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 84, 9),
    _Digitalout284_Type()
)
digitalout284.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout284.setStatus("mandatory")


class _ComError84_Type(Integer32):
    """Custom type comError84 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError84_Type.__name__ = "Integer32"
_ComError84_Object = MibScalar
comError84 = _ComError84_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 84, 10),
    _ComError84_Type()
)
comError84.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError84.setStatus("mandatory")
_Multisensor85_ObjectIdentity = ObjectIdentity
multisensor85 = _Multisensor85_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 85)
)
_Sensorname85_Type = DisplayString
_Sensorname85_Object = MibScalar
sensorname85 = _Sensorname85_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 85, 1),
    _Sensorname85_Type()
)
sensorname85.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname85.setStatus("mandatory")


class _Temperature85_Type(Integer32):
    """Custom type temperature85 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature85_Type.__name__ = "Integer32"
_Temperature85_Object = MibScalar
temperature85 = _Temperature85_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 85, 2),
    _Temperature85_Type()
)
temperature85.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature85.setStatus("mandatory")


class _Humidity85_Type(Integer32):
    """Custom type humidity85 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity85_Type.__name__ = "Integer32"
_Humidity85_Object = MibScalar
humidity85 = _Humidity85_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 85, 3),
    _Humidity85_Type()
)
humidity85.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity85.setStatus("mandatory")


class _Dewpoint85_Type(Integer32):
    """Custom type dewpoint85 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint85_Type.__name__ = "Integer32"
_Dewpoint85_Object = MibScalar
dewpoint85 = _Dewpoint85_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 85, 4),
    _Dewpoint85_Type()
)
dewpoint85.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint85.setStatus("mandatory")


class _Co85_Type(Integer32):
    """Custom type co85 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co85_Type.__name__ = "Integer32"
_Co85_Object = MibScalar
co85 = _Co85_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 85, 5),
    _Co85_Type()
)
co85.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co85.setStatus("mandatory")


class _Motion85_Type(Integer32):
    """Custom type motion85 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion85_Type.__name__ = "Integer32"
_Motion85_Object = MibScalar
motion85 = _Motion85_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 85, 6),
    _Motion85_Type()
)
motion85.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion85.setStatus("mandatory")


class _Digitalin185_Type(Integer32):
    """Custom type digitalin185 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin185_Type.__name__ = "Integer32"
_Digitalin185_Object = MibScalar
digitalin185 = _Digitalin185_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 85, 7),
    _Digitalin185_Type()
)
digitalin185.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin185.setStatus("mandatory")


class _Digitalin285_Type(Integer32):
    """Custom type digitalin285 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin285_Type.__name__ = "Integer32"
_Digitalin285_Object = MibScalar
digitalin285 = _Digitalin285_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 85, 8),
    _Digitalin285_Type()
)
digitalin285.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin285.setStatus("mandatory")


class _Digitalout285_Type(Integer32):
    """Custom type digitalout285 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout285_Type.__name__ = "Integer32"
_Digitalout285_Object = MibScalar
digitalout285 = _Digitalout285_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 85, 9),
    _Digitalout285_Type()
)
digitalout285.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout285.setStatus("mandatory")


class _ComError85_Type(Integer32):
    """Custom type comError85 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError85_Type.__name__ = "Integer32"
_ComError85_Object = MibScalar
comError85 = _ComError85_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 85, 10),
    _ComError85_Type()
)
comError85.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError85.setStatus("mandatory")
_Multisensor86_ObjectIdentity = ObjectIdentity
multisensor86 = _Multisensor86_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 86)
)
_Sensorname86_Type = DisplayString
_Sensorname86_Object = MibScalar
sensorname86 = _Sensorname86_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 86, 1),
    _Sensorname86_Type()
)
sensorname86.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname86.setStatus("mandatory")


class _Temperature86_Type(Integer32):
    """Custom type temperature86 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature86_Type.__name__ = "Integer32"
_Temperature86_Object = MibScalar
temperature86 = _Temperature86_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 86, 2),
    _Temperature86_Type()
)
temperature86.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature86.setStatus("mandatory")


class _Humidity86_Type(Integer32):
    """Custom type humidity86 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity86_Type.__name__ = "Integer32"
_Humidity86_Object = MibScalar
humidity86 = _Humidity86_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 86, 3),
    _Humidity86_Type()
)
humidity86.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity86.setStatus("mandatory")


class _Dewpoint86_Type(Integer32):
    """Custom type dewpoint86 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint86_Type.__name__ = "Integer32"
_Dewpoint86_Object = MibScalar
dewpoint86 = _Dewpoint86_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 86, 4),
    _Dewpoint86_Type()
)
dewpoint86.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint86.setStatus("mandatory")


class _Co86_Type(Integer32):
    """Custom type co86 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co86_Type.__name__ = "Integer32"
_Co86_Object = MibScalar
co86 = _Co86_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 86, 5),
    _Co86_Type()
)
co86.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co86.setStatus("mandatory")


class _Motion86_Type(Integer32):
    """Custom type motion86 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion86_Type.__name__ = "Integer32"
_Motion86_Object = MibScalar
motion86 = _Motion86_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 86, 6),
    _Motion86_Type()
)
motion86.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion86.setStatus("mandatory")


class _Digitalin186_Type(Integer32):
    """Custom type digitalin186 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin186_Type.__name__ = "Integer32"
_Digitalin186_Object = MibScalar
digitalin186 = _Digitalin186_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 86, 7),
    _Digitalin186_Type()
)
digitalin186.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin186.setStatus("mandatory")


class _Digitalin286_Type(Integer32):
    """Custom type digitalin286 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin286_Type.__name__ = "Integer32"
_Digitalin286_Object = MibScalar
digitalin286 = _Digitalin286_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 86, 8),
    _Digitalin286_Type()
)
digitalin286.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin286.setStatus("mandatory")


class _Digitalout286_Type(Integer32):
    """Custom type digitalout286 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout286_Type.__name__ = "Integer32"
_Digitalout286_Object = MibScalar
digitalout286 = _Digitalout286_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 86, 9),
    _Digitalout286_Type()
)
digitalout286.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout286.setStatus("mandatory")


class _ComError86_Type(Integer32):
    """Custom type comError86 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError86_Type.__name__ = "Integer32"
_ComError86_Object = MibScalar
comError86 = _ComError86_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 86, 10),
    _ComError86_Type()
)
comError86.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError86.setStatus("mandatory")
_Multisensor87_ObjectIdentity = ObjectIdentity
multisensor87 = _Multisensor87_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 87)
)
_Sensorname87_Type = DisplayString
_Sensorname87_Object = MibScalar
sensorname87 = _Sensorname87_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 87, 1),
    _Sensorname87_Type()
)
sensorname87.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname87.setStatus("mandatory")


class _Temperature87_Type(Integer32):
    """Custom type temperature87 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature87_Type.__name__ = "Integer32"
_Temperature87_Object = MibScalar
temperature87 = _Temperature87_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 87, 2),
    _Temperature87_Type()
)
temperature87.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature87.setStatus("mandatory")


class _Humidity87_Type(Integer32):
    """Custom type humidity87 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity87_Type.__name__ = "Integer32"
_Humidity87_Object = MibScalar
humidity87 = _Humidity87_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 87, 3),
    _Humidity87_Type()
)
humidity87.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity87.setStatus("mandatory")


class _Dewpoint87_Type(Integer32):
    """Custom type dewpoint87 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint87_Type.__name__ = "Integer32"
_Dewpoint87_Object = MibScalar
dewpoint87 = _Dewpoint87_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 87, 4),
    _Dewpoint87_Type()
)
dewpoint87.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint87.setStatus("mandatory")


class _Co87_Type(Integer32):
    """Custom type co87 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co87_Type.__name__ = "Integer32"
_Co87_Object = MibScalar
co87 = _Co87_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 87, 5),
    _Co87_Type()
)
co87.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co87.setStatus("mandatory")


class _Motion87_Type(Integer32):
    """Custom type motion87 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion87_Type.__name__ = "Integer32"
_Motion87_Object = MibScalar
motion87 = _Motion87_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 87, 6),
    _Motion87_Type()
)
motion87.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion87.setStatus("mandatory")


class _Digitalin187_Type(Integer32):
    """Custom type digitalin187 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin187_Type.__name__ = "Integer32"
_Digitalin187_Object = MibScalar
digitalin187 = _Digitalin187_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 87, 7),
    _Digitalin187_Type()
)
digitalin187.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin187.setStatus("mandatory")


class _Digitalin287_Type(Integer32):
    """Custom type digitalin287 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin287_Type.__name__ = "Integer32"
_Digitalin287_Object = MibScalar
digitalin287 = _Digitalin287_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 87, 8),
    _Digitalin287_Type()
)
digitalin287.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin287.setStatus("mandatory")


class _Digitalout287_Type(Integer32):
    """Custom type digitalout287 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout287_Type.__name__ = "Integer32"
_Digitalout287_Object = MibScalar
digitalout287 = _Digitalout287_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 87, 9),
    _Digitalout287_Type()
)
digitalout287.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout287.setStatus("mandatory")


class _ComError87_Type(Integer32):
    """Custom type comError87 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError87_Type.__name__ = "Integer32"
_ComError87_Object = MibScalar
comError87 = _ComError87_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 87, 10),
    _ComError87_Type()
)
comError87.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError87.setStatus("mandatory")
_Multisensor88_ObjectIdentity = ObjectIdentity
multisensor88 = _Multisensor88_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 88)
)
_Sensorname88_Type = DisplayString
_Sensorname88_Object = MibScalar
sensorname88 = _Sensorname88_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 88, 1),
    _Sensorname88_Type()
)
sensorname88.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname88.setStatus("mandatory")


class _Temperature88_Type(Integer32):
    """Custom type temperature88 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature88_Type.__name__ = "Integer32"
_Temperature88_Object = MibScalar
temperature88 = _Temperature88_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 88, 2),
    _Temperature88_Type()
)
temperature88.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature88.setStatus("mandatory")


class _Humidity88_Type(Integer32):
    """Custom type humidity88 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity88_Type.__name__ = "Integer32"
_Humidity88_Object = MibScalar
humidity88 = _Humidity88_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 88, 3),
    _Humidity88_Type()
)
humidity88.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity88.setStatus("mandatory")


class _Dewpoint88_Type(Integer32):
    """Custom type dewpoint88 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint88_Type.__name__ = "Integer32"
_Dewpoint88_Object = MibScalar
dewpoint88 = _Dewpoint88_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 88, 4),
    _Dewpoint88_Type()
)
dewpoint88.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint88.setStatus("mandatory")


class _Co88_Type(Integer32):
    """Custom type co88 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co88_Type.__name__ = "Integer32"
_Co88_Object = MibScalar
co88 = _Co88_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 88, 5),
    _Co88_Type()
)
co88.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co88.setStatus("mandatory")


class _Motion88_Type(Integer32):
    """Custom type motion88 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion88_Type.__name__ = "Integer32"
_Motion88_Object = MibScalar
motion88 = _Motion88_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 88, 6),
    _Motion88_Type()
)
motion88.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion88.setStatus("mandatory")


class _Digitalin188_Type(Integer32):
    """Custom type digitalin188 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin188_Type.__name__ = "Integer32"
_Digitalin188_Object = MibScalar
digitalin188 = _Digitalin188_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 88, 7),
    _Digitalin188_Type()
)
digitalin188.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin188.setStatus("mandatory")


class _Digitalin288_Type(Integer32):
    """Custom type digitalin288 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin288_Type.__name__ = "Integer32"
_Digitalin288_Object = MibScalar
digitalin288 = _Digitalin288_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 88, 8),
    _Digitalin288_Type()
)
digitalin288.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin288.setStatus("mandatory")


class _Digitalout288_Type(Integer32):
    """Custom type digitalout288 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout288_Type.__name__ = "Integer32"
_Digitalout288_Object = MibScalar
digitalout288 = _Digitalout288_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 88, 9),
    _Digitalout288_Type()
)
digitalout288.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout288.setStatus("mandatory")


class _ComError88_Type(Integer32):
    """Custom type comError88 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError88_Type.__name__ = "Integer32"
_ComError88_Object = MibScalar
comError88 = _ComError88_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 88, 10),
    _ComError88_Type()
)
comError88.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError88.setStatus("mandatory")
_Multisensor89_ObjectIdentity = ObjectIdentity
multisensor89 = _Multisensor89_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 89)
)
_Sensorname89_Type = DisplayString
_Sensorname89_Object = MibScalar
sensorname89 = _Sensorname89_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 89, 1),
    _Sensorname89_Type()
)
sensorname89.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname89.setStatus("mandatory")


class _Temperature89_Type(Integer32):
    """Custom type temperature89 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature89_Type.__name__ = "Integer32"
_Temperature89_Object = MibScalar
temperature89 = _Temperature89_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 89, 2),
    _Temperature89_Type()
)
temperature89.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature89.setStatus("mandatory")


class _Humidity89_Type(Integer32):
    """Custom type humidity89 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity89_Type.__name__ = "Integer32"
_Humidity89_Object = MibScalar
humidity89 = _Humidity89_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 89, 3),
    _Humidity89_Type()
)
humidity89.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity89.setStatus("mandatory")


class _Dewpoint89_Type(Integer32):
    """Custom type dewpoint89 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint89_Type.__name__ = "Integer32"
_Dewpoint89_Object = MibScalar
dewpoint89 = _Dewpoint89_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 89, 4),
    _Dewpoint89_Type()
)
dewpoint89.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint89.setStatus("mandatory")


class _Co89_Type(Integer32):
    """Custom type co89 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co89_Type.__name__ = "Integer32"
_Co89_Object = MibScalar
co89 = _Co89_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 89, 5),
    _Co89_Type()
)
co89.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co89.setStatus("mandatory")


class _Motion89_Type(Integer32):
    """Custom type motion89 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion89_Type.__name__ = "Integer32"
_Motion89_Object = MibScalar
motion89 = _Motion89_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 89, 6),
    _Motion89_Type()
)
motion89.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion89.setStatus("mandatory")


class _Digitalin189_Type(Integer32):
    """Custom type digitalin189 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin189_Type.__name__ = "Integer32"
_Digitalin189_Object = MibScalar
digitalin189 = _Digitalin189_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 89, 7),
    _Digitalin189_Type()
)
digitalin189.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin189.setStatus("mandatory")


class _Digitalin289_Type(Integer32):
    """Custom type digitalin289 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin289_Type.__name__ = "Integer32"
_Digitalin289_Object = MibScalar
digitalin289 = _Digitalin289_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 89, 8),
    _Digitalin289_Type()
)
digitalin289.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin289.setStatus("mandatory")


class _Digitalout289_Type(Integer32):
    """Custom type digitalout289 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout289_Type.__name__ = "Integer32"
_Digitalout289_Object = MibScalar
digitalout289 = _Digitalout289_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 89, 9),
    _Digitalout289_Type()
)
digitalout289.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout289.setStatus("mandatory")


class _ComError89_Type(Integer32):
    """Custom type comError89 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError89_Type.__name__ = "Integer32"
_ComError89_Object = MibScalar
comError89 = _ComError89_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 89, 10),
    _ComError89_Type()
)
comError89.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError89.setStatus("mandatory")
_Multisensor90_ObjectIdentity = ObjectIdentity
multisensor90 = _Multisensor90_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 90)
)
_Sensorname90_Type = DisplayString
_Sensorname90_Object = MibScalar
sensorname90 = _Sensorname90_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 90, 1),
    _Sensorname90_Type()
)
sensorname90.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname90.setStatus("mandatory")


class _Temperature90_Type(Integer32):
    """Custom type temperature90 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature90_Type.__name__ = "Integer32"
_Temperature90_Object = MibScalar
temperature90 = _Temperature90_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 90, 2),
    _Temperature90_Type()
)
temperature90.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature90.setStatus("mandatory")


class _Humidity90_Type(Integer32):
    """Custom type humidity90 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity90_Type.__name__ = "Integer32"
_Humidity90_Object = MibScalar
humidity90 = _Humidity90_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 90, 3),
    _Humidity90_Type()
)
humidity90.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity90.setStatus("mandatory")


class _Dewpoint90_Type(Integer32):
    """Custom type dewpoint90 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint90_Type.__name__ = "Integer32"
_Dewpoint90_Object = MibScalar
dewpoint90 = _Dewpoint90_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 90, 4),
    _Dewpoint90_Type()
)
dewpoint90.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint90.setStatus("mandatory")


class _Co90_Type(Integer32):
    """Custom type co90 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co90_Type.__name__ = "Integer32"
_Co90_Object = MibScalar
co90 = _Co90_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 90, 5),
    _Co90_Type()
)
co90.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co90.setStatus("mandatory")


class _Motion90_Type(Integer32):
    """Custom type motion90 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion90_Type.__name__ = "Integer32"
_Motion90_Object = MibScalar
motion90 = _Motion90_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 90, 6),
    _Motion90_Type()
)
motion90.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion90.setStatus("mandatory")


class _Digitalin190_Type(Integer32):
    """Custom type digitalin190 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin190_Type.__name__ = "Integer32"
_Digitalin190_Object = MibScalar
digitalin190 = _Digitalin190_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 90, 7),
    _Digitalin190_Type()
)
digitalin190.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin190.setStatus("mandatory")


class _Digitalin290_Type(Integer32):
    """Custom type digitalin290 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin290_Type.__name__ = "Integer32"
_Digitalin290_Object = MibScalar
digitalin290 = _Digitalin290_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 90, 8),
    _Digitalin290_Type()
)
digitalin290.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin290.setStatus("mandatory")


class _Digitalout290_Type(Integer32):
    """Custom type digitalout290 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout290_Type.__name__ = "Integer32"
_Digitalout290_Object = MibScalar
digitalout290 = _Digitalout290_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 90, 9),
    _Digitalout290_Type()
)
digitalout290.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout290.setStatus("mandatory")


class _ComError90_Type(Integer32):
    """Custom type comError90 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError90_Type.__name__ = "Integer32"
_ComError90_Object = MibScalar
comError90 = _ComError90_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 90, 10),
    _ComError90_Type()
)
comError90.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError90.setStatus("mandatory")
_Multisensor91_ObjectIdentity = ObjectIdentity
multisensor91 = _Multisensor91_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 91)
)
_Sensorname91_Type = DisplayString
_Sensorname91_Object = MibScalar
sensorname91 = _Sensorname91_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 91, 1),
    _Sensorname91_Type()
)
sensorname91.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname91.setStatus("mandatory")


class _Temperature91_Type(Integer32):
    """Custom type temperature91 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature91_Type.__name__ = "Integer32"
_Temperature91_Object = MibScalar
temperature91 = _Temperature91_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 91, 2),
    _Temperature91_Type()
)
temperature91.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature91.setStatus("mandatory")


class _Humidity91_Type(Integer32):
    """Custom type humidity91 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity91_Type.__name__ = "Integer32"
_Humidity91_Object = MibScalar
humidity91 = _Humidity91_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 91, 3),
    _Humidity91_Type()
)
humidity91.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity91.setStatus("mandatory")


class _Dewpoint91_Type(Integer32):
    """Custom type dewpoint91 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint91_Type.__name__ = "Integer32"
_Dewpoint91_Object = MibScalar
dewpoint91 = _Dewpoint91_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 91, 4),
    _Dewpoint91_Type()
)
dewpoint91.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint91.setStatus("mandatory")


class _Co91_Type(Integer32):
    """Custom type co91 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co91_Type.__name__ = "Integer32"
_Co91_Object = MibScalar
co91 = _Co91_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 91, 5),
    _Co91_Type()
)
co91.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co91.setStatus("mandatory")


class _Motion91_Type(Integer32):
    """Custom type motion91 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion91_Type.__name__ = "Integer32"
_Motion91_Object = MibScalar
motion91 = _Motion91_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 91, 6),
    _Motion91_Type()
)
motion91.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion91.setStatus("mandatory")


class _Digitalin191_Type(Integer32):
    """Custom type digitalin191 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin191_Type.__name__ = "Integer32"
_Digitalin191_Object = MibScalar
digitalin191 = _Digitalin191_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 91, 7),
    _Digitalin191_Type()
)
digitalin191.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin191.setStatus("mandatory")


class _Digitalin291_Type(Integer32):
    """Custom type digitalin291 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin291_Type.__name__ = "Integer32"
_Digitalin291_Object = MibScalar
digitalin291 = _Digitalin291_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 91, 8),
    _Digitalin291_Type()
)
digitalin291.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin291.setStatus("mandatory")


class _Digitalout291_Type(Integer32):
    """Custom type digitalout291 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout291_Type.__name__ = "Integer32"
_Digitalout291_Object = MibScalar
digitalout291 = _Digitalout291_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 91, 9),
    _Digitalout291_Type()
)
digitalout291.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout291.setStatus("mandatory")


class _ComError91_Type(Integer32):
    """Custom type comError91 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError91_Type.__name__ = "Integer32"
_ComError91_Object = MibScalar
comError91 = _ComError91_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 91, 10),
    _ComError91_Type()
)
comError91.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError91.setStatus("mandatory")
_Multisensor92_ObjectIdentity = ObjectIdentity
multisensor92 = _Multisensor92_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 92)
)
_Sensorname92_Type = DisplayString
_Sensorname92_Object = MibScalar
sensorname92 = _Sensorname92_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 92, 1),
    _Sensorname92_Type()
)
sensorname92.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname92.setStatus("mandatory")


class _Temperature92_Type(Integer32):
    """Custom type temperature92 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature92_Type.__name__ = "Integer32"
_Temperature92_Object = MibScalar
temperature92 = _Temperature92_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 92, 2),
    _Temperature92_Type()
)
temperature92.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature92.setStatus("mandatory")


class _Humidity92_Type(Integer32):
    """Custom type humidity92 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity92_Type.__name__ = "Integer32"
_Humidity92_Object = MibScalar
humidity92 = _Humidity92_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 92, 3),
    _Humidity92_Type()
)
humidity92.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity92.setStatus("mandatory")


class _Dewpoint92_Type(Integer32):
    """Custom type dewpoint92 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint92_Type.__name__ = "Integer32"
_Dewpoint92_Object = MibScalar
dewpoint92 = _Dewpoint92_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 92, 4),
    _Dewpoint92_Type()
)
dewpoint92.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint92.setStatus("mandatory")


class _Co92_Type(Integer32):
    """Custom type co92 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co92_Type.__name__ = "Integer32"
_Co92_Object = MibScalar
co92 = _Co92_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 92, 5),
    _Co92_Type()
)
co92.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co92.setStatus("mandatory")


class _Motion92_Type(Integer32):
    """Custom type motion92 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion92_Type.__name__ = "Integer32"
_Motion92_Object = MibScalar
motion92 = _Motion92_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 92, 6),
    _Motion92_Type()
)
motion92.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion92.setStatus("mandatory")


class _Digitalin192_Type(Integer32):
    """Custom type digitalin192 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin192_Type.__name__ = "Integer32"
_Digitalin192_Object = MibScalar
digitalin192 = _Digitalin192_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 92, 7),
    _Digitalin192_Type()
)
digitalin192.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin192.setStatus("mandatory")


class _Digitalin292_Type(Integer32):
    """Custom type digitalin292 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin292_Type.__name__ = "Integer32"
_Digitalin292_Object = MibScalar
digitalin292 = _Digitalin292_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 92, 8),
    _Digitalin292_Type()
)
digitalin292.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin292.setStatus("mandatory")


class _Digitalout292_Type(Integer32):
    """Custom type digitalout292 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout292_Type.__name__ = "Integer32"
_Digitalout292_Object = MibScalar
digitalout292 = _Digitalout292_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 92, 9),
    _Digitalout292_Type()
)
digitalout292.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout292.setStatus("mandatory")


class _ComError92_Type(Integer32):
    """Custom type comError92 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError92_Type.__name__ = "Integer32"
_ComError92_Object = MibScalar
comError92 = _ComError92_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 92, 10),
    _ComError92_Type()
)
comError92.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError92.setStatus("mandatory")
_Multisensor93_ObjectIdentity = ObjectIdentity
multisensor93 = _Multisensor93_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 93)
)
_Sensorname93_Type = DisplayString
_Sensorname93_Object = MibScalar
sensorname93 = _Sensorname93_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 93, 1),
    _Sensorname93_Type()
)
sensorname93.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname93.setStatus("mandatory")


class _Temperature93_Type(Integer32):
    """Custom type temperature93 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature93_Type.__name__ = "Integer32"
_Temperature93_Object = MibScalar
temperature93 = _Temperature93_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 93, 2),
    _Temperature93_Type()
)
temperature93.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature93.setStatus("mandatory")


class _Humidity93_Type(Integer32):
    """Custom type humidity93 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity93_Type.__name__ = "Integer32"
_Humidity93_Object = MibScalar
humidity93 = _Humidity93_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 93, 3),
    _Humidity93_Type()
)
humidity93.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity93.setStatus("mandatory")


class _Dewpoint93_Type(Integer32):
    """Custom type dewpoint93 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint93_Type.__name__ = "Integer32"
_Dewpoint93_Object = MibScalar
dewpoint93 = _Dewpoint93_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 93, 4),
    _Dewpoint93_Type()
)
dewpoint93.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint93.setStatus("mandatory")


class _Co93_Type(Integer32):
    """Custom type co93 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co93_Type.__name__ = "Integer32"
_Co93_Object = MibScalar
co93 = _Co93_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 93, 5),
    _Co93_Type()
)
co93.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co93.setStatus("mandatory")


class _Motion93_Type(Integer32):
    """Custom type motion93 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion93_Type.__name__ = "Integer32"
_Motion93_Object = MibScalar
motion93 = _Motion93_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 93, 6),
    _Motion93_Type()
)
motion93.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion93.setStatus("mandatory")


class _Digitalin193_Type(Integer32):
    """Custom type digitalin193 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin193_Type.__name__ = "Integer32"
_Digitalin193_Object = MibScalar
digitalin193 = _Digitalin193_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 93, 7),
    _Digitalin193_Type()
)
digitalin193.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin193.setStatus("mandatory")


class _Digitalin293_Type(Integer32):
    """Custom type digitalin293 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin293_Type.__name__ = "Integer32"
_Digitalin293_Object = MibScalar
digitalin293 = _Digitalin293_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 93, 8),
    _Digitalin293_Type()
)
digitalin293.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin293.setStatus("mandatory")


class _Digitalout293_Type(Integer32):
    """Custom type digitalout293 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout293_Type.__name__ = "Integer32"
_Digitalout293_Object = MibScalar
digitalout293 = _Digitalout293_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 93, 9),
    _Digitalout293_Type()
)
digitalout293.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout293.setStatus("mandatory")


class _ComError93_Type(Integer32):
    """Custom type comError93 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError93_Type.__name__ = "Integer32"
_ComError93_Object = MibScalar
comError93 = _ComError93_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 93, 10),
    _ComError93_Type()
)
comError93.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError93.setStatus("mandatory")
_Multisensor94_ObjectIdentity = ObjectIdentity
multisensor94 = _Multisensor94_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 94)
)
_Sensorname94_Type = DisplayString
_Sensorname94_Object = MibScalar
sensorname94 = _Sensorname94_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 94, 1),
    _Sensorname94_Type()
)
sensorname94.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname94.setStatus("mandatory")


class _Temperature94_Type(Integer32):
    """Custom type temperature94 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature94_Type.__name__ = "Integer32"
_Temperature94_Object = MibScalar
temperature94 = _Temperature94_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 94, 2),
    _Temperature94_Type()
)
temperature94.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature94.setStatus("mandatory")


class _Humidity94_Type(Integer32):
    """Custom type humidity94 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity94_Type.__name__ = "Integer32"
_Humidity94_Object = MibScalar
humidity94 = _Humidity94_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 94, 3),
    _Humidity94_Type()
)
humidity94.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity94.setStatus("mandatory")


class _Dewpoint94_Type(Integer32):
    """Custom type dewpoint94 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint94_Type.__name__ = "Integer32"
_Dewpoint94_Object = MibScalar
dewpoint94 = _Dewpoint94_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 94, 4),
    _Dewpoint94_Type()
)
dewpoint94.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint94.setStatus("mandatory")


class _Co94_Type(Integer32):
    """Custom type co94 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co94_Type.__name__ = "Integer32"
_Co94_Object = MibScalar
co94 = _Co94_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 94, 5),
    _Co94_Type()
)
co94.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co94.setStatus("mandatory")


class _Motion94_Type(Integer32):
    """Custom type motion94 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion94_Type.__name__ = "Integer32"
_Motion94_Object = MibScalar
motion94 = _Motion94_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 94, 6),
    _Motion94_Type()
)
motion94.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion94.setStatus("mandatory")


class _Digitalin194_Type(Integer32):
    """Custom type digitalin194 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin194_Type.__name__ = "Integer32"
_Digitalin194_Object = MibScalar
digitalin194 = _Digitalin194_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 94, 7),
    _Digitalin194_Type()
)
digitalin194.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin194.setStatus("mandatory")


class _Digitalin294_Type(Integer32):
    """Custom type digitalin294 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin294_Type.__name__ = "Integer32"
_Digitalin294_Object = MibScalar
digitalin294 = _Digitalin294_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 94, 8),
    _Digitalin294_Type()
)
digitalin294.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin294.setStatus("mandatory")


class _Digitalout294_Type(Integer32):
    """Custom type digitalout294 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout294_Type.__name__ = "Integer32"
_Digitalout294_Object = MibScalar
digitalout294 = _Digitalout294_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 94, 9),
    _Digitalout294_Type()
)
digitalout294.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout294.setStatus("mandatory")


class _ComError94_Type(Integer32):
    """Custom type comError94 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError94_Type.__name__ = "Integer32"
_ComError94_Object = MibScalar
comError94 = _ComError94_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 94, 10),
    _ComError94_Type()
)
comError94.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError94.setStatus("mandatory")
_Multisensor95_ObjectIdentity = ObjectIdentity
multisensor95 = _Multisensor95_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 95)
)
_Sensorname95_Type = DisplayString
_Sensorname95_Object = MibScalar
sensorname95 = _Sensorname95_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 95, 1),
    _Sensorname95_Type()
)
sensorname95.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname95.setStatus("mandatory")


class _Temperature95_Type(Integer32):
    """Custom type temperature95 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature95_Type.__name__ = "Integer32"
_Temperature95_Object = MibScalar
temperature95 = _Temperature95_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 95, 2),
    _Temperature95_Type()
)
temperature95.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature95.setStatus("mandatory")


class _Humidity95_Type(Integer32):
    """Custom type humidity95 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity95_Type.__name__ = "Integer32"
_Humidity95_Object = MibScalar
humidity95 = _Humidity95_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 95, 3),
    _Humidity95_Type()
)
humidity95.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity95.setStatus("mandatory")


class _Dewpoint95_Type(Integer32):
    """Custom type dewpoint95 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint95_Type.__name__ = "Integer32"
_Dewpoint95_Object = MibScalar
dewpoint95 = _Dewpoint95_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 95, 4),
    _Dewpoint95_Type()
)
dewpoint95.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint95.setStatus("mandatory")


class _Co95_Type(Integer32):
    """Custom type co95 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co95_Type.__name__ = "Integer32"
_Co95_Object = MibScalar
co95 = _Co95_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 95, 5),
    _Co95_Type()
)
co95.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co95.setStatus("mandatory")


class _Motion95_Type(Integer32):
    """Custom type motion95 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion95_Type.__name__ = "Integer32"
_Motion95_Object = MibScalar
motion95 = _Motion95_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 95, 6),
    _Motion95_Type()
)
motion95.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion95.setStatus("mandatory")


class _Digitalin195_Type(Integer32):
    """Custom type digitalin195 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin195_Type.__name__ = "Integer32"
_Digitalin195_Object = MibScalar
digitalin195 = _Digitalin195_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 95, 7),
    _Digitalin195_Type()
)
digitalin195.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin195.setStatus("mandatory")


class _Digitalin295_Type(Integer32):
    """Custom type digitalin295 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin295_Type.__name__ = "Integer32"
_Digitalin295_Object = MibScalar
digitalin295 = _Digitalin295_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 95, 8),
    _Digitalin295_Type()
)
digitalin295.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin295.setStatus("mandatory")


class _Digitalout295_Type(Integer32):
    """Custom type digitalout295 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout295_Type.__name__ = "Integer32"
_Digitalout295_Object = MibScalar
digitalout295 = _Digitalout295_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 95, 9),
    _Digitalout295_Type()
)
digitalout295.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout295.setStatus("mandatory")


class _ComError95_Type(Integer32):
    """Custom type comError95 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError95_Type.__name__ = "Integer32"
_ComError95_Object = MibScalar
comError95 = _ComError95_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 95, 10),
    _ComError95_Type()
)
comError95.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError95.setStatus("mandatory")
_Multisensor96_ObjectIdentity = ObjectIdentity
multisensor96 = _Multisensor96_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 96)
)
_Sensorname96_Type = DisplayString
_Sensorname96_Object = MibScalar
sensorname96 = _Sensorname96_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 96, 1),
    _Sensorname96_Type()
)
sensorname96.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname96.setStatus("mandatory")


class _Temperature96_Type(Integer32):
    """Custom type temperature96 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature96_Type.__name__ = "Integer32"
_Temperature96_Object = MibScalar
temperature96 = _Temperature96_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 96, 2),
    _Temperature96_Type()
)
temperature96.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature96.setStatus("mandatory")


class _Humidity96_Type(Integer32):
    """Custom type humidity96 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity96_Type.__name__ = "Integer32"
_Humidity96_Object = MibScalar
humidity96 = _Humidity96_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 96, 3),
    _Humidity96_Type()
)
humidity96.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity96.setStatus("mandatory")


class _Dewpoint96_Type(Integer32):
    """Custom type dewpoint96 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint96_Type.__name__ = "Integer32"
_Dewpoint96_Object = MibScalar
dewpoint96 = _Dewpoint96_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 96, 4),
    _Dewpoint96_Type()
)
dewpoint96.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint96.setStatus("mandatory")


class _Co96_Type(Integer32):
    """Custom type co96 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co96_Type.__name__ = "Integer32"
_Co96_Object = MibScalar
co96 = _Co96_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 96, 5),
    _Co96_Type()
)
co96.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co96.setStatus("mandatory")


class _Motion96_Type(Integer32):
    """Custom type motion96 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion96_Type.__name__ = "Integer32"
_Motion96_Object = MibScalar
motion96 = _Motion96_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 96, 6),
    _Motion96_Type()
)
motion96.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion96.setStatus("mandatory")


class _Digitalin196_Type(Integer32):
    """Custom type digitalin196 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin196_Type.__name__ = "Integer32"
_Digitalin196_Object = MibScalar
digitalin196 = _Digitalin196_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 96, 7),
    _Digitalin196_Type()
)
digitalin196.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin196.setStatus("mandatory")


class _Digitalin296_Type(Integer32):
    """Custom type digitalin296 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin296_Type.__name__ = "Integer32"
_Digitalin296_Object = MibScalar
digitalin296 = _Digitalin296_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 96, 8),
    _Digitalin296_Type()
)
digitalin296.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin296.setStatus("mandatory")


class _Digitalout296_Type(Integer32):
    """Custom type digitalout296 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout296_Type.__name__ = "Integer32"
_Digitalout296_Object = MibScalar
digitalout296 = _Digitalout296_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 96, 9),
    _Digitalout296_Type()
)
digitalout296.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout296.setStatus("mandatory")


class _ComError96_Type(Integer32):
    """Custom type comError96 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError96_Type.__name__ = "Integer32"
_ComError96_Object = MibScalar
comError96 = _ComError96_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 96, 10),
    _ComError96_Type()
)
comError96.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError96.setStatus("mandatory")
_Multisensor97_ObjectIdentity = ObjectIdentity
multisensor97 = _Multisensor97_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 97)
)
_Sensorname97_Type = DisplayString
_Sensorname97_Object = MibScalar
sensorname97 = _Sensorname97_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 97, 1),
    _Sensorname97_Type()
)
sensorname97.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname97.setStatus("mandatory")


class _Temperature97_Type(Integer32):
    """Custom type temperature97 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature97_Type.__name__ = "Integer32"
_Temperature97_Object = MibScalar
temperature97 = _Temperature97_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 97, 2),
    _Temperature97_Type()
)
temperature97.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature97.setStatus("mandatory")


class _Humidity97_Type(Integer32):
    """Custom type humidity97 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity97_Type.__name__ = "Integer32"
_Humidity97_Object = MibScalar
humidity97 = _Humidity97_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 97, 3),
    _Humidity97_Type()
)
humidity97.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity97.setStatus("mandatory")


class _Dewpoint97_Type(Integer32):
    """Custom type dewpoint97 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint97_Type.__name__ = "Integer32"
_Dewpoint97_Object = MibScalar
dewpoint97 = _Dewpoint97_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 97, 4),
    _Dewpoint97_Type()
)
dewpoint97.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint97.setStatus("mandatory")


class _Co97_Type(Integer32):
    """Custom type co97 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co97_Type.__name__ = "Integer32"
_Co97_Object = MibScalar
co97 = _Co97_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 97, 5),
    _Co97_Type()
)
co97.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co97.setStatus("mandatory")


class _Motion97_Type(Integer32):
    """Custom type motion97 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion97_Type.__name__ = "Integer32"
_Motion97_Object = MibScalar
motion97 = _Motion97_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 97, 6),
    _Motion97_Type()
)
motion97.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion97.setStatus("mandatory")


class _Digitalin197_Type(Integer32):
    """Custom type digitalin197 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin197_Type.__name__ = "Integer32"
_Digitalin197_Object = MibScalar
digitalin197 = _Digitalin197_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 97, 7),
    _Digitalin197_Type()
)
digitalin197.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin197.setStatus("mandatory")


class _Digitalin297_Type(Integer32):
    """Custom type digitalin297 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin297_Type.__name__ = "Integer32"
_Digitalin297_Object = MibScalar
digitalin297 = _Digitalin297_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 97, 8),
    _Digitalin297_Type()
)
digitalin297.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin297.setStatus("mandatory")


class _Digitalout297_Type(Integer32):
    """Custom type digitalout297 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout297_Type.__name__ = "Integer32"
_Digitalout297_Object = MibScalar
digitalout297 = _Digitalout297_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 97, 9),
    _Digitalout297_Type()
)
digitalout297.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout297.setStatus("mandatory")


class _ComError97_Type(Integer32):
    """Custom type comError97 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError97_Type.__name__ = "Integer32"
_ComError97_Object = MibScalar
comError97 = _ComError97_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 97, 10),
    _ComError97_Type()
)
comError97.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError97.setStatus("mandatory")
_Multisensor98_ObjectIdentity = ObjectIdentity
multisensor98 = _Multisensor98_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 98)
)
_Sensorname98_Type = DisplayString
_Sensorname98_Object = MibScalar
sensorname98 = _Sensorname98_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 98, 1),
    _Sensorname98_Type()
)
sensorname98.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname98.setStatus("mandatory")


class _Temperature98_Type(Integer32):
    """Custom type temperature98 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature98_Type.__name__ = "Integer32"
_Temperature98_Object = MibScalar
temperature98 = _Temperature98_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 98, 2),
    _Temperature98_Type()
)
temperature98.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature98.setStatus("mandatory")


class _Humidity98_Type(Integer32):
    """Custom type humidity98 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity98_Type.__name__ = "Integer32"
_Humidity98_Object = MibScalar
humidity98 = _Humidity98_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 98, 3),
    _Humidity98_Type()
)
humidity98.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity98.setStatus("mandatory")


class _Dewpoint98_Type(Integer32):
    """Custom type dewpoint98 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint98_Type.__name__ = "Integer32"
_Dewpoint98_Object = MibScalar
dewpoint98 = _Dewpoint98_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 98, 4),
    _Dewpoint98_Type()
)
dewpoint98.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint98.setStatus("mandatory")


class _Co98_Type(Integer32):
    """Custom type co98 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co98_Type.__name__ = "Integer32"
_Co98_Object = MibScalar
co98 = _Co98_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 98, 5),
    _Co98_Type()
)
co98.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co98.setStatus("mandatory")


class _Motion98_Type(Integer32):
    """Custom type motion98 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion98_Type.__name__ = "Integer32"
_Motion98_Object = MibScalar
motion98 = _Motion98_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 98, 6),
    _Motion98_Type()
)
motion98.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion98.setStatus("mandatory")


class _Digitalin198_Type(Integer32):
    """Custom type digitalin198 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin198_Type.__name__ = "Integer32"
_Digitalin198_Object = MibScalar
digitalin198 = _Digitalin198_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 98, 7),
    _Digitalin198_Type()
)
digitalin198.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin198.setStatus("mandatory")


class _Digitalin298_Type(Integer32):
    """Custom type digitalin298 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin298_Type.__name__ = "Integer32"
_Digitalin298_Object = MibScalar
digitalin298 = _Digitalin298_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 98, 8),
    _Digitalin298_Type()
)
digitalin298.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin298.setStatus("mandatory")


class _Digitalout298_Type(Integer32):
    """Custom type digitalout298 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout298_Type.__name__ = "Integer32"
_Digitalout298_Object = MibScalar
digitalout298 = _Digitalout298_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 98, 9),
    _Digitalout298_Type()
)
digitalout298.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout298.setStatus("mandatory")


class _ComError98_Type(Integer32):
    """Custom type comError98 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError98_Type.__name__ = "Integer32"
_ComError98_Object = MibScalar
comError98 = _ComError98_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 98, 10),
    _ComError98_Type()
)
comError98.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError98.setStatus("mandatory")
_Multisensor99_ObjectIdentity = ObjectIdentity
multisensor99 = _Multisensor99_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 99)
)
_Sensorname99_Type = DisplayString
_Sensorname99_Object = MibScalar
sensorname99 = _Sensorname99_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 99, 1),
    _Sensorname99_Type()
)
sensorname99.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname99.setStatus("mandatory")


class _Temperature99_Type(Integer32):
    """Custom type temperature99 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature99_Type.__name__ = "Integer32"
_Temperature99_Object = MibScalar
temperature99 = _Temperature99_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 99, 2),
    _Temperature99_Type()
)
temperature99.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature99.setStatus("mandatory")


class _Humidity99_Type(Integer32):
    """Custom type humidity99 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity99_Type.__name__ = "Integer32"
_Humidity99_Object = MibScalar
humidity99 = _Humidity99_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 99, 3),
    _Humidity99_Type()
)
humidity99.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity99.setStatus("mandatory")


class _Dewpoint99_Type(Integer32):
    """Custom type dewpoint99 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint99_Type.__name__ = "Integer32"
_Dewpoint99_Object = MibScalar
dewpoint99 = _Dewpoint99_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 99, 4),
    _Dewpoint99_Type()
)
dewpoint99.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint99.setStatus("mandatory")


class _Co99_Type(Integer32):
    """Custom type co99 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co99_Type.__name__ = "Integer32"
_Co99_Object = MibScalar
co99 = _Co99_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 99, 5),
    _Co99_Type()
)
co99.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co99.setStatus("mandatory")


class _Motion99_Type(Integer32):
    """Custom type motion99 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion99_Type.__name__ = "Integer32"
_Motion99_Object = MibScalar
motion99 = _Motion99_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 99, 6),
    _Motion99_Type()
)
motion99.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion99.setStatus("mandatory")


class _Digitalin199_Type(Integer32):
    """Custom type digitalin199 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin199_Type.__name__ = "Integer32"
_Digitalin199_Object = MibScalar
digitalin199 = _Digitalin199_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 99, 7),
    _Digitalin199_Type()
)
digitalin199.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin199.setStatus("mandatory")


class _Digitalin299_Type(Integer32):
    """Custom type digitalin299 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin299_Type.__name__ = "Integer32"
_Digitalin299_Object = MibScalar
digitalin299 = _Digitalin299_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 99, 8),
    _Digitalin299_Type()
)
digitalin299.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin299.setStatus("mandatory")


class _Digitalout299_Type(Integer32):
    """Custom type digitalout299 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout299_Type.__name__ = "Integer32"
_Digitalout299_Object = MibScalar
digitalout299 = _Digitalout299_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 99, 9),
    _Digitalout299_Type()
)
digitalout299.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout299.setStatus("mandatory")


class _ComError99_Type(Integer32):
    """Custom type comError99 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError99_Type.__name__ = "Integer32"
_ComError99_Object = MibScalar
comError99 = _ComError99_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 99, 10),
    _ComError99_Type()
)
comError99.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError99.setStatus("mandatory")
_Multisensor100_ObjectIdentity = ObjectIdentity
multisensor100 = _Multisensor100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 100)
)
_Sensorname100_Type = DisplayString
_Sensorname100_Object = MibScalar
sensorname100 = _Sensorname100_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 100, 1),
    _Sensorname100_Type()
)
sensorname100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensorname100.setStatus("mandatory")


class _Temperature100_Type(Integer32):
    """Custom type temperature100 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Temperature100_Type.__name__ = "Integer32"
_Temperature100_Object = MibScalar
temperature100 = _Temperature100_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 100, 2),
    _Temperature100_Type()
)
temperature100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    temperature100.setStatus("mandatory")


class _Humidity100_Type(Integer32):
    """Custom type humidity100 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Humidity100_Type.__name__ = "Integer32"
_Humidity100_Object = MibScalar
humidity100 = _Humidity100_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 100, 3),
    _Humidity100_Type()
)
humidity100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidity100.setStatus("mandatory")


class _Dewpoint100_Type(Integer32):
    """Custom type dewpoint100 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_Dewpoint100_Type.__name__ = "Integer32"
_Dewpoint100_Object = MibScalar
dewpoint100 = _Dewpoint100_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 100, 4),
    _Dewpoint100_Type()
)
dewpoint100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dewpoint100.setStatus("mandatory")


class _Co100_Type(Integer32):
    """Custom type co100 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 100),
    )


_Co100_Type.__name__ = "Integer32"
_Co100_Object = MibScalar
co100 = _Co100_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 100, 5),
    _Co100_Type()
)
co100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    co100.setStatus("mandatory")


class _Motion100_Type(Integer32):
    """Custom type motion100 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_Motion100_Type.__name__ = "Integer32"
_Motion100_Object = MibScalar
motion100 = _Motion100_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 100, 6),
    _Motion100_Type()
)
motion100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    motion100.setStatus("mandatory")


class _Digitalin1100_Type(Integer32):
    """Custom type digitalin1100 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin1100_Type.__name__ = "Integer32"
_Digitalin1100_Object = MibScalar
digitalin1100 = _Digitalin1100_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 100, 7),
    _Digitalin1100_Type()
)
digitalin1100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin1100.setStatus("mandatory")


class _Digitalin2100_Type(Integer32):
    """Custom type digitalin2100 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalin2100_Type.__name__ = "Integer32"
_Digitalin2100_Object = MibScalar
digitalin2100 = _Digitalin2100_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 100, 8),
    _Digitalin2100_Type()
)
digitalin2100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalin2100.setStatus("mandatory")


class _Digitalout2100_Type(Integer32):
    """Custom type digitalout2100 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Digitalout2100_Type.__name__ = "Integer32"
_Digitalout2100_Object = MibScalar
digitalout2100 = _Digitalout2100_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 100, 9),
    _Digitalout2100_Type()
)
digitalout2100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digitalout2100.setStatus("mandatory")


class _ComError100_Type(Integer32):
    """Custom type comError100 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ComError100_Type.__name__ = "Integer32"
_ComError100_Object = MibScalar
comError100 = _ComError100_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 2, 100, 10),
    _ComError100_Type()
)
comError100.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    comError100.setStatus("mandatory")
_Ext_module_ObjectIdentity = ObjectIdentity
ext_module = _Ext_module_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3)
)
_Modul01port01_ObjectIdentity = ObjectIdentity
modul01port01 = _Modul01port01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 1)
)
_Modul01portname01_Type = DisplayString
_Modul01portname01_Object = MibScalar
modul01portname01 = _Modul01portname01_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 1, 1),
    _Modul01portname01_Type()
)
modul01portname01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portname01.setStatus("mandatory")


class _Modul01portstate01_Type(Integer32):
    """Custom type modul01portstate01 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul01portstate01_Type.__name__ = "Integer32"
_Modul01portstate01_Object = MibScalar
modul01portstate01 = _Modul01portstate01_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 1, 2),
    _Modul01portstate01_Type()
)
modul01portstate01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portstate01.setStatus("mandatory")
_Modul01port02_ObjectIdentity = ObjectIdentity
modul01port02 = _Modul01port02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 2)
)
_Modul01portname02_Type = DisplayString
_Modul01portname02_Object = MibScalar
modul01portname02 = _Modul01portname02_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 2, 1),
    _Modul01portname02_Type()
)
modul01portname02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portname02.setStatus("mandatory")


class _Modul01portstate02_Type(Integer32):
    """Custom type modul01portstate02 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul01portstate02_Type.__name__ = "Integer32"
_Modul01portstate02_Object = MibScalar
modul01portstate02 = _Modul01portstate02_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 2, 2),
    _Modul01portstate02_Type()
)
modul01portstate02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portstate02.setStatus("mandatory")
_Modul01port03_ObjectIdentity = ObjectIdentity
modul01port03 = _Modul01port03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 3)
)
_Modul01portname03_Type = DisplayString
_Modul01portname03_Object = MibScalar
modul01portname03 = _Modul01portname03_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 3, 1),
    _Modul01portname03_Type()
)
modul01portname03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portname03.setStatus("mandatory")


class _Modul01portstate03_Type(Integer32):
    """Custom type modul01portstate03 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul01portstate03_Type.__name__ = "Integer32"
_Modul01portstate03_Object = MibScalar
modul01portstate03 = _Modul01portstate03_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 3, 2),
    _Modul01portstate03_Type()
)
modul01portstate03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portstate03.setStatus("mandatory")
_Modul01port04_ObjectIdentity = ObjectIdentity
modul01port04 = _Modul01port04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 4)
)
_Modul01portname04_Type = DisplayString
_Modul01portname04_Object = MibScalar
modul01portname04 = _Modul01portname04_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 4, 1),
    _Modul01portname04_Type()
)
modul01portname04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portname04.setStatus("mandatory")


class _Modul01portstate04_Type(Integer32):
    """Custom type modul01portstate04 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul01portstate04_Type.__name__ = "Integer32"
_Modul01portstate04_Object = MibScalar
modul01portstate04 = _Modul01portstate04_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 4, 2),
    _Modul01portstate04_Type()
)
modul01portstate04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portstate04.setStatus("mandatory")
_Modul01port05_ObjectIdentity = ObjectIdentity
modul01port05 = _Modul01port05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 5)
)
_Modul01portname05_Type = DisplayString
_Modul01portname05_Object = MibScalar
modul01portname05 = _Modul01portname05_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 5, 1),
    _Modul01portname05_Type()
)
modul01portname05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portname05.setStatus("mandatory")


class _Modul01portstate05_Type(Integer32):
    """Custom type modul01portstate05 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul01portstate05_Type.__name__ = "Integer32"
_Modul01portstate05_Object = MibScalar
modul01portstate05 = _Modul01portstate05_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 5, 2),
    _Modul01portstate05_Type()
)
modul01portstate05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portstate05.setStatus("mandatory")
_Modul01port06_ObjectIdentity = ObjectIdentity
modul01port06 = _Modul01port06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 6)
)
_Modul01portname06_Type = DisplayString
_Modul01portname06_Object = MibScalar
modul01portname06 = _Modul01portname06_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 6, 1),
    _Modul01portname06_Type()
)
modul01portname06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portname06.setStatus("mandatory")


class _Modul01portstate06_Type(Integer32):
    """Custom type modul01portstate06 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul01portstate06_Type.__name__ = "Integer32"
_Modul01portstate06_Object = MibScalar
modul01portstate06 = _Modul01portstate06_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 6, 2),
    _Modul01portstate06_Type()
)
modul01portstate06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portstate06.setStatus("mandatory")
_Modul01port07_ObjectIdentity = ObjectIdentity
modul01port07 = _Modul01port07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 7)
)
_Modul01portname07_Type = DisplayString
_Modul01portname07_Object = MibScalar
modul01portname07 = _Modul01portname07_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 7, 1),
    _Modul01portname07_Type()
)
modul01portname07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portname07.setStatus("mandatory")


class _Modul01portstate07_Type(Integer32):
    """Custom type modul01portstate07 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul01portstate07_Type.__name__ = "Integer32"
_Modul01portstate07_Object = MibScalar
modul01portstate07 = _Modul01portstate07_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 7, 2),
    _Modul01portstate07_Type()
)
modul01portstate07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portstate07.setStatus("mandatory")
_Modul01port08_ObjectIdentity = ObjectIdentity
modul01port08 = _Modul01port08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 8)
)
_Modul01portname08_Type = DisplayString
_Modul01portname08_Object = MibScalar
modul01portname08 = _Modul01portname08_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 8, 1),
    _Modul01portname08_Type()
)
modul01portname08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portname08.setStatus("mandatory")


class _Modul01portstate08_Type(Integer32):
    """Custom type modul01portstate08 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul01portstate08_Type.__name__ = "Integer32"
_Modul01portstate08_Object = MibScalar
modul01portstate08 = _Modul01portstate08_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 8, 2),
    _Modul01portstate08_Type()
)
modul01portstate08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portstate08.setStatus("mandatory")
_Modul01port09_ObjectIdentity = ObjectIdentity
modul01port09 = _Modul01port09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 9)
)
_Modul01portname09_Type = DisplayString
_Modul01portname09_Object = MibScalar
modul01portname09 = _Modul01portname09_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 9, 1),
    _Modul01portname09_Type()
)
modul01portname09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portname09.setStatus("mandatory")


class _Modul01portstate09_Type(Integer32):
    """Custom type modul01portstate09 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul01portstate09_Type.__name__ = "Integer32"
_Modul01portstate09_Object = MibScalar
modul01portstate09 = _Modul01portstate09_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 9, 2),
    _Modul01portstate09_Type()
)
modul01portstate09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portstate09.setStatus("mandatory")
_Modul01port10_ObjectIdentity = ObjectIdentity
modul01port10 = _Modul01port10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 10)
)
_Modul01portname10_Type = DisplayString
_Modul01portname10_Object = MibScalar
modul01portname10 = _Modul01portname10_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 10, 1),
    _Modul01portname10_Type()
)
modul01portname10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portname10.setStatus("mandatory")


class _Modul01portstate10_Type(Integer32):
    """Custom type modul01portstate10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul01portstate10_Type.__name__ = "Integer32"
_Modul01portstate10_Object = MibScalar
modul01portstate10 = _Modul01portstate10_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 10, 2),
    _Modul01portstate10_Type()
)
modul01portstate10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portstate10.setStatus("mandatory")
_Modul01port11_ObjectIdentity = ObjectIdentity
modul01port11 = _Modul01port11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 11)
)
_Modul01portname11_Type = DisplayString
_Modul01portname11_Object = MibScalar
modul01portname11 = _Modul01portname11_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 11, 1),
    _Modul01portname11_Type()
)
modul01portname11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portname11.setStatus("mandatory")


class _Modul01portstate11_Type(Integer32):
    """Custom type modul01portstate11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul01portstate11_Type.__name__ = "Integer32"
_Modul01portstate11_Object = MibScalar
modul01portstate11 = _Modul01portstate11_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 11, 2),
    _Modul01portstate11_Type()
)
modul01portstate11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portstate11.setStatus("mandatory")
_Modul01port12_ObjectIdentity = ObjectIdentity
modul01port12 = _Modul01port12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 12)
)
_Modul01portname12_Type = DisplayString
_Modul01portname12_Object = MibScalar
modul01portname12 = _Modul01portname12_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 12, 1),
    _Modul01portname12_Type()
)
modul01portname12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portname12.setStatus("mandatory")


class _Modul01portstate12_Type(Integer32):
    """Custom type modul01portstate12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul01portstate12_Type.__name__ = "Integer32"
_Modul01portstate12_Object = MibScalar
modul01portstate12 = _Modul01portstate12_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 12, 2),
    _Modul01portstate12_Type()
)
modul01portstate12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portstate12.setStatus("mandatory")
_Modul01port13_ObjectIdentity = ObjectIdentity
modul01port13 = _Modul01port13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 13)
)
_Modul01portname13_Type = DisplayString
_Modul01portname13_Object = MibScalar
modul01portname13 = _Modul01portname13_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 13, 1),
    _Modul01portname13_Type()
)
modul01portname13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portname13.setStatus("mandatory")


class _Modul01portstate13_Type(Integer32):
    """Custom type modul01portstate13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul01portstate13_Type.__name__ = "Integer32"
_Modul01portstate13_Object = MibScalar
modul01portstate13 = _Modul01portstate13_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 13, 2),
    _Modul01portstate13_Type()
)
modul01portstate13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portstate13.setStatus("mandatory")
_Modul01port14_ObjectIdentity = ObjectIdentity
modul01port14 = _Modul01port14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 14)
)
_Modul01portname14_Type = DisplayString
_Modul01portname14_Object = MibScalar
modul01portname14 = _Modul01portname14_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 14, 1),
    _Modul01portname14_Type()
)
modul01portname14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portname14.setStatus("mandatory")


class _Modul01portstate14_Type(Integer32):
    """Custom type modul01portstate14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul01portstate14_Type.__name__ = "Integer32"
_Modul01portstate14_Object = MibScalar
modul01portstate14 = _Modul01portstate14_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 14, 2),
    _Modul01portstate14_Type()
)
modul01portstate14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portstate14.setStatus("mandatory")
_Modul01port15_ObjectIdentity = ObjectIdentity
modul01port15 = _Modul01port15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 15)
)
_Modul01portname15_Type = DisplayString
_Modul01portname15_Object = MibScalar
modul01portname15 = _Modul01portname15_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 15, 1),
    _Modul01portname15_Type()
)
modul01portname15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portname15.setStatus("mandatory")


class _Modul01portstate15_Type(Integer32):
    """Custom type modul01portstate15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul01portstate15_Type.__name__ = "Integer32"
_Modul01portstate15_Object = MibScalar
modul01portstate15 = _Modul01portstate15_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 15, 2),
    _Modul01portstate15_Type()
)
modul01portstate15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portstate15.setStatus("mandatory")
_Modul01port16_ObjectIdentity = ObjectIdentity
modul01port16 = _Modul01port16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 16)
)
_Modul01portname16_Type = DisplayString
_Modul01portname16_Object = MibScalar
modul01portname16 = _Modul01portname16_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 16, 1),
    _Modul01portname16_Type()
)
modul01portname16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portname16.setStatus("mandatory")


class _Modul01portstate16_Type(Integer32):
    """Custom type modul01portstate16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul01portstate16_Type.__name__ = "Integer32"
_Modul01portstate16_Object = MibScalar
modul01portstate16 = _Modul01portstate16_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 16, 2),
    _Modul01portstate16_Type()
)
modul01portstate16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul01portstate16.setStatus("mandatory")
_Modul02port01_ObjectIdentity = ObjectIdentity
modul02port01 = _Modul02port01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 17)
)
_Modul02portname01_Type = DisplayString
_Modul02portname01_Object = MibScalar
modul02portname01 = _Modul02portname01_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 17, 1),
    _Modul02portname01_Type()
)
modul02portname01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portname01.setStatus("mandatory")


class _Modul02portstate01_Type(Integer32):
    """Custom type modul02portstate01 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul02portstate01_Type.__name__ = "Integer32"
_Modul02portstate01_Object = MibScalar
modul02portstate01 = _Modul02portstate01_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 17, 2),
    _Modul02portstate01_Type()
)
modul02portstate01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portstate01.setStatus("mandatory")
_Modul02port02_ObjectIdentity = ObjectIdentity
modul02port02 = _Modul02port02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 18)
)
_Modul02portname02_Type = DisplayString
_Modul02portname02_Object = MibScalar
modul02portname02 = _Modul02portname02_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 18, 1),
    _Modul02portname02_Type()
)
modul02portname02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portname02.setStatus("mandatory")


class _Modul02portstate02_Type(Integer32):
    """Custom type modul02portstate02 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul02portstate02_Type.__name__ = "Integer32"
_Modul02portstate02_Object = MibScalar
modul02portstate02 = _Modul02portstate02_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 18, 2),
    _Modul02portstate02_Type()
)
modul02portstate02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portstate02.setStatus("mandatory")
_Modul02port03_ObjectIdentity = ObjectIdentity
modul02port03 = _Modul02port03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 19)
)
_Modul02portname03_Type = DisplayString
_Modul02portname03_Object = MibScalar
modul02portname03 = _Modul02portname03_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 19, 1),
    _Modul02portname03_Type()
)
modul02portname03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portname03.setStatus("mandatory")


class _Modul02portstate03_Type(Integer32):
    """Custom type modul02portstate03 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul02portstate03_Type.__name__ = "Integer32"
_Modul02portstate03_Object = MibScalar
modul02portstate03 = _Modul02portstate03_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 19, 2),
    _Modul02portstate03_Type()
)
modul02portstate03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portstate03.setStatus("mandatory")
_Modul02port04_ObjectIdentity = ObjectIdentity
modul02port04 = _Modul02port04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 20)
)
_Modul02portname04_Type = DisplayString
_Modul02portname04_Object = MibScalar
modul02portname04 = _Modul02portname04_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 20, 1),
    _Modul02portname04_Type()
)
modul02portname04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portname04.setStatus("mandatory")


class _Modul02portstate04_Type(Integer32):
    """Custom type modul02portstate04 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul02portstate04_Type.__name__ = "Integer32"
_Modul02portstate04_Object = MibScalar
modul02portstate04 = _Modul02portstate04_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 20, 2),
    _Modul02portstate04_Type()
)
modul02portstate04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portstate04.setStatus("mandatory")
_Modul02port05_ObjectIdentity = ObjectIdentity
modul02port05 = _Modul02port05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 21)
)
_Modul02portname05_Type = DisplayString
_Modul02portname05_Object = MibScalar
modul02portname05 = _Modul02portname05_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 21, 1),
    _Modul02portname05_Type()
)
modul02portname05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portname05.setStatus("mandatory")


class _Modul02portstate05_Type(Integer32):
    """Custom type modul02portstate05 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul02portstate05_Type.__name__ = "Integer32"
_Modul02portstate05_Object = MibScalar
modul02portstate05 = _Modul02portstate05_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 21, 2),
    _Modul02portstate05_Type()
)
modul02portstate05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portstate05.setStatus("mandatory")
_Modul02port06_ObjectIdentity = ObjectIdentity
modul02port06 = _Modul02port06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 22)
)
_Modul02portname06_Type = DisplayString
_Modul02portname06_Object = MibScalar
modul02portname06 = _Modul02portname06_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 22, 1),
    _Modul02portname06_Type()
)
modul02portname06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portname06.setStatus("mandatory")


class _Modul02portstate06_Type(Integer32):
    """Custom type modul02portstate06 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul02portstate06_Type.__name__ = "Integer32"
_Modul02portstate06_Object = MibScalar
modul02portstate06 = _Modul02portstate06_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 22, 2),
    _Modul02portstate06_Type()
)
modul02portstate06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portstate06.setStatus("mandatory")
_Modul02port07_ObjectIdentity = ObjectIdentity
modul02port07 = _Modul02port07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 23)
)
_Modul02portname07_Type = DisplayString
_Modul02portname07_Object = MibScalar
modul02portname07 = _Modul02portname07_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 23, 1),
    _Modul02portname07_Type()
)
modul02portname07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portname07.setStatus("mandatory")


class _Modul02portstate07_Type(Integer32):
    """Custom type modul02portstate07 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul02portstate07_Type.__name__ = "Integer32"
_Modul02portstate07_Object = MibScalar
modul02portstate07 = _Modul02portstate07_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 23, 2),
    _Modul02portstate07_Type()
)
modul02portstate07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portstate07.setStatus("mandatory")
_Modul02port08_ObjectIdentity = ObjectIdentity
modul02port08 = _Modul02port08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 24)
)
_Modul02portname08_Type = DisplayString
_Modul02portname08_Object = MibScalar
modul02portname08 = _Modul02portname08_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 24, 1),
    _Modul02portname08_Type()
)
modul02portname08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portname08.setStatus("mandatory")


class _Modul02portstate08_Type(Integer32):
    """Custom type modul02portstate08 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul02portstate08_Type.__name__ = "Integer32"
_Modul02portstate08_Object = MibScalar
modul02portstate08 = _Modul02portstate08_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 24, 2),
    _Modul02portstate08_Type()
)
modul02portstate08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portstate08.setStatus("mandatory")
_Modul02port09_ObjectIdentity = ObjectIdentity
modul02port09 = _Modul02port09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 25)
)
_Modul02portname09_Type = DisplayString
_Modul02portname09_Object = MibScalar
modul02portname09 = _Modul02portname09_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 25, 1),
    _Modul02portname09_Type()
)
modul02portname09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portname09.setStatus("mandatory")


class _Modul02portstate09_Type(Integer32):
    """Custom type modul02portstate09 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul02portstate09_Type.__name__ = "Integer32"
_Modul02portstate09_Object = MibScalar
modul02portstate09 = _Modul02portstate09_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 25, 2),
    _Modul02portstate09_Type()
)
modul02portstate09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portstate09.setStatus("mandatory")
_Modul02port10_ObjectIdentity = ObjectIdentity
modul02port10 = _Modul02port10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 26)
)
_Modul02portname10_Type = DisplayString
_Modul02portname10_Object = MibScalar
modul02portname10 = _Modul02portname10_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 26, 1),
    _Modul02portname10_Type()
)
modul02portname10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portname10.setStatus("mandatory")


class _Modul02portstate10_Type(Integer32):
    """Custom type modul02portstate10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul02portstate10_Type.__name__ = "Integer32"
_Modul02portstate10_Object = MibScalar
modul02portstate10 = _Modul02portstate10_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 26, 2),
    _Modul02portstate10_Type()
)
modul02portstate10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portstate10.setStatus("mandatory")
_Modul02port11_ObjectIdentity = ObjectIdentity
modul02port11 = _Modul02port11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 27)
)
_Modul02portname11_Type = DisplayString
_Modul02portname11_Object = MibScalar
modul02portname11 = _Modul02portname11_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 27, 1),
    _Modul02portname11_Type()
)
modul02portname11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portname11.setStatus("mandatory")


class _Modul02portstate11_Type(Integer32):
    """Custom type modul02portstate11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul02portstate11_Type.__name__ = "Integer32"
_Modul02portstate11_Object = MibScalar
modul02portstate11 = _Modul02portstate11_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 27, 2),
    _Modul02portstate11_Type()
)
modul02portstate11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portstate11.setStatus("mandatory")
_Modul02port12_ObjectIdentity = ObjectIdentity
modul02port12 = _Modul02port12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 28)
)
_Modul02portname12_Type = DisplayString
_Modul02portname12_Object = MibScalar
modul02portname12 = _Modul02portname12_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 28, 1),
    _Modul02portname12_Type()
)
modul02portname12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portname12.setStatus("mandatory")


class _Modul02portstate12_Type(Integer32):
    """Custom type modul02portstate12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul02portstate12_Type.__name__ = "Integer32"
_Modul02portstate12_Object = MibScalar
modul02portstate12 = _Modul02portstate12_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 28, 2),
    _Modul02portstate12_Type()
)
modul02portstate12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portstate12.setStatus("mandatory")
_Modul02port13_ObjectIdentity = ObjectIdentity
modul02port13 = _Modul02port13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 29)
)
_Modul02portname13_Type = DisplayString
_Modul02portname13_Object = MibScalar
modul02portname13 = _Modul02portname13_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 29, 1),
    _Modul02portname13_Type()
)
modul02portname13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portname13.setStatus("mandatory")


class _Modul02portstate13_Type(Integer32):
    """Custom type modul02portstate13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul02portstate13_Type.__name__ = "Integer32"
_Modul02portstate13_Object = MibScalar
modul02portstate13 = _Modul02portstate13_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 29, 2),
    _Modul02portstate13_Type()
)
modul02portstate13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portstate13.setStatus("mandatory")
_Modul02port14_ObjectIdentity = ObjectIdentity
modul02port14 = _Modul02port14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 30)
)
_Modul02portname14_Type = DisplayString
_Modul02portname14_Object = MibScalar
modul02portname14 = _Modul02portname14_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 30, 1),
    _Modul02portname14_Type()
)
modul02portname14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portname14.setStatus("mandatory")


class _Modul02portstate14_Type(Integer32):
    """Custom type modul02portstate14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul02portstate14_Type.__name__ = "Integer32"
_Modul02portstate14_Object = MibScalar
modul02portstate14 = _Modul02portstate14_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 30, 2),
    _Modul02portstate14_Type()
)
modul02portstate14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portstate14.setStatus("mandatory")
_Modul02port15_ObjectIdentity = ObjectIdentity
modul02port15 = _Modul02port15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 31)
)
_Modul02portname15_Type = DisplayString
_Modul02portname15_Object = MibScalar
modul02portname15 = _Modul02portname15_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 31, 1),
    _Modul02portname15_Type()
)
modul02portname15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portname15.setStatus("mandatory")


class _Modul02portstate15_Type(Integer32):
    """Custom type modul02portstate15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul02portstate15_Type.__name__ = "Integer32"
_Modul02portstate15_Object = MibScalar
modul02portstate15 = _Modul02portstate15_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 31, 2),
    _Modul02portstate15_Type()
)
modul02portstate15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portstate15.setStatus("mandatory")
_Modul02port16_ObjectIdentity = ObjectIdentity
modul02port16 = _Modul02port16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 32)
)
_Modul02portname16_Type = DisplayString
_Modul02portname16_Object = MibScalar
modul02portname16 = _Modul02portname16_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 32, 1),
    _Modul02portname16_Type()
)
modul02portname16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portname16.setStatus("mandatory")


class _Modul02portstate16_Type(Integer32):
    """Custom type modul02portstate16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul02portstate16_Type.__name__ = "Integer32"
_Modul02portstate16_Object = MibScalar
modul02portstate16 = _Modul02portstate16_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 32, 2),
    _Modul02portstate16_Type()
)
modul02portstate16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul02portstate16.setStatus("mandatory")
_Modul03port01_ObjectIdentity = ObjectIdentity
modul03port01 = _Modul03port01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 33)
)
_Modul03portname01_Type = DisplayString
_Modul03portname01_Object = MibScalar
modul03portname01 = _Modul03portname01_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 33, 1),
    _Modul03portname01_Type()
)
modul03portname01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portname01.setStatus("mandatory")


class _Modul03portstate01_Type(Integer32):
    """Custom type modul03portstate01 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul03portstate01_Type.__name__ = "Integer32"
_Modul03portstate01_Object = MibScalar
modul03portstate01 = _Modul03portstate01_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 33, 2),
    _Modul03portstate01_Type()
)
modul03portstate01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portstate01.setStatus("mandatory")
_Modul03port02_ObjectIdentity = ObjectIdentity
modul03port02 = _Modul03port02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 34)
)
_Modul03portname02_Type = DisplayString
_Modul03portname02_Object = MibScalar
modul03portname02 = _Modul03portname02_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 34, 1),
    _Modul03portname02_Type()
)
modul03portname02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portname02.setStatus("mandatory")


class _Modul03portstate02_Type(Integer32):
    """Custom type modul03portstate02 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul03portstate02_Type.__name__ = "Integer32"
_Modul03portstate02_Object = MibScalar
modul03portstate02 = _Modul03portstate02_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 34, 2),
    _Modul03portstate02_Type()
)
modul03portstate02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portstate02.setStatus("mandatory")
_Modul03port03_ObjectIdentity = ObjectIdentity
modul03port03 = _Modul03port03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 35)
)
_Modul03portname03_Type = DisplayString
_Modul03portname03_Object = MibScalar
modul03portname03 = _Modul03portname03_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 35, 1),
    _Modul03portname03_Type()
)
modul03portname03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portname03.setStatus("mandatory")


class _Modul03portstate03_Type(Integer32):
    """Custom type modul03portstate03 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul03portstate03_Type.__name__ = "Integer32"
_Modul03portstate03_Object = MibScalar
modul03portstate03 = _Modul03portstate03_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 35, 2),
    _Modul03portstate03_Type()
)
modul03portstate03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portstate03.setStatus("mandatory")
_Modul03port04_ObjectIdentity = ObjectIdentity
modul03port04 = _Modul03port04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 36)
)
_Modul03portname04_Type = DisplayString
_Modul03portname04_Object = MibScalar
modul03portname04 = _Modul03portname04_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 36, 1),
    _Modul03portname04_Type()
)
modul03portname04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portname04.setStatus("mandatory")


class _Modul03portstate04_Type(Integer32):
    """Custom type modul03portstate04 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul03portstate04_Type.__name__ = "Integer32"
_Modul03portstate04_Object = MibScalar
modul03portstate04 = _Modul03portstate04_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 36, 2),
    _Modul03portstate04_Type()
)
modul03portstate04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portstate04.setStatus("mandatory")
_Modul03port05_ObjectIdentity = ObjectIdentity
modul03port05 = _Modul03port05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 37)
)
_Modul03portname05_Type = DisplayString
_Modul03portname05_Object = MibScalar
modul03portname05 = _Modul03portname05_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 37, 1),
    _Modul03portname05_Type()
)
modul03portname05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portname05.setStatus("mandatory")


class _Modul03portstate05_Type(Integer32):
    """Custom type modul03portstate05 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul03portstate05_Type.__name__ = "Integer32"
_Modul03portstate05_Object = MibScalar
modul03portstate05 = _Modul03portstate05_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 37, 2),
    _Modul03portstate05_Type()
)
modul03portstate05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portstate05.setStatus("mandatory")
_Modul03port06_ObjectIdentity = ObjectIdentity
modul03port06 = _Modul03port06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 38)
)
_Modul03portname06_Type = DisplayString
_Modul03portname06_Object = MibScalar
modul03portname06 = _Modul03portname06_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 38, 1),
    _Modul03portname06_Type()
)
modul03portname06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portname06.setStatus("mandatory")


class _Modul03portstate06_Type(Integer32):
    """Custom type modul03portstate06 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul03portstate06_Type.__name__ = "Integer32"
_Modul03portstate06_Object = MibScalar
modul03portstate06 = _Modul03portstate06_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 38, 2),
    _Modul03portstate06_Type()
)
modul03portstate06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portstate06.setStatus("mandatory")
_Modul03port07_ObjectIdentity = ObjectIdentity
modul03port07 = _Modul03port07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 39)
)
_Modul03portname07_Type = DisplayString
_Modul03portname07_Object = MibScalar
modul03portname07 = _Modul03portname07_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 39, 1),
    _Modul03portname07_Type()
)
modul03portname07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portname07.setStatus("mandatory")


class _Modul03portstate07_Type(Integer32):
    """Custom type modul03portstate07 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul03portstate07_Type.__name__ = "Integer32"
_Modul03portstate07_Object = MibScalar
modul03portstate07 = _Modul03portstate07_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 39, 2),
    _Modul03portstate07_Type()
)
modul03portstate07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portstate07.setStatus("mandatory")
_Modul03port08_ObjectIdentity = ObjectIdentity
modul03port08 = _Modul03port08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 40)
)
_Modul03portname08_Type = DisplayString
_Modul03portname08_Object = MibScalar
modul03portname08 = _Modul03portname08_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 40, 1),
    _Modul03portname08_Type()
)
modul03portname08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portname08.setStatus("mandatory")


class _Modul03portstate08_Type(Integer32):
    """Custom type modul03portstate08 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul03portstate08_Type.__name__ = "Integer32"
_Modul03portstate08_Object = MibScalar
modul03portstate08 = _Modul03portstate08_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 40, 2),
    _Modul03portstate08_Type()
)
modul03portstate08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portstate08.setStatus("mandatory")
_Modul03port09_ObjectIdentity = ObjectIdentity
modul03port09 = _Modul03port09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 41)
)
_Modul03portname09_Type = DisplayString
_Modul03portname09_Object = MibScalar
modul03portname09 = _Modul03portname09_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 41, 1),
    _Modul03portname09_Type()
)
modul03portname09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portname09.setStatus("mandatory")


class _Modul03portstate09_Type(Integer32):
    """Custom type modul03portstate09 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul03portstate09_Type.__name__ = "Integer32"
_Modul03portstate09_Object = MibScalar
modul03portstate09 = _Modul03portstate09_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 41, 2),
    _Modul03portstate09_Type()
)
modul03portstate09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portstate09.setStatus("mandatory")
_Modul03port10_ObjectIdentity = ObjectIdentity
modul03port10 = _Modul03port10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 42)
)
_Modul03portname10_Type = DisplayString
_Modul03portname10_Object = MibScalar
modul03portname10 = _Modul03portname10_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 42, 1),
    _Modul03portname10_Type()
)
modul03portname10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portname10.setStatus("mandatory")


class _Modul03portstate10_Type(Integer32):
    """Custom type modul03portstate10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul03portstate10_Type.__name__ = "Integer32"
_Modul03portstate10_Object = MibScalar
modul03portstate10 = _Modul03portstate10_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 42, 2),
    _Modul03portstate10_Type()
)
modul03portstate10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portstate10.setStatus("mandatory")
_Modul03port11_ObjectIdentity = ObjectIdentity
modul03port11 = _Modul03port11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 43)
)
_Modul03portname11_Type = DisplayString
_Modul03portname11_Object = MibScalar
modul03portname11 = _Modul03portname11_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 43, 1),
    _Modul03portname11_Type()
)
modul03portname11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portname11.setStatus("mandatory")


class _Modul03portstate11_Type(Integer32):
    """Custom type modul03portstate11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul03portstate11_Type.__name__ = "Integer32"
_Modul03portstate11_Object = MibScalar
modul03portstate11 = _Modul03portstate11_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 43, 2),
    _Modul03portstate11_Type()
)
modul03portstate11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portstate11.setStatus("mandatory")
_Modul03port12_ObjectIdentity = ObjectIdentity
modul03port12 = _Modul03port12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 44)
)
_Modul03portname12_Type = DisplayString
_Modul03portname12_Object = MibScalar
modul03portname12 = _Modul03portname12_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 44, 1),
    _Modul03portname12_Type()
)
modul03portname12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portname12.setStatus("mandatory")


class _Modul03portstate12_Type(Integer32):
    """Custom type modul03portstate12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul03portstate12_Type.__name__ = "Integer32"
_Modul03portstate12_Object = MibScalar
modul03portstate12 = _Modul03portstate12_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 44, 2),
    _Modul03portstate12_Type()
)
modul03portstate12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portstate12.setStatus("mandatory")
_Modul03port13_ObjectIdentity = ObjectIdentity
modul03port13 = _Modul03port13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 45)
)
_Modul03portname13_Type = DisplayString
_Modul03portname13_Object = MibScalar
modul03portname13 = _Modul03portname13_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 45, 1),
    _Modul03portname13_Type()
)
modul03portname13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portname13.setStatus("mandatory")


class _Modul03portstate13_Type(Integer32):
    """Custom type modul03portstate13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul03portstate13_Type.__name__ = "Integer32"
_Modul03portstate13_Object = MibScalar
modul03portstate13 = _Modul03portstate13_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 45, 2),
    _Modul03portstate13_Type()
)
modul03portstate13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portstate13.setStatus("mandatory")
_Modul03port14_ObjectIdentity = ObjectIdentity
modul03port14 = _Modul03port14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 46)
)
_Modul03portname14_Type = DisplayString
_Modul03portname14_Object = MibScalar
modul03portname14 = _Modul03portname14_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 46, 1),
    _Modul03portname14_Type()
)
modul03portname14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portname14.setStatus("mandatory")


class _Modul03portstate14_Type(Integer32):
    """Custom type modul03portstate14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul03portstate14_Type.__name__ = "Integer32"
_Modul03portstate14_Object = MibScalar
modul03portstate14 = _Modul03portstate14_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 46, 2),
    _Modul03portstate14_Type()
)
modul03portstate14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portstate14.setStatus("mandatory")
_Modul03port15_ObjectIdentity = ObjectIdentity
modul03port15 = _Modul03port15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 47)
)
_Modul03portname15_Type = DisplayString
_Modul03portname15_Object = MibScalar
modul03portname15 = _Modul03portname15_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 47, 1),
    _Modul03portname15_Type()
)
modul03portname15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portname15.setStatus("mandatory")


class _Modul03portstate15_Type(Integer32):
    """Custom type modul03portstate15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul03portstate15_Type.__name__ = "Integer32"
_Modul03portstate15_Object = MibScalar
modul03portstate15 = _Modul03portstate15_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 47, 2),
    _Modul03portstate15_Type()
)
modul03portstate15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portstate15.setStatus("mandatory")
_Modul03port16_ObjectIdentity = ObjectIdentity
modul03port16 = _Modul03port16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 48)
)
_Modul03portname16_Type = DisplayString
_Modul03portname16_Object = MibScalar
modul03portname16 = _Modul03portname16_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 48, 1),
    _Modul03portname16_Type()
)
modul03portname16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portname16.setStatus("mandatory")


class _Modul03portstate16_Type(Integer32):
    """Custom type modul03portstate16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul03portstate16_Type.__name__ = "Integer32"
_Modul03portstate16_Object = MibScalar
modul03portstate16 = _Modul03portstate16_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 48, 2),
    _Modul03portstate16_Type()
)
modul03portstate16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul03portstate16.setStatus("mandatory")
_Modul04port01_ObjectIdentity = ObjectIdentity
modul04port01 = _Modul04port01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 49)
)
_Modul04portname01_Type = DisplayString
_Modul04portname01_Object = MibScalar
modul04portname01 = _Modul04portname01_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 49, 1),
    _Modul04portname01_Type()
)
modul04portname01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portname01.setStatus("mandatory")


class _Modul04portstate01_Type(Integer32):
    """Custom type modul04portstate01 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul04portstate01_Type.__name__ = "Integer32"
_Modul04portstate01_Object = MibScalar
modul04portstate01 = _Modul04portstate01_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 49, 2),
    _Modul04portstate01_Type()
)
modul04portstate01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portstate01.setStatus("mandatory")
_Modul04port02_ObjectIdentity = ObjectIdentity
modul04port02 = _Modul04port02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 50)
)
_Modul04portname02_Type = DisplayString
_Modul04portname02_Object = MibScalar
modul04portname02 = _Modul04portname02_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 50, 1),
    _Modul04portname02_Type()
)
modul04portname02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portname02.setStatus("mandatory")


class _Modul04portstate02_Type(Integer32):
    """Custom type modul04portstate02 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul04portstate02_Type.__name__ = "Integer32"
_Modul04portstate02_Object = MibScalar
modul04portstate02 = _Modul04portstate02_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 50, 2),
    _Modul04portstate02_Type()
)
modul04portstate02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portstate02.setStatus("mandatory")
_Modul04port03_ObjectIdentity = ObjectIdentity
modul04port03 = _Modul04port03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 51)
)
_Modul04portname03_Type = DisplayString
_Modul04portname03_Object = MibScalar
modul04portname03 = _Modul04portname03_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 51, 1),
    _Modul04portname03_Type()
)
modul04portname03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portname03.setStatus("mandatory")


class _Modul04portstate03_Type(Integer32):
    """Custom type modul04portstate03 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul04portstate03_Type.__name__ = "Integer32"
_Modul04portstate03_Object = MibScalar
modul04portstate03 = _Modul04portstate03_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 51, 2),
    _Modul04portstate03_Type()
)
modul04portstate03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portstate03.setStatus("mandatory")
_Modul04port04_ObjectIdentity = ObjectIdentity
modul04port04 = _Modul04port04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 52)
)
_Modul04portname04_Type = DisplayString
_Modul04portname04_Object = MibScalar
modul04portname04 = _Modul04portname04_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 52, 1),
    _Modul04portname04_Type()
)
modul04portname04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portname04.setStatus("mandatory")


class _Modul04portstate04_Type(Integer32):
    """Custom type modul04portstate04 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul04portstate04_Type.__name__ = "Integer32"
_Modul04portstate04_Object = MibScalar
modul04portstate04 = _Modul04portstate04_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 52, 2),
    _Modul04portstate04_Type()
)
modul04portstate04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portstate04.setStatus("mandatory")
_Modul04port05_ObjectIdentity = ObjectIdentity
modul04port05 = _Modul04port05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 53)
)
_Modul04portname05_Type = DisplayString
_Modul04portname05_Object = MibScalar
modul04portname05 = _Modul04portname05_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 53, 1),
    _Modul04portname05_Type()
)
modul04portname05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portname05.setStatus("mandatory")


class _Modul04portstate05_Type(Integer32):
    """Custom type modul04portstate05 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul04portstate05_Type.__name__ = "Integer32"
_Modul04portstate05_Object = MibScalar
modul04portstate05 = _Modul04portstate05_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 53, 2),
    _Modul04portstate05_Type()
)
modul04portstate05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portstate05.setStatus("mandatory")
_Modul04port06_ObjectIdentity = ObjectIdentity
modul04port06 = _Modul04port06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 54)
)
_Modul04portname06_Type = DisplayString
_Modul04portname06_Object = MibScalar
modul04portname06 = _Modul04portname06_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 54, 1),
    _Modul04portname06_Type()
)
modul04portname06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portname06.setStatus("mandatory")


class _Modul04portstate06_Type(Integer32):
    """Custom type modul04portstate06 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul04portstate06_Type.__name__ = "Integer32"
_Modul04portstate06_Object = MibScalar
modul04portstate06 = _Modul04portstate06_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 54, 2),
    _Modul04portstate06_Type()
)
modul04portstate06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portstate06.setStatus("mandatory")
_Modul04port07_ObjectIdentity = ObjectIdentity
modul04port07 = _Modul04port07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 55)
)
_Modul04portname07_Type = DisplayString
_Modul04portname07_Object = MibScalar
modul04portname07 = _Modul04portname07_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 55, 1),
    _Modul04portname07_Type()
)
modul04portname07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portname07.setStatus("mandatory")


class _Modul04portstate07_Type(Integer32):
    """Custom type modul04portstate07 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul04portstate07_Type.__name__ = "Integer32"
_Modul04portstate07_Object = MibScalar
modul04portstate07 = _Modul04portstate07_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 55, 2),
    _Modul04portstate07_Type()
)
modul04portstate07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portstate07.setStatus("mandatory")
_Modul04port08_ObjectIdentity = ObjectIdentity
modul04port08 = _Modul04port08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 56)
)
_Modul04portname08_Type = DisplayString
_Modul04portname08_Object = MibScalar
modul04portname08 = _Modul04portname08_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 56, 1),
    _Modul04portname08_Type()
)
modul04portname08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portname08.setStatus("mandatory")


class _Modul04portstate08_Type(Integer32):
    """Custom type modul04portstate08 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul04portstate08_Type.__name__ = "Integer32"
_Modul04portstate08_Object = MibScalar
modul04portstate08 = _Modul04portstate08_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 56, 2),
    _Modul04portstate08_Type()
)
modul04portstate08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portstate08.setStatus("mandatory")
_Modul04port09_ObjectIdentity = ObjectIdentity
modul04port09 = _Modul04port09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 57)
)
_Modul04portname09_Type = DisplayString
_Modul04portname09_Object = MibScalar
modul04portname09 = _Modul04portname09_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 57, 1),
    _Modul04portname09_Type()
)
modul04portname09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portname09.setStatus("mandatory")


class _Modul04portstate09_Type(Integer32):
    """Custom type modul04portstate09 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul04portstate09_Type.__name__ = "Integer32"
_Modul04portstate09_Object = MibScalar
modul04portstate09 = _Modul04portstate09_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 57, 2),
    _Modul04portstate09_Type()
)
modul04portstate09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portstate09.setStatus("mandatory")
_Modul04port10_ObjectIdentity = ObjectIdentity
modul04port10 = _Modul04port10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 58)
)
_Modul04portname10_Type = DisplayString
_Modul04portname10_Object = MibScalar
modul04portname10 = _Modul04portname10_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 58, 1),
    _Modul04portname10_Type()
)
modul04portname10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portname10.setStatus("mandatory")


class _Modul04portstate10_Type(Integer32):
    """Custom type modul04portstate10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul04portstate10_Type.__name__ = "Integer32"
_Modul04portstate10_Object = MibScalar
modul04portstate10 = _Modul04portstate10_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 58, 2),
    _Modul04portstate10_Type()
)
modul04portstate10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portstate10.setStatus("mandatory")
_Modul04port11_ObjectIdentity = ObjectIdentity
modul04port11 = _Modul04port11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 59)
)
_Modul04portname11_Type = DisplayString
_Modul04portname11_Object = MibScalar
modul04portname11 = _Modul04portname11_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 59, 1),
    _Modul04portname11_Type()
)
modul04portname11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portname11.setStatus("mandatory")


class _Modul04portstate11_Type(Integer32):
    """Custom type modul04portstate11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul04portstate11_Type.__name__ = "Integer32"
_Modul04portstate11_Object = MibScalar
modul04portstate11 = _Modul04portstate11_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 59, 2),
    _Modul04portstate11_Type()
)
modul04portstate11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portstate11.setStatus("mandatory")
_Modul04port12_ObjectIdentity = ObjectIdentity
modul04port12 = _Modul04port12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 60)
)
_Modul04portname12_Type = DisplayString
_Modul04portname12_Object = MibScalar
modul04portname12 = _Modul04portname12_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 60, 1),
    _Modul04portname12_Type()
)
modul04portname12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portname12.setStatus("mandatory")


class _Modul04portstate12_Type(Integer32):
    """Custom type modul04portstate12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul04portstate12_Type.__name__ = "Integer32"
_Modul04portstate12_Object = MibScalar
modul04portstate12 = _Modul04portstate12_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 60, 2),
    _Modul04portstate12_Type()
)
modul04portstate12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portstate12.setStatus("mandatory")
_Modul04port13_ObjectIdentity = ObjectIdentity
modul04port13 = _Modul04port13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 61)
)
_Modul04portname13_Type = DisplayString
_Modul04portname13_Object = MibScalar
modul04portname13 = _Modul04portname13_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 61, 1),
    _Modul04portname13_Type()
)
modul04portname13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portname13.setStatus("mandatory")


class _Modul04portstate13_Type(Integer32):
    """Custom type modul04portstate13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul04portstate13_Type.__name__ = "Integer32"
_Modul04portstate13_Object = MibScalar
modul04portstate13 = _Modul04portstate13_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 61, 2),
    _Modul04portstate13_Type()
)
modul04portstate13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portstate13.setStatus("mandatory")
_Modul04port14_ObjectIdentity = ObjectIdentity
modul04port14 = _Modul04port14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 62)
)
_Modul04portname14_Type = DisplayString
_Modul04portname14_Object = MibScalar
modul04portname14 = _Modul04portname14_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 62, 1),
    _Modul04portname14_Type()
)
modul04portname14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portname14.setStatus("mandatory")


class _Modul04portstate14_Type(Integer32):
    """Custom type modul04portstate14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul04portstate14_Type.__name__ = "Integer32"
_Modul04portstate14_Object = MibScalar
modul04portstate14 = _Modul04portstate14_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 62, 2),
    _Modul04portstate14_Type()
)
modul04portstate14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portstate14.setStatus("mandatory")
_Modul04port15_ObjectIdentity = ObjectIdentity
modul04port15 = _Modul04port15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 63)
)
_Modul04portname15_Type = DisplayString
_Modul04portname15_Object = MibScalar
modul04portname15 = _Modul04portname15_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 63, 1),
    _Modul04portname15_Type()
)
modul04portname15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portname15.setStatus("mandatory")


class _Modul04portstate15_Type(Integer32):
    """Custom type modul04portstate15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul04portstate15_Type.__name__ = "Integer32"
_Modul04portstate15_Object = MibScalar
modul04portstate15 = _Modul04portstate15_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 63, 2),
    _Modul04portstate15_Type()
)
modul04portstate15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portstate15.setStatus("mandatory")
_Modul04port16_ObjectIdentity = ObjectIdentity
modul04port16 = _Modul04port16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 64)
)
_Modul04portname16_Type = DisplayString
_Modul04portname16_Object = MibScalar
modul04portname16 = _Modul04portname16_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 64, 1),
    _Modul04portname16_Type()
)
modul04portname16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portname16.setStatus("mandatory")


class _Modul04portstate16_Type(Integer32):
    """Custom type modul04portstate16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul04portstate16_Type.__name__ = "Integer32"
_Modul04portstate16_Object = MibScalar
modul04portstate16 = _Modul04portstate16_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 64, 2),
    _Modul04portstate16_Type()
)
modul04portstate16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul04portstate16.setStatus("mandatory")
_Modul05port01_ObjectIdentity = ObjectIdentity
modul05port01 = _Modul05port01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 65)
)
_Modul05portname01_Type = DisplayString
_Modul05portname01_Object = MibScalar
modul05portname01 = _Modul05portname01_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 65, 1),
    _Modul05portname01_Type()
)
modul05portname01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portname01.setStatus("mandatory")


class _Modul05portstate01_Type(Integer32):
    """Custom type modul05portstate01 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul05portstate01_Type.__name__ = "Integer32"
_Modul05portstate01_Object = MibScalar
modul05portstate01 = _Modul05portstate01_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 65, 2),
    _Modul05portstate01_Type()
)
modul05portstate01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portstate01.setStatus("mandatory")
_Modul05port02_ObjectIdentity = ObjectIdentity
modul05port02 = _Modul05port02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 66)
)
_Modul05portname02_Type = DisplayString
_Modul05portname02_Object = MibScalar
modul05portname02 = _Modul05portname02_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 66, 1),
    _Modul05portname02_Type()
)
modul05portname02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portname02.setStatus("mandatory")


class _Modul05portstate02_Type(Integer32):
    """Custom type modul05portstate02 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul05portstate02_Type.__name__ = "Integer32"
_Modul05portstate02_Object = MibScalar
modul05portstate02 = _Modul05portstate02_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 66, 2),
    _Modul05portstate02_Type()
)
modul05portstate02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portstate02.setStatus("mandatory")
_Modul05port03_ObjectIdentity = ObjectIdentity
modul05port03 = _Modul05port03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 67)
)
_Modul05portname03_Type = DisplayString
_Modul05portname03_Object = MibScalar
modul05portname03 = _Modul05portname03_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 67, 1),
    _Modul05portname03_Type()
)
modul05portname03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portname03.setStatus("mandatory")


class _Modul05portstate03_Type(Integer32):
    """Custom type modul05portstate03 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul05portstate03_Type.__name__ = "Integer32"
_Modul05portstate03_Object = MibScalar
modul05portstate03 = _Modul05portstate03_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 67, 2),
    _Modul05portstate03_Type()
)
modul05portstate03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portstate03.setStatus("mandatory")
_Modul05port04_ObjectIdentity = ObjectIdentity
modul05port04 = _Modul05port04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 68)
)
_Modul05portname04_Type = DisplayString
_Modul05portname04_Object = MibScalar
modul05portname04 = _Modul05portname04_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 68, 1),
    _Modul05portname04_Type()
)
modul05portname04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portname04.setStatus("mandatory")


class _Modul05portstate04_Type(Integer32):
    """Custom type modul05portstate04 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul05portstate04_Type.__name__ = "Integer32"
_Modul05portstate04_Object = MibScalar
modul05portstate04 = _Modul05portstate04_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 68, 2),
    _Modul05portstate04_Type()
)
modul05portstate04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portstate04.setStatus("mandatory")
_Modul05port05_ObjectIdentity = ObjectIdentity
modul05port05 = _Modul05port05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 69)
)
_Modul05portname05_Type = DisplayString
_Modul05portname05_Object = MibScalar
modul05portname05 = _Modul05portname05_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 69, 1),
    _Modul05portname05_Type()
)
modul05portname05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portname05.setStatus("mandatory")


class _Modul05portstate05_Type(Integer32):
    """Custom type modul05portstate05 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul05portstate05_Type.__name__ = "Integer32"
_Modul05portstate05_Object = MibScalar
modul05portstate05 = _Modul05portstate05_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 69, 2),
    _Modul05portstate05_Type()
)
modul05portstate05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portstate05.setStatus("mandatory")
_Modul05port06_ObjectIdentity = ObjectIdentity
modul05port06 = _Modul05port06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 70)
)
_Modul05portname06_Type = DisplayString
_Modul05portname06_Object = MibScalar
modul05portname06 = _Modul05portname06_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 70, 1),
    _Modul05portname06_Type()
)
modul05portname06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portname06.setStatus("mandatory")


class _Modul05portstate06_Type(Integer32):
    """Custom type modul05portstate06 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul05portstate06_Type.__name__ = "Integer32"
_Modul05portstate06_Object = MibScalar
modul05portstate06 = _Modul05portstate06_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 70, 2),
    _Modul05portstate06_Type()
)
modul05portstate06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portstate06.setStatus("mandatory")
_Modul05port07_ObjectIdentity = ObjectIdentity
modul05port07 = _Modul05port07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 71)
)
_Modul05portname07_Type = DisplayString
_Modul05portname07_Object = MibScalar
modul05portname07 = _Modul05portname07_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 71, 1),
    _Modul05portname07_Type()
)
modul05portname07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portname07.setStatus("mandatory")


class _Modul05portstate07_Type(Integer32):
    """Custom type modul05portstate07 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul05portstate07_Type.__name__ = "Integer32"
_Modul05portstate07_Object = MibScalar
modul05portstate07 = _Modul05portstate07_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 71, 2),
    _Modul05portstate07_Type()
)
modul05portstate07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portstate07.setStatus("mandatory")
_Modul05port08_ObjectIdentity = ObjectIdentity
modul05port08 = _Modul05port08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 72)
)
_Modul05portname08_Type = DisplayString
_Modul05portname08_Object = MibScalar
modul05portname08 = _Modul05portname08_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 72, 1),
    _Modul05portname08_Type()
)
modul05portname08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portname08.setStatus("mandatory")


class _Modul05portstate08_Type(Integer32):
    """Custom type modul05portstate08 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul05portstate08_Type.__name__ = "Integer32"
_Modul05portstate08_Object = MibScalar
modul05portstate08 = _Modul05portstate08_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 72, 2),
    _Modul05portstate08_Type()
)
modul05portstate08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portstate08.setStatus("mandatory")
_Modul05port09_ObjectIdentity = ObjectIdentity
modul05port09 = _Modul05port09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 73)
)
_Modul05portname09_Type = DisplayString
_Modul05portname09_Object = MibScalar
modul05portname09 = _Modul05portname09_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 73, 1),
    _Modul05portname09_Type()
)
modul05portname09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portname09.setStatus("mandatory")


class _Modul05portstate09_Type(Integer32):
    """Custom type modul05portstate09 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul05portstate09_Type.__name__ = "Integer32"
_Modul05portstate09_Object = MibScalar
modul05portstate09 = _Modul05portstate09_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 73, 2),
    _Modul05portstate09_Type()
)
modul05portstate09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portstate09.setStatus("mandatory")
_Modul05port10_ObjectIdentity = ObjectIdentity
modul05port10 = _Modul05port10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 74)
)
_Modul05portname10_Type = DisplayString
_Modul05portname10_Object = MibScalar
modul05portname10 = _Modul05portname10_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 74, 1),
    _Modul05portname10_Type()
)
modul05portname10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portname10.setStatus("mandatory")


class _Modul05portstate10_Type(Integer32):
    """Custom type modul05portstate10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul05portstate10_Type.__name__ = "Integer32"
_Modul05portstate10_Object = MibScalar
modul05portstate10 = _Modul05portstate10_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 74, 2),
    _Modul05portstate10_Type()
)
modul05portstate10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portstate10.setStatus("mandatory")
_Modul05port11_ObjectIdentity = ObjectIdentity
modul05port11 = _Modul05port11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 75)
)
_Modul05portname11_Type = DisplayString
_Modul05portname11_Object = MibScalar
modul05portname11 = _Modul05portname11_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 75, 1),
    _Modul05portname11_Type()
)
modul05portname11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portname11.setStatus("mandatory")


class _Modul05portstate11_Type(Integer32):
    """Custom type modul05portstate11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul05portstate11_Type.__name__ = "Integer32"
_Modul05portstate11_Object = MibScalar
modul05portstate11 = _Modul05portstate11_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 75, 2),
    _Modul05portstate11_Type()
)
modul05portstate11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portstate11.setStatus("mandatory")
_Modul05port12_ObjectIdentity = ObjectIdentity
modul05port12 = _Modul05port12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 76)
)
_Modul05portname12_Type = DisplayString
_Modul05portname12_Object = MibScalar
modul05portname12 = _Modul05portname12_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 76, 1),
    _Modul05portname12_Type()
)
modul05portname12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portname12.setStatus("mandatory")


class _Modul05portstate12_Type(Integer32):
    """Custom type modul05portstate12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul05portstate12_Type.__name__ = "Integer32"
_Modul05portstate12_Object = MibScalar
modul05portstate12 = _Modul05portstate12_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 76, 2),
    _Modul05portstate12_Type()
)
modul05portstate12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portstate12.setStatus("mandatory")
_Modul05port13_ObjectIdentity = ObjectIdentity
modul05port13 = _Modul05port13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 77)
)
_Modul05portname13_Type = DisplayString
_Modul05portname13_Object = MibScalar
modul05portname13 = _Modul05portname13_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 77, 1),
    _Modul05portname13_Type()
)
modul05portname13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portname13.setStatus("mandatory")


class _Modul05portstate13_Type(Integer32):
    """Custom type modul05portstate13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul05portstate13_Type.__name__ = "Integer32"
_Modul05portstate13_Object = MibScalar
modul05portstate13 = _Modul05portstate13_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 77, 2),
    _Modul05portstate13_Type()
)
modul05portstate13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portstate13.setStatus("mandatory")
_Modul05port14_ObjectIdentity = ObjectIdentity
modul05port14 = _Modul05port14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 78)
)
_Modul05portname14_Type = DisplayString
_Modul05portname14_Object = MibScalar
modul05portname14 = _Modul05portname14_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 78, 1),
    _Modul05portname14_Type()
)
modul05portname14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portname14.setStatus("mandatory")


class _Modul05portstate14_Type(Integer32):
    """Custom type modul05portstate14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul05portstate14_Type.__name__ = "Integer32"
_Modul05portstate14_Object = MibScalar
modul05portstate14 = _Modul05portstate14_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 78, 2),
    _Modul05portstate14_Type()
)
modul05portstate14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portstate14.setStatus("mandatory")
_Modul05port15_ObjectIdentity = ObjectIdentity
modul05port15 = _Modul05port15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 79)
)
_Modul05portname15_Type = DisplayString
_Modul05portname15_Object = MibScalar
modul05portname15 = _Modul05portname15_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 79, 1),
    _Modul05portname15_Type()
)
modul05portname15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portname15.setStatus("mandatory")


class _Modul05portstate15_Type(Integer32):
    """Custom type modul05portstate15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul05portstate15_Type.__name__ = "Integer32"
_Modul05portstate15_Object = MibScalar
modul05portstate15 = _Modul05portstate15_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 79, 2),
    _Modul05portstate15_Type()
)
modul05portstate15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portstate15.setStatus("mandatory")
_Modul05port16_ObjectIdentity = ObjectIdentity
modul05port16 = _Modul05port16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 80)
)
_Modul05portname16_Type = DisplayString
_Modul05portname16_Object = MibScalar
modul05portname16 = _Modul05portname16_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 80, 1),
    _Modul05portname16_Type()
)
modul05portname16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portname16.setStatus("mandatory")


class _Modul05portstate16_Type(Integer32):
    """Custom type modul05portstate16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul05portstate16_Type.__name__ = "Integer32"
_Modul05portstate16_Object = MibScalar
modul05portstate16 = _Modul05portstate16_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 80, 2),
    _Modul05portstate16_Type()
)
modul05portstate16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul05portstate16.setStatus("mandatory")
_Modul06port01_ObjectIdentity = ObjectIdentity
modul06port01 = _Modul06port01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 81)
)
_Modul06portname01_Type = DisplayString
_Modul06portname01_Object = MibScalar
modul06portname01 = _Modul06portname01_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 81, 1),
    _Modul06portname01_Type()
)
modul06portname01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portname01.setStatus("mandatory")


class _Modul06portstate01_Type(Integer32):
    """Custom type modul06portstate01 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul06portstate01_Type.__name__ = "Integer32"
_Modul06portstate01_Object = MibScalar
modul06portstate01 = _Modul06portstate01_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 81, 2),
    _Modul06portstate01_Type()
)
modul06portstate01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portstate01.setStatus("mandatory")
_Modul06port02_ObjectIdentity = ObjectIdentity
modul06port02 = _Modul06port02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 82)
)
_Modul06portname02_Type = DisplayString
_Modul06portname02_Object = MibScalar
modul06portname02 = _Modul06portname02_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 82, 1),
    _Modul06portname02_Type()
)
modul06portname02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portname02.setStatus("mandatory")


class _Modul06portstate02_Type(Integer32):
    """Custom type modul06portstate02 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul06portstate02_Type.__name__ = "Integer32"
_Modul06portstate02_Object = MibScalar
modul06portstate02 = _Modul06portstate02_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 82, 2),
    _Modul06portstate02_Type()
)
modul06portstate02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portstate02.setStatus("mandatory")
_Modul06port03_ObjectIdentity = ObjectIdentity
modul06port03 = _Modul06port03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 83)
)
_Modul06portname03_Type = DisplayString
_Modul06portname03_Object = MibScalar
modul06portname03 = _Modul06portname03_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 83, 1),
    _Modul06portname03_Type()
)
modul06portname03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portname03.setStatus("mandatory")


class _Modul06portstate03_Type(Integer32):
    """Custom type modul06portstate03 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul06portstate03_Type.__name__ = "Integer32"
_Modul06portstate03_Object = MibScalar
modul06portstate03 = _Modul06portstate03_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 83, 2),
    _Modul06portstate03_Type()
)
modul06portstate03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portstate03.setStatus("mandatory")
_Modul06port04_ObjectIdentity = ObjectIdentity
modul06port04 = _Modul06port04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 84)
)
_Modul06portname04_Type = DisplayString
_Modul06portname04_Object = MibScalar
modul06portname04 = _Modul06portname04_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 84, 1),
    _Modul06portname04_Type()
)
modul06portname04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portname04.setStatus("mandatory")


class _Modul06portstate04_Type(Integer32):
    """Custom type modul06portstate04 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul06portstate04_Type.__name__ = "Integer32"
_Modul06portstate04_Object = MibScalar
modul06portstate04 = _Modul06portstate04_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 84, 2),
    _Modul06portstate04_Type()
)
modul06portstate04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portstate04.setStatus("mandatory")
_Modul06port05_ObjectIdentity = ObjectIdentity
modul06port05 = _Modul06port05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 85)
)
_Modul06portname05_Type = DisplayString
_Modul06portname05_Object = MibScalar
modul06portname05 = _Modul06portname05_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 85, 1),
    _Modul06portname05_Type()
)
modul06portname05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portname05.setStatus("mandatory")


class _Modul06portstate05_Type(Integer32):
    """Custom type modul06portstate05 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul06portstate05_Type.__name__ = "Integer32"
_Modul06portstate05_Object = MibScalar
modul06portstate05 = _Modul06portstate05_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 85, 2),
    _Modul06portstate05_Type()
)
modul06portstate05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portstate05.setStatus("mandatory")
_Modul06port06_ObjectIdentity = ObjectIdentity
modul06port06 = _Modul06port06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 86)
)
_Modul06portname06_Type = DisplayString
_Modul06portname06_Object = MibScalar
modul06portname06 = _Modul06portname06_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 86, 1),
    _Modul06portname06_Type()
)
modul06portname06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portname06.setStatus("mandatory")


class _Modul06portstate06_Type(Integer32):
    """Custom type modul06portstate06 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul06portstate06_Type.__name__ = "Integer32"
_Modul06portstate06_Object = MibScalar
modul06portstate06 = _Modul06portstate06_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 86, 2),
    _Modul06portstate06_Type()
)
modul06portstate06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portstate06.setStatus("mandatory")
_Modul06port07_ObjectIdentity = ObjectIdentity
modul06port07 = _Modul06port07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 87)
)
_Modul06portname07_Type = DisplayString
_Modul06portname07_Object = MibScalar
modul06portname07 = _Modul06portname07_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 87, 1),
    _Modul06portname07_Type()
)
modul06portname07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portname07.setStatus("mandatory")


class _Modul06portstate07_Type(Integer32):
    """Custom type modul06portstate07 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul06portstate07_Type.__name__ = "Integer32"
_Modul06portstate07_Object = MibScalar
modul06portstate07 = _Modul06portstate07_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 87, 2),
    _Modul06portstate07_Type()
)
modul06portstate07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portstate07.setStatus("mandatory")
_Modul06port08_ObjectIdentity = ObjectIdentity
modul06port08 = _Modul06port08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 88)
)
_Modul06portname08_Type = DisplayString
_Modul06portname08_Object = MibScalar
modul06portname08 = _Modul06portname08_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 88, 1),
    _Modul06portname08_Type()
)
modul06portname08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portname08.setStatus("mandatory")


class _Modul06portstate08_Type(Integer32):
    """Custom type modul06portstate08 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul06portstate08_Type.__name__ = "Integer32"
_Modul06portstate08_Object = MibScalar
modul06portstate08 = _Modul06portstate08_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 88, 2),
    _Modul06portstate08_Type()
)
modul06portstate08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portstate08.setStatus("mandatory")
_Modul06port09_ObjectIdentity = ObjectIdentity
modul06port09 = _Modul06port09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 89)
)
_Modul06portname09_Type = DisplayString
_Modul06portname09_Object = MibScalar
modul06portname09 = _Modul06portname09_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 89, 1),
    _Modul06portname09_Type()
)
modul06portname09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portname09.setStatus("mandatory")


class _Modul06portstate09_Type(Integer32):
    """Custom type modul06portstate09 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul06portstate09_Type.__name__ = "Integer32"
_Modul06portstate09_Object = MibScalar
modul06portstate09 = _Modul06portstate09_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 89, 2),
    _Modul06portstate09_Type()
)
modul06portstate09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portstate09.setStatus("mandatory")
_Modul06port10_ObjectIdentity = ObjectIdentity
modul06port10 = _Modul06port10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 90)
)
_Modul06portname10_Type = DisplayString
_Modul06portname10_Object = MibScalar
modul06portname10 = _Modul06portname10_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 90, 1),
    _Modul06portname10_Type()
)
modul06portname10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portname10.setStatus("mandatory")


class _Modul06portstate10_Type(Integer32):
    """Custom type modul06portstate10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul06portstate10_Type.__name__ = "Integer32"
_Modul06portstate10_Object = MibScalar
modul06portstate10 = _Modul06portstate10_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 90, 2),
    _Modul06portstate10_Type()
)
modul06portstate10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portstate10.setStatus("mandatory")
_Modul06port11_ObjectIdentity = ObjectIdentity
modul06port11 = _Modul06port11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 91)
)
_Modul06portname11_Type = DisplayString
_Modul06portname11_Object = MibScalar
modul06portname11 = _Modul06portname11_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 91, 1),
    _Modul06portname11_Type()
)
modul06portname11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portname11.setStatus("mandatory")


class _Modul06portstate11_Type(Integer32):
    """Custom type modul06portstate11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul06portstate11_Type.__name__ = "Integer32"
_Modul06portstate11_Object = MibScalar
modul06portstate11 = _Modul06portstate11_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 91, 2),
    _Modul06portstate11_Type()
)
modul06portstate11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portstate11.setStatus("mandatory")
_Modul06port12_ObjectIdentity = ObjectIdentity
modul06port12 = _Modul06port12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 92)
)
_Modul06portname12_Type = DisplayString
_Modul06portname12_Object = MibScalar
modul06portname12 = _Modul06portname12_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 92, 1),
    _Modul06portname12_Type()
)
modul06portname12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portname12.setStatus("mandatory")


class _Modul06portstate12_Type(Integer32):
    """Custom type modul06portstate12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul06portstate12_Type.__name__ = "Integer32"
_Modul06portstate12_Object = MibScalar
modul06portstate12 = _Modul06portstate12_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 92, 2),
    _Modul06portstate12_Type()
)
modul06portstate12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portstate12.setStatus("mandatory")
_Modul06port13_ObjectIdentity = ObjectIdentity
modul06port13 = _Modul06port13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 93)
)
_Modul06portname13_Type = DisplayString
_Modul06portname13_Object = MibScalar
modul06portname13 = _Modul06portname13_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 93, 1),
    _Modul06portname13_Type()
)
modul06portname13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portname13.setStatus("mandatory")


class _Modul06portstate13_Type(Integer32):
    """Custom type modul06portstate13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul06portstate13_Type.__name__ = "Integer32"
_Modul06portstate13_Object = MibScalar
modul06portstate13 = _Modul06portstate13_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 93, 2),
    _Modul06portstate13_Type()
)
modul06portstate13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portstate13.setStatus("mandatory")
_Modul06port14_ObjectIdentity = ObjectIdentity
modul06port14 = _Modul06port14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 94)
)
_Modul06portname14_Type = DisplayString
_Modul06portname14_Object = MibScalar
modul06portname14 = _Modul06portname14_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 94, 1),
    _Modul06portname14_Type()
)
modul06portname14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portname14.setStatus("mandatory")


class _Modul06portstate14_Type(Integer32):
    """Custom type modul06portstate14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul06portstate14_Type.__name__ = "Integer32"
_Modul06portstate14_Object = MibScalar
modul06portstate14 = _Modul06portstate14_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 94, 2),
    _Modul06portstate14_Type()
)
modul06portstate14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portstate14.setStatus("mandatory")
_Modul06port15_ObjectIdentity = ObjectIdentity
modul06port15 = _Modul06port15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 95)
)
_Modul06portname15_Type = DisplayString
_Modul06portname15_Object = MibScalar
modul06portname15 = _Modul06portname15_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 95, 1),
    _Modul06portname15_Type()
)
modul06portname15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portname15.setStatus("mandatory")


class _Modul06portstate15_Type(Integer32):
    """Custom type modul06portstate15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul06portstate15_Type.__name__ = "Integer32"
_Modul06portstate15_Object = MibScalar
modul06portstate15 = _Modul06portstate15_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 95, 2),
    _Modul06portstate15_Type()
)
modul06portstate15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portstate15.setStatus("mandatory")
_Modul06port16_ObjectIdentity = ObjectIdentity
modul06port16 = _Modul06port16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 96)
)
_Modul06portname16_Type = DisplayString
_Modul06portname16_Object = MibScalar
modul06portname16 = _Modul06portname16_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 96, 1),
    _Modul06portname16_Type()
)
modul06portname16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portname16.setStatus("mandatory")


class _Modul06portstate16_Type(Integer32):
    """Custom type modul06portstate16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Modul06portstate16_Type.__name__ = "Integer32"
_Modul06portstate16_Object = MibScalar
modul06portstate16 = _Modul06portstate16_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 3, 96, 2),
    _Modul06portstate16_Type()
)
modul06portstate16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modul06portstate16.setStatus("mandatory")
_Server_monitoring_ObjectIdentity = ObjectIdentity
server_monitoring = _Server_monitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4)
)
_Server01_ObjectIdentity = ObjectIdentity
server01 = _Server01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 1)
)
_Servername01_Type = DisplayString
_Servername01_Object = MibScalar
servername01 = _Servername01_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 1, 1),
    _Servername01_Type()
)
servername01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servername01.setStatus("mandatory")
_Ip01_Type = DisplayString
_Ip01_Object = MibScalar
ip01 = _Ip01_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 1, 2),
    _Ip01_Type()
)
ip01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip01.setStatus("mandatory")
_Connectionport01_Type = DisplayString
_Connectionport01_Object = MibScalar
connectionport01 = _Connectionport01_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 1, 3),
    _Connectionport01_Type()
)
connectionport01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionport01.setStatus("mandatory")


class _Latency01_Type(Integer32):
    """Custom type latency01 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Latency01_Type.__name__ = "Integer32"
_Latency01_Object = MibScalar
latency01 = _Latency01_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 1, 4),
    _Latency01_Type()
)
latency01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latency01.setStatus("mandatory")


class _Serverstate01_Type(Integer32):
    """Custom type serverstate01 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Serverstate01_Type.__name__ = "Integer32"
_Serverstate01_Object = MibScalar
serverstate01 = _Serverstate01_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 1, 5),
    _Serverstate01_Type()
)
serverstate01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverstate01.setStatus("mandatory")
_Server02_ObjectIdentity = ObjectIdentity
server02 = _Server02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 2)
)
_Servername02_Type = DisplayString
_Servername02_Object = MibScalar
servername02 = _Servername02_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 2, 1),
    _Servername02_Type()
)
servername02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servername02.setStatus("mandatory")
_Ip02_Type = DisplayString
_Ip02_Object = MibScalar
ip02 = _Ip02_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 2, 2),
    _Ip02_Type()
)
ip02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip02.setStatus("mandatory")
_Connectionport02_Type = DisplayString
_Connectionport02_Object = MibScalar
connectionport02 = _Connectionport02_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 2, 3),
    _Connectionport02_Type()
)
connectionport02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionport02.setStatus("mandatory")


class _Latency02_Type(Integer32):
    """Custom type latency02 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Latency02_Type.__name__ = "Integer32"
_Latency02_Object = MibScalar
latency02 = _Latency02_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 2, 4),
    _Latency02_Type()
)
latency02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latency02.setStatus("mandatory")


class _Serverstate02_Type(Integer32):
    """Custom type serverstate02 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Serverstate02_Type.__name__ = "Integer32"
_Serverstate02_Object = MibScalar
serverstate02 = _Serverstate02_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 2, 5),
    _Serverstate02_Type()
)
serverstate02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverstate02.setStatus("mandatory")
_Server03_ObjectIdentity = ObjectIdentity
server03 = _Server03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 3)
)
_Servername03_Type = DisplayString
_Servername03_Object = MibScalar
servername03 = _Servername03_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 3, 1),
    _Servername03_Type()
)
servername03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servername03.setStatus("mandatory")
_Ip03_Type = DisplayString
_Ip03_Object = MibScalar
ip03 = _Ip03_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 3, 2),
    _Ip03_Type()
)
ip03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip03.setStatus("mandatory")
_Connectionport03_Type = DisplayString
_Connectionport03_Object = MibScalar
connectionport03 = _Connectionport03_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 3, 3),
    _Connectionport03_Type()
)
connectionport03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionport03.setStatus("mandatory")


class _Latency03_Type(Integer32):
    """Custom type latency03 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Latency03_Type.__name__ = "Integer32"
_Latency03_Object = MibScalar
latency03 = _Latency03_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 3, 4),
    _Latency03_Type()
)
latency03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latency03.setStatus("mandatory")


class _Serverstate03_Type(Integer32):
    """Custom type serverstate03 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Serverstate03_Type.__name__ = "Integer32"
_Serverstate03_Object = MibScalar
serverstate03 = _Serverstate03_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 3, 5),
    _Serverstate03_Type()
)
serverstate03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverstate03.setStatus("mandatory")
_Server04_ObjectIdentity = ObjectIdentity
server04 = _Server04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 4)
)
_Servername04_Type = DisplayString
_Servername04_Object = MibScalar
servername04 = _Servername04_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 4, 1),
    _Servername04_Type()
)
servername04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servername04.setStatus("mandatory")
_Ip04_Type = DisplayString
_Ip04_Object = MibScalar
ip04 = _Ip04_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 4, 2),
    _Ip04_Type()
)
ip04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip04.setStatus("mandatory")
_Connectionport04_Type = DisplayString
_Connectionport04_Object = MibScalar
connectionport04 = _Connectionport04_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 4, 3),
    _Connectionport04_Type()
)
connectionport04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionport04.setStatus("mandatory")


class _Latency04_Type(Integer32):
    """Custom type latency04 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Latency04_Type.__name__ = "Integer32"
_Latency04_Object = MibScalar
latency04 = _Latency04_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 4, 4),
    _Latency04_Type()
)
latency04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latency04.setStatus("mandatory")


class _Serverstate04_Type(Integer32):
    """Custom type serverstate04 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Serverstate04_Type.__name__ = "Integer32"
_Serverstate04_Object = MibScalar
serverstate04 = _Serverstate04_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 4, 5),
    _Serverstate04_Type()
)
serverstate04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverstate04.setStatus("mandatory")
_Server05_ObjectIdentity = ObjectIdentity
server05 = _Server05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 5)
)
_Servername05_Type = DisplayString
_Servername05_Object = MibScalar
servername05 = _Servername05_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 5, 1),
    _Servername05_Type()
)
servername05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servername05.setStatus("mandatory")
_Ip05_Type = DisplayString
_Ip05_Object = MibScalar
ip05 = _Ip05_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 5, 2),
    _Ip05_Type()
)
ip05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip05.setStatus("mandatory")
_Connectionport05_Type = DisplayString
_Connectionport05_Object = MibScalar
connectionport05 = _Connectionport05_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 5, 3),
    _Connectionport05_Type()
)
connectionport05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionport05.setStatus("mandatory")


class _Latency05_Type(Integer32):
    """Custom type latency05 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Latency05_Type.__name__ = "Integer32"
_Latency05_Object = MibScalar
latency05 = _Latency05_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 5, 4),
    _Latency05_Type()
)
latency05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latency05.setStatus("mandatory")


class _Serverstate05_Type(Integer32):
    """Custom type serverstate05 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Serverstate05_Type.__name__ = "Integer32"
_Serverstate05_Object = MibScalar
serverstate05 = _Serverstate05_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 5, 5),
    _Serverstate05_Type()
)
serverstate05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverstate05.setStatus("mandatory")
_Server06_ObjectIdentity = ObjectIdentity
server06 = _Server06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 6)
)
_Servername06_Type = DisplayString
_Servername06_Object = MibScalar
servername06 = _Servername06_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 6, 1),
    _Servername06_Type()
)
servername06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servername06.setStatus("mandatory")
_Ip06_Type = DisplayString
_Ip06_Object = MibScalar
ip06 = _Ip06_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 6, 2),
    _Ip06_Type()
)
ip06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip06.setStatus("mandatory")
_Connectionport06_Type = DisplayString
_Connectionport06_Object = MibScalar
connectionport06 = _Connectionport06_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 6, 3),
    _Connectionport06_Type()
)
connectionport06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionport06.setStatus("mandatory")


class _Latency06_Type(Integer32):
    """Custom type latency06 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Latency06_Type.__name__ = "Integer32"
_Latency06_Object = MibScalar
latency06 = _Latency06_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 6, 4),
    _Latency06_Type()
)
latency06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latency06.setStatus("mandatory")


class _Serverstate06_Type(Integer32):
    """Custom type serverstate06 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Serverstate06_Type.__name__ = "Integer32"
_Serverstate06_Object = MibScalar
serverstate06 = _Serverstate06_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 6, 5),
    _Serverstate06_Type()
)
serverstate06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverstate06.setStatus("mandatory")
_Server07_ObjectIdentity = ObjectIdentity
server07 = _Server07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 7)
)
_Servername07_Type = DisplayString
_Servername07_Object = MibScalar
servername07 = _Servername07_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 7, 1),
    _Servername07_Type()
)
servername07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servername07.setStatus("mandatory")
_Ip07_Type = DisplayString
_Ip07_Object = MibScalar
ip07 = _Ip07_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 7, 2),
    _Ip07_Type()
)
ip07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip07.setStatus("mandatory")
_Connectionport07_Type = DisplayString
_Connectionport07_Object = MibScalar
connectionport07 = _Connectionport07_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 7, 3),
    _Connectionport07_Type()
)
connectionport07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionport07.setStatus("mandatory")


class _Latency07_Type(Integer32):
    """Custom type latency07 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Latency07_Type.__name__ = "Integer32"
_Latency07_Object = MibScalar
latency07 = _Latency07_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 7, 4),
    _Latency07_Type()
)
latency07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latency07.setStatus("mandatory")


class _Serverstate07_Type(Integer32):
    """Custom type serverstate07 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Serverstate07_Type.__name__ = "Integer32"
_Serverstate07_Object = MibScalar
serverstate07 = _Serverstate07_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 7, 5),
    _Serverstate07_Type()
)
serverstate07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverstate07.setStatus("mandatory")
_Server08_ObjectIdentity = ObjectIdentity
server08 = _Server08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 8)
)
_Servername08_Type = DisplayString
_Servername08_Object = MibScalar
servername08 = _Servername08_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 8, 1),
    _Servername08_Type()
)
servername08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servername08.setStatus("mandatory")
_Ip08_Type = DisplayString
_Ip08_Object = MibScalar
ip08 = _Ip08_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 8, 2),
    _Ip08_Type()
)
ip08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip08.setStatus("mandatory")
_Connectionport08_Type = DisplayString
_Connectionport08_Object = MibScalar
connectionport08 = _Connectionport08_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 8, 3),
    _Connectionport08_Type()
)
connectionport08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionport08.setStatus("mandatory")


class _Latency08_Type(Integer32):
    """Custom type latency08 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Latency08_Type.__name__ = "Integer32"
_Latency08_Object = MibScalar
latency08 = _Latency08_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 8, 4),
    _Latency08_Type()
)
latency08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latency08.setStatus("mandatory")


class _Serverstate08_Type(Integer32):
    """Custom type serverstate08 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Serverstate08_Type.__name__ = "Integer32"
_Serverstate08_Object = MibScalar
serverstate08 = _Serverstate08_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 8, 5),
    _Serverstate08_Type()
)
serverstate08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverstate08.setStatus("mandatory")
_Server09_ObjectIdentity = ObjectIdentity
server09 = _Server09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 9)
)
_Servername09_Type = DisplayString
_Servername09_Object = MibScalar
servername09 = _Servername09_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 9, 1),
    _Servername09_Type()
)
servername09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servername09.setStatus("mandatory")
_Ip09_Type = DisplayString
_Ip09_Object = MibScalar
ip09 = _Ip09_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 9, 2),
    _Ip09_Type()
)
ip09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip09.setStatus("mandatory")
_Connectionport09_Type = DisplayString
_Connectionport09_Object = MibScalar
connectionport09 = _Connectionport09_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 9, 3),
    _Connectionport09_Type()
)
connectionport09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionport09.setStatus("mandatory")


class _Latency09_Type(Integer32):
    """Custom type latency09 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Latency09_Type.__name__ = "Integer32"
_Latency09_Object = MibScalar
latency09 = _Latency09_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 9, 4),
    _Latency09_Type()
)
latency09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latency09.setStatus("mandatory")


class _Serverstate09_Type(Integer32):
    """Custom type serverstate09 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Serverstate09_Type.__name__ = "Integer32"
_Serverstate09_Object = MibScalar
serverstate09 = _Serverstate09_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 9, 5),
    _Serverstate09_Type()
)
serverstate09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverstate09.setStatus("mandatory")
_Server10_ObjectIdentity = ObjectIdentity
server10 = _Server10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 10)
)
_Servername10_Type = DisplayString
_Servername10_Object = MibScalar
servername10 = _Servername10_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 10, 1),
    _Servername10_Type()
)
servername10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servername10.setStatus("mandatory")
_Ip10_Type = DisplayString
_Ip10_Object = MibScalar
ip10 = _Ip10_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 10, 2),
    _Ip10_Type()
)
ip10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip10.setStatus("mandatory")
_Connectionport10_Type = DisplayString
_Connectionport10_Object = MibScalar
connectionport10 = _Connectionport10_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 10, 3),
    _Connectionport10_Type()
)
connectionport10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionport10.setStatus("mandatory")


class _Latency10_Type(Integer32):
    """Custom type latency10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Latency10_Type.__name__ = "Integer32"
_Latency10_Object = MibScalar
latency10 = _Latency10_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 10, 4),
    _Latency10_Type()
)
latency10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latency10.setStatus("mandatory")


class _Serverstate10_Type(Integer32):
    """Custom type serverstate10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Serverstate10_Type.__name__ = "Integer32"
_Serverstate10_Object = MibScalar
serverstate10 = _Serverstate10_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 10, 5),
    _Serverstate10_Type()
)
serverstate10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverstate10.setStatus("mandatory")
_Server11_ObjectIdentity = ObjectIdentity
server11 = _Server11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 11)
)
_Servername11_Type = DisplayString
_Servername11_Object = MibScalar
servername11 = _Servername11_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 11, 1),
    _Servername11_Type()
)
servername11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servername11.setStatus("mandatory")
_Ip11_Type = DisplayString
_Ip11_Object = MibScalar
ip11 = _Ip11_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 11, 2),
    _Ip11_Type()
)
ip11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip11.setStatus("mandatory")
_Connectionport11_Type = DisplayString
_Connectionport11_Object = MibScalar
connectionport11 = _Connectionport11_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 11, 3),
    _Connectionport11_Type()
)
connectionport11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionport11.setStatus("mandatory")


class _Latency11_Type(Integer32):
    """Custom type latency11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Latency11_Type.__name__ = "Integer32"
_Latency11_Object = MibScalar
latency11 = _Latency11_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 11, 4),
    _Latency11_Type()
)
latency11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latency11.setStatus("mandatory")


class _Serverstate11_Type(Integer32):
    """Custom type serverstate11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Serverstate11_Type.__name__ = "Integer32"
_Serverstate11_Object = MibScalar
serverstate11 = _Serverstate11_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 11, 5),
    _Serverstate11_Type()
)
serverstate11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverstate11.setStatus("mandatory")
_Server12_ObjectIdentity = ObjectIdentity
server12 = _Server12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 12)
)
_Servername12_Type = DisplayString
_Servername12_Object = MibScalar
servername12 = _Servername12_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 12, 1),
    _Servername12_Type()
)
servername12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servername12.setStatus("mandatory")
_Ip12_Type = DisplayString
_Ip12_Object = MibScalar
ip12 = _Ip12_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 12, 2),
    _Ip12_Type()
)
ip12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip12.setStatus("mandatory")
_Connectionport12_Type = DisplayString
_Connectionport12_Object = MibScalar
connectionport12 = _Connectionport12_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 12, 3),
    _Connectionport12_Type()
)
connectionport12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionport12.setStatus("mandatory")


class _Latency12_Type(Integer32):
    """Custom type latency12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Latency12_Type.__name__ = "Integer32"
_Latency12_Object = MibScalar
latency12 = _Latency12_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 12, 4),
    _Latency12_Type()
)
latency12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latency12.setStatus("mandatory")


class _Serverstate12_Type(Integer32):
    """Custom type serverstate12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Serverstate12_Type.__name__ = "Integer32"
_Serverstate12_Object = MibScalar
serverstate12 = _Serverstate12_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 12, 5),
    _Serverstate12_Type()
)
serverstate12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverstate12.setStatus("mandatory")
_Server13_ObjectIdentity = ObjectIdentity
server13 = _Server13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 13)
)
_Servername13_Type = DisplayString
_Servername13_Object = MibScalar
servername13 = _Servername13_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 13, 1),
    _Servername13_Type()
)
servername13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servername13.setStatus("mandatory")
_Ip13_Type = DisplayString
_Ip13_Object = MibScalar
ip13 = _Ip13_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 13, 2),
    _Ip13_Type()
)
ip13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip13.setStatus("mandatory")
_Connectionport13_Type = DisplayString
_Connectionport13_Object = MibScalar
connectionport13 = _Connectionport13_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 13, 3),
    _Connectionport13_Type()
)
connectionport13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionport13.setStatus("mandatory")


class _Latency13_Type(Integer32):
    """Custom type latency13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Latency13_Type.__name__ = "Integer32"
_Latency13_Object = MibScalar
latency13 = _Latency13_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 13, 4),
    _Latency13_Type()
)
latency13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latency13.setStatus("mandatory")


class _Serverstate13_Type(Integer32):
    """Custom type serverstate13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Serverstate13_Type.__name__ = "Integer32"
_Serverstate13_Object = MibScalar
serverstate13 = _Serverstate13_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 13, 5),
    _Serverstate13_Type()
)
serverstate13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverstate13.setStatus("mandatory")
_Server14_ObjectIdentity = ObjectIdentity
server14 = _Server14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 14)
)
_Servername14_Type = DisplayString
_Servername14_Object = MibScalar
servername14 = _Servername14_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 14, 1),
    _Servername14_Type()
)
servername14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servername14.setStatus("mandatory")
_Ip14_Type = DisplayString
_Ip14_Object = MibScalar
ip14 = _Ip14_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 14, 2),
    _Ip14_Type()
)
ip14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip14.setStatus("mandatory")
_Connectionport14_Type = DisplayString
_Connectionport14_Object = MibScalar
connectionport14 = _Connectionport14_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 14, 3),
    _Connectionport14_Type()
)
connectionport14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionport14.setStatus("mandatory")


class _Latency14_Type(Integer32):
    """Custom type latency14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Latency14_Type.__name__ = "Integer32"
_Latency14_Object = MibScalar
latency14 = _Latency14_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 14, 4),
    _Latency14_Type()
)
latency14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latency14.setStatus("mandatory")


class _Serverstate14_Type(Integer32):
    """Custom type serverstate14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Serverstate14_Type.__name__ = "Integer32"
_Serverstate14_Object = MibScalar
serverstate14 = _Serverstate14_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 14, 5),
    _Serverstate14_Type()
)
serverstate14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverstate14.setStatus("mandatory")
_Server15_ObjectIdentity = ObjectIdentity
server15 = _Server15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 15)
)
_Servername15_Type = DisplayString
_Servername15_Object = MibScalar
servername15 = _Servername15_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 15, 1),
    _Servername15_Type()
)
servername15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servername15.setStatus("mandatory")
_Ip15_Type = DisplayString
_Ip15_Object = MibScalar
ip15 = _Ip15_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 15, 2),
    _Ip15_Type()
)
ip15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip15.setStatus("mandatory")
_Connectionport15_Type = DisplayString
_Connectionport15_Object = MibScalar
connectionport15 = _Connectionport15_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 15, 3),
    _Connectionport15_Type()
)
connectionport15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionport15.setStatus("mandatory")


class _Latency15_Type(Integer32):
    """Custom type latency15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Latency15_Type.__name__ = "Integer32"
_Latency15_Object = MibScalar
latency15 = _Latency15_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 15, 4),
    _Latency15_Type()
)
latency15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latency15.setStatus("mandatory")


class _Serverstate15_Type(Integer32):
    """Custom type serverstate15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Serverstate15_Type.__name__ = "Integer32"
_Serverstate15_Object = MibScalar
serverstate15 = _Serverstate15_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 15, 5),
    _Serverstate15_Type()
)
serverstate15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverstate15.setStatus("mandatory")
_Server16_ObjectIdentity = ObjectIdentity
server16 = _Server16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 16)
)
_Servername16_Type = DisplayString
_Servername16_Object = MibScalar
servername16 = _Servername16_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 16, 1),
    _Servername16_Type()
)
servername16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servername16.setStatus("mandatory")
_Ip16_Type = DisplayString
_Ip16_Object = MibScalar
ip16 = _Ip16_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 16, 2),
    _Ip16_Type()
)
ip16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip16.setStatus("mandatory")
_Connectionport16_Type = DisplayString
_Connectionport16_Object = MibScalar
connectionport16 = _Connectionport16_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 16, 3),
    _Connectionport16_Type()
)
connectionport16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionport16.setStatus("mandatory")


class _Latency16_Type(Integer32):
    """Custom type latency16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Latency16_Type.__name__ = "Integer32"
_Latency16_Object = MibScalar
latency16 = _Latency16_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 16, 4),
    _Latency16_Type()
)
latency16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latency16.setStatus("mandatory")


class _Serverstate16_Type(Integer32):
    """Custom type serverstate16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Serverstate16_Type.__name__ = "Integer32"
_Serverstate16_Object = MibScalar
serverstate16 = _Serverstate16_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 16, 5),
    _Serverstate16_Type()
)
serverstate16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverstate16.setStatus("mandatory")
_Server17_ObjectIdentity = ObjectIdentity
server17 = _Server17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 17)
)
_Servername17_Type = DisplayString
_Servername17_Object = MibScalar
servername17 = _Servername17_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 17, 1),
    _Servername17_Type()
)
servername17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servername17.setStatus("mandatory")
_Ip17_Type = DisplayString
_Ip17_Object = MibScalar
ip17 = _Ip17_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 17, 2),
    _Ip17_Type()
)
ip17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip17.setStatus("mandatory")
_Connectionport17_Type = DisplayString
_Connectionport17_Object = MibScalar
connectionport17 = _Connectionport17_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 17, 3),
    _Connectionport17_Type()
)
connectionport17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionport17.setStatus("mandatory")


class _Latency17_Type(Integer32):
    """Custom type latency17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Latency17_Type.__name__ = "Integer32"
_Latency17_Object = MibScalar
latency17 = _Latency17_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 17, 4),
    _Latency17_Type()
)
latency17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latency17.setStatus("mandatory")


class _Serverstate17_Type(Integer32):
    """Custom type serverstate17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Serverstate17_Type.__name__ = "Integer32"
_Serverstate17_Object = MibScalar
serverstate17 = _Serverstate17_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 17, 5),
    _Serverstate17_Type()
)
serverstate17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverstate17.setStatus("mandatory")
_Server18_ObjectIdentity = ObjectIdentity
server18 = _Server18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 18)
)
_Servername18_Type = DisplayString
_Servername18_Object = MibScalar
servername18 = _Servername18_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 18, 1),
    _Servername18_Type()
)
servername18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servername18.setStatus("mandatory")
_Ip18_Type = DisplayString
_Ip18_Object = MibScalar
ip18 = _Ip18_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 18, 2),
    _Ip18_Type()
)
ip18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip18.setStatus("mandatory")
_Connectionport18_Type = DisplayString
_Connectionport18_Object = MibScalar
connectionport18 = _Connectionport18_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 18, 3),
    _Connectionport18_Type()
)
connectionport18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionport18.setStatus("mandatory")


class _Latency18_Type(Integer32):
    """Custom type latency18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Latency18_Type.__name__ = "Integer32"
_Latency18_Object = MibScalar
latency18 = _Latency18_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 18, 4),
    _Latency18_Type()
)
latency18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latency18.setStatus("mandatory")


class _Serverstate18_Type(Integer32):
    """Custom type serverstate18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Serverstate18_Type.__name__ = "Integer32"
_Serverstate18_Object = MibScalar
serverstate18 = _Serverstate18_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 18, 5),
    _Serverstate18_Type()
)
serverstate18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverstate18.setStatus("mandatory")
_Server19_ObjectIdentity = ObjectIdentity
server19 = _Server19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 19)
)
_Servername19_Type = DisplayString
_Servername19_Object = MibScalar
servername19 = _Servername19_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 19, 1),
    _Servername19_Type()
)
servername19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servername19.setStatus("mandatory")
_Ip19_Type = DisplayString
_Ip19_Object = MibScalar
ip19 = _Ip19_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 19, 2),
    _Ip19_Type()
)
ip19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip19.setStatus("mandatory")
_Connectionport19_Type = DisplayString
_Connectionport19_Object = MibScalar
connectionport19 = _Connectionport19_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 19, 3),
    _Connectionport19_Type()
)
connectionport19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionport19.setStatus("mandatory")


class _Latency19_Type(Integer32):
    """Custom type latency19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Latency19_Type.__name__ = "Integer32"
_Latency19_Object = MibScalar
latency19 = _Latency19_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 19, 4),
    _Latency19_Type()
)
latency19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latency19.setStatus("mandatory")


class _Serverstate19_Type(Integer32):
    """Custom type serverstate19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Serverstate19_Type.__name__ = "Integer32"
_Serverstate19_Object = MibScalar
serverstate19 = _Serverstate19_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 19, 5),
    _Serverstate19_Type()
)
serverstate19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverstate19.setStatus("mandatory")
_Server20_ObjectIdentity = ObjectIdentity
server20 = _Server20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 20)
)
_Servername20_Type = DisplayString
_Servername20_Object = MibScalar
servername20 = _Servername20_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 20, 1),
    _Servername20_Type()
)
servername20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    servername20.setStatus("mandatory")
_Ip20_Type = DisplayString
_Ip20_Object = MibScalar
ip20 = _Ip20_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 20, 2),
    _Ip20_Type()
)
ip20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ip20.setStatus("mandatory")
_Connectionport20_Type = DisplayString
_Connectionport20_Object = MibScalar
connectionport20 = _Connectionport20_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 20, 3),
    _Connectionport20_Type()
)
connectionport20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    connectionport20.setStatus("mandatory")


class _Latency20_Type(Integer32):
    """Custom type latency20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999),
    )


_Latency20_Type.__name__ = "Integer32"
_Latency20_Object = MibScalar
latency20 = _Latency20_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 20, 4),
    _Latency20_Type()
)
latency20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    latency20.setStatus("mandatory")


class _Serverstate20_Type(Integer32):
    """Custom type serverstate20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Serverstate20_Type.__name__ = "Integer32"
_Serverstate20_Object = MibScalar
serverstate20 = _Serverstate20_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 4, 20, 5),
    _Serverstate20_Type()
)
serverstate20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serverstate20.setStatus("mandatory")
_Alarm_zones_ObjectIdentity = ObjectIdentity
alarm_zones = _Alarm_zones_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5)
)
_Alarmzone01_ObjectIdentity = ObjectIdentity
alarmzone01 = _Alarmzone01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 1)
)
_Alarmzonename01_Type = DisplayString
_Alarmzonename01_Object = MibScalar
alarmzonename01 = _Alarmzonename01_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 1, 1),
    _Alarmzonename01_Type()
)
alarmzonename01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename01.setStatus("mandatory")


class _Alarmzonestate01_Type(Integer32):
    """Custom type alarmzonestate01 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate01_Type.__name__ = "Integer32"
_Alarmzonestate01_Object = MibScalar
alarmzonestate01 = _Alarmzonestate01_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 1, 2),
    _Alarmzonestate01_Type()
)
alarmzonestate01.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate01.setStatus("mandatory")


class _Alarmzonealarm101_Type(Integer32):
    """Custom type alarmzonealarm101 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm101_Type.__name__ = "Integer32"
_Alarmzonealarm101_Object = MibScalar
alarmzonealarm101 = _Alarmzonealarm101_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 1, 3),
    _Alarmzonealarm101_Type()
)
alarmzonealarm101.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm101.setStatus("mandatory")
_Alarmzone02_ObjectIdentity = ObjectIdentity
alarmzone02 = _Alarmzone02_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 2)
)
_Alarmzonename02_Type = DisplayString
_Alarmzonename02_Object = MibScalar
alarmzonename02 = _Alarmzonename02_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 2, 1),
    _Alarmzonename02_Type()
)
alarmzonename02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename02.setStatus("mandatory")


class _Alarmzonestate02_Type(Integer32):
    """Custom type alarmzonestate02 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate02_Type.__name__ = "Integer32"
_Alarmzonestate02_Object = MibScalar
alarmzonestate02 = _Alarmzonestate02_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 2, 2),
    _Alarmzonestate02_Type()
)
alarmzonestate02.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate02.setStatus("mandatory")


class _Alarmzonealarm102_Type(Integer32):
    """Custom type alarmzonealarm102 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm102_Type.__name__ = "Integer32"
_Alarmzonealarm102_Object = MibScalar
alarmzonealarm102 = _Alarmzonealarm102_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 2, 3),
    _Alarmzonealarm102_Type()
)
alarmzonealarm102.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm102.setStatus("mandatory")
_Alarmzone03_ObjectIdentity = ObjectIdentity
alarmzone03 = _Alarmzone03_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 3)
)
_Alarmzonename03_Type = DisplayString
_Alarmzonename03_Object = MibScalar
alarmzonename03 = _Alarmzonename03_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 3, 1),
    _Alarmzonename03_Type()
)
alarmzonename03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename03.setStatus("mandatory")


class _Alarmzonestate03_Type(Integer32):
    """Custom type alarmzonestate03 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate03_Type.__name__ = "Integer32"
_Alarmzonestate03_Object = MibScalar
alarmzonestate03 = _Alarmzonestate03_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 3, 2),
    _Alarmzonestate03_Type()
)
alarmzonestate03.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate03.setStatus("mandatory")


class _Alarmzonealarm103_Type(Integer32):
    """Custom type alarmzonealarm103 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm103_Type.__name__ = "Integer32"
_Alarmzonealarm103_Object = MibScalar
alarmzonealarm103 = _Alarmzonealarm103_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 3, 3),
    _Alarmzonealarm103_Type()
)
alarmzonealarm103.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm103.setStatus("mandatory")
_Alarmzone04_ObjectIdentity = ObjectIdentity
alarmzone04 = _Alarmzone04_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 4)
)
_Alarmzonename04_Type = DisplayString
_Alarmzonename04_Object = MibScalar
alarmzonename04 = _Alarmzonename04_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 4, 1),
    _Alarmzonename04_Type()
)
alarmzonename04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename04.setStatus("mandatory")


class _Alarmzonestate04_Type(Integer32):
    """Custom type alarmzonestate04 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate04_Type.__name__ = "Integer32"
_Alarmzonestate04_Object = MibScalar
alarmzonestate04 = _Alarmzonestate04_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 4, 2),
    _Alarmzonestate04_Type()
)
alarmzonestate04.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate04.setStatus("mandatory")


class _Alarmzonealarm104_Type(Integer32):
    """Custom type alarmzonealarm104 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm104_Type.__name__ = "Integer32"
_Alarmzonealarm104_Object = MibScalar
alarmzonealarm104 = _Alarmzonealarm104_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 4, 3),
    _Alarmzonealarm104_Type()
)
alarmzonealarm104.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm104.setStatus("mandatory")
_Alarmzone05_ObjectIdentity = ObjectIdentity
alarmzone05 = _Alarmzone05_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 5)
)
_Alarmzonename05_Type = DisplayString
_Alarmzonename05_Object = MibScalar
alarmzonename05 = _Alarmzonename05_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 5, 1),
    _Alarmzonename05_Type()
)
alarmzonename05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename05.setStatus("mandatory")


class _Alarmzonestate05_Type(Integer32):
    """Custom type alarmzonestate05 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate05_Type.__name__ = "Integer32"
_Alarmzonestate05_Object = MibScalar
alarmzonestate05 = _Alarmzonestate05_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 5, 2),
    _Alarmzonestate05_Type()
)
alarmzonestate05.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate05.setStatus("mandatory")


class _Alarmzonealarm105_Type(Integer32):
    """Custom type alarmzonealarm105 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm105_Type.__name__ = "Integer32"
_Alarmzonealarm105_Object = MibScalar
alarmzonealarm105 = _Alarmzonealarm105_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 5, 3),
    _Alarmzonealarm105_Type()
)
alarmzonealarm105.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm105.setStatus("mandatory")
_Alarmzone06_ObjectIdentity = ObjectIdentity
alarmzone06 = _Alarmzone06_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 6)
)
_Alarmzonename06_Type = DisplayString
_Alarmzonename06_Object = MibScalar
alarmzonename06 = _Alarmzonename06_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 6, 1),
    _Alarmzonename06_Type()
)
alarmzonename06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename06.setStatus("mandatory")


class _Alarmzonestate06_Type(Integer32):
    """Custom type alarmzonestate06 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate06_Type.__name__ = "Integer32"
_Alarmzonestate06_Object = MibScalar
alarmzonestate06 = _Alarmzonestate06_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 6, 2),
    _Alarmzonestate06_Type()
)
alarmzonestate06.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate06.setStatus("mandatory")


class _Alarmzonealarm106_Type(Integer32):
    """Custom type alarmzonealarm106 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm106_Type.__name__ = "Integer32"
_Alarmzonealarm106_Object = MibScalar
alarmzonealarm106 = _Alarmzonealarm106_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 6, 3),
    _Alarmzonealarm106_Type()
)
alarmzonealarm106.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm106.setStatus("mandatory")
_Alarmzone07_ObjectIdentity = ObjectIdentity
alarmzone07 = _Alarmzone07_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 7)
)
_Alarmzonename07_Type = DisplayString
_Alarmzonename07_Object = MibScalar
alarmzonename07 = _Alarmzonename07_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 7, 1),
    _Alarmzonename07_Type()
)
alarmzonename07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename07.setStatus("mandatory")


class _Alarmzonestate07_Type(Integer32):
    """Custom type alarmzonestate07 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate07_Type.__name__ = "Integer32"
_Alarmzonestate07_Object = MibScalar
alarmzonestate07 = _Alarmzonestate07_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 7, 2),
    _Alarmzonestate07_Type()
)
alarmzonestate07.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate07.setStatus("mandatory")


class _Alarmzonealarm107_Type(Integer32):
    """Custom type alarmzonealarm107 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm107_Type.__name__ = "Integer32"
_Alarmzonealarm107_Object = MibScalar
alarmzonealarm107 = _Alarmzonealarm107_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 7, 3),
    _Alarmzonealarm107_Type()
)
alarmzonealarm107.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm107.setStatus("mandatory")
_Alarmzone08_ObjectIdentity = ObjectIdentity
alarmzone08 = _Alarmzone08_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 8)
)
_Alarmzonename08_Type = DisplayString
_Alarmzonename08_Object = MibScalar
alarmzonename08 = _Alarmzonename08_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 8, 1),
    _Alarmzonename08_Type()
)
alarmzonename08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename08.setStatus("mandatory")


class _Alarmzonestate08_Type(Integer32):
    """Custom type alarmzonestate08 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate08_Type.__name__ = "Integer32"
_Alarmzonestate08_Object = MibScalar
alarmzonestate08 = _Alarmzonestate08_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 8, 2),
    _Alarmzonestate08_Type()
)
alarmzonestate08.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate08.setStatus("mandatory")


class _Alarmzonealarm108_Type(Integer32):
    """Custom type alarmzonealarm108 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm108_Type.__name__ = "Integer32"
_Alarmzonealarm108_Object = MibScalar
alarmzonealarm108 = _Alarmzonealarm108_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 8, 3),
    _Alarmzonealarm108_Type()
)
alarmzonealarm108.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm108.setStatus("mandatory")
_Alarmzone09_ObjectIdentity = ObjectIdentity
alarmzone09 = _Alarmzone09_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 9)
)
_Alarmzonename09_Type = DisplayString
_Alarmzonename09_Object = MibScalar
alarmzonename09 = _Alarmzonename09_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 9, 1),
    _Alarmzonename09_Type()
)
alarmzonename09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename09.setStatus("mandatory")


class _Alarmzonestate09_Type(Integer32):
    """Custom type alarmzonestate09 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate09_Type.__name__ = "Integer32"
_Alarmzonestate09_Object = MibScalar
alarmzonestate09 = _Alarmzonestate09_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 9, 2),
    _Alarmzonestate09_Type()
)
alarmzonestate09.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate09.setStatus("mandatory")


class _Alarmzonealarm109_Type(Integer32):
    """Custom type alarmzonealarm109 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm109_Type.__name__ = "Integer32"
_Alarmzonealarm109_Object = MibScalar
alarmzonealarm109 = _Alarmzonealarm109_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 9, 3),
    _Alarmzonealarm109_Type()
)
alarmzonealarm109.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm109.setStatus("mandatory")
_Alarmzone10_ObjectIdentity = ObjectIdentity
alarmzone10 = _Alarmzone10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 10)
)
_Alarmzonename10_Type = DisplayString
_Alarmzonename10_Object = MibScalar
alarmzonename10 = _Alarmzonename10_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 10, 1),
    _Alarmzonename10_Type()
)
alarmzonename10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename10.setStatus("mandatory")


class _Alarmzonestate10_Type(Integer32):
    """Custom type alarmzonestate10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate10_Type.__name__ = "Integer32"
_Alarmzonestate10_Object = MibScalar
alarmzonestate10 = _Alarmzonestate10_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 10, 2),
    _Alarmzonestate10_Type()
)
alarmzonestate10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate10.setStatus("mandatory")


class _Alarmzonealarm110_Type(Integer32):
    """Custom type alarmzonealarm110 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm110_Type.__name__ = "Integer32"
_Alarmzonealarm110_Object = MibScalar
alarmzonealarm110 = _Alarmzonealarm110_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 10, 3),
    _Alarmzonealarm110_Type()
)
alarmzonealarm110.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm110.setStatus("mandatory")
_Alarmzone11_ObjectIdentity = ObjectIdentity
alarmzone11 = _Alarmzone11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 11)
)
_Alarmzonename11_Type = DisplayString
_Alarmzonename11_Object = MibScalar
alarmzonename11 = _Alarmzonename11_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 11, 1),
    _Alarmzonename11_Type()
)
alarmzonename11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename11.setStatus("mandatory")


class _Alarmzonestate11_Type(Integer32):
    """Custom type alarmzonestate11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate11_Type.__name__ = "Integer32"
_Alarmzonestate11_Object = MibScalar
alarmzonestate11 = _Alarmzonestate11_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 11, 2),
    _Alarmzonestate11_Type()
)
alarmzonestate11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate11.setStatus("mandatory")


class _Alarmzonealarm111_Type(Integer32):
    """Custom type alarmzonealarm111 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm111_Type.__name__ = "Integer32"
_Alarmzonealarm111_Object = MibScalar
alarmzonealarm111 = _Alarmzonealarm111_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 11, 3),
    _Alarmzonealarm111_Type()
)
alarmzonealarm111.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm111.setStatus("mandatory")
_Alarmzone12_ObjectIdentity = ObjectIdentity
alarmzone12 = _Alarmzone12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 12)
)
_Alarmzonename12_Type = DisplayString
_Alarmzonename12_Object = MibScalar
alarmzonename12 = _Alarmzonename12_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 12, 1),
    _Alarmzonename12_Type()
)
alarmzonename12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename12.setStatus("mandatory")


class _Alarmzonestate12_Type(Integer32):
    """Custom type alarmzonestate12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate12_Type.__name__ = "Integer32"
_Alarmzonestate12_Object = MibScalar
alarmzonestate12 = _Alarmzonestate12_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 12, 2),
    _Alarmzonestate12_Type()
)
alarmzonestate12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate12.setStatus("mandatory")


class _Alarmzonealarm112_Type(Integer32):
    """Custom type alarmzonealarm112 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm112_Type.__name__ = "Integer32"
_Alarmzonealarm112_Object = MibScalar
alarmzonealarm112 = _Alarmzonealarm112_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 12, 3),
    _Alarmzonealarm112_Type()
)
alarmzonealarm112.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm112.setStatus("mandatory")
_Alarmzone13_ObjectIdentity = ObjectIdentity
alarmzone13 = _Alarmzone13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 13)
)
_Alarmzonename13_Type = DisplayString
_Alarmzonename13_Object = MibScalar
alarmzonename13 = _Alarmzonename13_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 13, 1),
    _Alarmzonename13_Type()
)
alarmzonename13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename13.setStatus("mandatory")


class _Alarmzonestate13_Type(Integer32):
    """Custom type alarmzonestate13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate13_Type.__name__ = "Integer32"
_Alarmzonestate13_Object = MibScalar
alarmzonestate13 = _Alarmzonestate13_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 13, 2),
    _Alarmzonestate13_Type()
)
alarmzonestate13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate13.setStatus("mandatory")


class _Alarmzonealarm113_Type(Integer32):
    """Custom type alarmzonealarm113 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm113_Type.__name__ = "Integer32"
_Alarmzonealarm113_Object = MibScalar
alarmzonealarm113 = _Alarmzonealarm113_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 13, 3),
    _Alarmzonealarm113_Type()
)
alarmzonealarm113.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm113.setStatus("mandatory")
_Alarmzone14_ObjectIdentity = ObjectIdentity
alarmzone14 = _Alarmzone14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 14)
)
_Alarmzonename14_Type = DisplayString
_Alarmzonename14_Object = MibScalar
alarmzonename14 = _Alarmzonename14_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 14, 1),
    _Alarmzonename14_Type()
)
alarmzonename14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename14.setStatus("mandatory")


class _Alarmzonestate14_Type(Integer32):
    """Custom type alarmzonestate14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate14_Type.__name__ = "Integer32"
_Alarmzonestate14_Object = MibScalar
alarmzonestate14 = _Alarmzonestate14_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 14, 2),
    _Alarmzonestate14_Type()
)
alarmzonestate14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate14.setStatus("mandatory")


class _Alarmzonealarm114_Type(Integer32):
    """Custom type alarmzonealarm114 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm114_Type.__name__ = "Integer32"
_Alarmzonealarm114_Object = MibScalar
alarmzonealarm114 = _Alarmzonealarm114_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 14, 3),
    _Alarmzonealarm114_Type()
)
alarmzonealarm114.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm114.setStatus("mandatory")
_Alarmzone15_ObjectIdentity = ObjectIdentity
alarmzone15 = _Alarmzone15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 15)
)
_Alarmzonename15_Type = DisplayString
_Alarmzonename15_Object = MibScalar
alarmzonename15 = _Alarmzonename15_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 15, 1),
    _Alarmzonename15_Type()
)
alarmzonename15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename15.setStatus("mandatory")


class _Alarmzonestate15_Type(Integer32):
    """Custom type alarmzonestate15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate15_Type.__name__ = "Integer32"
_Alarmzonestate15_Object = MibScalar
alarmzonestate15 = _Alarmzonestate15_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 15, 2),
    _Alarmzonestate15_Type()
)
alarmzonestate15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate15.setStatus("mandatory")


class _Alarmzonealarm115_Type(Integer32):
    """Custom type alarmzonealarm115 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm115_Type.__name__ = "Integer32"
_Alarmzonealarm115_Object = MibScalar
alarmzonealarm115 = _Alarmzonealarm115_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 15, 3),
    _Alarmzonealarm115_Type()
)
alarmzonealarm115.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm115.setStatus("mandatory")
_Alarmzone16_ObjectIdentity = ObjectIdentity
alarmzone16 = _Alarmzone16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 16)
)
_Alarmzonename16_Type = DisplayString
_Alarmzonename16_Object = MibScalar
alarmzonename16 = _Alarmzonename16_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 16, 1),
    _Alarmzonename16_Type()
)
alarmzonename16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename16.setStatus("mandatory")


class _Alarmzonestate16_Type(Integer32):
    """Custom type alarmzonestate16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate16_Type.__name__ = "Integer32"
_Alarmzonestate16_Object = MibScalar
alarmzonestate16 = _Alarmzonestate16_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 16, 2),
    _Alarmzonestate16_Type()
)
alarmzonestate16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate16.setStatus("mandatory")


class _Alarmzonealarm116_Type(Integer32):
    """Custom type alarmzonealarm116 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm116_Type.__name__ = "Integer32"
_Alarmzonealarm116_Object = MibScalar
alarmzonealarm116 = _Alarmzonealarm116_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 16, 3),
    _Alarmzonealarm116_Type()
)
alarmzonealarm116.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm116.setStatus("mandatory")
_Alarmzone17_ObjectIdentity = ObjectIdentity
alarmzone17 = _Alarmzone17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 17)
)
_Alarmzonename17_Type = DisplayString
_Alarmzonename17_Object = MibScalar
alarmzonename17 = _Alarmzonename17_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 17, 1),
    _Alarmzonename17_Type()
)
alarmzonename17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename17.setStatus("mandatory")


class _Alarmzonestate17_Type(Integer32):
    """Custom type alarmzonestate17 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate17_Type.__name__ = "Integer32"
_Alarmzonestate17_Object = MibScalar
alarmzonestate17 = _Alarmzonestate17_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 17, 2),
    _Alarmzonestate17_Type()
)
alarmzonestate17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate17.setStatus("mandatory")


class _Alarmzonealarm117_Type(Integer32):
    """Custom type alarmzonealarm117 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm117_Type.__name__ = "Integer32"
_Alarmzonealarm117_Object = MibScalar
alarmzonealarm117 = _Alarmzonealarm117_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 17, 3),
    _Alarmzonealarm117_Type()
)
alarmzonealarm117.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm117.setStatus("mandatory")
_Alarmzone18_ObjectIdentity = ObjectIdentity
alarmzone18 = _Alarmzone18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 18)
)
_Alarmzonename18_Type = DisplayString
_Alarmzonename18_Object = MibScalar
alarmzonename18 = _Alarmzonename18_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 18, 1),
    _Alarmzonename18_Type()
)
alarmzonename18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename18.setStatus("mandatory")


class _Alarmzonestate18_Type(Integer32):
    """Custom type alarmzonestate18 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate18_Type.__name__ = "Integer32"
_Alarmzonestate18_Object = MibScalar
alarmzonestate18 = _Alarmzonestate18_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 18, 2),
    _Alarmzonestate18_Type()
)
alarmzonestate18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate18.setStatus("mandatory")


class _Alarmzonealarm118_Type(Integer32):
    """Custom type alarmzonealarm118 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm118_Type.__name__ = "Integer32"
_Alarmzonealarm118_Object = MibScalar
alarmzonealarm118 = _Alarmzonealarm118_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 18, 3),
    _Alarmzonealarm118_Type()
)
alarmzonealarm118.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm118.setStatus("mandatory")
_Alarmzone19_ObjectIdentity = ObjectIdentity
alarmzone19 = _Alarmzone19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 19)
)
_Alarmzonename19_Type = DisplayString
_Alarmzonename19_Object = MibScalar
alarmzonename19 = _Alarmzonename19_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 19, 1),
    _Alarmzonename19_Type()
)
alarmzonename19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename19.setStatus("mandatory")


class _Alarmzonestate19_Type(Integer32):
    """Custom type alarmzonestate19 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate19_Type.__name__ = "Integer32"
_Alarmzonestate19_Object = MibScalar
alarmzonestate19 = _Alarmzonestate19_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 19, 2),
    _Alarmzonestate19_Type()
)
alarmzonestate19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate19.setStatus("mandatory")


class _Alarmzonealarm119_Type(Integer32):
    """Custom type alarmzonealarm119 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm119_Type.__name__ = "Integer32"
_Alarmzonealarm119_Object = MibScalar
alarmzonealarm119 = _Alarmzonealarm119_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 19, 3),
    _Alarmzonealarm119_Type()
)
alarmzonealarm119.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm119.setStatus("mandatory")
_Alarmzone20_ObjectIdentity = ObjectIdentity
alarmzone20 = _Alarmzone20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 20)
)
_Alarmzonename20_Type = DisplayString
_Alarmzonename20_Object = MibScalar
alarmzonename20 = _Alarmzonename20_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 20, 1),
    _Alarmzonename20_Type()
)
alarmzonename20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename20.setStatus("mandatory")


class _Alarmzonestate20_Type(Integer32):
    """Custom type alarmzonestate20 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate20_Type.__name__ = "Integer32"
_Alarmzonestate20_Object = MibScalar
alarmzonestate20 = _Alarmzonestate20_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 20, 2),
    _Alarmzonestate20_Type()
)
alarmzonestate20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate20.setStatus("mandatory")


class _Alarmzonealarm120_Type(Integer32):
    """Custom type alarmzonealarm120 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm120_Type.__name__ = "Integer32"
_Alarmzonealarm120_Object = MibScalar
alarmzonealarm120 = _Alarmzonealarm120_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 20, 3),
    _Alarmzonealarm120_Type()
)
alarmzonealarm120.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm120.setStatus("mandatory")
_Alarmzone21_ObjectIdentity = ObjectIdentity
alarmzone21 = _Alarmzone21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 21)
)
_Alarmzonename21_Type = DisplayString
_Alarmzonename21_Object = MibScalar
alarmzonename21 = _Alarmzonename21_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 21, 1),
    _Alarmzonename21_Type()
)
alarmzonename21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename21.setStatus("mandatory")


class _Alarmzonestate21_Type(Integer32):
    """Custom type alarmzonestate21 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate21_Type.__name__ = "Integer32"
_Alarmzonestate21_Object = MibScalar
alarmzonestate21 = _Alarmzonestate21_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 21, 2),
    _Alarmzonestate21_Type()
)
alarmzonestate21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate21.setStatus("mandatory")


class _Alarmzonealarm121_Type(Integer32):
    """Custom type alarmzonealarm121 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm121_Type.__name__ = "Integer32"
_Alarmzonealarm121_Object = MibScalar
alarmzonealarm121 = _Alarmzonealarm121_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 21, 3),
    _Alarmzonealarm121_Type()
)
alarmzonealarm121.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm121.setStatus("mandatory")
_Alarmzone22_ObjectIdentity = ObjectIdentity
alarmzone22 = _Alarmzone22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 22)
)
_Alarmzonename22_Type = DisplayString
_Alarmzonename22_Object = MibScalar
alarmzonename22 = _Alarmzonename22_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 22, 1),
    _Alarmzonename22_Type()
)
alarmzonename22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename22.setStatus("mandatory")


class _Alarmzonestate22_Type(Integer32):
    """Custom type alarmzonestate22 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate22_Type.__name__ = "Integer32"
_Alarmzonestate22_Object = MibScalar
alarmzonestate22 = _Alarmzonestate22_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 22, 2),
    _Alarmzonestate22_Type()
)
alarmzonestate22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate22.setStatus("mandatory")


class _Alarmzonealarm122_Type(Integer32):
    """Custom type alarmzonealarm122 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm122_Type.__name__ = "Integer32"
_Alarmzonealarm122_Object = MibScalar
alarmzonealarm122 = _Alarmzonealarm122_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 22, 3),
    _Alarmzonealarm122_Type()
)
alarmzonealarm122.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm122.setStatus("mandatory")
_Alarmzone23_ObjectIdentity = ObjectIdentity
alarmzone23 = _Alarmzone23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 23)
)
_Alarmzonename23_Type = DisplayString
_Alarmzonename23_Object = MibScalar
alarmzonename23 = _Alarmzonename23_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 23, 1),
    _Alarmzonename23_Type()
)
alarmzonename23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename23.setStatus("mandatory")


class _Alarmzonestate23_Type(Integer32):
    """Custom type alarmzonestate23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate23_Type.__name__ = "Integer32"
_Alarmzonestate23_Object = MibScalar
alarmzonestate23 = _Alarmzonestate23_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 23, 2),
    _Alarmzonestate23_Type()
)
alarmzonestate23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate23.setStatus("mandatory")


class _Alarmzonealarm123_Type(Integer32):
    """Custom type alarmzonealarm123 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm123_Type.__name__ = "Integer32"
_Alarmzonealarm123_Object = MibScalar
alarmzonealarm123 = _Alarmzonealarm123_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 23, 3),
    _Alarmzonealarm123_Type()
)
alarmzonealarm123.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm123.setStatus("mandatory")
_Alarmzone24_ObjectIdentity = ObjectIdentity
alarmzone24 = _Alarmzone24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 24)
)
_Alarmzonename24_Type = DisplayString
_Alarmzonename24_Object = MibScalar
alarmzonename24 = _Alarmzonename24_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 24, 1),
    _Alarmzonename24_Type()
)
alarmzonename24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename24.setStatus("mandatory")


class _Alarmzonestate24_Type(Integer32):
    """Custom type alarmzonestate24 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate24_Type.__name__ = "Integer32"
_Alarmzonestate24_Object = MibScalar
alarmzonestate24 = _Alarmzonestate24_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 24, 2),
    _Alarmzonestate24_Type()
)
alarmzonestate24.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate24.setStatus("mandatory")


class _Alarmzonealarm124_Type(Integer32):
    """Custom type alarmzonealarm124 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm124_Type.__name__ = "Integer32"
_Alarmzonealarm124_Object = MibScalar
alarmzonealarm124 = _Alarmzonealarm124_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 24, 3),
    _Alarmzonealarm124_Type()
)
alarmzonealarm124.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm124.setStatus("mandatory")
_Alarmzone25_ObjectIdentity = ObjectIdentity
alarmzone25 = _Alarmzone25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 25)
)
_Alarmzonename25_Type = DisplayString
_Alarmzonename25_Object = MibScalar
alarmzonename25 = _Alarmzonename25_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 25, 1),
    _Alarmzonename25_Type()
)
alarmzonename25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename25.setStatus("mandatory")


class _Alarmzonestate25_Type(Integer32):
    """Custom type alarmzonestate25 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate25_Type.__name__ = "Integer32"
_Alarmzonestate25_Object = MibScalar
alarmzonestate25 = _Alarmzonestate25_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 25, 2),
    _Alarmzonestate25_Type()
)
alarmzonestate25.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate25.setStatus("mandatory")


class _Alarmzonealarm125_Type(Integer32):
    """Custom type alarmzonealarm125 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm125_Type.__name__ = "Integer32"
_Alarmzonealarm125_Object = MibScalar
alarmzonealarm125 = _Alarmzonealarm125_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 25, 3),
    _Alarmzonealarm125_Type()
)
alarmzonealarm125.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm125.setStatus("mandatory")
_Alarmzone26_ObjectIdentity = ObjectIdentity
alarmzone26 = _Alarmzone26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 26)
)
_Alarmzonename26_Type = DisplayString
_Alarmzonename26_Object = MibScalar
alarmzonename26 = _Alarmzonename26_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 26, 1),
    _Alarmzonename26_Type()
)
alarmzonename26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename26.setStatus("mandatory")


class _Alarmzonestate26_Type(Integer32):
    """Custom type alarmzonestate26 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate26_Type.__name__ = "Integer32"
_Alarmzonestate26_Object = MibScalar
alarmzonestate26 = _Alarmzonestate26_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 26, 2),
    _Alarmzonestate26_Type()
)
alarmzonestate26.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate26.setStatus("mandatory")


class _Alarmzonealarm126_Type(Integer32):
    """Custom type alarmzonealarm126 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm126_Type.__name__ = "Integer32"
_Alarmzonealarm126_Object = MibScalar
alarmzonealarm126 = _Alarmzonealarm126_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 26, 3),
    _Alarmzonealarm126_Type()
)
alarmzonealarm126.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm126.setStatus("mandatory")
_Alarmzone27_ObjectIdentity = ObjectIdentity
alarmzone27 = _Alarmzone27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 27)
)
_Alarmzonename27_Type = DisplayString
_Alarmzonename27_Object = MibScalar
alarmzonename27 = _Alarmzonename27_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 27, 1),
    _Alarmzonename27_Type()
)
alarmzonename27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename27.setStatus("mandatory")


class _Alarmzonestate27_Type(Integer32):
    """Custom type alarmzonestate27 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate27_Type.__name__ = "Integer32"
_Alarmzonestate27_Object = MibScalar
alarmzonestate27 = _Alarmzonestate27_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 27, 2),
    _Alarmzonestate27_Type()
)
alarmzonestate27.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate27.setStatus("mandatory")


class _Alarmzonealarm127_Type(Integer32):
    """Custom type alarmzonealarm127 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm127_Type.__name__ = "Integer32"
_Alarmzonealarm127_Object = MibScalar
alarmzonealarm127 = _Alarmzonealarm127_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 27, 3),
    _Alarmzonealarm127_Type()
)
alarmzonealarm127.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm127.setStatus("mandatory")
_Alarmzone28_ObjectIdentity = ObjectIdentity
alarmzone28 = _Alarmzone28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 28)
)
_Alarmzonename28_Type = DisplayString
_Alarmzonename28_Object = MibScalar
alarmzonename28 = _Alarmzonename28_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 28, 1),
    _Alarmzonename28_Type()
)
alarmzonename28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename28.setStatus("mandatory")


class _Alarmzonestate28_Type(Integer32):
    """Custom type alarmzonestate28 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate28_Type.__name__ = "Integer32"
_Alarmzonestate28_Object = MibScalar
alarmzonestate28 = _Alarmzonestate28_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 28, 2),
    _Alarmzonestate28_Type()
)
alarmzonestate28.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate28.setStatus("mandatory")


class _Alarmzonealarm128_Type(Integer32):
    """Custom type alarmzonealarm128 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm128_Type.__name__ = "Integer32"
_Alarmzonealarm128_Object = MibScalar
alarmzonealarm128 = _Alarmzonealarm128_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 28, 3),
    _Alarmzonealarm128_Type()
)
alarmzonealarm128.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm128.setStatus("mandatory")
_Alarmzone29_ObjectIdentity = ObjectIdentity
alarmzone29 = _Alarmzone29_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 29)
)
_Alarmzonename29_Type = DisplayString
_Alarmzonename29_Object = MibScalar
alarmzonename29 = _Alarmzonename29_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 29, 1),
    _Alarmzonename29_Type()
)
alarmzonename29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename29.setStatus("mandatory")


class _Alarmzonestate29_Type(Integer32):
    """Custom type alarmzonestate29 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate29_Type.__name__ = "Integer32"
_Alarmzonestate29_Object = MibScalar
alarmzonestate29 = _Alarmzonestate29_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 29, 2),
    _Alarmzonestate29_Type()
)
alarmzonestate29.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate29.setStatus("mandatory")


class _Alarmzonealarm129_Type(Integer32):
    """Custom type alarmzonealarm129 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm129_Type.__name__ = "Integer32"
_Alarmzonealarm129_Object = MibScalar
alarmzonealarm129 = _Alarmzonealarm129_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 29, 3),
    _Alarmzonealarm129_Type()
)
alarmzonealarm129.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm129.setStatus("mandatory")
_Alarmzone30_ObjectIdentity = ObjectIdentity
alarmzone30 = _Alarmzone30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 30)
)
_Alarmzonename30_Type = DisplayString
_Alarmzonename30_Object = MibScalar
alarmzonename30 = _Alarmzonename30_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 30, 1),
    _Alarmzonename30_Type()
)
alarmzonename30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonename30.setStatus("mandatory")


class _Alarmzonestate30_Type(Integer32):
    """Custom type alarmzonestate30 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonestate30_Type.__name__ = "Integer32"
_Alarmzonestate30_Object = MibScalar
alarmzonestate30 = _Alarmzonestate30_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 30, 2),
    _Alarmzonestate30_Type()
)
alarmzonestate30.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonestate30.setStatus("mandatory")


class _Alarmzonealarm130_Type(Integer32):
    """Custom type alarmzonealarm130 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarmzonealarm130_Type.__name__ = "Integer32"
_Alarmzonealarm130_Object = MibScalar
alarmzonealarm130 = _Alarmzonealarm130_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 5, 30, 3),
    _Alarmzonealarm130_Type()
)
alarmzonealarm130.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmzonealarm130.setStatus("mandatory")
_AlarmText_Type = DisplayString
_AlarmText_Object = MibScalar
alarmText = _AlarmText_Object(
    (1, 3, 6, 1, 4, 1, 37954, 1, 10),
    _AlarmText_Type()
)
alarmText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmText.setStatus("mandatory")

# Managed Objects groups


# Notification objects

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
    ("KAM-PRO", "alarmText")
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
    "KAM-PRO",
    **{"kentix": kentix,
       "login": login,
       "alarm": alarm,
       "alarmmanager-pro": alarmmanager_pro,
       "state": state,
       "alarm1": alarm1,
       "alarm2": alarm2,
       "serverstate": serverstate,
       "sensorcommunication": sensorcommunication,
       "extalarm": extalarm,
       "extarmed": extarmed,
       "extpower": extpower,
       "sabotage": sabotage,
       "gsmsignal": gsmsignal,
       "gsmok": gsmok,
       "systemarmed": systemarmed,
       "alarmtemp": alarmtemp,
       "alarmhum": alarmhum,
       "alarmdewpoint": alarmdewpoint,
       "alarmco": alarmco,
       "multisensors": multisensors,
       "multisensor01": multisensor01,
       "sensorname01": sensorname01,
       "temperature01": temperature01,
       "humidity01": humidity01,
       "dewpoint01": dewpoint01,
       "co01": co01,
       "motion01": motion01,
       "digitalin101": digitalin101,
       "digitalin201": digitalin201,
       "digitalout201": digitalout201,
       "comError01": comError01,
       "multisensor02": multisensor02,
       "sensorname02": sensorname02,
       "temperature02": temperature02,
       "humidity02": humidity02,
       "dewpoint02": dewpoint02,
       "co02": co02,
       "motion02": motion02,
       "digitalin102": digitalin102,
       "digitalin202": digitalin202,
       "digitalout202": digitalout202,
       "comError02": comError02,
       "multisensor03": multisensor03,
       "sensorname03": sensorname03,
       "temperature03": temperature03,
       "humidity03": humidity03,
       "dewpoint03": dewpoint03,
       "co03": co03,
       "motion03": motion03,
       "digitalin103": digitalin103,
       "digitalin203": digitalin203,
       "digitalout203": digitalout203,
       "comError03": comError03,
       "multisensor04": multisensor04,
       "sensorname04": sensorname04,
       "temperature04": temperature04,
       "humidity04": humidity04,
       "dewpoint04": dewpoint04,
       "co04": co04,
       "motion04": motion04,
       "digitalin104": digitalin104,
       "digitalin204": digitalin204,
       "digitalout204": digitalout204,
       "comError04": comError04,
       "multisensor05": multisensor05,
       "sensorname05": sensorname05,
       "temperature05": temperature05,
       "humidity05": humidity05,
       "dewpoint05": dewpoint05,
       "co05": co05,
       "motion05": motion05,
       "digitalin105": digitalin105,
       "digitalin205": digitalin205,
       "digitalout205": digitalout205,
       "comError05": comError05,
       "multisensor06": multisensor06,
       "sensorname06": sensorname06,
       "temperature06": temperature06,
       "humidity06": humidity06,
       "dewpoint06": dewpoint06,
       "co06": co06,
       "motion06": motion06,
       "digitalin106": digitalin106,
       "digitalin206": digitalin206,
       "digitalout206": digitalout206,
       "comError06": comError06,
       "multisensor07": multisensor07,
       "sensorname07": sensorname07,
       "temperature07": temperature07,
       "humidity07": humidity07,
       "dewpoint07": dewpoint07,
       "co07": co07,
       "motion07": motion07,
       "digitalin107": digitalin107,
       "digitalin207": digitalin207,
       "digitalout207": digitalout207,
       "comError07": comError07,
       "multisensor08": multisensor08,
       "sensorname08": sensorname08,
       "temperature08": temperature08,
       "humidity08": humidity08,
       "dewpoint08": dewpoint08,
       "co08": co08,
       "motion08": motion08,
       "digitalin108": digitalin108,
       "digitalin208": digitalin208,
       "digitalout208": digitalout208,
       "comError08": comError08,
       "multisensor09": multisensor09,
       "sensorname09": sensorname09,
       "temperature09": temperature09,
       "humidity09": humidity09,
       "dewpoint09": dewpoint09,
       "co09": co09,
       "motion09": motion09,
       "digitalin109": digitalin109,
       "digitalin209": digitalin209,
       "digitalout209": digitalout209,
       "comError09": comError09,
       "multisensor10": multisensor10,
       "sensorname10": sensorname10,
       "temperature10": temperature10,
       "humidity10": humidity10,
       "dewpoint10": dewpoint10,
       "co10": co10,
       "motion10": motion10,
       "digitalin110": digitalin110,
       "digitalin210": digitalin210,
       "digitalout210": digitalout210,
       "comError10": comError10,
       "multisensor11": multisensor11,
       "sensorname11": sensorname11,
       "temperature11": temperature11,
       "humidity11": humidity11,
       "dewpoint11": dewpoint11,
       "co11": co11,
       "motion11": motion11,
       "digitalin111": digitalin111,
       "digitalin211": digitalin211,
       "digitalout211": digitalout211,
       "comError11": comError11,
       "multisensor12": multisensor12,
       "sensorname12": sensorname12,
       "temperature12": temperature12,
       "humidity12": humidity12,
       "dewpoint12": dewpoint12,
       "co12": co12,
       "motion12": motion12,
       "digitalin112": digitalin112,
       "digitalin212": digitalin212,
       "digitalout212": digitalout212,
       "comError12": comError12,
       "multisensor13": multisensor13,
       "sensorname13": sensorname13,
       "temperature13": temperature13,
       "humidity13": humidity13,
       "dewpoint13": dewpoint13,
       "co13": co13,
       "motion13": motion13,
       "digitalin113": digitalin113,
       "digitalin213": digitalin213,
       "digitalout213": digitalout213,
       "comError13": comError13,
       "multisensor14": multisensor14,
       "sensorname14": sensorname14,
       "temperature14": temperature14,
       "humidity14": humidity14,
       "dewpoint14": dewpoint14,
       "co14": co14,
       "motion14": motion14,
       "digitalin114": digitalin114,
       "digitalin214": digitalin214,
       "digitalout214": digitalout214,
       "comError14": comError14,
       "multisensor15": multisensor15,
       "sensorname15": sensorname15,
       "temperature15": temperature15,
       "humidity15": humidity15,
       "dewpoint15": dewpoint15,
       "co15": co15,
       "motion15": motion15,
       "digitalin115": digitalin115,
       "digitalin215": digitalin215,
       "digitalout215": digitalout215,
       "comError15": comError15,
       "multisensor16": multisensor16,
       "sensorname16": sensorname16,
       "temperature16": temperature16,
       "humidity16": humidity16,
       "dewpoint16": dewpoint16,
       "co16": co16,
       "motion16": motion16,
       "digitalin116": digitalin116,
       "digitalin216": digitalin216,
       "digitalout216": digitalout216,
       "comError16": comError16,
       "multisensor17": multisensor17,
       "sensorname17": sensorname17,
       "temperature17": temperature17,
       "humidity17": humidity17,
       "dewpoint17": dewpoint17,
       "co17": co17,
       "motion17": motion17,
       "digitalin117": digitalin117,
       "digitalin217": digitalin217,
       "digitalout217": digitalout217,
       "comError17": comError17,
       "multisensor18": multisensor18,
       "sensorname18": sensorname18,
       "temperature18": temperature18,
       "humidity18": humidity18,
       "dewpoint18": dewpoint18,
       "co18": co18,
       "motion18": motion18,
       "digitalin118": digitalin118,
       "digitalin218": digitalin218,
       "digitalout218": digitalout218,
       "comError18": comError18,
       "multisensor19": multisensor19,
       "sensorname19": sensorname19,
       "temperature19": temperature19,
       "humidity19": humidity19,
       "dewpoint19": dewpoint19,
       "co19": co19,
       "motion19": motion19,
       "digitalin119": digitalin119,
       "digitalin219": digitalin219,
       "digitalout219": digitalout219,
       "comError19": comError19,
       "multisensor20": multisensor20,
       "sensorname20": sensorname20,
       "temperature20": temperature20,
       "humidity20": humidity20,
       "dewpoint20": dewpoint20,
       "co20": co20,
       "motion20": motion20,
       "digitalin120": digitalin120,
       "digitalin220": digitalin220,
       "digitalout220": digitalout220,
       "comError20": comError20,
       "multisensor21": multisensor21,
       "sensorname21": sensorname21,
       "temperature21": temperature21,
       "humidity21": humidity21,
       "dewpoint21": dewpoint21,
       "co21": co21,
       "motion21": motion21,
       "digitalin121": digitalin121,
       "digitalin221": digitalin221,
       "digitalout221": digitalout221,
       "comError21": comError21,
       "multisensor22": multisensor22,
       "sensorname22": sensorname22,
       "temperature22": temperature22,
       "humidity22": humidity22,
       "dewpoint22": dewpoint22,
       "co22": co22,
       "motion22": motion22,
       "digitalin122": digitalin122,
       "digitalin222": digitalin222,
       "digitalout222": digitalout222,
       "comError22": comError22,
       "multisensor23": multisensor23,
       "sensorname23": sensorname23,
       "temperature23": temperature23,
       "humidity23": humidity23,
       "dewpoint23": dewpoint23,
       "co23": co23,
       "motion23": motion23,
       "digitalin123": digitalin123,
       "digitalin223": digitalin223,
       "digitalout223": digitalout223,
       "comError23": comError23,
       "multisensor24": multisensor24,
       "sensorname24": sensorname24,
       "temperature24": temperature24,
       "humidity24": humidity24,
       "dewpoint24": dewpoint24,
       "co24": co24,
       "motion24": motion24,
       "digitalin124": digitalin124,
       "digitalin224": digitalin224,
       "digitalout224": digitalout224,
       "comError24": comError24,
       "multisensor25": multisensor25,
       "sensorname25": sensorname25,
       "temperature25": temperature25,
       "humidity25": humidity25,
       "dewpoint25": dewpoint25,
       "co25": co25,
       "motion25": motion25,
       "digitalin125": digitalin125,
       "digitalin225": digitalin225,
       "digitalout225": digitalout225,
       "comError25": comError25,
       "multisensor26": multisensor26,
       "sensorname26": sensorname26,
       "temperature26": temperature26,
       "humidity26": humidity26,
       "dewpoint26": dewpoint26,
       "co26": co26,
       "motion26": motion26,
       "digitalin126": digitalin126,
       "digitalin226": digitalin226,
       "digitalout226": digitalout226,
       "comError26": comError26,
       "multisensor27": multisensor27,
       "sensorname27": sensorname27,
       "temperature27": temperature27,
       "humidity27": humidity27,
       "dewpoint27": dewpoint27,
       "co27": co27,
       "motion27": motion27,
       "digitalin127": digitalin127,
       "digitalin227": digitalin227,
       "digitalout227": digitalout227,
       "comError27": comError27,
       "multisensor28": multisensor28,
       "sensorname28": sensorname28,
       "temperature28": temperature28,
       "humidity28": humidity28,
       "dewpoint28": dewpoint28,
       "co28": co28,
       "motion28": motion28,
       "digitalin128": digitalin128,
       "digitalin228": digitalin228,
       "digitalout228": digitalout228,
       "comError28": comError28,
       "multisensor29": multisensor29,
       "sensorname29": sensorname29,
       "temperature29": temperature29,
       "humidity29": humidity29,
       "dewpoint29": dewpoint29,
       "co29": co29,
       "motion29": motion29,
       "digitalin129": digitalin129,
       "digitalin229": digitalin229,
       "digitalout229": digitalout229,
       "comError29": comError29,
       "multisensor30": multisensor30,
       "sensorname30": sensorname30,
       "temperature30": temperature30,
       "humidity30": humidity30,
       "dewpoint30": dewpoint30,
       "co30": co30,
       "motion30": motion30,
       "digitalin130": digitalin130,
       "digitalin230": digitalin230,
       "digitalout230": digitalout230,
       "comError30": comError30,
       "multisensor31": multisensor31,
       "sensorname31": sensorname31,
       "temperature31": temperature31,
       "humidity31": humidity31,
       "dewpoint31": dewpoint31,
       "co31": co31,
       "motion31": motion31,
       "digitalin131": digitalin131,
       "digitalin231": digitalin231,
       "digitalout231": digitalout231,
       "comError31": comError31,
       "multisensor32": multisensor32,
       "sensorname32": sensorname32,
       "temperature32": temperature32,
       "humidity32": humidity32,
       "dewpoint32": dewpoint32,
       "co32": co32,
       "motion32": motion32,
       "digitalin132": digitalin132,
       "digitalin232": digitalin232,
       "digitalout232": digitalout232,
       "comError32": comError32,
       "multisensor33": multisensor33,
       "sensorname33": sensorname33,
       "temperature33": temperature33,
       "humidity33": humidity33,
       "dewpoint33": dewpoint33,
       "co33": co33,
       "motion33": motion33,
       "digitalin133": digitalin133,
       "digitalin233": digitalin233,
       "digitalout233": digitalout233,
       "comError33": comError33,
       "multisensor34": multisensor34,
       "sensorname34": sensorname34,
       "temperature34": temperature34,
       "humidity34": humidity34,
       "dewpoint34": dewpoint34,
       "co34": co34,
       "motion34": motion34,
       "digitalin134": digitalin134,
       "digitalin234": digitalin234,
       "digitalout234": digitalout234,
       "comError34": comError34,
       "multisensor35": multisensor35,
       "sensorname35": sensorname35,
       "temperature35": temperature35,
       "humidity35": humidity35,
       "dewpoint35": dewpoint35,
       "co35": co35,
       "motion35": motion35,
       "digitalin135": digitalin135,
       "digitalin235": digitalin235,
       "digitalout235": digitalout235,
       "comError35": comError35,
       "multisensor36": multisensor36,
       "sensorname36": sensorname36,
       "temperature36": temperature36,
       "humidity36": humidity36,
       "dewpoint36": dewpoint36,
       "co36": co36,
       "motion36": motion36,
       "digitalin136": digitalin136,
       "digitalin236": digitalin236,
       "digitalout236": digitalout236,
       "comError36": comError36,
       "multisensor37": multisensor37,
       "sensorname37": sensorname37,
       "temperature37": temperature37,
       "humidity37": humidity37,
       "dewpoint37": dewpoint37,
       "co37": co37,
       "motion37": motion37,
       "digitalin137": digitalin137,
       "digitalin237": digitalin237,
       "digitalout237": digitalout237,
       "comError37": comError37,
       "multisensor38": multisensor38,
       "sensorname38": sensorname38,
       "temperature38": temperature38,
       "humidity38": humidity38,
       "dewpoint38": dewpoint38,
       "co38": co38,
       "motion38": motion38,
       "digitalin138": digitalin138,
       "digitalin238": digitalin238,
       "digitalout238": digitalout238,
       "comError38": comError38,
       "multisensor39": multisensor39,
       "sensorname39": sensorname39,
       "temperature39": temperature39,
       "humidity39": humidity39,
       "dewpoint39": dewpoint39,
       "co39": co39,
       "motion39": motion39,
       "digitalin139": digitalin139,
       "digitalin239": digitalin239,
       "digitalout239": digitalout239,
       "comError39": comError39,
       "multisensor40": multisensor40,
       "sensorname40": sensorname40,
       "temperature40": temperature40,
       "humidity40": humidity40,
       "dewpoint40": dewpoint40,
       "co40": co40,
       "motion40": motion40,
       "digitalin140": digitalin140,
       "digitalin240": digitalin240,
       "digitalout240": digitalout240,
       "comError40": comError40,
       "multisensor41": multisensor41,
       "sensorname41": sensorname41,
       "temperature41": temperature41,
       "humidity41": humidity41,
       "dewpoint41": dewpoint41,
       "co41": co41,
       "motion41": motion41,
       "digitalin141": digitalin141,
       "digitalin241": digitalin241,
       "digitalout241": digitalout241,
       "comError41": comError41,
       "multisensor42": multisensor42,
       "sensorname42": sensorname42,
       "temperature42": temperature42,
       "humidity42": humidity42,
       "dewpoint42": dewpoint42,
       "co42": co42,
       "motion42": motion42,
       "digitalin142": digitalin142,
       "digitalin242": digitalin242,
       "digitalout242": digitalout242,
       "comError42": comError42,
       "multisensor43": multisensor43,
       "sensorname43": sensorname43,
       "temperature43": temperature43,
       "humidity43": humidity43,
       "dewpoint43": dewpoint43,
       "co43": co43,
       "motion43": motion43,
       "digitalin143": digitalin143,
       "digitalin243": digitalin243,
       "digitalout243": digitalout243,
       "comError43": comError43,
       "multisensor44": multisensor44,
       "sensorname44": sensorname44,
       "temperature44": temperature44,
       "humidity44": humidity44,
       "dewpoint44": dewpoint44,
       "co44": co44,
       "motion44": motion44,
       "digitalin144": digitalin144,
       "digitalin244": digitalin244,
       "digitalout244": digitalout244,
       "comError44": comError44,
       "multisensor45": multisensor45,
       "sensorname45": sensorname45,
       "temperature45": temperature45,
       "humidity45": humidity45,
       "dewpoint45": dewpoint45,
       "co45": co45,
       "motion45": motion45,
       "digitalin145": digitalin145,
       "digitalin245": digitalin245,
       "digitalout245": digitalout245,
       "comError45": comError45,
       "multisensor46": multisensor46,
       "sensorname46": sensorname46,
       "temperature46": temperature46,
       "humidity46": humidity46,
       "dewpoint46": dewpoint46,
       "co46": co46,
       "motion46": motion46,
       "digitalin146": digitalin146,
       "digitalin246": digitalin246,
       "digitalout246": digitalout246,
       "comError46": comError46,
       "multisensor47": multisensor47,
       "sensorname47": sensorname47,
       "temperature47": temperature47,
       "humidity47": humidity47,
       "dewpoint47": dewpoint47,
       "co47": co47,
       "motion47": motion47,
       "digitalin147": digitalin147,
       "digitalin247": digitalin247,
       "digitalout247": digitalout247,
       "comError47": comError47,
       "multisensor48": multisensor48,
       "sensorname48": sensorname48,
       "temperature48": temperature48,
       "humidity48": humidity48,
       "dewpoint48": dewpoint48,
       "co48": co48,
       "motion48": motion48,
       "digitalin148": digitalin148,
       "digitalin248": digitalin248,
       "digitalout248": digitalout248,
       "comError48": comError48,
       "multisensor49": multisensor49,
       "sensorname49": sensorname49,
       "temperature49": temperature49,
       "humidity49": humidity49,
       "dewpoint49": dewpoint49,
       "co49": co49,
       "motion49": motion49,
       "digitalin149": digitalin149,
       "digitalin249": digitalin249,
       "digitalout249": digitalout249,
       "comError49": comError49,
       "multisensor50": multisensor50,
       "sensorname50": sensorname50,
       "temperature50": temperature50,
       "humidity50": humidity50,
       "dewpoint50": dewpoint50,
       "co50": co50,
       "motion50": motion50,
       "digitalin150": digitalin150,
       "digitalin250": digitalin250,
       "digitalout250": digitalout250,
       "comError50": comError50,
       "multisensor51": multisensor51,
       "sensorname51": sensorname51,
       "temperature51": temperature51,
       "humidity51": humidity51,
       "dewpoint51": dewpoint51,
       "co51": co51,
       "motion51": motion51,
       "digitalin151": digitalin151,
       "digitalin251": digitalin251,
       "digitalout251": digitalout251,
       "comError51": comError51,
       "multisensor52": multisensor52,
       "sensorname52": sensorname52,
       "temperature52": temperature52,
       "humidity52": humidity52,
       "dewpoint52": dewpoint52,
       "co52": co52,
       "motion52": motion52,
       "digitalin152": digitalin152,
       "digitalin252": digitalin252,
       "digitalout252": digitalout252,
       "comError52": comError52,
       "multisensor53": multisensor53,
       "sensorname53": sensorname53,
       "temperature53": temperature53,
       "humidity53": humidity53,
       "dewpoint53": dewpoint53,
       "co53": co53,
       "motion53": motion53,
       "digitalin153": digitalin153,
       "digitalin253": digitalin253,
       "digitalout253": digitalout253,
       "comError53": comError53,
       "multisensor54": multisensor54,
       "sensorname54": sensorname54,
       "temperature54": temperature54,
       "humidity54": humidity54,
       "dewpoint54": dewpoint54,
       "co54": co54,
       "motion54": motion54,
       "digitalin154": digitalin154,
       "digitalin254": digitalin254,
       "digitalout254": digitalout254,
       "comError54": comError54,
       "multisensor55": multisensor55,
       "sensorname55": sensorname55,
       "temperature55": temperature55,
       "humidity55": humidity55,
       "dewpoint55": dewpoint55,
       "co55": co55,
       "motion55": motion55,
       "digitalin155": digitalin155,
       "digitalin255": digitalin255,
       "digitalout255": digitalout255,
       "comError55": comError55,
       "multisensor56": multisensor56,
       "sensorname56": sensorname56,
       "temperature56": temperature56,
       "humidity56": humidity56,
       "dewpoint56": dewpoint56,
       "co56": co56,
       "motion56": motion56,
       "digitalin156": digitalin156,
       "digitalin256": digitalin256,
       "digitalout256": digitalout256,
       "comError56": comError56,
       "multisensor57": multisensor57,
       "sensorname57": sensorname57,
       "temperature57": temperature57,
       "humidity57": humidity57,
       "dewpoint57": dewpoint57,
       "co57": co57,
       "motion57": motion57,
       "digitalin157": digitalin157,
       "digitalin257": digitalin257,
       "digitalout257": digitalout257,
       "comError57": comError57,
       "multisensor58": multisensor58,
       "sensorname58": sensorname58,
       "temperature58": temperature58,
       "humidity58": humidity58,
       "dewpoint58": dewpoint58,
       "co58": co58,
       "motion58": motion58,
       "digitalin158": digitalin158,
       "digitalin258": digitalin258,
       "digitalout258": digitalout258,
       "comError58": comError58,
       "multisensor59": multisensor59,
       "sensorname59": sensorname59,
       "temperature59": temperature59,
       "humidity59": humidity59,
       "dewpoint59": dewpoint59,
       "co59": co59,
       "motion59": motion59,
       "digitalin159": digitalin159,
       "digitalin259": digitalin259,
       "digitalout259": digitalout259,
       "comError59": comError59,
       "multisensor60": multisensor60,
       "sensorname60": sensorname60,
       "temperature60": temperature60,
       "humidity60": humidity60,
       "dewpoint60": dewpoint60,
       "co60": co60,
       "motion60": motion60,
       "digitalin160": digitalin160,
       "digitalin260": digitalin260,
       "digitalout260": digitalout260,
       "comError60": comError60,
       "multisensor61": multisensor61,
       "sensorname61": sensorname61,
       "temperature61": temperature61,
       "humidity61": humidity61,
       "dewpoint61": dewpoint61,
       "co61": co61,
       "motion61": motion61,
       "digitalin161": digitalin161,
       "digitalin261": digitalin261,
       "digitalout261": digitalout261,
       "comError61": comError61,
       "multisensor62": multisensor62,
       "sensorname62": sensorname62,
       "temperature62": temperature62,
       "humidity62": humidity62,
       "dewpoint62": dewpoint62,
       "co62": co62,
       "motion62": motion62,
       "digitalin162": digitalin162,
       "digitalin262": digitalin262,
       "digitalout262": digitalout262,
       "comError62": comError62,
       "multisensor63": multisensor63,
       "sensorname63": sensorname63,
       "temperature63": temperature63,
       "humidity63": humidity63,
       "dewpoint63": dewpoint63,
       "co63": co63,
       "motion63": motion63,
       "digitalin163": digitalin163,
       "digitalin263": digitalin263,
       "digitalout263": digitalout263,
       "comError63": comError63,
       "multisensor64": multisensor64,
       "sensorname64": sensorname64,
       "temperature64": temperature64,
       "humidity64": humidity64,
       "dewpoint64": dewpoint64,
       "co64": co64,
       "motion64": motion64,
       "digitalin164": digitalin164,
       "digitalin264": digitalin264,
       "digitalout264": digitalout264,
       "comError64": comError64,
       "multisensor65": multisensor65,
       "sensorname65": sensorname65,
       "temperature65": temperature65,
       "humidity65": humidity65,
       "dewpoint65": dewpoint65,
       "co65": co65,
       "motion65": motion65,
       "digitalin165": digitalin165,
       "digitalin265": digitalin265,
       "digitalout265": digitalout265,
       "comError65": comError65,
       "multisensor66": multisensor66,
       "sensorname66": sensorname66,
       "temperature66": temperature66,
       "humidity66": humidity66,
       "dewpoint66": dewpoint66,
       "co66": co66,
       "motion66": motion66,
       "digitalin166": digitalin166,
       "digitalin266": digitalin266,
       "digitalout266": digitalout266,
       "comError66": comError66,
       "multisensor67": multisensor67,
       "sensorname67": sensorname67,
       "temperature67": temperature67,
       "humidity67": humidity67,
       "dewpoint67": dewpoint67,
       "co67": co67,
       "motion67": motion67,
       "digitalin167": digitalin167,
       "digitalin267": digitalin267,
       "digitalout267": digitalout267,
       "comError67": comError67,
       "multisensor68": multisensor68,
       "sensorname68": sensorname68,
       "temperature68": temperature68,
       "humidity68": humidity68,
       "dewpoint68": dewpoint68,
       "co68": co68,
       "motion68": motion68,
       "digitalin168": digitalin168,
       "digitalin268": digitalin268,
       "digitalout268": digitalout268,
       "comError68": comError68,
       "multisensor69": multisensor69,
       "sensorname69": sensorname69,
       "temperature69": temperature69,
       "humidity69": humidity69,
       "dewpoint69": dewpoint69,
       "co69": co69,
       "motion69": motion69,
       "digitalin169": digitalin169,
       "digitalin269": digitalin269,
       "digitalout269": digitalout269,
       "comError69": comError69,
       "multisensor70": multisensor70,
       "sensorname70": sensorname70,
       "temperature70": temperature70,
       "humidity70": humidity70,
       "dewpoint70": dewpoint70,
       "co70": co70,
       "motion70": motion70,
       "digitalin170": digitalin170,
       "digitalin270": digitalin270,
       "digitalout270": digitalout270,
       "comError70": comError70,
       "multisensor71": multisensor71,
       "sensorname71": sensorname71,
       "temperature71": temperature71,
       "humidity71": humidity71,
       "dewpoint71": dewpoint71,
       "co71": co71,
       "motion71": motion71,
       "digitalin171": digitalin171,
       "digitalin271": digitalin271,
       "digitalout271": digitalout271,
       "comError71": comError71,
       "multisensor72": multisensor72,
       "sensorname72": sensorname72,
       "temperature72": temperature72,
       "humidity72": humidity72,
       "dewpoint72": dewpoint72,
       "co72": co72,
       "motion72": motion72,
       "digitalin172": digitalin172,
       "digitalin272": digitalin272,
       "digitalout272": digitalout272,
       "comError72": comError72,
       "multisensor73": multisensor73,
       "sensorname73": sensorname73,
       "temperature73": temperature73,
       "humidity73": humidity73,
       "dewpoint73": dewpoint73,
       "co73": co73,
       "motion73": motion73,
       "digitalin173": digitalin173,
       "digitalin273": digitalin273,
       "digitalout273": digitalout273,
       "comError73": comError73,
       "multisensor74": multisensor74,
       "sensorname74": sensorname74,
       "temperature74": temperature74,
       "humidity74": humidity74,
       "dewpoint74": dewpoint74,
       "co74": co74,
       "motion74": motion74,
       "digitalin174": digitalin174,
       "digitalin274": digitalin274,
       "digitalout274": digitalout274,
       "comError74": comError74,
       "multisensor75": multisensor75,
       "sensorname75": sensorname75,
       "temperature75": temperature75,
       "humidity75": humidity75,
       "dewpoint75": dewpoint75,
       "co75": co75,
       "motion75": motion75,
       "digitalin175": digitalin175,
       "digitalin275": digitalin275,
       "digitalout275": digitalout275,
       "comError75": comError75,
       "multisensor76": multisensor76,
       "sensorname76": sensorname76,
       "temperature76": temperature76,
       "humidity76": humidity76,
       "dewpoint76": dewpoint76,
       "co76": co76,
       "motion76": motion76,
       "digitalin176": digitalin176,
       "digitalin276": digitalin276,
       "digitalout276": digitalout276,
       "comError76": comError76,
       "multisensor77": multisensor77,
       "sensorname77": sensorname77,
       "temperature77": temperature77,
       "humidity77": humidity77,
       "dewpoint77": dewpoint77,
       "co77": co77,
       "motion77": motion77,
       "digitalin177": digitalin177,
       "digitalin277": digitalin277,
       "digitalout277": digitalout277,
       "comError77": comError77,
       "multisensor78": multisensor78,
       "sensorname78": sensorname78,
       "temperature78": temperature78,
       "humidity78": humidity78,
       "dewpoint78": dewpoint78,
       "co78": co78,
       "motion78": motion78,
       "digitalin178": digitalin178,
       "digitalin278": digitalin278,
       "digitalout278": digitalout278,
       "comError78": comError78,
       "multisensor79": multisensor79,
       "sensorname79": sensorname79,
       "temperature79": temperature79,
       "humidity79": humidity79,
       "dewpoint79": dewpoint79,
       "co79": co79,
       "motion79": motion79,
       "digitalin179": digitalin179,
       "digitalin279": digitalin279,
       "digitalout279": digitalout279,
       "comError79": comError79,
       "multisensor80": multisensor80,
       "sensorname80": sensorname80,
       "temperature80": temperature80,
       "humidity80": humidity80,
       "dewpoint80": dewpoint80,
       "co80": co80,
       "motion80": motion80,
       "digitalin180": digitalin180,
       "digitalin280": digitalin280,
       "digitalout280": digitalout280,
       "comError80": comError80,
       "multisensor81": multisensor81,
       "sensorname81": sensorname81,
       "temperature81": temperature81,
       "humidity81": humidity81,
       "dewpoint81": dewpoint81,
       "co81": co81,
       "motion81": motion81,
       "digitalin181": digitalin181,
       "digitalin281": digitalin281,
       "digitalout281": digitalout281,
       "comError81": comError81,
       "multisensor82": multisensor82,
       "sensorname82": sensorname82,
       "temperature82": temperature82,
       "humidity82": humidity82,
       "dewpoint82": dewpoint82,
       "co82": co82,
       "motion82": motion82,
       "digitalin182": digitalin182,
       "digitalin282": digitalin282,
       "digitalout282": digitalout282,
       "comError82": comError82,
       "multisensor83": multisensor83,
       "sensorname83": sensorname83,
       "temperature83": temperature83,
       "humidity83": humidity83,
       "dewpoint83": dewpoint83,
       "co83": co83,
       "motion83": motion83,
       "digitalin183": digitalin183,
       "digitalin283": digitalin283,
       "digitalout283": digitalout283,
       "comError83": comError83,
       "multisensor84": multisensor84,
       "sensorname84": sensorname84,
       "temperature84": temperature84,
       "humidity84": humidity84,
       "dewpoint84": dewpoint84,
       "co84": co84,
       "motion84": motion84,
       "digitalin184": digitalin184,
       "digitalin284": digitalin284,
       "digitalout284": digitalout284,
       "comError84": comError84,
       "multisensor85": multisensor85,
       "sensorname85": sensorname85,
       "temperature85": temperature85,
       "humidity85": humidity85,
       "dewpoint85": dewpoint85,
       "co85": co85,
       "motion85": motion85,
       "digitalin185": digitalin185,
       "digitalin285": digitalin285,
       "digitalout285": digitalout285,
       "comError85": comError85,
       "multisensor86": multisensor86,
       "sensorname86": sensorname86,
       "temperature86": temperature86,
       "humidity86": humidity86,
       "dewpoint86": dewpoint86,
       "co86": co86,
       "motion86": motion86,
       "digitalin186": digitalin186,
       "digitalin286": digitalin286,
       "digitalout286": digitalout286,
       "comError86": comError86,
       "multisensor87": multisensor87,
       "sensorname87": sensorname87,
       "temperature87": temperature87,
       "humidity87": humidity87,
       "dewpoint87": dewpoint87,
       "co87": co87,
       "motion87": motion87,
       "digitalin187": digitalin187,
       "digitalin287": digitalin287,
       "digitalout287": digitalout287,
       "comError87": comError87,
       "multisensor88": multisensor88,
       "sensorname88": sensorname88,
       "temperature88": temperature88,
       "humidity88": humidity88,
       "dewpoint88": dewpoint88,
       "co88": co88,
       "motion88": motion88,
       "digitalin188": digitalin188,
       "digitalin288": digitalin288,
       "digitalout288": digitalout288,
       "comError88": comError88,
       "multisensor89": multisensor89,
       "sensorname89": sensorname89,
       "temperature89": temperature89,
       "humidity89": humidity89,
       "dewpoint89": dewpoint89,
       "co89": co89,
       "motion89": motion89,
       "digitalin189": digitalin189,
       "digitalin289": digitalin289,
       "digitalout289": digitalout289,
       "comError89": comError89,
       "multisensor90": multisensor90,
       "sensorname90": sensorname90,
       "temperature90": temperature90,
       "humidity90": humidity90,
       "dewpoint90": dewpoint90,
       "co90": co90,
       "motion90": motion90,
       "digitalin190": digitalin190,
       "digitalin290": digitalin290,
       "digitalout290": digitalout290,
       "comError90": comError90,
       "multisensor91": multisensor91,
       "sensorname91": sensorname91,
       "temperature91": temperature91,
       "humidity91": humidity91,
       "dewpoint91": dewpoint91,
       "co91": co91,
       "motion91": motion91,
       "digitalin191": digitalin191,
       "digitalin291": digitalin291,
       "digitalout291": digitalout291,
       "comError91": comError91,
       "multisensor92": multisensor92,
       "sensorname92": sensorname92,
       "temperature92": temperature92,
       "humidity92": humidity92,
       "dewpoint92": dewpoint92,
       "co92": co92,
       "motion92": motion92,
       "digitalin192": digitalin192,
       "digitalin292": digitalin292,
       "digitalout292": digitalout292,
       "comError92": comError92,
       "multisensor93": multisensor93,
       "sensorname93": sensorname93,
       "temperature93": temperature93,
       "humidity93": humidity93,
       "dewpoint93": dewpoint93,
       "co93": co93,
       "motion93": motion93,
       "digitalin193": digitalin193,
       "digitalin293": digitalin293,
       "digitalout293": digitalout293,
       "comError93": comError93,
       "multisensor94": multisensor94,
       "sensorname94": sensorname94,
       "temperature94": temperature94,
       "humidity94": humidity94,
       "dewpoint94": dewpoint94,
       "co94": co94,
       "motion94": motion94,
       "digitalin194": digitalin194,
       "digitalin294": digitalin294,
       "digitalout294": digitalout294,
       "comError94": comError94,
       "multisensor95": multisensor95,
       "sensorname95": sensorname95,
       "temperature95": temperature95,
       "humidity95": humidity95,
       "dewpoint95": dewpoint95,
       "co95": co95,
       "motion95": motion95,
       "digitalin195": digitalin195,
       "digitalin295": digitalin295,
       "digitalout295": digitalout295,
       "comError95": comError95,
       "multisensor96": multisensor96,
       "sensorname96": sensorname96,
       "temperature96": temperature96,
       "humidity96": humidity96,
       "dewpoint96": dewpoint96,
       "co96": co96,
       "motion96": motion96,
       "digitalin196": digitalin196,
       "digitalin296": digitalin296,
       "digitalout296": digitalout296,
       "comError96": comError96,
       "multisensor97": multisensor97,
       "sensorname97": sensorname97,
       "temperature97": temperature97,
       "humidity97": humidity97,
       "dewpoint97": dewpoint97,
       "co97": co97,
       "motion97": motion97,
       "digitalin197": digitalin197,
       "digitalin297": digitalin297,
       "digitalout297": digitalout297,
       "comError97": comError97,
       "multisensor98": multisensor98,
       "sensorname98": sensorname98,
       "temperature98": temperature98,
       "humidity98": humidity98,
       "dewpoint98": dewpoint98,
       "co98": co98,
       "motion98": motion98,
       "digitalin198": digitalin198,
       "digitalin298": digitalin298,
       "digitalout298": digitalout298,
       "comError98": comError98,
       "multisensor99": multisensor99,
       "sensorname99": sensorname99,
       "temperature99": temperature99,
       "humidity99": humidity99,
       "dewpoint99": dewpoint99,
       "co99": co99,
       "motion99": motion99,
       "digitalin199": digitalin199,
       "digitalin299": digitalin299,
       "digitalout299": digitalout299,
       "comError99": comError99,
       "multisensor100": multisensor100,
       "sensorname100": sensorname100,
       "temperature100": temperature100,
       "humidity100": humidity100,
       "dewpoint100": dewpoint100,
       "co100": co100,
       "motion100": motion100,
       "digitalin1100": digitalin1100,
       "digitalin2100": digitalin2100,
       "digitalout2100": digitalout2100,
       "comError100": comError100,
       "ext-module": ext_module,
       "modul01port01": modul01port01,
       "modul01portname01": modul01portname01,
       "modul01portstate01": modul01portstate01,
       "modul01port02": modul01port02,
       "modul01portname02": modul01portname02,
       "modul01portstate02": modul01portstate02,
       "modul01port03": modul01port03,
       "modul01portname03": modul01portname03,
       "modul01portstate03": modul01portstate03,
       "modul01port04": modul01port04,
       "modul01portname04": modul01portname04,
       "modul01portstate04": modul01portstate04,
       "modul01port05": modul01port05,
       "modul01portname05": modul01portname05,
       "modul01portstate05": modul01portstate05,
       "modul01port06": modul01port06,
       "modul01portname06": modul01portname06,
       "modul01portstate06": modul01portstate06,
       "modul01port07": modul01port07,
       "modul01portname07": modul01portname07,
       "modul01portstate07": modul01portstate07,
       "modul01port08": modul01port08,
       "modul01portname08": modul01portname08,
       "modul01portstate08": modul01portstate08,
       "modul01port09": modul01port09,
       "modul01portname09": modul01portname09,
       "modul01portstate09": modul01portstate09,
       "modul01port10": modul01port10,
       "modul01portname10": modul01portname10,
       "modul01portstate10": modul01portstate10,
       "modul01port11": modul01port11,
       "modul01portname11": modul01portname11,
       "modul01portstate11": modul01portstate11,
       "modul01port12": modul01port12,
       "modul01portname12": modul01portname12,
       "modul01portstate12": modul01portstate12,
       "modul01port13": modul01port13,
       "modul01portname13": modul01portname13,
       "modul01portstate13": modul01portstate13,
       "modul01port14": modul01port14,
       "modul01portname14": modul01portname14,
       "modul01portstate14": modul01portstate14,
       "modul01port15": modul01port15,
       "modul01portname15": modul01portname15,
       "modul01portstate15": modul01portstate15,
       "modul01port16": modul01port16,
       "modul01portname16": modul01portname16,
       "modul01portstate16": modul01portstate16,
       "modul02port01": modul02port01,
       "modul02portname01": modul02portname01,
       "modul02portstate01": modul02portstate01,
       "modul02port02": modul02port02,
       "modul02portname02": modul02portname02,
       "modul02portstate02": modul02portstate02,
       "modul02port03": modul02port03,
       "modul02portname03": modul02portname03,
       "modul02portstate03": modul02portstate03,
       "modul02port04": modul02port04,
       "modul02portname04": modul02portname04,
       "modul02portstate04": modul02portstate04,
       "modul02port05": modul02port05,
       "modul02portname05": modul02portname05,
       "modul02portstate05": modul02portstate05,
       "modul02port06": modul02port06,
       "modul02portname06": modul02portname06,
       "modul02portstate06": modul02portstate06,
       "modul02port07": modul02port07,
       "modul02portname07": modul02portname07,
       "modul02portstate07": modul02portstate07,
       "modul02port08": modul02port08,
       "modul02portname08": modul02portname08,
       "modul02portstate08": modul02portstate08,
       "modul02port09": modul02port09,
       "modul02portname09": modul02portname09,
       "modul02portstate09": modul02portstate09,
       "modul02port10": modul02port10,
       "modul02portname10": modul02portname10,
       "modul02portstate10": modul02portstate10,
       "modul02port11": modul02port11,
       "modul02portname11": modul02portname11,
       "modul02portstate11": modul02portstate11,
       "modul02port12": modul02port12,
       "modul02portname12": modul02portname12,
       "modul02portstate12": modul02portstate12,
       "modul02port13": modul02port13,
       "modul02portname13": modul02portname13,
       "modul02portstate13": modul02portstate13,
       "modul02port14": modul02port14,
       "modul02portname14": modul02portname14,
       "modul02portstate14": modul02portstate14,
       "modul02port15": modul02port15,
       "modul02portname15": modul02portname15,
       "modul02portstate15": modul02portstate15,
       "modul02port16": modul02port16,
       "modul02portname16": modul02portname16,
       "modul02portstate16": modul02portstate16,
       "modul03port01": modul03port01,
       "modul03portname01": modul03portname01,
       "modul03portstate01": modul03portstate01,
       "modul03port02": modul03port02,
       "modul03portname02": modul03portname02,
       "modul03portstate02": modul03portstate02,
       "modul03port03": modul03port03,
       "modul03portname03": modul03portname03,
       "modul03portstate03": modul03portstate03,
       "modul03port04": modul03port04,
       "modul03portname04": modul03portname04,
       "modul03portstate04": modul03portstate04,
       "modul03port05": modul03port05,
       "modul03portname05": modul03portname05,
       "modul03portstate05": modul03portstate05,
       "modul03port06": modul03port06,
       "modul03portname06": modul03portname06,
       "modul03portstate06": modul03portstate06,
       "modul03port07": modul03port07,
       "modul03portname07": modul03portname07,
       "modul03portstate07": modul03portstate07,
       "modul03port08": modul03port08,
       "modul03portname08": modul03portname08,
       "modul03portstate08": modul03portstate08,
       "modul03port09": modul03port09,
       "modul03portname09": modul03portname09,
       "modul03portstate09": modul03portstate09,
       "modul03port10": modul03port10,
       "modul03portname10": modul03portname10,
       "modul03portstate10": modul03portstate10,
       "modul03port11": modul03port11,
       "modul03portname11": modul03portname11,
       "modul03portstate11": modul03portstate11,
       "modul03port12": modul03port12,
       "modul03portname12": modul03portname12,
       "modul03portstate12": modul03portstate12,
       "modul03port13": modul03port13,
       "modul03portname13": modul03portname13,
       "modul03portstate13": modul03portstate13,
       "modul03port14": modul03port14,
       "modul03portname14": modul03portname14,
       "modul03portstate14": modul03portstate14,
       "modul03port15": modul03port15,
       "modul03portname15": modul03portname15,
       "modul03portstate15": modul03portstate15,
       "modul03port16": modul03port16,
       "modul03portname16": modul03portname16,
       "modul03portstate16": modul03portstate16,
       "modul04port01": modul04port01,
       "modul04portname01": modul04portname01,
       "modul04portstate01": modul04portstate01,
       "modul04port02": modul04port02,
       "modul04portname02": modul04portname02,
       "modul04portstate02": modul04portstate02,
       "modul04port03": modul04port03,
       "modul04portname03": modul04portname03,
       "modul04portstate03": modul04portstate03,
       "modul04port04": modul04port04,
       "modul04portname04": modul04portname04,
       "modul04portstate04": modul04portstate04,
       "modul04port05": modul04port05,
       "modul04portname05": modul04portname05,
       "modul04portstate05": modul04portstate05,
       "modul04port06": modul04port06,
       "modul04portname06": modul04portname06,
       "modul04portstate06": modul04portstate06,
       "modul04port07": modul04port07,
       "modul04portname07": modul04portname07,
       "modul04portstate07": modul04portstate07,
       "modul04port08": modul04port08,
       "modul04portname08": modul04portname08,
       "modul04portstate08": modul04portstate08,
       "modul04port09": modul04port09,
       "modul04portname09": modul04portname09,
       "modul04portstate09": modul04portstate09,
       "modul04port10": modul04port10,
       "modul04portname10": modul04portname10,
       "modul04portstate10": modul04portstate10,
       "modul04port11": modul04port11,
       "modul04portname11": modul04portname11,
       "modul04portstate11": modul04portstate11,
       "modul04port12": modul04port12,
       "modul04portname12": modul04portname12,
       "modul04portstate12": modul04portstate12,
       "modul04port13": modul04port13,
       "modul04portname13": modul04portname13,
       "modul04portstate13": modul04portstate13,
       "modul04port14": modul04port14,
       "modul04portname14": modul04portname14,
       "modul04portstate14": modul04portstate14,
       "modul04port15": modul04port15,
       "modul04portname15": modul04portname15,
       "modul04portstate15": modul04portstate15,
       "modul04port16": modul04port16,
       "modul04portname16": modul04portname16,
       "modul04portstate16": modul04portstate16,
       "modul05port01": modul05port01,
       "modul05portname01": modul05portname01,
       "modul05portstate01": modul05portstate01,
       "modul05port02": modul05port02,
       "modul05portname02": modul05portname02,
       "modul05portstate02": modul05portstate02,
       "modul05port03": modul05port03,
       "modul05portname03": modul05portname03,
       "modul05portstate03": modul05portstate03,
       "modul05port04": modul05port04,
       "modul05portname04": modul05portname04,
       "modul05portstate04": modul05portstate04,
       "modul05port05": modul05port05,
       "modul05portname05": modul05portname05,
       "modul05portstate05": modul05portstate05,
       "modul05port06": modul05port06,
       "modul05portname06": modul05portname06,
       "modul05portstate06": modul05portstate06,
       "modul05port07": modul05port07,
       "modul05portname07": modul05portname07,
       "modul05portstate07": modul05portstate07,
       "modul05port08": modul05port08,
       "modul05portname08": modul05portname08,
       "modul05portstate08": modul05portstate08,
       "modul05port09": modul05port09,
       "modul05portname09": modul05portname09,
       "modul05portstate09": modul05portstate09,
       "modul05port10": modul05port10,
       "modul05portname10": modul05portname10,
       "modul05portstate10": modul05portstate10,
       "modul05port11": modul05port11,
       "modul05portname11": modul05portname11,
       "modul05portstate11": modul05portstate11,
       "modul05port12": modul05port12,
       "modul05portname12": modul05portname12,
       "modul05portstate12": modul05portstate12,
       "modul05port13": modul05port13,
       "modul05portname13": modul05portname13,
       "modul05portstate13": modul05portstate13,
       "modul05port14": modul05port14,
       "modul05portname14": modul05portname14,
       "modul05portstate14": modul05portstate14,
       "modul05port15": modul05port15,
       "modul05portname15": modul05portname15,
       "modul05portstate15": modul05portstate15,
       "modul05port16": modul05port16,
       "modul05portname16": modul05portname16,
       "modul05portstate16": modul05portstate16,
       "modul06port01": modul06port01,
       "modul06portname01": modul06portname01,
       "modul06portstate01": modul06portstate01,
       "modul06port02": modul06port02,
       "modul06portname02": modul06portname02,
       "modul06portstate02": modul06portstate02,
       "modul06port03": modul06port03,
       "modul06portname03": modul06portname03,
       "modul06portstate03": modul06portstate03,
       "modul06port04": modul06port04,
       "modul06portname04": modul06portname04,
       "modul06portstate04": modul06portstate04,
       "modul06port05": modul06port05,
       "modul06portname05": modul06portname05,
       "modul06portstate05": modul06portstate05,
       "modul06port06": modul06port06,
       "modul06portname06": modul06portname06,
       "modul06portstate06": modul06portstate06,
       "modul06port07": modul06port07,
       "modul06portname07": modul06portname07,
       "modul06portstate07": modul06portstate07,
       "modul06port08": modul06port08,
       "modul06portname08": modul06portname08,
       "modul06portstate08": modul06portstate08,
       "modul06port09": modul06port09,
       "modul06portname09": modul06portname09,
       "modul06portstate09": modul06portstate09,
       "modul06port10": modul06port10,
       "modul06portname10": modul06portname10,
       "modul06portstate10": modul06portstate10,
       "modul06port11": modul06port11,
       "modul06portname11": modul06portname11,
       "modul06portstate11": modul06portstate11,
       "modul06port12": modul06port12,
       "modul06portname12": modul06portname12,
       "modul06portstate12": modul06portstate12,
       "modul06port13": modul06port13,
       "modul06portname13": modul06portname13,
       "modul06portstate13": modul06portstate13,
       "modul06port14": modul06port14,
       "modul06portname14": modul06portname14,
       "modul06portstate14": modul06portstate14,
       "modul06port15": modul06port15,
       "modul06portname15": modul06portname15,
       "modul06portstate15": modul06portstate15,
       "modul06port16": modul06port16,
       "modul06portname16": modul06portname16,
       "modul06portstate16": modul06portstate16,
       "server-monitoring": server_monitoring,
       "server01": server01,
       "servername01": servername01,
       "ip01": ip01,
       "connectionport01": connectionport01,
       "latency01": latency01,
       "serverstate01": serverstate01,
       "server02": server02,
       "servername02": servername02,
       "ip02": ip02,
       "connectionport02": connectionport02,
       "latency02": latency02,
       "serverstate02": serverstate02,
       "server03": server03,
       "servername03": servername03,
       "ip03": ip03,
       "connectionport03": connectionport03,
       "latency03": latency03,
       "serverstate03": serverstate03,
       "server04": server04,
       "servername04": servername04,
       "ip04": ip04,
       "connectionport04": connectionport04,
       "latency04": latency04,
       "serverstate04": serverstate04,
       "server05": server05,
       "servername05": servername05,
       "ip05": ip05,
       "connectionport05": connectionport05,
       "latency05": latency05,
       "serverstate05": serverstate05,
       "server06": server06,
       "servername06": servername06,
       "ip06": ip06,
       "connectionport06": connectionport06,
       "latency06": latency06,
       "serverstate06": serverstate06,
       "server07": server07,
       "servername07": servername07,
       "ip07": ip07,
       "connectionport07": connectionport07,
       "latency07": latency07,
       "serverstate07": serverstate07,
       "server08": server08,
       "servername08": servername08,
       "ip08": ip08,
       "connectionport08": connectionport08,
       "latency08": latency08,
       "serverstate08": serverstate08,
       "server09": server09,
       "servername09": servername09,
       "ip09": ip09,
       "connectionport09": connectionport09,
       "latency09": latency09,
       "serverstate09": serverstate09,
       "server10": server10,
       "servername10": servername10,
       "ip10": ip10,
       "connectionport10": connectionport10,
       "latency10": latency10,
       "serverstate10": serverstate10,
       "server11": server11,
       "servername11": servername11,
       "ip11": ip11,
       "connectionport11": connectionport11,
       "latency11": latency11,
       "serverstate11": serverstate11,
       "server12": server12,
       "servername12": servername12,
       "ip12": ip12,
       "connectionport12": connectionport12,
       "latency12": latency12,
       "serverstate12": serverstate12,
       "server13": server13,
       "servername13": servername13,
       "ip13": ip13,
       "connectionport13": connectionport13,
       "latency13": latency13,
       "serverstate13": serverstate13,
       "server14": server14,
       "servername14": servername14,
       "ip14": ip14,
       "connectionport14": connectionport14,
       "latency14": latency14,
       "serverstate14": serverstate14,
       "server15": server15,
       "servername15": servername15,
       "ip15": ip15,
       "connectionport15": connectionport15,
       "latency15": latency15,
       "serverstate15": serverstate15,
       "server16": server16,
       "servername16": servername16,
       "ip16": ip16,
       "connectionport16": connectionport16,
       "latency16": latency16,
       "serverstate16": serverstate16,
       "server17": server17,
       "servername17": servername17,
       "ip17": ip17,
       "connectionport17": connectionport17,
       "latency17": latency17,
       "serverstate17": serverstate17,
       "server18": server18,
       "servername18": servername18,
       "ip18": ip18,
       "connectionport18": connectionport18,
       "latency18": latency18,
       "serverstate18": serverstate18,
       "server19": server19,
       "servername19": servername19,
       "ip19": ip19,
       "connectionport19": connectionport19,
       "latency19": latency19,
       "serverstate19": serverstate19,
       "server20": server20,
       "servername20": servername20,
       "ip20": ip20,
       "connectionport20": connectionport20,
       "latency20": latency20,
       "serverstate20": serverstate20,
       "alarm-zones": alarm_zones,
       "alarmzone01": alarmzone01,
       "alarmzonename01": alarmzonename01,
       "alarmzonestate01": alarmzonestate01,
       "alarmzonealarm101": alarmzonealarm101,
       "alarmzone02": alarmzone02,
       "alarmzonename02": alarmzonename02,
       "alarmzonestate02": alarmzonestate02,
       "alarmzonealarm102": alarmzonealarm102,
       "alarmzone03": alarmzone03,
       "alarmzonename03": alarmzonename03,
       "alarmzonestate03": alarmzonestate03,
       "alarmzonealarm103": alarmzonealarm103,
       "alarmzone04": alarmzone04,
       "alarmzonename04": alarmzonename04,
       "alarmzonestate04": alarmzonestate04,
       "alarmzonealarm104": alarmzonealarm104,
       "alarmzone05": alarmzone05,
       "alarmzonename05": alarmzonename05,
       "alarmzonestate05": alarmzonestate05,
       "alarmzonealarm105": alarmzonealarm105,
       "alarmzone06": alarmzone06,
       "alarmzonename06": alarmzonename06,
       "alarmzonestate06": alarmzonestate06,
       "alarmzonealarm106": alarmzonealarm106,
       "alarmzone07": alarmzone07,
       "alarmzonename07": alarmzonename07,
       "alarmzonestate07": alarmzonestate07,
       "alarmzonealarm107": alarmzonealarm107,
       "alarmzone08": alarmzone08,
       "alarmzonename08": alarmzonename08,
       "alarmzonestate08": alarmzonestate08,
       "alarmzonealarm108": alarmzonealarm108,
       "alarmzone09": alarmzone09,
       "alarmzonename09": alarmzonename09,
       "alarmzonestate09": alarmzonestate09,
       "alarmzonealarm109": alarmzonealarm109,
       "alarmzone10": alarmzone10,
       "alarmzonename10": alarmzonename10,
       "alarmzonestate10": alarmzonestate10,
       "alarmzonealarm110": alarmzonealarm110,
       "alarmzone11": alarmzone11,
       "alarmzonename11": alarmzonename11,
       "alarmzonestate11": alarmzonestate11,
       "alarmzonealarm111": alarmzonealarm111,
       "alarmzone12": alarmzone12,
       "alarmzonename12": alarmzonename12,
       "alarmzonestate12": alarmzonestate12,
       "alarmzonealarm112": alarmzonealarm112,
       "alarmzone13": alarmzone13,
       "alarmzonename13": alarmzonename13,
       "alarmzonestate13": alarmzonestate13,
       "alarmzonealarm113": alarmzonealarm113,
       "alarmzone14": alarmzone14,
       "alarmzonename14": alarmzonename14,
       "alarmzonestate14": alarmzonestate14,
       "alarmzonealarm114": alarmzonealarm114,
       "alarmzone15": alarmzone15,
       "alarmzonename15": alarmzonename15,
       "alarmzonestate15": alarmzonestate15,
       "alarmzonealarm115": alarmzonealarm115,
       "alarmzone16": alarmzone16,
       "alarmzonename16": alarmzonename16,
       "alarmzonestate16": alarmzonestate16,
       "alarmzonealarm116": alarmzonealarm116,
       "alarmzone17": alarmzone17,
       "alarmzonename17": alarmzonename17,
       "alarmzonestate17": alarmzonestate17,
       "alarmzonealarm117": alarmzonealarm117,
       "alarmzone18": alarmzone18,
       "alarmzonename18": alarmzonename18,
       "alarmzonestate18": alarmzonestate18,
       "alarmzonealarm118": alarmzonealarm118,
       "alarmzone19": alarmzone19,
       "alarmzonename19": alarmzonename19,
       "alarmzonestate19": alarmzonestate19,
       "alarmzonealarm119": alarmzonealarm119,
       "alarmzone20": alarmzone20,
       "alarmzonename20": alarmzonename20,
       "alarmzonestate20": alarmzonestate20,
       "alarmzonealarm120": alarmzonealarm120,
       "alarmzone21": alarmzone21,
       "alarmzonename21": alarmzonename21,
       "alarmzonestate21": alarmzonestate21,
       "alarmzonealarm121": alarmzonealarm121,
       "alarmzone22": alarmzone22,
       "alarmzonename22": alarmzonename22,
       "alarmzonestate22": alarmzonestate22,
       "alarmzonealarm122": alarmzonealarm122,
       "alarmzone23": alarmzone23,
       "alarmzonename23": alarmzonename23,
       "alarmzonestate23": alarmzonestate23,
       "alarmzonealarm123": alarmzonealarm123,
       "alarmzone24": alarmzone24,
       "alarmzonename24": alarmzonename24,
       "alarmzonestate24": alarmzonestate24,
       "alarmzonealarm124": alarmzonealarm124,
       "alarmzone25": alarmzone25,
       "alarmzonename25": alarmzonename25,
       "alarmzonestate25": alarmzonestate25,
       "alarmzonealarm125": alarmzonealarm125,
       "alarmzone26": alarmzone26,
       "alarmzonename26": alarmzonename26,
       "alarmzonestate26": alarmzonestate26,
       "alarmzonealarm126": alarmzonealarm126,
       "alarmzone27": alarmzone27,
       "alarmzonename27": alarmzonename27,
       "alarmzonestate27": alarmzonestate27,
       "alarmzonealarm127": alarmzonealarm127,
       "alarmzone28": alarmzone28,
       "alarmzonename28": alarmzonename28,
       "alarmzonestate28": alarmzonestate28,
       "alarmzonealarm128": alarmzonealarm128,
       "alarmzone29": alarmzone29,
       "alarmzonename29": alarmzonename29,
       "alarmzonestate29": alarmzonestate29,
       "alarmzonealarm129": alarmzonealarm129,
       "alarmzone30": alarmzone30,
       "alarmzonename30": alarmzonename30,
       "alarmzonestate30": alarmzonestate30,
       "alarmzonealarm130": alarmzonealarm130,
       "alarmText": alarmText}
)
