# SNMP MIB module (RL8200-ACU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/radeus_47773/RL8200-ACU-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:49:38 2025
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

(rl8200acu,) = mibBuilder.importSymbols(
    "RADEUS-LABS-PRODUCTS-MIB",
    "rl8200acu")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rl8200AcuMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1)
)
if mibBuilder.loadTexts:
    rl8200AcuMib.setRevisions(
        ("2016-05-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Rl8200AngleTC(TextualConvention, Integer32):
    status = "current"
    displayHint = "d-6"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-360000000, 360000000),
    )



class Rl8200MillisecondsTC(TextualConvention, Unsigned32):
    status = "current"


class Rl8200MotorDriveStatusTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("onRev", -1),
          ("off", 0),
          ("onFwd", 1))
    )



class Rl8200TargetsTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("immediate", 2),
          ("target1", 3),
          ("target2", 4),
          ("target3", 5),
          ("target4", 6),
          ("target5", 7),
          ("target6", 8),
          ("target7", 9),
          ("target8", 10),
          ("target9", 11),
          ("target10", 12),
          ("target11", 13),
          ("target12", 14),
          ("target13", 15),
          ("target14", 16),
          ("target15", 17),
          ("target16", 18),
          ("target17", 19),
          ("target18", 20),
          ("target19", 21),
          ("target20", 22),
          ("target21", 23),
          ("target22", 24),
          ("target23", 25),
          ("target24", 26),
          ("target25", 27),
          ("target26", 28),
          ("target27", 29),
          ("target28", 30),
          ("target29", 31),
          ("target30", 32),
          ("target31", 33),
          ("target32", 34),
          ("target33", 35),
          ("target34", 36),
          ("target35", 37),
          ("target36", 38),
          ("target37", 39),
          ("target38", 40),
          ("target39", 41),
          ("target40", 42),
          ("target41", 43),
          ("target42", 44),
          ("target43", 45),
          ("target44", 46),
          ("target45", 47),
          ("target46", 48),
          ("target47", 49),
          ("target48", 50),
          ("target49", 51),
          ("target50", 52),
          ("target51", 53),
          ("target52", 54),
          ("target53", 55),
          ("target54", 56),
          ("target55", 57),
          ("target56", 58),
          ("target57", 59),
          ("target58", 60),
          ("target59", 61),
          ("target60", 62),
          ("target61", 63),
          ("target62", 64),
          ("target63", 65),
          ("target64", 66),
          ("target65", 67),
          ("target66", 68),
          ("target67", 69),
          ("target68", 70),
          ("target69", 71),
          ("target70", 72),
          ("target71", 73),
          ("target72", 74),
          ("target73", 75),
          ("target74", 76),
          ("target75", 77),
          ("target76", 78),
          ("target77", 79),
          ("target78", 80),
          ("target79", 81),
          ("target80", 82),
          ("target81", 83),
          ("target82", 84),
          ("target83", 85),
          ("target84", 86),
          ("target85", 87),
          ("target86", 88),
          ("target87", 89),
          ("target88", 90),
          ("target89", 91),
          ("target90", 92),
          ("target91", 93),
          ("target92", 94),
          ("target93", 95),
          ("target94", 96),
          ("target95", 97),
          ("target96", 98),
          ("target97", 99),
          ("target98", 100))
    )



class Rl8200FaultsTC(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("azRunaway", 0),
          ("azImmobile", 1),
          ("azReversed", 2),
          ("azEncoderFault", 3),
          ("azCcwSoftTravelLimit", 4),
          ("azCwSoftTravelLimit", 5),
          ("azMotorControllerFault", 6),
          ("azTravelLimitSwitchTripped", 7),
          ("elRunaway", 8),
          ("elImmobile", 9),
          ("elReversed", 10),
          ("elEncoderFault", 11),
          ("elLowerSoftTravelLimit", 12),
          ("elUpperSoftTravelLimit", 13),
          ("elMotorControllerFault", 14),
          ("elTravelLimitSwitchTripped", 15),
          ("polRunaway", 16),
          ("polImmobile", 17),
          ("polReversed", 18),
          ("polEncoderFault", 19),
          ("polCcwSoftTravelLimit", 20),
          ("polCwSoftTravelLimit", 21),
          ("polTravelLimitSwitchTripped", 22),
          ("emergencyStopPressed", 23),
          ("driveDisabledAtControlPanel", 24),
          ("maintOverrideAtDriveCabinet", 25),
          ("softTravelLimitDisabled", 26),
          ("travelLimitSwitchTripped", 27),
          ("noPowerAtDriveCabinet", 28),
          ("lowTrackingSignalLevel", 29),
          ("unstableTrackingSignalLevel", 30),
          ("iocCommFailure", 31),
          ("encCommFailure", 32),
          ("rdcCommFailure", 33),
          ("fpCommFailure", 34),
          ("iocFwUpdateFailed", 35),
          ("encFwUpdateFailed", 36),
          ("rdcFwUpdateFailed", 37),
          ("jpFwUpdateFailed", 38),
          ("cantAccessSettingsFile", 39),
          ("cantAccessTrackingHistFile", 40),
          ("receiverCommFailure", 41),
          ("receiverNotRunning", 42),
          ("receiverNotLocked", 43),
          ("usbIoInterfaceId1NotFound", 44),
          ("usbIoInterfaceId2NotFound", 45),
          ("beaconFreqOutOfRange", 46),
          ("ioc2CommFailure", 47),
          ("ioc2FwUpdateFailed", 48),
          ("polSelFailure", 49),
          ("tleEpoch", 50))
    )


class Rl8200InitiateTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              1)
        )
    )
    namedValues = NamedValues(
        *(("undefined", -1),
          ("initiate", 1))
    )



class Rl8200EnabledTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 0),
          ("disabled", 1))
    )



# MIB Managed Objects in the order of their OIDs

_Rl8200MibObjects_ObjectIdentity = ObjectIdentity
rl8200MibObjects = _Rl8200MibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1)
)
_Rl8200SettingsDatabaseVars_ObjectIdentity = ObjectIdentity
rl8200SettingsDatabaseVars = _Rl8200SettingsDatabaseVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 1)
)
_Rl8200DatabaseVersion_Type = Integer32
_Rl8200DatabaseVersion_Object = MibScalar
rl8200DatabaseVersion = _Rl8200DatabaseVersion_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 1, 1),
    _Rl8200DatabaseVersion_Type()
)
rl8200DatabaseVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rl8200DatabaseVersion.setStatus("current")


class _Rl8200DatabaseTimestamp_Type(OctetString):
    """Custom type rl8200DatabaseTimestamp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_Rl8200DatabaseTimestamp_Type.__name__ = "OctetString"
_Rl8200DatabaseTimestamp_Object = MibScalar
rl8200DatabaseTimestamp = _Rl8200DatabaseTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 1, 2),
    _Rl8200DatabaseTimestamp_Type()
)
rl8200DatabaseTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rl8200DatabaseTimestamp.setStatus("current")
if mibBuilder.loadTexts:
    rl8200DatabaseTimestamp.setUnits("100 ns")
_Rl8200AntennaPositionVars_ObjectIdentity = ObjectIdentity
rl8200AntennaPositionVars = _Rl8200AntennaPositionVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2)
)
_Rl8200SoftTravelLimitCwAz_Type = Rl8200AngleTC
_Rl8200SoftTravelLimitCwAz_Object = MibScalar
rl8200SoftTravelLimitCwAz = _Rl8200SoftTravelLimitCwAz_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 1),
    _Rl8200SoftTravelLimitCwAz_Type()
)
rl8200SoftTravelLimitCwAz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200SoftTravelLimitCwAz.setStatus("current")
if mibBuilder.loadTexts:
    rl8200SoftTravelLimitCwAz.setUnits("10e-6 degrees")
_Rl8200SoftTravelLimitCwEl_Type = Rl8200AngleTC
_Rl8200SoftTravelLimitCwEl_Object = MibScalar
rl8200SoftTravelLimitCwEl = _Rl8200SoftTravelLimitCwEl_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 2),
    _Rl8200SoftTravelLimitCwEl_Type()
)
rl8200SoftTravelLimitCwEl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200SoftTravelLimitCwEl.setStatus("current")
if mibBuilder.loadTexts:
    rl8200SoftTravelLimitCwEl.setUnits("10e-6 degrees")
_Rl8200SoftTravelLimitCwPol1_Type = Rl8200AngleTC
_Rl8200SoftTravelLimitCwPol1_Object = MibScalar
rl8200SoftTravelLimitCwPol1 = _Rl8200SoftTravelLimitCwPol1_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 3),
    _Rl8200SoftTravelLimitCwPol1_Type()
)
rl8200SoftTravelLimitCwPol1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200SoftTravelLimitCwPol1.setStatus("current")
if mibBuilder.loadTexts:
    rl8200SoftTravelLimitCwPol1.setUnits("10e-6 degrees")
_Rl8200SoftTravelLimitCwPol2_Type = Rl8200AngleTC
_Rl8200SoftTravelLimitCwPol2_Object = MibScalar
rl8200SoftTravelLimitCwPol2 = _Rl8200SoftTravelLimitCwPol2_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 4),
    _Rl8200SoftTravelLimitCwPol2_Type()
)
rl8200SoftTravelLimitCwPol2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200SoftTravelLimitCwPol2.setStatus("current")
if mibBuilder.loadTexts:
    rl8200SoftTravelLimitCwPol2.setUnits("10e-6 degrees")
_Rl8200SoftTravelLimitCcwAz_Type = Rl8200AngleTC
_Rl8200SoftTravelLimitCcwAz_Object = MibScalar
rl8200SoftTravelLimitCcwAz = _Rl8200SoftTravelLimitCcwAz_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 5),
    _Rl8200SoftTravelLimitCcwAz_Type()
)
rl8200SoftTravelLimitCcwAz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200SoftTravelLimitCcwAz.setStatus("current")
if mibBuilder.loadTexts:
    rl8200SoftTravelLimitCcwAz.setUnits("10e-6 degrees")
_Rl8200SoftTravelLimitCcwEl_Type = Rl8200AngleTC
_Rl8200SoftTravelLimitCcwEl_Object = MibScalar
rl8200SoftTravelLimitCcwEl = _Rl8200SoftTravelLimitCcwEl_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 6),
    _Rl8200SoftTravelLimitCcwEl_Type()
)
rl8200SoftTravelLimitCcwEl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200SoftTravelLimitCcwEl.setStatus("current")
if mibBuilder.loadTexts:
    rl8200SoftTravelLimitCcwEl.setUnits("10e-6 degrees")
_Rl8200SoftTravelLimitCcwPol1_Type = Rl8200AngleTC
_Rl8200SoftTravelLimitCcwPol1_Object = MibScalar
rl8200SoftTravelLimitCcwPol1 = _Rl8200SoftTravelLimitCcwPol1_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 7),
    _Rl8200SoftTravelLimitCcwPol1_Type()
)
rl8200SoftTravelLimitCcwPol1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200SoftTravelLimitCcwPol1.setStatus("current")
if mibBuilder.loadTexts:
    rl8200SoftTravelLimitCcwPol1.setUnits("10e-6 degrees")
_Rl8200SoftTravelLimitCcwPol2_Type = Rl8200AngleTC
_Rl8200SoftTravelLimitCcwPol2_Object = MibScalar
rl8200SoftTravelLimitCcwPol2 = _Rl8200SoftTravelLimitCcwPol2_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 8),
    _Rl8200SoftTravelLimitCcwPol2_Type()
)
rl8200SoftTravelLimitCcwPol2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200SoftTravelLimitCcwPol2.setStatus("current")
if mibBuilder.loadTexts:
    rl8200SoftTravelLimitCcwPol2.setUnits("10e-6 degrees")


class _Rl8200SoftTravelLimitEnabled_Type(Rl8200EnabledTC):
    """Custom type rl8200SoftTravelLimitEnabled based on Rl8200EnabledTC"""
    defaultValue = 0


_Rl8200SoftTravelLimitEnabled_Type.__name__ = "Rl8200EnabledTC"
_Rl8200SoftTravelLimitEnabled_Object = MibScalar
rl8200SoftTravelLimitEnabled = _Rl8200SoftTravelLimitEnabled_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 9),
    _Rl8200SoftTravelLimitEnabled_Type()
)
rl8200SoftTravelLimitEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200SoftTravelLimitEnabled.setStatus("current")


class _Rl8200PolarizationType_Type(Integer32):
    """Custom type rl8200PolarizationType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("circular", 0),
          ("linear1Pol", 1),
          ("linear2Pol", 2))
    )


_Rl8200PolarizationType_Type.__name__ = "Integer32"
_Rl8200PolarizationType_Object = MibScalar
rl8200PolarizationType = _Rl8200PolarizationType_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 10),
    _Rl8200PolarizationType_Type()
)
rl8200PolarizationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200PolarizationType.setStatus("current")
_Rl8200SlewAz_Type = Rl8200AngleTC
_Rl8200SlewAz_Object = MibScalar
rl8200SlewAz = _Rl8200SlewAz_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 11),
    _Rl8200SlewAz_Type()
)
rl8200SlewAz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200SlewAz.setStatus("current")
if mibBuilder.loadTexts:
    rl8200SlewAz.setUnits("10e-6 degrees")
_Rl8200SlewEl_Type = Rl8200AngleTC
_Rl8200SlewEl_Object = MibScalar
rl8200SlewEl = _Rl8200SlewEl_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 12),
    _Rl8200SlewEl_Type()
)
rl8200SlewEl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200SlewEl.setStatus("current")
if mibBuilder.loadTexts:
    rl8200SlewEl.setUnits("10e-6 degrees")
_Rl8200SlewCoastTimeAz_Type = Rl8200MillisecondsTC
_Rl8200SlewCoastTimeAz_Object = MibScalar
rl8200SlewCoastTimeAz = _Rl8200SlewCoastTimeAz_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 13),
    _Rl8200SlewCoastTimeAz_Type()
)
rl8200SlewCoastTimeAz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200SlewCoastTimeAz.setStatus("current")
if mibBuilder.loadTexts:
    rl8200SlewCoastTimeAz.setUnits("ms")
_Rl8200SlewCoastTimeEl_Type = Rl8200MillisecondsTC
_Rl8200SlewCoastTimeEl_Object = MibScalar
rl8200SlewCoastTimeEl = _Rl8200SlewCoastTimeEl_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 14),
    _Rl8200SlewCoastTimeEl_Type()
)
rl8200SlewCoastTimeEl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200SlewCoastTimeEl.setStatus("current")
if mibBuilder.loadTexts:
    rl8200SlewCoastTimeEl.setUnits("ms")
_Rl8200TrackCoastTimeAz_Type = Rl8200MillisecondsTC
_Rl8200TrackCoastTimeAz_Object = MibScalar
rl8200TrackCoastTimeAz = _Rl8200TrackCoastTimeAz_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 15),
    _Rl8200TrackCoastTimeAz_Type()
)
rl8200TrackCoastTimeAz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TrackCoastTimeAz.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TrackCoastTimeAz.setUnits("ms")
_Rl8200TrackCoastTimeEl_Type = Rl8200MillisecondsTC
_Rl8200TrackCoastTimeEl_Object = MibScalar
rl8200TrackCoastTimeEl = _Rl8200TrackCoastTimeEl_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 16),
    _Rl8200TrackCoastTimeEl_Type()
)
rl8200TrackCoastTimeEl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TrackCoastTimeEl.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TrackCoastTimeEl.setUnits("ms")
_Rl8200TrackCoastTimePol1_Type = Rl8200MillisecondsTC
_Rl8200TrackCoastTimePol1_Object = MibScalar
rl8200TrackCoastTimePol1 = _Rl8200TrackCoastTimePol1_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 17),
    _Rl8200TrackCoastTimePol1_Type()
)
rl8200TrackCoastTimePol1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TrackCoastTimePol1.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TrackCoastTimePol1.setUnits("ms")
_Rl8200TrackCoastTimePol2_Type = Rl8200MillisecondsTC
_Rl8200TrackCoastTimePol2_Object = MibScalar
rl8200TrackCoastTimePol2 = _Rl8200TrackCoastTimePol2_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 18),
    _Rl8200TrackCoastTimePol2_Type()
)
rl8200TrackCoastTimePol2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TrackCoastTimePol2.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TrackCoastTimePol2.setUnits("ms")
_Rl8200PositionDeadbandAz_Type = Rl8200AngleTC
_Rl8200PositionDeadbandAz_Object = MibScalar
rl8200PositionDeadbandAz = _Rl8200PositionDeadbandAz_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 19),
    _Rl8200PositionDeadbandAz_Type()
)
rl8200PositionDeadbandAz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200PositionDeadbandAz.setStatus("current")
if mibBuilder.loadTexts:
    rl8200PositionDeadbandAz.setUnits("10e-6 degrees")
_Rl8200PositionDeadbandEl_Type = Rl8200AngleTC
_Rl8200PositionDeadbandEl_Object = MibScalar
rl8200PositionDeadbandEl = _Rl8200PositionDeadbandEl_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 20),
    _Rl8200PositionDeadbandEl_Type()
)
rl8200PositionDeadbandEl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200PositionDeadbandEl.setStatus("current")
if mibBuilder.loadTexts:
    rl8200PositionDeadbandEl.setUnits("10e-6 degrees")
_Rl8200PositionDeadbandPol1_Type = Rl8200AngleTC
_Rl8200PositionDeadbandPol1_Object = MibScalar
rl8200PositionDeadbandPol1 = _Rl8200PositionDeadbandPol1_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 21),
    _Rl8200PositionDeadbandPol1_Type()
)
rl8200PositionDeadbandPol1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200PositionDeadbandPol1.setStatus("current")
if mibBuilder.loadTexts:
    rl8200PositionDeadbandPol1.setUnits("10e-6 degrees")
_Rl8200PositionDeadbandPol2_Type = Rl8200AngleTC
_Rl8200PositionDeadbandPol2_Object = MibScalar
rl8200PositionDeadbandPol2 = _Rl8200PositionDeadbandPol2_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 22),
    _Rl8200PositionDeadbandPol2_Type()
)
rl8200PositionDeadbandPol2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200PositionDeadbandPol2.setStatus("current")
if mibBuilder.loadTexts:
    rl8200PositionDeadbandPol2.setUnits("10e-6 degrees")
_Rl8200BumpTimeAz_Type = Rl8200MillisecondsTC
_Rl8200BumpTimeAz_Object = MibScalar
rl8200BumpTimeAz = _Rl8200BumpTimeAz_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 23),
    _Rl8200BumpTimeAz_Type()
)
rl8200BumpTimeAz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200BumpTimeAz.setStatus("current")
if mibBuilder.loadTexts:
    rl8200BumpTimeAz.setUnits("ms")
_Rl8200BumpTimeEl_Type = Rl8200MillisecondsTC
_Rl8200BumpTimeEl_Object = MibScalar
rl8200BumpTimeEl = _Rl8200BumpTimeEl_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 24),
    _Rl8200BumpTimeEl_Type()
)
rl8200BumpTimeEl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200BumpTimeEl.setStatus("current")
if mibBuilder.loadTexts:
    rl8200BumpTimeEl.setUnits("ms")
_Rl8200BumpTimePol1_Type = Rl8200MillisecondsTC
_Rl8200BumpTimePol1_Object = MibScalar
rl8200BumpTimePol1 = _Rl8200BumpTimePol1_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 25),
    _Rl8200BumpTimePol1_Type()
)
rl8200BumpTimePol1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200BumpTimePol1.setStatus("current")
if mibBuilder.loadTexts:
    rl8200BumpTimePol1.setUnits("ms")
_Rl8200BumpTimePol2_Type = Rl8200MillisecondsTC
_Rl8200BumpTimePol2_Object = MibScalar
rl8200BumpTimePol2 = _Rl8200BumpTimePol2_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 26),
    _Rl8200BumpTimePol2_Type()
)
rl8200BumpTimePol2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200BumpTimePol2.setStatus("current")
if mibBuilder.loadTexts:
    rl8200BumpTimePol2.setUnits("ms")
_Rl8200BumpOffTimeAz_Type = Rl8200MillisecondsTC
_Rl8200BumpOffTimeAz_Object = MibScalar
rl8200BumpOffTimeAz = _Rl8200BumpOffTimeAz_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 27),
    _Rl8200BumpOffTimeAz_Type()
)
rl8200BumpOffTimeAz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200BumpOffTimeAz.setStatus("current")
if mibBuilder.loadTexts:
    rl8200BumpOffTimeAz.setUnits("ms")
_Rl8200BumpOffTimeEl_Type = Rl8200MillisecondsTC
_Rl8200BumpOffTimeEl_Object = MibScalar
rl8200BumpOffTimeEl = _Rl8200BumpOffTimeEl_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 28),
    _Rl8200BumpOffTimeEl_Type()
)
rl8200BumpOffTimeEl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200BumpOffTimeEl.setStatus("current")
if mibBuilder.loadTexts:
    rl8200BumpOffTimeEl.setUnits("ms")
_Rl8200BumpOffTimePol1_Type = Rl8200MillisecondsTC
_Rl8200BumpOffTimePol1_Object = MibScalar
rl8200BumpOffTimePol1 = _Rl8200BumpOffTimePol1_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 29),
    _Rl8200BumpOffTimePol1_Type()
)
rl8200BumpOffTimePol1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200BumpOffTimePol1.setStatus("current")
if mibBuilder.loadTexts:
    rl8200BumpOffTimePol1.setUnits("ms")
_Rl8200BumpOffTimePol2_Type = Rl8200MillisecondsTC
_Rl8200BumpOffTimePol2_Object = MibScalar
rl8200BumpOffTimePol2 = _Rl8200BumpOffTimePol2_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 30),
    _Rl8200BumpOffTimePol2_Type()
)
rl8200BumpOffTimePol2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200BumpOffTimePol2.setStatus("current")
if mibBuilder.loadTexts:
    rl8200BumpOffTimePol2.setUnits("ms")
_Rl8200OffsetAz_Type = Rl8200AngleTC
_Rl8200OffsetAz_Object = MibScalar
rl8200OffsetAz = _Rl8200OffsetAz_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 31),
    _Rl8200OffsetAz_Type()
)
rl8200OffsetAz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200OffsetAz.setStatus("current")
if mibBuilder.loadTexts:
    rl8200OffsetAz.setUnits("10e-6 degrees")
_Rl8200OffsetEl_Type = Rl8200AngleTC
_Rl8200OffsetEl_Object = MibScalar
rl8200OffsetEl = _Rl8200OffsetEl_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 32),
    _Rl8200OffsetEl_Type()
)
rl8200OffsetEl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200OffsetEl.setStatus("current")
if mibBuilder.loadTexts:
    rl8200OffsetEl.setUnits("10e-6 degrees")
_Rl8200OffsetPol1_Type = Rl8200AngleTC
_Rl8200OffsetPol1_Object = MibScalar
rl8200OffsetPol1 = _Rl8200OffsetPol1_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 33),
    _Rl8200OffsetPol1_Type()
)
rl8200OffsetPol1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200OffsetPol1.setStatus("current")
if mibBuilder.loadTexts:
    rl8200OffsetPol1.setUnits("10e-6 degrees")
_Rl8200OffsetPol2_Type = Rl8200AngleTC
_Rl8200OffsetPol2_Object = MibScalar
rl8200OffsetPol2 = _Rl8200OffsetPol2_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 34),
    _Rl8200OffsetPol2_Type()
)
rl8200OffsetPol2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200OffsetPol2.setStatus("current")
if mibBuilder.loadTexts:
    rl8200OffsetPol2.setUnits("10e-6 degrees")
_Rl8200ReverseCountSenseAz_Type = TruthValue
_Rl8200ReverseCountSenseAz_Object = MibScalar
rl8200ReverseCountSenseAz = _Rl8200ReverseCountSenseAz_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 35),
    _Rl8200ReverseCountSenseAz_Type()
)
rl8200ReverseCountSenseAz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200ReverseCountSenseAz.setStatus("current")
_Rl8200ReverseCountSenseEl_Type = TruthValue
_Rl8200ReverseCountSenseEl_Object = MibScalar
rl8200ReverseCountSenseEl = _Rl8200ReverseCountSenseEl_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 36),
    _Rl8200ReverseCountSenseEl_Type()
)
rl8200ReverseCountSenseEl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200ReverseCountSenseEl.setStatus("current")
_Rl8200ReverseCountSensePol1_Type = TruthValue
_Rl8200ReverseCountSensePol1_Object = MibScalar
rl8200ReverseCountSensePol1 = _Rl8200ReverseCountSensePol1_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 37),
    _Rl8200ReverseCountSensePol1_Type()
)
rl8200ReverseCountSensePol1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200ReverseCountSensePol1.setStatus("current")
_Rl8200ReverseCountSensePol2_Type = TruthValue
_Rl8200ReverseCountSensePol2_Object = MibScalar
rl8200ReverseCountSensePol2 = _Rl8200ReverseCountSensePol2_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 38),
    _Rl8200ReverseCountSensePol2_Type()
)
rl8200ReverseCountSensePol2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200ReverseCountSensePol2.setStatus("current")


class _Rl8200FaultTestPeriodAz_Type(Rl8200MillisecondsTC):
    """Custom type rl8200FaultTestPeriodAz based on Rl8200MillisecondsTC"""
    subtypeSpec = Rl8200MillisecondsTC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_Rl8200FaultTestPeriodAz_Type.__name__ = "Rl8200MillisecondsTC"
_Rl8200FaultTestPeriodAz_Object = MibScalar
rl8200FaultTestPeriodAz = _Rl8200FaultTestPeriodAz_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 39),
    _Rl8200FaultTestPeriodAz_Type()
)
rl8200FaultTestPeriodAz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200FaultTestPeriodAz.setStatus("current")
if mibBuilder.loadTexts:
    rl8200FaultTestPeriodAz.setUnits("ms")


class _Rl8200FaultTestPeriodEl_Type(Rl8200MillisecondsTC):
    """Custom type rl8200FaultTestPeriodEl based on Rl8200MillisecondsTC"""
    subtypeSpec = Rl8200MillisecondsTC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_Rl8200FaultTestPeriodEl_Type.__name__ = "Rl8200MillisecondsTC"
_Rl8200FaultTestPeriodEl_Object = MibScalar
rl8200FaultTestPeriodEl = _Rl8200FaultTestPeriodEl_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 40),
    _Rl8200FaultTestPeriodEl_Type()
)
rl8200FaultTestPeriodEl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200FaultTestPeriodEl.setStatus("current")
if mibBuilder.loadTexts:
    rl8200FaultTestPeriodEl.setUnits("ms")


class _Rl8200FaultTestPeriodPol1_Type(Rl8200MillisecondsTC):
    """Custom type rl8200FaultTestPeriodPol1 based on Rl8200MillisecondsTC"""
    subtypeSpec = Rl8200MillisecondsTC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_Rl8200FaultTestPeriodPol1_Type.__name__ = "Rl8200MillisecondsTC"
_Rl8200FaultTestPeriodPol1_Object = MibScalar
rl8200FaultTestPeriodPol1 = _Rl8200FaultTestPeriodPol1_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 41),
    _Rl8200FaultTestPeriodPol1_Type()
)
rl8200FaultTestPeriodPol1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200FaultTestPeriodPol1.setStatus("current")
if mibBuilder.loadTexts:
    rl8200FaultTestPeriodPol1.setUnits("ms")


class _Rl8200FaultTestPeriodPol2_Type(Rl8200MillisecondsTC):
    """Custom type rl8200FaultTestPeriodPol2 based on Rl8200MillisecondsTC"""
    subtypeSpec = Rl8200MillisecondsTC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_Rl8200FaultTestPeriodPol2_Type.__name__ = "Rl8200MillisecondsTC"
_Rl8200FaultTestPeriodPol2_Object = MibScalar
rl8200FaultTestPeriodPol2 = _Rl8200FaultTestPeriodPol2_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 42),
    _Rl8200FaultTestPeriodPol2_Type()
)
rl8200FaultTestPeriodPol2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200FaultTestPeriodPol2.setStatus("current")
if mibBuilder.loadTexts:
    rl8200FaultTestPeriodPol2.setUnits("ms")
_Rl8200MotionAz_Type = Rl8200AngleTC
_Rl8200MotionAz_Object = MibScalar
rl8200MotionAz = _Rl8200MotionAz_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 43),
    _Rl8200MotionAz_Type()
)
rl8200MotionAz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200MotionAz.setStatus("current")
if mibBuilder.loadTexts:
    rl8200MotionAz.setUnits("10e-6 degrees")
_Rl8200OMotionEl_Type = Rl8200AngleTC
_Rl8200OMotionEl_Object = MibScalar
rl8200OMotionEl = _Rl8200OMotionEl_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 44),
    _Rl8200OMotionEl_Type()
)
rl8200OMotionEl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200OMotionEl.setStatus("current")
if mibBuilder.loadTexts:
    rl8200OMotionEl.setUnits("10e-6 degrees")
_Rl8200MotionPol1_Type = Rl8200AngleTC
_Rl8200MotionPol1_Object = MibScalar
rl8200MotionPol1 = _Rl8200MotionPol1_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 45),
    _Rl8200MotionPol1_Type()
)
rl8200MotionPol1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200MotionPol1.setStatus("current")
if mibBuilder.loadTexts:
    rl8200MotionPol1.setUnits("10e-6 degrees")
_Rl8200MotionPol2_Type = Rl8200AngleTC
_Rl8200MotionPol2_Object = MibScalar
rl8200MotionPol2 = _Rl8200MotionPol2_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 46),
    _Rl8200MotionPol2_Type()
)
rl8200MotionPol2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200MotionPol2.setStatus("current")
if mibBuilder.loadTexts:
    rl8200MotionPol2.setUnits("10e-6 degrees")
_Rl8200RunawayAz_Type = Rl8200AngleTC
_Rl8200RunawayAz_Object = MibScalar
rl8200RunawayAz = _Rl8200RunawayAz_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 47),
    _Rl8200RunawayAz_Type()
)
rl8200RunawayAz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200RunawayAz.setStatus("current")
if mibBuilder.loadTexts:
    rl8200RunawayAz.setUnits("10e-6 degrees")
_Rl8200ORunawayEl_Type = Rl8200AngleTC
_Rl8200ORunawayEl_Object = MibScalar
rl8200ORunawayEl = _Rl8200ORunawayEl_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 48),
    _Rl8200ORunawayEl_Type()
)
rl8200ORunawayEl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200ORunawayEl.setStatus("current")
if mibBuilder.loadTexts:
    rl8200ORunawayEl.setUnits("10e-6 degrees")
_Rl8200RunawayPol1_Type = Rl8200AngleTC
_Rl8200RunawayPol1_Object = MibScalar
rl8200RunawayPol1 = _Rl8200RunawayPol1_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 49),
    _Rl8200RunawayPol1_Type()
)
rl8200RunawayPol1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200RunawayPol1.setStatus("current")
if mibBuilder.loadTexts:
    rl8200RunawayPol1.setUnits("10e-6 degrees")
_Rl8200RunawayPol2_Type = Rl8200AngleTC
_Rl8200RunawayPol2_Object = MibScalar
rl8200RunawayPol2 = _Rl8200RunawayPol2_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 2, 50),
    _Rl8200RunawayPol2_Type()
)
rl8200RunawayPol2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200RunawayPol2.setStatus("current")
if mibBuilder.loadTexts:
    rl8200RunawayPol2.setUnits("10e-6 degrees")
_Rl8200StatusVars_ObjectIdentity = ObjectIdentity
rl8200StatusVars = _Rl8200StatusVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 3)
)
_Rl8200ActualPositionAz_Type = Rl8200AngleTC
_Rl8200ActualPositionAz_Object = MibScalar
rl8200ActualPositionAz = _Rl8200ActualPositionAz_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 3, 1),
    _Rl8200ActualPositionAz_Type()
)
rl8200ActualPositionAz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rl8200ActualPositionAz.setStatus("current")
if mibBuilder.loadTexts:
    rl8200ActualPositionAz.setUnits("10e-6 degrees")
_Rl8200ActualPositionEl_Type = Rl8200AngleTC
_Rl8200ActualPositionEl_Object = MibScalar
rl8200ActualPositionEl = _Rl8200ActualPositionEl_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 3, 2),
    _Rl8200ActualPositionEl_Type()
)
rl8200ActualPositionEl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rl8200ActualPositionEl.setStatus("current")
if mibBuilder.loadTexts:
    rl8200ActualPositionEl.setUnits("10e-6 degrees")
_Rl8200ActualPositionPol1_Type = Rl8200AngleTC
_Rl8200ActualPositionPol1_Object = MibScalar
rl8200ActualPositionPol1 = _Rl8200ActualPositionPol1_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 3, 3),
    _Rl8200ActualPositionPol1_Type()
)
rl8200ActualPositionPol1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rl8200ActualPositionPol1.setStatus("current")
if mibBuilder.loadTexts:
    rl8200ActualPositionPol1.setUnits("10e-6 degrees")
_Rl8200ActualPositionPol2_Type = Rl8200AngleTC
_Rl8200ActualPositionPol2_Object = MibScalar
rl8200ActualPositionPol2 = _Rl8200ActualPositionPol2_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 3, 4),
    _Rl8200ActualPositionPol2_Type()
)
rl8200ActualPositionPol2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rl8200ActualPositionPol2.setStatus("current")
if mibBuilder.loadTexts:
    rl8200ActualPositionPol2.setUnits("10e-6 degrees")
_Rl8200CommandPositionAz_Type = Rl8200AngleTC
_Rl8200CommandPositionAz_Object = MibScalar
rl8200CommandPositionAz = _Rl8200CommandPositionAz_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 3, 5),
    _Rl8200CommandPositionAz_Type()
)
rl8200CommandPositionAz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rl8200CommandPositionAz.setStatus("current")
if mibBuilder.loadTexts:
    rl8200CommandPositionAz.setUnits("10e-6 degrees")
_Rl8200CommandPositionEl_Type = Rl8200AngleTC
_Rl8200CommandPositionEl_Object = MibScalar
rl8200CommandPositionEl = _Rl8200CommandPositionEl_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 3, 6),
    _Rl8200CommandPositionEl_Type()
)
rl8200CommandPositionEl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rl8200CommandPositionEl.setStatus("current")
if mibBuilder.loadTexts:
    rl8200CommandPositionEl.setUnits("10e-6 degrees")
_Rl8200CommandPositionPol1_Type = Rl8200AngleTC
_Rl8200CommandPositionPol1_Object = MibScalar
rl8200CommandPositionPol1 = _Rl8200CommandPositionPol1_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 3, 7),
    _Rl8200CommandPositionPol1_Type()
)
rl8200CommandPositionPol1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rl8200CommandPositionPol1.setStatus("current")
if mibBuilder.loadTexts:
    rl8200CommandPositionPol1.setUnits("10e-6 degrees")
_Rl8200CommandPositionPol2_Type = Rl8200AngleTC
_Rl8200CommandPositionPol2_Object = MibScalar
rl8200CommandPositionPol2 = _Rl8200CommandPositionPol2_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 3, 8),
    _Rl8200CommandPositionPol2_Type()
)
rl8200CommandPositionPol2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rl8200CommandPositionPol2.setStatus("current")
if mibBuilder.loadTexts:
    rl8200CommandPositionPol2.setUnits("10e-6 degrees")
_Rl8200TargetPositionAz_Type = Rl8200AngleTC
_Rl8200TargetPositionAz_Object = MibScalar
rl8200TargetPositionAz = _Rl8200TargetPositionAz_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 3, 9),
    _Rl8200TargetPositionAz_Type()
)
rl8200TargetPositionAz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rl8200TargetPositionAz.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TargetPositionAz.setUnits("10e-6 degrees")
_Rl8200TargetPositionEl_Type = Rl8200AngleTC
_Rl8200TargetPositionEl_Object = MibScalar
rl8200TargetPositionEl = _Rl8200TargetPositionEl_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 3, 10),
    _Rl8200TargetPositionEl_Type()
)
rl8200TargetPositionEl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rl8200TargetPositionEl.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TargetPositionEl.setUnits("10e-6 degrees")
_Rl8200TargetPositionPol1_Type = Rl8200AngleTC
_Rl8200TargetPositionPol1_Object = MibScalar
rl8200TargetPositionPol1 = _Rl8200TargetPositionPol1_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 3, 11),
    _Rl8200TargetPositionPol1_Type()
)
rl8200TargetPositionPol1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rl8200TargetPositionPol1.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TargetPositionPol1.setUnits("10e-6 degrees")
_Rl8200TargetPositionPol2_Type = Rl8200AngleTC
_Rl8200TargetPositionPol2_Object = MibScalar
rl8200TargetPositionPol2 = _Rl8200TargetPositionPol2_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 3, 12),
    _Rl8200TargetPositionPol2_Type()
)
rl8200TargetPositionPol2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rl8200TargetPositionPol2.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TargetPositionPol2.setUnits("10e-6 degrees")
_Rl8200TargetAcquisitionStatus_Type = TruthValue
_Rl8200TargetAcquisitionStatus_Object = MibScalar
rl8200TargetAcquisitionStatus = _Rl8200TargetAcquisitionStatus_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 3, 13),
    _Rl8200TargetAcquisitionStatus_Type()
)
rl8200TargetAcquisitionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rl8200TargetAcquisitionStatus.setStatus("current")


class _Rl8200TrackingMode_Type(Integer32):
    """Custom type rl8200TrackingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("standby", 0),
          ("setup", 1),
          ("manual", 2),
          ("manualPeaking", 3),
          ("acquiring", 4),
          ("scanning", 5),
          ("holding", 6),
          ("ptModel", 7),
          ("ptWait", 8),
          ("ptPeakingAz", 9),
          ("ptPeakingEl", 10))
    )


_Rl8200TrackingMode_Type.__name__ = "Integer32"
_Rl8200TrackingMode_Object = MibScalar
rl8200TrackingMode = _Rl8200TrackingMode_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 3, 14),
    _Rl8200TrackingMode_Type()
)
rl8200TrackingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rl8200TrackingMode.setStatus("current")
_Rl8200MotorDriveStatusAz_Type = Rl8200MotorDriveStatusTC
_Rl8200MotorDriveStatusAz_Object = MibScalar
rl8200MotorDriveStatusAz = _Rl8200MotorDriveStatusAz_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 3, 15),
    _Rl8200MotorDriveStatusAz_Type()
)
rl8200MotorDriveStatusAz.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rl8200MotorDriveStatusAz.setStatus("current")
_Rl8200MotorDriveStatusEl_Type = Rl8200MotorDriveStatusTC
_Rl8200MotorDriveStatusEl_Object = MibScalar
rl8200MotorDriveStatusEl = _Rl8200MotorDriveStatusEl_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 3, 16),
    _Rl8200MotorDriveStatusEl_Type()
)
rl8200MotorDriveStatusEl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rl8200MotorDriveStatusEl.setStatus("current")
_Rl8200MotorDriveStatusPol1_Type = Rl8200MotorDriveStatusTC
_Rl8200MotorDriveStatusPol1_Object = MibScalar
rl8200MotorDriveStatusPol1 = _Rl8200MotorDriveStatusPol1_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 3, 17),
    _Rl8200MotorDriveStatusPol1_Type()
)
rl8200MotorDriveStatusPol1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rl8200MotorDriveStatusPol1.setStatus("current")
_Rl8200MotorDriveStatusPol2_Type = Rl8200MotorDriveStatusTC
_Rl8200MotorDriveStatusPol2_Object = MibScalar
rl8200MotorDriveStatusPol2 = _Rl8200MotorDriveStatusPol2_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 3, 18),
    _Rl8200MotorDriveStatusPol2_Type()
)
rl8200MotorDriveStatusPol2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rl8200MotorDriveStatusPol2.setStatus("current")
_Rl8200ReceivedSignalLevel_Type = Integer32
_Rl8200ReceivedSignalLevel_Object = MibScalar
rl8200ReceivedSignalLevel = _Rl8200ReceivedSignalLevel_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 3, 19),
    _Rl8200ReceivedSignalLevel_Type()
)
rl8200ReceivedSignalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rl8200ReceivedSignalLevel.setStatus("current")
if mibBuilder.loadTexts:
    rl8200ReceivedSignalLevel.setUnits("10e-6 dB")


class _Rl8200ReceiverInputSource_Type(Integer32):
    """Custom type rl8200ReceiverInputSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rf1", 0),
          ("rf2", 1))
    )


_Rl8200ReceiverInputSource_Type.__name__ = "Integer32"
_Rl8200ReceiverInputSource_Object = MibScalar
rl8200ReceiverInputSource = _Rl8200ReceiverInputSource_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 3, 20),
    _Rl8200ReceiverInputSource_Type()
)
rl8200ReceiverInputSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rl8200ReceiverInputSource.setStatus("current")
_Rl8200ReceiverBeaconFrequency_Type = Integer32
_Rl8200ReceiverBeaconFrequency_Object = MibScalar
rl8200ReceiverBeaconFrequency = _Rl8200ReceiverBeaconFrequency_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 3, 21),
    _Rl8200ReceiverBeaconFrequency_Type()
)
rl8200ReceiverBeaconFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rl8200ReceiverBeaconFrequency.setStatus("current")
if mibBuilder.loadTexts:
    rl8200ReceiverBeaconFrequency.setUnits("kHz")
_Rl8200AcknowledgedFaults_Type = Rl8200FaultsTC
_Rl8200AcknowledgedFaults_Object = MibScalar
rl8200AcknowledgedFaults = _Rl8200AcknowledgedFaults_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 3, 22),
    _Rl8200AcknowledgedFaults_Type()
)
rl8200AcknowledgedFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rl8200AcknowledgedFaults.setStatus("current")
_Rl8200UnacknowledgedFaults_Type = Rl8200FaultsTC
_Rl8200UnacknowledgedFaults_Object = MibScalar
rl8200UnacknowledgedFaults = _Rl8200UnacknowledgedFaults_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 3, 23),
    _Rl8200UnacknowledgedFaults_Type()
)
rl8200UnacknowledgedFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rl8200UnacknowledgedFaults.setStatus("current")
_Rl8200DateAndTime_Type = DateAndTime
_Rl8200DateAndTime_Object = MibScalar
rl8200DateAndTime = _Rl8200DateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 3, 24),
    _Rl8200DateAndTime_Type()
)
rl8200DateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rl8200DateAndTime.setStatus("current")
_Rl8200TargetVars_ObjectIdentity = ObjectIdentity
rl8200TargetVars = _Rl8200TargetVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4)
)
_Rl8200TargetsTable_Object = MibTable
rl8200TargetsTable = _Rl8200TargetsTable_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    rl8200TargetsTable.setStatus("current")
_Rl8200TargetsEntry_Object = MibTableRow
rl8200TargetsEntry = _Rl8200TargetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1, 1)
)
rl8200TargetsEntry.setIndexNames(
    (0, "RL8200-ACU-MIB", "rl8200TtTarget"),
)
if mibBuilder.loadTexts:
    rl8200TargetsEntry.setStatus("current")
_Rl8200TtTarget_Type = Rl8200TargetsTC
_Rl8200TtTarget_Object = MibTableColumn
rl8200TtTarget = _Rl8200TtTarget_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1, 1, 1),
    _Rl8200TtTarget_Type()
)
rl8200TtTarget.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rl8200TtTarget.setStatus("current")


class _Rl8200TtName_Type(SnmpAdminString):
    """Custom type rl8200TtName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Rl8200TtName_Type.__name__ = "SnmpAdminString"
_Rl8200TtName_Object = MibTableColumn
rl8200TtName = _Rl8200TtName_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1, 1, 2),
    _Rl8200TtName_Type()
)
rl8200TtName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TtName.setStatus("current")


class _Rl8200TtTrackMode_Type(Integer32):
    """Custom type rl8200TtTrackMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("lookAngles", 1),
          ("longitude", 2),
          ("predictive", 3),
          ("steptrack", 4),
          ("tletrack", 5))
    )


_Rl8200TtTrackMode_Type.__name__ = "Integer32"
_Rl8200TtTrackMode_Object = MibTableColumn
rl8200TtTrackMode = _Rl8200TtTrackMode_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1, 1, 3),
    _Rl8200TtTrackMode_Type()
)
rl8200TtTrackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TtTrackMode.setStatus("current")


class _Rl8200TtBiasAz_Type(Rl8200AngleTC):
    """Custom type rl8200TtBiasAz based on Rl8200AngleTC"""
    subtypeSpec = Rl8200AngleTC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000000, 2000000),
    )


_Rl8200TtBiasAz_Type.__name__ = "Rl8200AngleTC"
_Rl8200TtBiasAz_Object = MibTableColumn
rl8200TtBiasAz = _Rl8200TtBiasAz_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1, 1, 4),
    _Rl8200TtBiasAz_Type()
)
rl8200TtBiasAz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TtBiasAz.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TtBiasAz.setUnits("10e-6 degrees")


class _Rl8200TtBiasEl_Type(Rl8200AngleTC):
    """Custom type rl8200TtBiasEl based on Rl8200AngleTC"""
    subtypeSpec = Rl8200AngleTC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000000, 2000000),
    )


_Rl8200TtBiasEl_Type.__name__ = "Rl8200AngleTC"
_Rl8200TtBiasEl_Object = MibTableColumn
rl8200TtBiasEl = _Rl8200TtBiasEl_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1, 1, 5),
    _Rl8200TtBiasEl_Type()
)
rl8200TtBiasEl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TtBiasEl.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TtBiasEl.setUnits("10e-6 degrees")


class _Rl8200TtBiasPol1_Type(Rl8200AngleTC):
    """Custom type rl8200TtBiasPol1 based on Rl8200AngleTC"""
    subtypeSpec = Rl8200AngleTC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000000, 2000000),
    )


_Rl8200TtBiasPol1_Type.__name__ = "Rl8200AngleTC"
_Rl8200TtBiasPol1_Object = MibTableColumn
rl8200TtBiasPol1 = _Rl8200TtBiasPol1_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1, 1, 6),
    _Rl8200TtBiasPol1_Type()
)
rl8200TtBiasPol1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TtBiasPol1.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TtBiasPol1.setUnits("10e-6 degrees")


class _Rl8200TtBiasPol2_Type(Rl8200AngleTC):
    """Custom type rl8200TtBiasPol2 based on Rl8200AngleTC"""
    subtypeSpec = Rl8200AngleTC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2000000, 2000000),
    )


_Rl8200TtBiasPol2_Type.__name__ = "Rl8200AngleTC"
_Rl8200TtBiasPol2_Object = MibTableColumn
rl8200TtBiasPol2 = _Rl8200TtBiasPol2_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1, 1, 7),
    _Rl8200TtBiasPol2_Type()
)
rl8200TtBiasPol2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TtBiasPol2.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TtBiasPol2.setUnits("10e-6 degrees")


class _Rl8200TtFlags_Type(Bits):
    """Custom type rl8200TtFlags based on Bits"""
    namedValues = NamedValues(
        *(("axis", 0),
          ("solve", 1),
          ("sunOutage", 2),
          ("boxLimit", 3),
          ("orbitScan", 4),
          ("rfsw", 5),
          ("polSel", 6))
    )

_Rl8200TtFlags_Type.__name__ = "Bits"
_Rl8200TtFlags_Object = MibTableColumn
rl8200TtFlags = _Rl8200TtFlags_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1, 1, 8),
    _Rl8200TtFlags_Type()
)
rl8200TtFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TtFlags.setStatus("current")


class _Rl8200TtLookAz_Type(Rl8200AngleTC):
    """Custom type rl8200TtLookAz based on Rl8200AngleTC"""
    subtypeSpec = Rl8200AngleTC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 360000000),
    )


_Rl8200TtLookAz_Type.__name__ = "Rl8200AngleTC"
_Rl8200TtLookAz_Object = MibTableColumn
rl8200TtLookAz = _Rl8200TtLookAz_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1, 1, 9),
    _Rl8200TtLookAz_Type()
)
rl8200TtLookAz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TtLookAz.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TtLookAz.setUnits("10e-6 degrees")


class _Rl8200TtLookEl_Type(Rl8200AngleTC):
    """Custom type rl8200TtLookEl based on Rl8200AngleTC"""
    subtypeSpec = Rl8200AngleTC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 360000000),
    )


_Rl8200TtLookEl_Type.__name__ = "Rl8200AngleTC"
_Rl8200TtLookEl_Object = MibTableColumn
rl8200TtLookEl = _Rl8200TtLookEl_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1, 1, 10),
    _Rl8200TtLookEl_Type()
)
rl8200TtLookEl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TtLookEl.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TtLookEl.setUnits("10e-6 degrees")


class _Rl8200TtLookPol1_Type(Rl8200AngleTC):
    """Custom type rl8200TtLookPol1 based on Rl8200AngleTC"""
    subtypeSpec = Rl8200AngleTC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90000000, 90000000),
    )


_Rl8200TtLookPol1_Type.__name__ = "Rl8200AngleTC"
_Rl8200TtLookPol1_Object = MibTableColumn
rl8200TtLookPol1 = _Rl8200TtLookPol1_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1, 1, 11),
    _Rl8200TtLookPol1_Type()
)
rl8200TtLookPol1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TtLookPol1.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TtLookPol1.setUnits("10e-6 degrees")


class _Rl8200TtLookPol2_Type(Rl8200AngleTC):
    """Custom type rl8200TtLookPol2 based on Rl8200AngleTC"""
    subtypeSpec = Rl8200AngleTC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-90000000, 90000000),
    )


_Rl8200TtLookPol2_Type.__name__ = "Rl8200AngleTC"
_Rl8200TtLookPol2_Object = MibTableColumn
rl8200TtLookPol2 = _Rl8200TtLookPol2_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1, 1, 12),
    _Rl8200TtLookPol2_Type()
)
rl8200TtLookPol2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TtLookPol2.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TtLookPol2.setUnits("10e-6 degrees")


class _Rl8200TtLongitude_Type(Rl8200AngleTC):
    """Custom type rl8200TtLongitude based on Rl8200AngleTC"""
    subtypeSpec = Rl8200AngleTC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-180000000, 180000000),
    )


_Rl8200TtLongitude_Type.__name__ = "Rl8200AngleTC"
_Rl8200TtLongitude_Object = MibTableColumn
rl8200TtLongitude = _Rl8200TtLongitude_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1, 1, 13),
    _Rl8200TtLongitude_Type()
)
rl8200TtLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TtLongitude.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TtLongitude.setUnits("10e-6 degrees")


class _Rl8200TtZero_Type(Integer32):
    """Custom type rl8200TtZero based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 0),
    )


_Rl8200TtZero_Type.__name__ = "Integer32"
_Rl8200TtZero_Object = MibTableColumn
rl8200TtZero = _Rl8200TtZero_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1, 1, 14),
    _Rl8200TtZero_Type()
)
rl8200TtZero.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TtZero.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TtZero.setUnits("10e-1 dBm")
_Rl8200TtBeaconFreq_Type = Unsigned32
_Rl8200TtBeaconFreq_Object = MibTableColumn
rl8200TtBeaconFreq = _Rl8200TtBeaconFreq_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1, 1, 15),
    _Rl8200TtBeaconFreq_Type()
)
rl8200TtBeaconFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TtBeaconFreq.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TtBeaconFreq.setUnits("kHz")


class _Rl8200TtBeamWidth_Type(Rl8200AngleTC):
    """Custom type rl8200TtBeamWidth based on Rl8200AngleTC"""
    subtypeSpec = Rl8200AngleTC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 360000000),
    )


_Rl8200TtBeamWidth_Type.__name__ = "Rl8200AngleTC"
_Rl8200TtBeamWidth_Object = MibTableColumn
rl8200TtBeamWidth = _Rl8200TtBeamWidth_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1, 1, 16),
    _Rl8200TtBeamWidth_Type()
)
rl8200TtBeamWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TtBeamWidth.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TtBeamWidth.setUnits("10e-6 degrees")


class _Rl8200TtStepSize_Type(Integer32):
    """Custom type rl8200TtStepSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Rl8200TtStepSize_Type.__name__ = "Integer32"
_Rl8200TtStepSize_Object = MibTableColumn
rl8200TtStepSize = _Rl8200TtStepSize_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1, 1, 17),
    _Rl8200TtStepSize_Type()
)
rl8200TtStepSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TtStepSize.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TtStepSize.setUnits("%")


class _Rl8200TtDeadband_Type(Integer32):
    """Custom type rl8200TtDeadband based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Rl8200TtDeadband_Type.__name__ = "Integer32"
_Rl8200TtDeadband_Object = MibTableColumn
rl8200TtDeadband = _Rl8200TtDeadband_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1, 1, 18),
    _Rl8200TtDeadband_Type()
)
rl8200TtDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TtDeadband.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TtDeadband.setUnits("%")


class _Rl8200TtMaxStep_Type(Integer32):
    """Custom type rl8200TtMaxStep based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 50),
    )


_Rl8200TtMaxStep_Type.__name__ = "Integer32"
_Rl8200TtMaxStep_Object = MibTableColumn
rl8200TtMaxStep = _Rl8200TtMaxStep_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1, 1, 19),
    _Rl8200TtMaxStep_Type()
)
rl8200TtMaxStep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TtMaxStep.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TtMaxStep.setUnits("%")


class _Rl8200TtCycleTime_Type(Integer32):
    """Custom type rl8200TtCycleTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_Rl8200TtCycleTime_Type.__name__ = "Integer32"
_Rl8200TtCycleTime_Object = MibTableColumn
rl8200TtCycleTime = _Rl8200TtCycleTime_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1, 1, 20),
    _Rl8200TtCycleTime_Type()
)
rl8200TtCycleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TtCycleTime.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TtCycleTime.setUnits("s")


class _Rl8200TtMaxTries_Type(Integer32):
    """Custom type rl8200TtMaxTries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Rl8200TtMaxTries_Type.__name__ = "Integer32"
_Rl8200TtMaxTries_Object = MibTableColumn
rl8200TtMaxTries = _Rl8200TtMaxTries_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1, 1, 21),
    _Rl8200TtMaxTries_Type()
)
rl8200TtMaxTries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TtMaxTries.setStatus("current")


class _Rl8200TtLowSignal_Type(Integer32):
    """Custom type rl8200TtLowSignal based on Integer32"""
    defaultValue = -100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 0),
    )


_Rl8200TtLowSignal_Type.__name__ = "Integer32"
_Rl8200TtLowSignal_Object = MibTableColumn
rl8200TtLowSignal = _Rl8200TtLowSignal_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1, 1, 22),
    _Rl8200TtLowSignal_Type()
)
rl8200TtLowSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TtLowSignal.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TtLowSignal.setUnits("10e-1 dB")


class _Rl8200TtSunOutage_Type(Integer32):
    """Custom type rl8200TtSunOutage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 0),
    )


_Rl8200TtSunOutage_Type.__name__ = "Integer32"
_Rl8200TtSunOutage_Object = MibTableColumn
rl8200TtSunOutage = _Rl8200TtSunOutage_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1, 1, 23),
    _Rl8200TtSunOutage_Type()
)
rl8200TtSunOutage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TtSunOutage.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TtSunOutage.setUnits("10e-1 dB")


class _Rl8200TtShort_Type(Integer32):
    """Custom type rl8200TtShort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86200),
    )


_Rl8200TtShort_Type.__name__ = "Integer32"
_Rl8200TtShort_Object = MibTableColumn
rl8200TtShort = _Rl8200TtShort_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1, 1, 24),
    _Rl8200TtShort_Type()
)
rl8200TtShort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TtShort.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TtShort.setUnits("s")


class _Rl8200TtInclination_Type(Rl8200AngleTC):
    """Custom type rl8200TtInclination based on Rl8200AngleTC"""
    subtypeSpec = Rl8200AngleTC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 360000000),
    )


_Rl8200TtInclination_Type.__name__ = "Rl8200AngleTC"
_Rl8200TtInclination_Object = MibTableColumn
rl8200TtInclination = _Rl8200TtInclination_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1, 1, 25),
    _Rl8200TtInclination_Type()
)
rl8200TtInclination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TtInclination.setStatus("current")
if mibBuilder.loadTexts:
    rl8200TtInclination.setUnits("10e-6 degrees")


class _Rl8200TtSatnum_Type(Unsigned32):
    """Custom type rl8200TtSatnum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_Rl8200TtSatnum_Type.__name__ = "Unsigned32"
_Rl8200TtSatnum_Object = MibTableColumn
rl8200TtSatnum = _Rl8200TtSatnum_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 4, 1, 1, 26),
    _Rl8200TtSatnum_Type()
)
rl8200TtSatnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200TtSatnum.setStatus("current")
_Rl8200CommandVars_ObjectIdentity = ObjectIdentity
rl8200CommandVars = _Rl8200CommandVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 5)
)
_Rl8200CommandStandby_Type = Rl8200InitiateTC
_Rl8200CommandStandby_Object = MibScalar
rl8200CommandStandby = _Rl8200CommandStandby_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 5, 1),
    _Rl8200CommandStandby_Type()
)
rl8200CommandStandby.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200CommandStandby.setStatus("current")
_Rl8200CommandAcknowledgeFaults_Type = Rl8200InitiateTC
_Rl8200CommandAcknowledgeFaults_Object = MibScalar
rl8200CommandAcknowledgeFaults = _Rl8200CommandAcknowledgeFaults_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 5, 2),
    _Rl8200CommandAcknowledgeFaults_Type()
)
rl8200CommandAcknowledgeFaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200CommandAcknowledgeFaults.setStatus("current")
_Rl8200CommandClearFaults_Type = Rl8200InitiateTC
_Rl8200CommandClearFaults_Object = MibScalar
rl8200CommandClearFaults = _Rl8200CommandClearFaults_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 5, 3),
    _Rl8200CommandClearFaults_Type()
)
rl8200CommandClearFaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200CommandClearFaults.setStatus("current")


class _Rl8200CommandManualMode_Type(Rl8200EnabledTC):
    """Custom type rl8200CommandManualMode based on Rl8200EnabledTC"""
    defaultValue = 1


_Rl8200CommandManualMode_Type.__name__ = "Rl8200EnabledTC"
_Rl8200CommandManualMode_Object = MibScalar
rl8200CommandManualMode = _Rl8200CommandManualMode_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 5, 4),
    _Rl8200CommandManualMode_Type()
)
rl8200CommandManualMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200CommandManualMode.setStatus("current")


class _Rl8200CommandJogSpeed_Type(Integer32):
    """Custom type rl8200CommandJogSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-2,
              -1,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("slewSpeedRev", -2),
          ("trackSpeedRev", -1),
          ("trackSpeedFwd", 1),
          ("slewSpeedFwd", 2))
    )


_Rl8200CommandJogSpeed_Type.__name__ = "Integer32"
_Rl8200CommandJogSpeed_Object = MibScalar
rl8200CommandJogSpeed = _Rl8200CommandJogSpeed_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 5, 5),
    _Rl8200CommandJogSpeed_Type()
)
rl8200CommandJogSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200CommandJogSpeed.setStatus("current")
_Rl8200CommandJogTime_Type = Rl8200MillisecondsTC
_Rl8200CommandJogTime_Object = MibScalar
rl8200CommandJogTime = _Rl8200CommandJogTime_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 5, 6),
    _Rl8200CommandJogTime_Type()
)
rl8200CommandJogTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200CommandJogTime.setStatus("current")
if mibBuilder.loadTexts:
    rl8200CommandJogTime.setUnits("ms")


class _Rl8200CommandTrackTarget_Type(Rl8200TargetsTC):
    """Custom type rl8200CommandTrackTarget based on Rl8200TargetsTC"""
    subtypeSpec = Rl8200TargetsTC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82,
              83,
              84,
              85,
              86,
              87,
              88,
              89,
              90,
              91,
              92,
              93,
              94,
              95,
              96,
              97,
              98,
              99,
              100)
        )
    )
    namedValues = NamedValues(
        *(("target1", 3),
          ("target2", 4),
          ("target3", 5),
          ("target4", 6),
          ("target5", 7),
          ("target6", 8),
          ("target7", 9),
          ("target8", 10),
          ("target9", 11),
          ("target10", 12),
          ("target11", 13),
          ("target12", 14),
          ("target13", 15),
          ("target14", 16),
          ("target15", 17),
          ("target16", 18),
          ("target17", 19),
          ("target18", 20),
          ("target19", 21),
          ("target20", 22),
          ("target21", 23),
          ("target22", 24),
          ("target23", 25),
          ("target24", 26),
          ("target25", 27),
          ("target26", 28),
          ("target27", 29),
          ("target28", 30),
          ("target29", 31),
          ("target30", 32),
          ("target31", 33),
          ("target32", 34),
          ("target33", 35),
          ("target34", 36),
          ("target35", 37),
          ("target36", 38),
          ("target37", 39),
          ("target38", 40),
          ("target39", 41),
          ("target40", 42),
          ("target41", 43),
          ("target42", 44),
          ("target43", 45),
          ("target44", 46),
          ("target45", 47),
          ("target46", 48),
          ("target47", 49),
          ("target48", 50),
          ("target49", 51),
          ("target50", 52),
          ("target51", 53),
          ("target52", 54),
          ("target53", 55),
          ("target54", 56),
          ("target55", 57),
          ("target56", 58),
          ("target57", 59),
          ("target58", 60),
          ("target59", 61),
          ("target60", 62),
          ("target61", 63),
          ("target62", 64),
          ("target63", 65),
          ("target64", 66),
          ("target65", 67),
          ("target66", 68),
          ("target67", 69),
          ("target68", 70),
          ("target69", 71),
          ("target70", 72),
          ("target71", 73),
          ("target72", 74),
          ("target73", 75),
          ("target74", 76),
          ("target75", 77),
          ("target76", 78),
          ("target77", 79),
          ("target78", 80),
          ("target79", 81),
          ("target80", 82),
          ("target81", 83),
          ("target82", 84),
          ("target83", 85),
          ("target84", 86),
          ("target85", 87),
          ("target86", 88),
          ("target87", 89),
          ("target88", 90),
          ("target89", 91),
          ("target90", 92),
          ("target91", 93),
          ("target92", 94),
          ("target93", 95),
          ("target94", 96),
          ("target95", 97),
          ("target96", 98),
          ("target97", 99),
          ("target98", 100))
    )


_Rl8200CommandTrackTarget_Type.__name__ = "Rl8200TargetsTC"
_Rl8200CommandTrackTarget_Object = MibScalar
rl8200CommandTrackTarget = _Rl8200CommandTrackTarget_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 5, 7),
    _Rl8200CommandTrackTarget_Type()
)
rl8200CommandTrackTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200CommandTrackTarget.setStatus("current")
_Rl8200CommandBiasCurrentTarget_Type = Rl8200InitiateTC
_Rl8200CommandBiasCurrentTarget_Object = MibScalar
rl8200CommandBiasCurrentTarget = _Rl8200CommandBiasCurrentTarget_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 5, 8),
    _Rl8200CommandBiasCurrentTarget_Type()
)
rl8200CommandBiasCurrentTarget.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200CommandBiasCurrentTarget.setStatus("current")


class _Rl8200CommandJogAxis_Type(Integer32):
    """Custom type rl8200CommandJogAxis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("jogAz", 1),
          ("jogEl", 2),
          ("jogPol1", 3),
          ("jogPol2", 4))
    )


_Rl8200CommandJogAxis_Type.__name__ = "Integer32"
_Rl8200CommandJogAxis_Object = MibScalar
rl8200CommandJogAxis = _Rl8200CommandJogAxis_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 5, 9),
    _Rl8200CommandJogAxis_Type()
)
rl8200CommandJogAxis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200CommandJogAxis.setStatus("current")
_Rl8200SiteInfoVars_ObjectIdentity = ObjectIdentity
rl8200SiteInfoVars = _Rl8200SiteInfoVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 6)
)


class _Rl8200SiteAntennaName_Type(SnmpAdminString):
    """Custom type rl8200SiteAntennaName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_Rl8200SiteAntennaName_Type.__name__ = "SnmpAdminString"
_Rl8200SiteAntennaName_Object = MibScalar
rl8200SiteAntennaName = _Rl8200SiteAntennaName_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 6, 1),
    _Rl8200SiteAntennaName_Type()
)
rl8200SiteAntennaName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200SiteAntennaName.setStatus("current")


class _Rl8200SiteLatitude_Type(Rl8200AngleTC):
    """Custom type rl8200SiteLatitude based on Rl8200AngleTC"""
    subtypeSpec = Rl8200AngleTC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-180000000, 180000000),
    )


_Rl8200SiteLatitude_Type.__name__ = "Rl8200AngleTC"
_Rl8200SiteLatitude_Object = MibScalar
rl8200SiteLatitude = _Rl8200SiteLatitude_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 6, 2),
    _Rl8200SiteLatitude_Type()
)
rl8200SiteLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200SiteLatitude.setStatus("current")
if mibBuilder.loadTexts:
    rl8200SiteLatitude.setUnits("10e-6 degrees")


class _Rl8200SiteLongitude_Type(Rl8200AngleTC):
    """Custom type rl8200SiteLongitude based on Rl8200AngleTC"""
    subtypeSpec = Rl8200AngleTC.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-180000000, 180000000),
    )


_Rl8200SiteLongitude_Type.__name__ = "Rl8200AngleTC"
_Rl8200SiteLongitude_Object = MibScalar
rl8200SiteLongitude = _Rl8200SiteLongitude_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 6, 3),
    _Rl8200SiteLongitude_Type()
)
rl8200SiteLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200SiteLongitude.setStatus("current")
if mibBuilder.loadTexts:
    rl8200SiteLongitude.setUnits("10e-6 degrees")
_Rl8200SiteAltitude_Type = Integer32
_Rl8200SiteAltitude_Object = MibScalar
rl8200SiteAltitude = _Rl8200SiteAltitude_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 6, 4),
    _Rl8200SiteAltitude_Type()
)
rl8200SiteAltitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200SiteAltitude.setStatus("current")
if mibBuilder.loadTexts:
    rl8200SiteAltitude.setUnits("m")


class _Rl8200SiteSystemFlags_Type(Bits):
    """Custom type rl8200SiteSystemFlags based on Bits"""
    namedValues = NamedValues(
        *(("audibleAlert", 0),
          ("polSelCtrl", 1))
    )

_Rl8200SiteSystemFlags_Type.__name__ = "Bits"
_Rl8200SiteSystemFlags_Object = MibScalar
rl8200SiteSystemFlags = _Rl8200SiteSystemFlags_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 6, 5),
    _Rl8200SiteSystemFlags_Type()
)
rl8200SiteSystemFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200SiteSystemFlags.setStatus("current")
_Rl8200BeaconReceiverVars_ObjectIdentity = ObjectIdentity
rl8200BeaconReceiverVars = _Rl8200BeaconReceiverVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 7)
)
_Rl8200BeaconReceiverBdcF1_Type = Integer32
_Rl8200BeaconReceiverBdcF1_Object = MibScalar
rl8200BeaconReceiverBdcF1 = _Rl8200BeaconReceiverBdcF1_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 7, 1),
    _Rl8200BeaconReceiverBdcF1_Type()
)
rl8200BeaconReceiverBdcF1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200BeaconReceiverBdcF1.setStatus("current")
if mibBuilder.loadTexts:
    rl8200BeaconReceiverBdcF1.setUnits("kHz")
_Rl8200BeaconReceiverBdcF2_Type = Integer32
_Rl8200BeaconReceiverBdcF2_Object = MibScalar
rl8200BeaconReceiverBdcF2 = _Rl8200BeaconReceiverBdcF2_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 7, 2),
    _Rl8200BeaconReceiverBdcF2_Type()
)
rl8200BeaconReceiverBdcF2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200BeaconReceiverBdcF2.setStatus("current")
if mibBuilder.loadTexts:
    rl8200BeaconReceiverBdcF2.setUnits("kHz")


class _Rl8200BeaconReceiverAoVref_Type(Unsigned32):
    """Custom type rl8200BeaconReceiverAoVref based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_Rl8200BeaconReceiverAoVref_Type.__name__ = "Unsigned32"
_Rl8200BeaconReceiverAoVref_Object = MibScalar
rl8200BeaconReceiverAoVref = _Rl8200BeaconReceiverAoVref_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 7, 3),
    _Rl8200BeaconReceiverAoVref_Type()
)
rl8200BeaconReceiverAoVref.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200BeaconReceiverAoVref.setStatus("current")
if mibBuilder.loadTexts:
    rl8200BeaconReceiverAoVref.setUnits("mV")
_Rl8200BeaconReceiverAoSlope_Type = Integer32
_Rl8200BeaconReceiverAoSlope_Object = MibScalar
rl8200BeaconReceiverAoSlope = _Rl8200BeaconReceiverAoSlope_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 7, 4),
    _Rl8200BeaconReceiverAoSlope_Type()
)
rl8200BeaconReceiverAoSlope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200BeaconReceiverAoSlope.setStatus("current")
if mibBuilder.loadTexts:
    rl8200BeaconReceiverAoSlope.setUnits("mV/dBm")


class _Rl8200BeaconReceiverAttenuation_Type(Integer32):
    """Custom type rl8200BeaconReceiverAttenuation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 40),
    )


_Rl8200BeaconReceiverAttenuation_Type.__name__ = "Integer32"
_Rl8200BeaconReceiverAttenuation_Object = MibScalar
rl8200BeaconReceiverAttenuation = _Rl8200BeaconReceiverAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 1, 7, 5),
    _Rl8200BeaconReceiverAttenuation_Type()
)
rl8200BeaconReceiverAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rl8200BeaconReceiverAttenuation.setStatus("current")
if mibBuilder.loadTexts:
    rl8200BeaconReceiverAttenuation.setUnits("dBm")
_Rl8200MibConformance_ObjectIdentity = ObjectIdentity
rl8200MibConformance = _Rl8200MibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 2)
)
_Rl8200MibCompliances_ObjectIdentity = ObjectIdentity
rl8200MibCompliances = _Rl8200MibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 2, 1)
)
_Rl8200MibGroups_ObjectIdentity = ObjectIdentity
rl8200MibGroups = _Rl8200MibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 2, 2)
)

# Managed Objects groups

rl8200MibSettingsDatabaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 2, 2, 1)
)
rl8200MibSettingsDatabaseGroup.setObjects(
      *(("RL8200-ACU-MIB", "rl8200DatabaseVersion"),
        ("RL8200-ACU-MIB", "rl8200DatabaseTimestamp"))
)
if mibBuilder.loadTexts:
    rl8200MibSettingsDatabaseGroup.setStatus("current")

rl8200MibAntennaPositionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 2, 2, 2)
)
rl8200MibAntennaPositionGroup.setObjects(
      *(("RL8200-ACU-MIB", "rl8200SoftTravelLimitCwAz"),
        ("RL8200-ACU-MIB", "rl8200SoftTravelLimitCwEl"),
        ("RL8200-ACU-MIB", "rl8200SoftTravelLimitCwPol1"),
        ("RL8200-ACU-MIB", "rl8200SoftTravelLimitCwPol2"),
        ("RL8200-ACU-MIB", "rl8200SoftTravelLimitCcwAz"),
        ("RL8200-ACU-MIB", "rl8200SoftTravelLimitCcwEl"),
        ("RL8200-ACU-MIB", "rl8200SoftTravelLimitCcwPol1"),
        ("RL8200-ACU-MIB", "rl8200SoftTravelLimitCcwPol2"),
        ("RL8200-ACU-MIB", "rl8200SoftTravelLimitEnabled"),
        ("RL8200-ACU-MIB", "rl8200PolarizationType"),
        ("RL8200-ACU-MIB", "rl8200SlewAz"),
        ("RL8200-ACU-MIB", "rl8200SlewEl"),
        ("RL8200-ACU-MIB", "rl8200SlewCoastTimeAz"),
        ("RL8200-ACU-MIB", "rl8200SlewCoastTimeEl"),
        ("RL8200-ACU-MIB", "rl8200TrackCoastTimeAz"),
        ("RL8200-ACU-MIB", "rl8200TrackCoastTimeEl"),
        ("RL8200-ACU-MIB", "rl8200TrackCoastTimePol1"),
        ("RL8200-ACU-MIB", "rl8200TrackCoastTimePol2"),
        ("RL8200-ACU-MIB", "rl8200PositionDeadbandAz"),
        ("RL8200-ACU-MIB", "rl8200PositionDeadbandEl"),
        ("RL8200-ACU-MIB", "rl8200PositionDeadbandPol1"),
        ("RL8200-ACU-MIB", "rl8200PositionDeadbandPol2"),
        ("RL8200-ACU-MIB", "rl8200BumpTimeAz"),
        ("RL8200-ACU-MIB", "rl8200BumpTimeEl"),
        ("RL8200-ACU-MIB", "rl8200BumpTimePol1"),
        ("RL8200-ACU-MIB", "rl8200BumpTimePol2"),
        ("RL8200-ACU-MIB", "rl8200BumpOffTimeAz"),
        ("RL8200-ACU-MIB", "rl8200BumpOffTimeEl"),
        ("RL8200-ACU-MIB", "rl8200BumpOffTimePol1"),
        ("RL8200-ACU-MIB", "rl8200BumpOffTimePol2"),
        ("RL8200-ACU-MIB", "rl8200OffsetAz"),
        ("RL8200-ACU-MIB", "rl8200OffsetEl"),
        ("RL8200-ACU-MIB", "rl8200OffsetPol1"),
        ("RL8200-ACU-MIB", "rl8200OffsetPol2"),
        ("RL8200-ACU-MIB", "rl8200ReverseCountSenseAz"),
        ("RL8200-ACU-MIB", "rl8200ReverseCountSenseEl"),
        ("RL8200-ACU-MIB", "rl8200ReverseCountSensePol1"),
        ("RL8200-ACU-MIB", "rl8200ReverseCountSensePol2"),
        ("RL8200-ACU-MIB", "rl8200FaultTestPeriodAz"),
        ("RL8200-ACU-MIB", "rl8200FaultTestPeriodEl"),
        ("RL8200-ACU-MIB", "rl8200FaultTestPeriodPol1"),
        ("RL8200-ACU-MIB", "rl8200FaultTestPeriodPol2"),
        ("RL8200-ACU-MIB", "rl8200MotionAz"),
        ("RL8200-ACU-MIB", "rl8200OMotionEl"),
        ("RL8200-ACU-MIB", "rl8200MotionPol1"),
        ("RL8200-ACU-MIB", "rl8200MotionPol2"),
        ("RL8200-ACU-MIB", "rl8200RunawayAz"),
        ("RL8200-ACU-MIB", "rl8200ORunawayEl"),
        ("RL8200-ACU-MIB", "rl8200RunawayPol1"),
        ("RL8200-ACU-MIB", "rl8200RunawayPol2"))
)
if mibBuilder.loadTexts:
    rl8200MibAntennaPositionGroup.setStatus("current")

rl8200MibStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 2, 2, 3)
)
rl8200MibStatusGroup.setObjects(
      *(("RL8200-ACU-MIB", "rl8200ActualPositionAz"),
        ("RL8200-ACU-MIB", "rl8200ActualPositionEl"),
        ("RL8200-ACU-MIB", "rl8200ActualPositionPol1"),
        ("RL8200-ACU-MIB", "rl8200ActualPositionPol2"),
        ("RL8200-ACU-MIB", "rl8200CommandPositionAz"),
        ("RL8200-ACU-MIB", "rl8200CommandPositionEl"),
        ("RL8200-ACU-MIB", "rl8200CommandPositionPol1"),
        ("RL8200-ACU-MIB", "rl8200CommandPositionPol2"),
        ("RL8200-ACU-MIB", "rl8200TargetPositionAz"),
        ("RL8200-ACU-MIB", "rl8200TargetPositionEl"),
        ("RL8200-ACU-MIB", "rl8200TargetPositionPol1"),
        ("RL8200-ACU-MIB", "rl8200TargetPositionPol2"),
        ("RL8200-ACU-MIB", "rl8200TargetAcquisitionStatus"),
        ("RL8200-ACU-MIB", "rl8200TrackingMode"),
        ("RL8200-ACU-MIB", "rl8200MotorDriveStatusAz"),
        ("RL8200-ACU-MIB", "rl8200MotorDriveStatusEl"),
        ("RL8200-ACU-MIB", "rl8200MotorDriveStatusPol1"),
        ("RL8200-ACU-MIB", "rl8200MotorDriveStatusPol2"),
        ("RL8200-ACU-MIB", "rl8200ReceivedSignalLevel"),
        ("RL8200-ACU-MIB", "rl8200ReceiverInputSource"),
        ("RL8200-ACU-MIB", "rl8200ReceiverBeaconFrequency"),
        ("RL8200-ACU-MIB", "rl8200AcknowledgedFaults"),
        ("RL8200-ACU-MIB", "rl8200UnacknowledgedFaults"),
        ("RL8200-ACU-MIB", "rl8200DateAndTime"))
)
if mibBuilder.loadTexts:
    rl8200MibStatusGroup.setStatus("current")

rl8200MibTargetsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 2, 2, 4)
)
rl8200MibTargetsGroup.setObjects(
      *(("RL8200-ACU-MIB", "rl8200TtName"),
        ("RL8200-ACU-MIB", "rl8200TtTrackMode"),
        ("RL8200-ACU-MIB", "rl8200TtBiasAz"),
        ("RL8200-ACU-MIB", "rl8200TtBiasEl"),
        ("RL8200-ACU-MIB", "rl8200TtBiasPol1"),
        ("RL8200-ACU-MIB", "rl8200TtBiasPol2"),
        ("RL8200-ACU-MIB", "rl8200TtFlags"),
        ("RL8200-ACU-MIB", "rl8200TtLookAz"),
        ("RL8200-ACU-MIB", "rl8200TtLookEl"),
        ("RL8200-ACU-MIB", "rl8200TtLookPol1"),
        ("RL8200-ACU-MIB", "rl8200TtLookPol2"),
        ("RL8200-ACU-MIB", "rl8200TtLongitude"),
        ("RL8200-ACU-MIB", "rl8200TtZero"),
        ("RL8200-ACU-MIB", "rl8200TtBeaconFreq"),
        ("RL8200-ACU-MIB", "rl8200TtBeamWidth"),
        ("RL8200-ACU-MIB", "rl8200TtStepSize"),
        ("RL8200-ACU-MIB", "rl8200TtDeadband"),
        ("RL8200-ACU-MIB", "rl8200TtMaxStep"),
        ("RL8200-ACU-MIB", "rl8200TtCycleTime"),
        ("RL8200-ACU-MIB", "rl8200TtMaxTries"),
        ("RL8200-ACU-MIB", "rl8200TtLowSignal"),
        ("RL8200-ACU-MIB", "rl8200TtSunOutage"),
        ("RL8200-ACU-MIB", "rl8200TtShort"),
        ("RL8200-ACU-MIB", "rl8200TtInclination"),
        ("RL8200-ACU-MIB", "rl8200TtSatnum"))
)
if mibBuilder.loadTexts:
    rl8200MibTargetsGroup.setStatus("current")

rl8200MibCommandGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 2, 2, 5)
)
rl8200MibCommandGroup.setObjects(
      *(("RL8200-ACU-MIB", "rl8200CommandStandby"),
        ("RL8200-ACU-MIB", "rl8200CommandAcknowledgeFaults"),
        ("RL8200-ACU-MIB", "rl8200CommandClearFaults"),
        ("RL8200-ACU-MIB", "rl8200CommandManualMode"),
        ("RL8200-ACU-MIB", "rl8200CommandJogSpeed"),
        ("RL8200-ACU-MIB", "rl8200CommandJogTime"),
        ("RL8200-ACU-MIB", "rl8200CommandTrackTarget"),
        ("RL8200-ACU-MIB", "rl8200CommandBiasCurrentTarget"),
        ("RL8200-ACU-MIB", "rl8200CommandJogAxis"))
)
if mibBuilder.loadTexts:
    rl8200MibCommandGroup.setStatus("current")

rl8200MibSiteInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 2, 2, 6)
)
rl8200MibSiteInfoGroup.setObjects(
      *(("RL8200-ACU-MIB", "rl8200SiteAntennaName"),
        ("RL8200-ACU-MIB", "rl8200SiteLatitude"),
        ("RL8200-ACU-MIB", "rl8200SiteLongitude"),
        ("RL8200-ACU-MIB", "rl8200SiteAltitude"),
        ("RL8200-ACU-MIB", "rl8200SiteSystemFlags"))
)
if mibBuilder.loadTexts:
    rl8200MibSiteInfoGroup.setStatus("current")

rl8200MibBeaconReceiverGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 2, 2, 7)
)
rl8200MibBeaconReceiverGroup.setObjects(
      *(("RL8200-ACU-MIB", "rl8200BeaconReceiverBdcF1"),
        ("RL8200-ACU-MIB", "rl8200BeaconReceiverBdcF2"),
        ("RL8200-ACU-MIB", "rl8200BeaconReceiverAoVref"),
        ("RL8200-ACU-MIB", "rl8200BeaconReceiverAoSlope"),
        ("RL8200-ACU-MIB", "rl8200BeaconReceiverAttenuation"))
)
if mibBuilder.loadTexts:
    rl8200MibBeaconReceiverGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rl8200MibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 47773, 1, 1, 8200, 1, 2, 1, 1)
)
rl8200MibCompliance.setObjects(
      *(("RL8200-ACU-MIB", "rl8200MibSettingsDatabaseGroup"),
        ("RL8200-ACU-MIB", "rl8200MibAntennaPositionGroup"),
        ("RL8200-ACU-MIB", "rl8200MibStatusGroup"),
        ("RL8200-ACU-MIB", "rl8200MibTargetsGroup"),
        ("RL8200-ACU-MIB", "rl8200MibCommandGroup"),
        ("RL8200-ACU-MIB", "rl8200MibSiteInfoGroup"),
        ("RL8200-ACU-MIB", "rl8200MibBeaconReceiverGroup"))
)
if mibBuilder.loadTexts:
    rl8200MibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RL8200-ACU-MIB",
    **{"Rl8200AngleTC": Rl8200AngleTC,
       "Rl8200MillisecondsTC": Rl8200MillisecondsTC,
       "Rl8200MotorDriveStatusTC": Rl8200MotorDriveStatusTC,
       "Rl8200TargetsTC": Rl8200TargetsTC,
       "Rl8200FaultsTC": Rl8200FaultsTC,
       "Rl8200InitiateTC": Rl8200InitiateTC,
       "Rl8200EnabledTC": Rl8200EnabledTC,
       "rl8200AcuMib": rl8200AcuMib,
       "rl8200MibObjects": rl8200MibObjects,
       "rl8200SettingsDatabaseVars": rl8200SettingsDatabaseVars,
       "rl8200DatabaseVersion": rl8200DatabaseVersion,
       "rl8200DatabaseTimestamp": rl8200DatabaseTimestamp,
       "rl8200AntennaPositionVars": rl8200AntennaPositionVars,
       "rl8200SoftTravelLimitCwAz": rl8200SoftTravelLimitCwAz,
       "rl8200SoftTravelLimitCwEl": rl8200SoftTravelLimitCwEl,
       "rl8200SoftTravelLimitCwPol1": rl8200SoftTravelLimitCwPol1,
       "rl8200SoftTravelLimitCwPol2": rl8200SoftTravelLimitCwPol2,
       "rl8200SoftTravelLimitCcwAz": rl8200SoftTravelLimitCcwAz,
       "rl8200SoftTravelLimitCcwEl": rl8200SoftTravelLimitCcwEl,
       "rl8200SoftTravelLimitCcwPol1": rl8200SoftTravelLimitCcwPol1,
       "rl8200SoftTravelLimitCcwPol2": rl8200SoftTravelLimitCcwPol2,
       "rl8200SoftTravelLimitEnabled": rl8200SoftTravelLimitEnabled,
       "rl8200PolarizationType": rl8200PolarizationType,
       "rl8200SlewAz": rl8200SlewAz,
       "rl8200SlewEl": rl8200SlewEl,
       "rl8200SlewCoastTimeAz": rl8200SlewCoastTimeAz,
       "rl8200SlewCoastTimeEl": rl8200SlewCoastTimeEl,
       "rl8200TrackCoastTimeAz": rl8200TrackCoastTimeAz,
       "rl8200TrackCoastTimeEl": rl8200TrackCoastTimeEl,
       "rl8200TrackCoastTimePol1": rl8200TrackCoastTimePol1,
       "rl8200TrackCoastTimePol2": rl8200TrackCoastTimePol2,
       "rl8200PositionDeadbandAz": rl8200PositionDeadbandAz,
       "rl8200PositionDeadbandEl": rl8200PositionDeadbandEl,
       "rl8200PositionDeadbandPol1": rl8200PositionDeadbandPol1,
       "rl8200PositionDeadbandPol2": rl8200PositionDeadbandPol2,
       "rl8200BumpTimeAz": rl8200BumpTimeAz,
       "rl8200BumpTimeEl": rl8200BumpTimeEl,
       "rl8200BumpTimePol1": rl8200BumpTimePol1,
       "rl8200BumpTimePol2": rl8200BumpTimePol2,
       "rl8200BumpOffTimeAz": rl8200BumpOffTimeAz,
       "rl8200BumpOffTimeEl": rl8200BumpOffTimeEl,
       "rl8200BumpOffTimePol1": rl8200BumpOffTimePol1,
       "rl8200BumpOffTimePol2": rl8200BumpOffTimePol2,
       "rl8200OffsetAz": rl8200OffsetAz,
       "rl8200OffsetEl": rl8200OffsetEl,
       "rl8200OffsetPol1": rl8200OffsetPol1,
       "rl8200OffsetPol2": rl8200OffsetPol2,
       "rl8200ReverseCountSenseAz": rl8200ReverseCountSenseAz,
       "rl8200ReverseCountSenseEl": rl8200ReverseCountSenseEl,
       "rl8200ReverseCountSensePol1": rl8200ReverseCountSensePol1,
       "rl8200ReverseCountSensePol2": rl8200ReverseCountSensePol2,
       "rl8200FaultTestPeriodAz": rl8200FaultTestPeriodAz,
       "rl8200FaultTestPeriodEl": rl8200FaultTestPeriodEl,
       "rl8200FaultTestPeriodPol1": rl8200FaultTestPeriodPol1,
       "rl8200FaultTestPeriodPol2": rl8200FaultTestPeriodPol2,
       "rl8200MotionAz": rl8200MotionAz,
       "rl8200OMotionEl": rl8200OMotionEl,
       "rl8200MotionPol1": rl8200MotionPol1,
       "rl8200MotionPol2": rl8200MotionPol2,
       "rl8200RunawayAz": rl8200RunawayAz,
       "rl8200ORunawayEl": rl8200ORunawayEl,
       "rl8200RunawayPol1": rl8200RunawayPol1,
       "rl8200RunawayPol2": rl8200RunawayPol2,
       "rl8200StatusVars": rl8200StatusVars,
       "rl8200ActualPositionAz": rl8200ActualPositionAz,
       "rl8200ActualPositionEl": rl8200ActualPositionEl,
       "rl8200ActualPositionPol1": rl8200ActualPositionPol1,
       "rl8200ActualPositionPol2": rl8200ActualPositionPol2,
       "rl8200CommandPositionAz": rl8200CommandPositionAz,
       "rl8200CommandPositionEl": rl8200CommandPositionEl,
       "rl8200CommandPositionPol1": rl8200CommandPositionPol1,
       "rl8200CommandPositionPol2": rl8200CommandPositionPol2,
       "rl8200TargetPositionAz": rl8200TargetPositionAz,
       "rl8200TargetPositionEl": rl8200TargetPositionEl,
       "rl8200TargetPositionPol1": rl8200TargetPositionPol1,
       "rl8200TargetPositionPol2": rl8200TargetPositionPol2,
       "rl8200TargetAcquisitionStatus": rl8200TargetAcquisitionStatus,
       "rl8200TrackingMode": rl8200TrackingMode,
       "rl8200MotorDriveStatusAz": rl8200MotorDriveStatusAz,
       "rl8200MotorDriveStatusEl": rl8200MotorDriveStatusEl,
       "rl8200MotorDriveStatusPol1": rl8200MotorDriveStatusPol1,
       "rl8200MotorDriveStatusPol2": rl8200MotorDriveStatusPol2,
       "rl8200ReceivedSignalLevel": rl8200ReceivedSignalLevel,
       "rl8200ReceiverInputSource": rl8200ReceiverInputSource,
       "rl8200ReceiverBeaconFrequency": rl8200ReceiverBeaconFrequency,
       "rl8200AcknowledgedFaults": rl8200AcknowledgedFaults,
       "rl8200UnacknowledgedFaults": rl8200UnacknowledgedFaults,
       "rl8200DateAndTime": rl8200DateAndTime,
       "rl8200TargetVars": rl8200TargetVars,
       "rl8200TargetsTable": rl8200TargetsTable,
       "rl8200TargetsEntry": rl8200TargetsEntry,
       "rl8200TtTarget": rl8200TtTarget,
       "rl8200TtName": rl8200TtName,
       "rl8200TtTrackMode": rl8200TtTrackMode,
       "rl8200TtBiasAz": rl8200TtBiasAz,
       "rl8200TtBiasEl": rl8200TtBiasEl,
       "rl8200TtBiasPol1": rl8200TtBiasPol1,
       "rl8200TtBiasPol2": rl8200TtBiasPol2,
       "rl8200TtFlags": rl8200TtFlags,
       "rl8200TtLookAz": rl8200TtLookAz,
       "rl8200TtLookEl": rl8200TtLookEl,
       "rl8200TtLookPol1": rl8200TtLookPol1,
       "rl8200TtLookPol2": rl8200TtLookPol2,
       "rl8200TtLongitude": rl8200TtLongitude,
       "rl8200TtZero": rl8200TtZero,
       "rl8200TtBeaconFreq": rl8200TtBeaconFreq,
       "rl8200TtBeamWidth": rl8200TtBeamWidth,
       "rl8200TtStepSize": rl8200TtStepSize,
       "rl8200TtDeadband": rl8200TtDeadband,
       "rl8200TtMaxStep": rl8200TtMaxStep,
       "rl8200TtCycleTime": rl8200TtCycleTime,
       "rl8200TtMaxTries": rl8200TtMaxTries,
       "rl8200TtLowSignal": rl8200TtLowSignal,
       "rl8200TtSunOutage": rl8200TtSunOutage,
       "rl8200TtShort": rl8200TtShort,
       "rl8200TtInclination": rl8200TtInclination,
       "rl8200TtSatnum": rl8200TtSatnum,
       "rl8200CommandVars": rl8200CommandVars,
       "rl8200CommandStandby": rl8200CommandStandby,
       "rl8200CommandAcknowledgeFaults": rl8200CommandAcknowledgeFaults,
       "rl8200CommandClearFaults": rl8200CommandClearFaults,
       "rl8200CommandManualMode": rl8200CommandManualMode,
       "rl8200CommandJogSpeed": rl8200CommandJogSpeed,
       "rl8200CommandJogTime": rl8200CommandJogTime,
       "rl8200CommandTrackTarget": rl8200CommandTrackTarget,
       "rl8200CommandBiasCurrentTarget": rl8200CommandBiasCurrentTarget,
       "rl8200CommandJogAxis": rl8200CommandJogAxis,
       "rl8200SiteInfoVars": rl8200SiteInfoVars,
       "rl8200SiteAntennaName": rl8200SiteAntennaName,
       "rl8200SiteLatitude": rl8200SiteLatitude,
       "rl8200SiteLongitude": rl8200SiteLongitude,
       "rl8200SiteAltitude": rl8200SiteAltitude,
       "rl8200SiteSystemFlags": rl8200SiteSystemFlags,
       "rl8200BeaconReceiverVars": rl8200BeaconReceiverVars,
       "rl8200BeaconReceiverBdcF1": rl8200BeaconReceiverBdcF1,
       "rl8200BeaconReceiverBdcF2": rl8200BeaconReceiverBdcF2,
       "rl8200BeaconReceiverAoVref": rl8200BeaconReceiverAoVref,
       "rl8200BeaconReceiverAoSlope": rl8200BeaconReceiverAoSlope,
       "rl8200BeaconReceiverAttenuation": rl8200BeaconReceiverAttenuation,
       "rl8200MibConformance": rl8200MibConformance,
       "rl8200MibCompliances": rl8200MibCompliances,
       "rl8200MibCompliance": rl8200MibCompliance,
       "rl8200MibGroups": rl8200MibGroups,
       "rl8200MibSettingsDatabaseGroup": rl8200MibSettingsDatabaseGroup,
       "rl8200MibAntennaPositionGroup": rl8200MibAntennaPositionGroup,
       "rl8200MibStatusGroup": rl8200MibStatusGroup,
       "rl8200MibTargetsGroup": rl8200MibTargetsGroup,
       "rl8200MibCommandGroup": rl8200MibCommandGroup,
       "rl8200MibSiteInfoGroup": rl8200MibSiteInfoGroup,
       "rl8200MibBeaconReceiverGroup": rl8200MibBeaconReceiverGroup}
)
