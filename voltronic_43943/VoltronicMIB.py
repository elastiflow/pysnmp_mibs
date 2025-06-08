# SNMP MIB module (VoltronicMIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/voltronic_43943/VoltronicMIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 19:10:47 2025
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

(NonNegativeInteger,
 PositiveInteger) = mibBuilder.importSymbols(
    "UPS-MIB",
    "NonNegativeInteger",
    "PositiveInteger")


# MODULE-IDENTITY

voltronicMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 43943)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1)
)
_Ups_ObjectIdentity = ObjectIdentity
ups = _Ups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1)
)
_UpsIdent_ObjectIdentity = ObjectIdentity
upsIdent = _UpsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 1)
)


class _UpsIdManufacturer_Type(DisplayString):
    """Custom type upsIdManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsIdManufacturer_Type.__name__ = "DisplayString"
_UpsIdManufacturer_Object = MibScalar
upsIdManufacturer = _UpsIdManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 1, 1),
    _UpsIdManufacturer_Type()
)
upsIdManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdManufacturer.setStatus("mandatory")


class _UpsIdProtocol_Type(Integer32):
    """Custom type upsIdProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              80,
              99)
        )
    )
    namedValues = NamedValues(
        *(("unknown", -1),
          ("p00", 0),
          ("p01", 1),
          ("p02", 2),
          ("p03", 3),
          ("p04", 4),
          ("p05", 5),
          ("p06", 6),
          ("p07", 7),
          ("p08", 8),
          ("p09", 9),
          ("p10", 10),
          ("sec", 80),
          ("pmv", 99))
    )


_UpsIdProtocol_Type.__name__ = "Integer32"
_UpsIdProtocol_Object = MibScalar
upsIdProtocol = _UpsIdProtocol_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 1, 2),
    _UpsIdProtocol_Type()
)
upsIdProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdProtocol.setStatus("mandatory")


class _UpsIdModelName_Type(DisplayString):
    """Custom type upsIdModelName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_UpsIdModelName_Type.__name__ = "DisplayString"
_UpsIdModelName_Object = MibScalar
upsIdModelName = _UpsIdModelName_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 1, 3),
    _UpsIdModelName_Type()
)
upsIdModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdModelName.setStatus("mandatory")


class _UpsIdSerialNumber_Type(DisplayString):
    """Custom type upsIdSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsIdSerialNumber_Type.__name__ = "DisplayString"
_UpsIdSerialNumber_Object = MibScalar
upsIdSerialNumber = _UpsIdSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 1, 4),
    _UpsIdSerialNumber_Type()
)
upsIdSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdSerialNumber.setStatus("mandatory")


class _UpsIdName_Type(DisplayString):
    """Custom type upsIdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsIdName_Type.__name__ = "DisplayString"
_UpsIdName_Object = MibScalar
upsIdName = _UpsIdName_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 1, 5),
    _UpsIdName_Type()
)
upsIdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsIdName.setStatus("mandatory")


class _UpsIdFWVersion_Type(DisplayString):
    """Custom type upsIdFWVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UpsIdFWVersion_Type.__name__ = "DisplayString"
_UpsIdFWVersion_Object = MibScalar
upsIdFWVersion = _UpsIdFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 1, 6),
    _UpsIdFWVersion_Type()
)
upsIdFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdFWVersion.setStatus("mandatory")


class _UpsIdUPSType_Type(Integer32):
    """Custom type upsIdUPSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standy", 0),
          ("line-interactive", 1),
          ("on-line", 2))
    )


_UpsIdUPSType_Type.__name__ = "Integer32"
_UpsIdUPSType_Object = MibScalar
upsIdUPSType = _UpsIdUPSType_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 1, 7),
    _UpsIdUPSType_Type()
)
upsIdUPSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsIdUPSType.setStatus("mandatory")
_UpsRating_ObjectIdentity = ObjectIdentity
upsRating = _UpsRating_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 2)
)
_UpsRatinVoltage_Type = NonNegativeInteger
_UpsRatinVoltage_Object = MibScalar
upsRatinVoltage = _UpsRatinVoltage_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 2, 1),
    _UpsRatinVoltage_Type()
)
upsRatinVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsRatinVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsRatinVoltage.setUnits("0.1 Volt DC")
_UpsRatoutVoltage_Type = NonNegativeInteger
_UpsRatoutVoltage_Object = MibScalar
upsRatoutVoltage = _UpsRatoutVoltage_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 2, 2),
    _UpsRatoutVoltage_Type()
)
upsRatoutVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsRatoutVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsRatoutVoltage.setUnits("0.1 Volt DC")
_UpsRatoutFrequency_Type = NonNegativeInteger
_UpsRatoutFrequency_Object = MibScalar
upsRatoutFrequency = _UpsRatoutFrequency_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 2, 3),
    _UpsRatoutFrequency_Type()
)
upsRatoutFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsRatoutFrequency.setStatus("current")
if mibBuilder.loadTexts:
    upsRatoutFrequency.setUnits("0.1 HZ")
_UpsRatoutCurrent_Type = NonNegativeInteger
_UpsRatoutCurrent_Object = MibScalar
upsRatoutCurrent = _UpsRatoutCurrent_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 2, 4),
    _UpsRatoutCurrent_Type()
)
upsRatoutCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsRatoutCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsRatoutCurrent.setUnits("0.1 Amp DC")
_UpsRatoutApparentPower_Type = NonNegativeInteger
_UpsRatoutApparentPower_Object = MibScalar
upsRatoutApparentPower = _UpsRatoutApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 2, 5),
    _UpsRatoutApparentPower_Type()
)
upsRatoutApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsRatoutApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    upsRatoutApparentPower.setUnits("0.1 VA")
_UpsRatoutTruePower_Type = NonNegativeInteger
_UpsRatoutTruePower_Object = MibScalar
upsRatoutTruePower = _UpsRatoutTruePower_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 2, 6),
    _UpsRatoutTruePower_Type()
)
upsRatoutTruePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsRatoutTruePower.setStatus("current")
if mibBuilder.loadTexts:
    upsRatoutTruePower.setUnits("0.1 Wt")
_UpsRatBatVoltage_Type = NonNegativeInteger
_UpsRatBatVoltage_Object = MibScalar
upsRatBatVoltage = _UpsRatBatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 2, 7),
    _UpsRatBatVoltage_Type()
)
upsRatBatVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsRatBatVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsRatBatVoltage.setUnits("0.1 vol")
_UpsBattery_ObjectIdentity = ObjectIdentity
upsBattery = _UpsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 3)
)


class _UpsBatStatus_Type(Integer32):
    """Custom type upsBatStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("batteryNormal", 2),
          ("batteryLow", 3),
          ("batteryDepleted", 4),
          ("batteryDischarging", 5),
          ("batteryFailure", 6),
          ("batteryReplace", 7),
          ("batterysilence", 8))
    )


_UpsBatStatus_Type.__name__ = "Integer32"
_UpsBatStatus_Object = MibScalar
upsBatStatus = _UpsBatStatus_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 3, 1),
    _UpsBatStatus_Type()
)
upsBatStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatStatus.setStatus("mandatory")
_UpsBatSecondsOnBattery_Type = Integer32
_UpsBatSecondsOnBattery_Object = MibScalar
upsBatSecondsOnBattery = _UpsBatSecondsOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 3, 2),
    _UpsBatSecondsOnBattery_Type()
)
upsBatSecondsOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatSecondsOnBattery.setStatus("current")
if mibBuilder.loadTexts:
    upsBatSecondsOnBattery.setUnits("seconds")
_UpsBatEstMinutesRemaining_Type = Integer32
_UpsBatEstMinutesRemaining_Object = MibScalar
upsBatEstMinutesRemaining = _UpsBatEstMinutesRemaining_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 3, 3),
    _UpsBatEstMinutesRemaining_Type()
)
upsBatEstMinutesRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatEstMinutesRemaining.setStatus("current")
if mibBuilder.loadTexts:
    upsBatEstMinutesRemaining.setUnits("minutes")


class _UpsBatEstChargeRemaining_Type(Integer32):
    """Custom type upsBatEstChargeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpsBatEstChargeRemaining_Type.__name__ = "Integer32"
_UpsBatEstChargeRemaining_Object = MibScalar
upsBatEstChargeRemaining = _UpsBatEstChargeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 3, 4),
    _UpsBatEstChargeRemaining_Type()
)
upsBatEstChargeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatEstChargeRemaining.setStatus("current")
if mibBuilder.loadTexts:
    upsBatEstChargeRemaining.setUnits("percent")
_UpsBatPBatVoltage_Type = NonNegativeInteger
_UpsBatPBatVoltage_Object = MibScalar
upsBatPBatVoltage = _UpsBatPBatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 3, 5),
    _UpsBatPBatVoltage_Type()
)
upsBatPBatVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatPBatVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsBatPBatVoltage.setUnits("0.1 Volt DC")
_UpsBatNBatVoltage_Type = NonNegativeInteger
_UpsBatNBatVoltage_Object = MibScalar
upsBatNBatVoltage = _UpsBatNBatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 3, 6),
    _UpsBatNBatVoltage_Type()
)
upsBatNBatVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatNBatVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsBatNBatVoltage.setUnits("0.1 Volt DC")
_UpsBatPBatCurrent_Type = Integer32
_UpsBatPBatCurrent_Object = MibScalar
upsBatPBatCurrent = _UpsBatPBatCurrent_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 3, 7),
    _UpsBatPBatCurrent_Type()
)
upsBatPBatCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatPBatCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsBatPBatCurrent.setUnits("0.1 Amp DC")
_UpsBatNBatCurrent_Type = Integer32
_UpsBatNBatCurrent_Object = MibScalar
upsBatNBatCurrent = _UpsBatNBatCurrent_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 3, 8),
    _UpsBatNBatCurrent_Type()
)
upsBatNBatCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatNBatCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsBatNBatCurrent.setUnits("0.1 Amp DC")
_UpsBatPBatChargCurrent_Type = Integer32
_UpsBatPBatChargCurrent_Object = MibScalar
upsBatPBatChargCurrent = _UpsBatPBatChargCurrent_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 3, 9),
    _UpsBatPBatChargCurrent_Type()
)
upsBatPBatChargCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatPBatChargCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsBatPBatChargCurrent.setUnits("0.1 Amp DC")
_UpsBatNBatchargCurrent_Type = Integer32
_UpsBatNBatchargCurrent_Object = MibScalar
upsBatNBatchargCurrent = _UpsBatNBatchargCurrent_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 3, 10),
    _UpsBatNBatchargCurrent_Type()
)
upsBatNBatchargCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatNBatchargCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsBatNBatchargCurrent.setUnits("0.1 Amp DC")
_UpsBatPBatDischargCurrent_Type = Integer32
_UpsBatPBatDischargCurrent_Object = MibScalar
upsBatPBatDischargCurrent = _UpsBatPBatDischargCurrent_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 3, 11),
    _UpsBatPBatDischargCurrent_Type()
)
upsBatPBatDischargCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatPBatDischargCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsBatPBatDischargCurrent.setUnits("0.1 Amp DC")
_UpsBatNBatDischargCurrent_Type = Integer32
_UpsBatNBatDischargCurrent_Object = MibScalar
upsBatNBatDischargCurrent = _UpsBatNBatDischargCurrent_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 3, 12),
    _UpsBatNBatDischargCurrent_Type()
)
upsBatNBatDischargCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatNBatDischargCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsBatNBatDischargCurrent.setUnits("0.1 Amp DC")
_UpsBatTemperature_Type = Integer32
_UpsBatTemperature_Object = MibScalar
upsBatTemperature = _UpsBatTemperature_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 3, 13),
    _UpsBatTemperature_Type()
)
upsBatTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatTemperature.setStatus("current")
if mibBuilder.loadTexts:
    upsBatTemperature.setUnits("degrees 0.1 Centigrade")
_UpsBatNumberInSeries_Type = PositiveInteger
_UpsBatNumberInSeries_Object = MibScalar
upsBatNumberInSeries = _UpsBatNumberInSeries_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 3, 14),
    _UpsBatNumberInSeries_Type()
)
upsBatNumberInSeries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatNumberInSeries.setStatus("current")
_UpsBatNumberInParallel_Type = PositiveInteger
_UpsBatNumberInParallel_Object = MibScalar
upsBatNumberInParallel = _UpsBatNumberInParallel_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 3, 15),
    _UpsBatNumberInParallel_Type()
)
upsBatNumberInParallel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatNumberInParallel.setStatus("current")
_UpsBatPBatDischargCurrent2_Type = Integer32
_UpsBatPBatDischargCurrent2_Object = MibScalar
upsBatPBatDischargCurrent2 = _UpsBatPBatDischargCurrent2_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 3, 16),
    _UpsBatPBatDischargCurrent2_Type()
)
upsBatPBatDischargCurrent2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsBatPBatDischargCurrent2.setStatus("current")
if mibBuilder.loadTexts:
    upsBatPBatDischargCurrent2.setUnits("0.1 Amp DC")
_UpsInput_ObjectIdentity = ObjectIdentity
upsInput = _UpsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 4)
)
_UpsInLineBads_Type = NonNegativeInteger
_UpsInLineBads_Object = MibScalar
upsInLineBads = _UpsInLineBads_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 4, 1),
    _UpsInLineBads_Type()
)
upsInLineBads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInLineBads.setStatus("current")
_UpsInTtlApparentPower_Type = NonNegativeInteger
_UpsInTtlApparentPower_Object = MibScalar
upsInTtlApparentPower = _UpsInTtlApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 4, 2),
    _UpsInTtlApparentPower_Type()
)
upsInTtlApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInTtlApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    upsInTtlApparentPower.setUnits("0.1VA")
_UpsInTtlTruePower_Type = NonNegativeInteger
_UpsInTtlTruePower_Object = MibScalar
upsInTtlTruePower = _UpsInTtlTruePower_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 4, 3),
    _UpsInTtlTruePower_Type()
)
upsInTtlTruePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInTtlTruePower.setStatus("current")
if mibBuilder.loadTexts:
    upsInTtlTruePower.setUnits("0.1WT")
_UpsInNumLines_Type = NonNegativeInteger
_UpsInNumLines_Object = MibScalar
upsInNumLines = _UpsInNumLines_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 4, 4),
    _UpsInNumLines_Type()
)
upsInNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInNumLines.setStatus("current")
_UpsInTable_Object = MibTable
upsInTable = _UpsInTable_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 4, 5)
)
if mibBuilder.loadTexts:
    upsInTable.setStatus("current")
_UpsInEntry_Object = MibTableRow
upsInEntry = _UpsInEntry_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 4, 5, 1)
)
upsInEntry.setIndexNames(
    (0, "VoltronicMIB", "upsInLineIndex"),
)
if mibBuilder.loadTexts:
    upsInEntry.setStatus("current")


class _UpsInLineIndex_Type(Integer32):
    """Custom type upsInLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_UpsInLineIndex_Type.__name__ = "Integer32"
_UpsInLineIndex_Object = MibTableColumn
upsInLineIndex = _UpsInLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 4, 5, 1, 1),
    _UpsInLineIndex_Type()
)
upsInLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInLineIndex.setStatus("current")
_UpsInFrequency_Type = NonNegativeInteger
_UpsInFrequency_Object = MibTableColumn
upsInFrequency = _UpsInFrequency_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 4, 5, 1, 2),
    _UpsInFrequency_Type()
)
upsInFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInFrequency.setStatus("current")
if mibBuilder.loadTexts:
    upsInFrequency.setUnits("0.1 Hertz")
_UpsInVoltage_Type = Integer32
_UpsInVoltage_Object = MibTableColumn
upsInVoltage = _UpsInVoltage_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 4, 5, 1, 3),
    _UpsInVoltage_Type()
)
upsInVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsInVoltage.setUnits("0.1 Volts")
_UpsInCurrent_Type = Integer32
_UpsInCurrent_Object = MibTableColumn
upsInCurrent = _UpsInCurrent_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 4, 5, 1, 4),
    _UpsInCurrent_Type()
)
upsInCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsInCurrent.setUnits("0.1Amp")
_UpsInApparentPower_Type = NonNegativeInteger
_UpsInApparentPower_Object = MibTableColumn
upsInApparentPower = _UpsInApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 4, 5, 1, 5),
    _UpsInApparentPower_Type()
)
upsInApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    upsInApparentPower.setUnits("0.1VA")
_UpsInTruePower_Type = NonNegativeInteger
_UpsInTruePower_Object = MibTableColumn
upsInTruePower = _UpsInTruePower_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 4, 5, 1, 6),
    _UpsInTruePower_Type()
)
upsInTruePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInTruePower.setStatus("current")
if mibBuilder.loadTexts:
    upsInTruePower.setUnits("0.1Watts")
_UpsInPowerFactor_Type = NonNegativeInteger
_UpsInPowerFactor_Object = MibTableColumn
upsInPowerFactor = _UpsInPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 4, 5, 1, 7),
    _UpsInPowerFactor_Type()
)
upsInPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    upsInPowerFactor.setUnits("0.01")
_UpsInLineVoltage_Type = Integer32
_UpsInLineVoltage_Object = MibTableColumn
upsInLineVoltage = _UpsInLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 4, 5, 1, 8),
    _UpsInLineVoltage_Type()
)
upsInLineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInLineVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsInLineVoltage.setUnits("0.1 Volts")
_UpsInTtlVoltage_Type = Integer32
_UpsInTtlVoltage_Object = MibScalar
upsInTtlVoltage = _UpsInTtlVoltage_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 4, 6),
    _UpsInTtlVoltage_Type()
)
upsInTtlVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInTtlVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsInTtlVoltage.setUnits("0.1 Volts")
_UpsInTtlCurrent_Type = Integer32
_UpsInTtlCurrent_Object = MibScalar
upsInTtlCurrent = _UpsInTtlCurrent_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 4, 7),
    _UpsInTtlCurrent_Type()
)
upsInTtlCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsInTtlCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsInTtlCurrent.setUnits("0.1 A")
_UpsOutput_ObjectIdentity = ObjectIdentity
upsOutput = _UpsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 5)
)


class _UpsOutSource_Type(Integer32):
    """Custom type upsOutSource based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("none", 2),
          ("normal", 3),
          ("bypass", 4),
          ("battery", 5),
          ("booster", 6),
          ("reducer", 7),
          ("batterytest", 8),
          ("fault", 9),
          ("HE-ECO-mode", 10),
          ("converter-mode", 11))
    )


_UpsOutSource_Type.__name__ = "Integer32"
_UpsOutSource_Object = MibScalar
upsOutSource = _UpsOutSource_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 5, 1),
    _UpsOutSource_Type()
)
upsOutSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutSource.setStatus("current")
_UpsOutFreq_Type = Integer32
_UpsOutFreq_Object = MibScalar
upsOutFreq = _UpsOutFreq_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 5, 2),
    _UpsOutFreq_Type()
)
upsOutFreq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutFreq.setStatus("current")
if mibBuilder.loadTexts:
    upsOutFreq.setUnits("0.1 Hertz")
_UpsOutTtlApparentPower_Type = NonNegativeInteger
_UpsOutTtlApparentPower_Object = MibScalar
upsOutTtlApparentPower = _UpsOutTtlApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 5, 3),
    _UpsOutTtlApparentPower_Type()
)
upsOutTtlApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutTtlApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    upsOutTtlApparentPower.setUnits("0.1VA")
_UpsOutTtlTruePower_Type = NonNegativeInteger
_UpsOutTtlTruePower_Object = MibScalar
upsOutTtlTruePower = _UpsOutTtlTruePower_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 5, 4),
    _UpsOutTtlTruePower_Type()
)
upsOutTtlTruePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutTtlTruePower.setStatus("current")
if mibBuilder.loadTexts:
    upsOutTtlTruePower.setUnits("0.1Watts")


class _UpsOutTtlPercentLoad_Type(Integer32):
    """Custom type upsOutTtlPercentLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpsOutTtlPercentLoad_Type.__name__ = "Integer32"
_UpsOutTtlPercentLoad_Object = MibScalar
upsOutTtlPercentLoad = _UpsOutTtlPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 5, 5),
    _UpsOutTtlPercentLoad_Type()
)
upsOutTtlPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutTtlPercentLoad.setStatus("current")
if mibBuilder.loadTexts:
    upsOutTtlPercentLoad.setUnits("percent")
_UpsOutNumLines_Type = Integer32
_UpsOutNumLines_Object = MibScalar
upsOutNumLines = _UpsOutNumLines_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 5, 6),
    _UpsOutNumLines_Type()
)
upsOutNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutNumLines.setStatus("current")
_UpsOutTable_Object = MibTable
upsOutTable = _UpsOutTable_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 5, 7)
)
if mibBuilder.loadTexts:
    upsOutTable.setStatus("current")
_UpsOutEntry_Object = MibTableRow
upsOutEntry = _UpsOutEntry_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 5, 7, 1)
)
upsOutEntry.setIndexNames(
    (0, "VoltronicMIB", "upsOutLineIndex"),
)
if mibBuilder.loadTexts:
    upsOutEntry.setStatus("current")


class _UpsOutLineIndex_Type(Integer32):
    """Custom type upsOutLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_UpsOutLineIndex_Type.__name__ = "Integer32"
_UpsOutLineIndex_Object = MibTableColumn
upsOutLineIndex = _UpsOutLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 5, 7, 1, 1),
    _UpsOutLineIndex_Type()
)
upsOutLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutLineIndex.setStatus("current")
_UpsOutVoltage_Type = Integer32
_UpsOutVoltage_Object = MibTableColumn
upsOutVoltage = _UpsOutVoltage_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 5, 7, 1, 2),
    _UpsOutVoltage_Type()
)
upsOutVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsOutVoltage.setUnits("0.1 Volts")
_UpsOutCurrent_Type = Integer32
_UpsOutCurrent_Object = MibTableColumn
upsOutCurrent = _UpsOutCurrent_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 5, 7, 1, 3),
    _UpsOutCurrent_Type()
)
upsOutCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsOutCurrent.setUnits("0.1 Amp")
_UpsOutApparentPower_Type = NonNegativeInteger
_UpsOutApparentPower_Object = MibTableColumn
upsOutApparentPower = _UpsOutApparentPower_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 5, 7, 1, 4),
    _UpsOutApparentPower_Type()
)
upsOutApparentPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutApparentPower.setStatus("current")
if mibBuilder.loadTexts:
    upsOutApparentPower.setUnits("0.1VA")
_UpsOutTruePower_Type = NonNegativeInteger
_UpsOutTruePower_Object = MibTableColumn
upsOutTruePower = _UpsOutTruePower_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 5, 7, 1, 5),
    _UpsOutTruePower_Type()
)
upsOutTruePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutTruePower.setStatus("current")
if mibBuilder.loadTexts:
    upsOutTruePower.setUnits("0.1Watts")
_UpsOutPowerFactor_Type = NonNegativeInteger
_UpsOutPowerFactor_Object = MibTableColumn
upsOutPowerFactor = _UpsOutPowerFactor_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 5, 7, 1, 6),
    _UpsOutPowerFactor_Type()
)
upsOutPowerFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutPowerFactor.setStatus("current")
if mibBuilder.loadTexts:
    upsOutPowerFactor.setUnits("0.01")


class _UpsOutPercentLoad_Type(Integer32):
    """Custom type upsOutPercentLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_UpsOutPercentLoad_Type.__name__ = "Integer32"
_UpsOutPercentLoad_Object = MibTableColumn
upsOutPercentLoad = _UpsOutPercentLoad_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 5, 7, 1, 7),
    _UpsOutPercentLoad_Type()
)
upsOutPercentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutPercentLoad.setStatus("current")
if mibBuilder.loadTexts:
    upsOutPercentLoad.setUnits("percent")
_UpsOutLineVoltage_Type = Integer32
_UpsOutLineVoltage_Object = MibTableColumn
upsOutLineVoltage = _UpsOutLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 5, 7, 1, 8),
    _UpsOutLineVoltage_Type()
)
upsOutLineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutLineVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsOutLineVoltage.setUnits("0.1 Volts")
_UpsOutFrequency_Type = NonNegativeInteger
_UpsOutFrequency_Object = MibScalar
upsOutFrequency = _UpsOutFrequency_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 5, 7, 1, 9),
    _UpsOutFrequency_Type()
)
upsOutFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutFrequency.setStatus("current")
if mibBuilder.loadTexts:
    upsOutFrequency.setUnits("0.1Hertz")
_UpsOutTtlVoltage_Type = Integer32
_UpsOutTtlVoltage_Object = MibScalar
upsOutTtlVoltage = _UpsOutTtlVoltage_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 5, 8),
    _UpsOutTtlVoltage_Type()
)
upsOutTtlVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutTtlVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsOutTtlVoltage.setUnits("0.1vot")
_UpsOutTtlCurrent_Type = Integer32
_UpsOutTtlCurrent_Object = MibScalar
upsOutTtlCurrent = _UpsOutTtlCurrent_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 5, 9),
    _UpsOutTtlCurrent_Type()
)
upsOutTtlCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutTtlCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsOutTtlCurrent.setUnits("0.1A")


class _UpsOutStatus_Type(DisplayString):
    """Custom type upsOutStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_UpsOutStatus_Type.__name__ = "DisplayString"
_UpsOutStatus_Object = MibScalar
upsOutStatus = _UpsOutStatus_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 5, 10),
    _UpsOutStatus_Type()
)
upsOutStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutStatus.setStatus("current")


class _UpsOutSource2_Type(Integer32):
    """Custom type upsOutSource2 based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("none", 2),
          ("normal", 3),
          ("bypass", 4),
          ("battery", 5),
          ("booster", 6),
          ("reducer", 7),
          ("batterytest", 8),
          ("fault", 9),
          ("HE-ECO-mode", 10),
          ("converter-mode", 11))
    )


_UpsOutSource2_Type.__name__ = "Integer32"
_UpsOutSource2_Object = MibScalar
upsOutSource2 = _UpsOutSource2_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 5, 11),
    _UpsOutSource2_Type()
)
upsOutSource2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsOutSource2.setStatus("current")
_UpsBypass_ObjectIdentity = ObjectIdentity
upsBypass = _UpsBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 6)
)
_UpsByFrequency_Type = Integer32
_UpsByFrequency_Object = MibScalar
upsByFrequency = _UpsByFrequency_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 6, 1),
    _UpsByFrequency_Type()
)
upsByFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsByFrequency.setStatus("current")
if mibBuilder.loadTexts:
    upsByFrequency.setUnits("0.1 Hertz")
_UpsByNumLines_Type = Integer32
_UpsByNumLines_Object = MibScalar
upsByNumLines = _UpsByNumLines_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 6, 2),
    _UpsByNumLines_Type()
)
upsByNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsByNumLines.setStatus("current")
_UpsByTable_Object = MibTable
upsByTable = _UpsByTable_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 6, 3)
)
if mibBuilder.loadTexts:
    upsByTable.setStatus("current")
_UpsByEntry_Object = MibTableRow
upsByEntry = _UpsByEntry_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 6, 3, 1)
)
upsByEntry.setIndexNames(
    (0, "VoltronicMIB", "upsByLineIndex"),
)
if mibBuilder.loadTexts:
    upsByEntry.setStatus("current")


class _UpsByLineIndex_Type(Integer32):
    """Custom type upsByLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UpsByLineIndex_Type.__name__ = "Integer32"
_UpsByLineIndex_Object = MibTableColumn
upsByLineIndex = _UpsByLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 6, 3, 1, 1),
    _UpsByLineIndex_Type()
)
upsByLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsByLineIndex.setStatus("current")
_UpsByVoltage_Type = Integer32
_UpsByVoltage_Object = MibTableColumn
upsByVoltage = _UpsByVoltage_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 6, 3, 1, 2),
    _UpsByVoltage_Type()
)
upsByVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsByVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsByVoltage.setUnits("0.1 Volts")
_UpsByCurrent_Type = Integer32
_UpsByCurrent_Object = MibTableColumn
upsByCurrent = _UpsByCurrent_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 6, 3, 1, 3),
    _UpsByCurrent_Type()
)
upsByCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsByCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsByCurrent.setUnits("0.1 RMS Amp")
_UpsByPower_Type = NonNegativeInteger
_UpsByPower_Object = MibTableColumn
upsByPower = _UpsByPower_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 6, 3, 1, 4),
    _UpsByPower_Type()
)
upsByPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsByPower.setStatus("current")
if mibBuilder.loadTexts:
    upsByPower.setUnits("0.1Watts")
_UpsByLineVoltage_Type = Integer32
_UpsByLineVoltage_Object = MibTableColumn
upsByLineVoltage = _UpsByLineVoltage_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 6, 3, 1, 5),
    _UpsByLineVoltage_Type()
)
upsByLineVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsByLineVoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsByLineVoltage.setUnits("0.1 Volts")
_UpsTest_ObjectIdentity = ObjectIdentity
upsTest = _UpsTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 7)
)


class _UpsTstBatteryTest_Type(Integer32):
    """Custom type upsTstBatteryTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("battTest10sec", 2),
          ("battTestUntilLow", 3),
          ("battTestWithTime", 4),
          ("battTestCancelTest", 5),
          ("battTestClearInfo", 6))
    )


_UpsTstBatteryTest_Type.__name__ = "Integer32"
_UpsTstBatteryTest_Object = MibScalar
upsTstBatteryTest = _UpsTstBatteryTest_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 7, 1),
    _UpsTstBatteryTest_Type()
)
upsTstBatteryTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTstBatteryTest.setStatus("current")


class _UpsTstBatteryTestResult_Type(Integer32):
    """Custom type upsTstBatteryTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("donePassed", 1),
          ("doneWarning", 2),
          ("doneError", 3),
          ("aborted", 4),
          ("inProgress", 5),
          ("noTestsInitiated", 6))
    )


_UpsTstBatteryTestResult_Type.__name__ = "Integer32"
_UpsTstBatteryTestResult_Object = MibScalar
upsTstBatteryTestResult = _UpsTstBatteryTestResult_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 7, 2),
    _UpsTstBatteryTestResult_Type()
)
upsTstBatteryTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTstBatteryTestResult.setStatus("mandatory")


class _UpsTstBatteryTestStartTime_Type(DisplayString):
    """Custom type upsTstBatteryTestStartTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )
    fixed_length = 19


_UpsTstBatteryTestStartTime_Type.__name__ = "DisplayString"
_UpsTstBatteryTestStartTime_Object = MibScalar
upsTstBatteryTestStartTime = _UpsTstBatteryTestStartTime_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 7, 3),
    _UpsTstBatteryTestStartTime_Type()
)
upsTstBatteryTestStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsTstBatteryTestStartTime.setStatus("current")


class _UpsTstBatterySettingTime_Type(Integer32):
    """Custom type upsTstBatterySettingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(12, 5940),
    )


_UpsTstBatterySettingTime_Type.__name__ = "Integer32"
_UpsTstBatterySettingTime_Object = MibScalar
upsTstBatterySettingTime = _UpsTstBatterySettingTime_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 7, 4),
    _UpsTstBatterySettingTime_Type()
)
upsTstBatterySettingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsTstBatterySettingTime.setStatus("mandatory")
_UpsControl_ObjectIdentity = ObjectIdentity
upsControl = _UpsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 8)
)


class _UpsCtlShutdownDelay_Type(Integer32):
    """Custom type upsCtlShutdownDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2, 2147483648),
    )


_UpsCtlShutdownDelay_Type.__name__ = "Integer32"
_UpsCtlShutdownDelay_Object = MibScalar
upsCtlShutdownDelay = _UpsCtlShutdownDelay_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 8, 1),
    _UpsCtlShutdownDelay_Type()
)
upsCtlShutdownDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCtlShutdownDelay.setStatus("current")
if mibBuilder.loadTexts:
    upsCtlShutdownDelay.setUnits("seconds")


class _UpsCtlSleepTime_Type(Integer32):
    """Custom type upsCtlSleepTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483648),
    )


_UpsCtlSleepTime_Type.__name__ = "Integer32"
_UpsCtlSleepTime_Object = MibScalar
upsCtlSleepTime = _UpsCtlSleepTime_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 8, 2),
    _UpsCtlSleepTime_Type()
)
upsCtlSleepTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCtlSleepTime.setStatus("current")
if mibBuilder.loadTexts:
    upsCtlSleepTime.setUnits("minutes")


class _UpsCtlStartupAfterDelay_Type(Integer32):
    """Custom type upsCtlStartupAfterDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483648),
    )


_UpsCtlStartupAfterDelay_Type.__name__ = "Integer32"
_UpsCtlStartupAfterDelay_Object = MibScalar
upsCtlStartupAfterDelay = _UpsCtlStartupAfterDelay_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 8, 3),
    _UpsCtlStartupAfterDelay_Type()
)
upsCtlStartupAfterDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCtlStartupAfterDelay.setStatus("current")
if mibBuilder.loadTexts:
    upsCtlStartupAfterDelay.setUnits("seconds")


class _UpsCtlbuzzer_Type(Integer32):
    """Custom type upsCtlbuzzer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_UpsCtlbuzzer_Type.__name__ = "Integer32"
_UpsCtlbuzzer_Object = MibScalar
upsCtlbuzzer = _UpsCtlbuzzer_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 8, 4),
    _UpsCtlbuzzer_Type()
)
upsCtlbuzzer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCtlbuzzer.setStatus("current")


class _UpsCtlRemoteControlUPS_Type(Integer32):
    """Custom type upsCtlRemoteControlUPS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_UpsCtlRemoteControlUPS_Type.__name__ = "Integer32"
_UpsCtlRemoteControlUPS_Object = MibScalar
upsCtlRemoteControlUPS = _UpsCtlRemoteControlUPS_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 8, 5),
    _UpsCtlRemoteControlUPS_Type()
)
upsCtlRemoteControlUPS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCtlRemoteControlUPS.setStatus("current")


class _UpsCtloutletPoweron_Type(Integer32):
    """Custom type upsCtloutletPoweron based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_UpsCtloutletPoweron_Type.__name__ = "Integer32"
_UpsCtloutletPoweron_Object = MibScalar
upsCtloutletPoweron = _UpsCtloutletPoweron_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 8, 6),
    _UpsCtloutletPoweron_Type()
)
upsCtloutletPoweron.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    upsCtloutletPoweron.setStatus("current")


class _UpsCtloutletPoweroff_Type(Integer32):
    """Custom type upsCtloutletPoweroff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_UpsCtloutletPoweroff_Type.__name__ = "Integer32"
_UpsCtloutletPoweroff_Object = MibScalar
upsCtloutletPoweroff = _UpsCtloutletPoweroff_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 8, 7),
    _UpsCtloutletPoweroff_Type()
)
upsCtloutletPoweroff.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    upsCtloutletPoweroff.setStatus("current")


class _UpsCtlOutlet1Powerofftime_Type(Integer32):
    """Custom type upsCtlOutlet1Powerofftime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 999),
    )


_UpsCtlOutlet1Powerofftime_Type.__name__ = "Integer32"
_UpsCtlOutlet1Powerofftime_Object = MibScalar
upsCtlOutlet1Powerofftime = _UpsCtlOutlet1Powerofftime_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 8, 8),
    _UpsCtlOutlet1Powerofftime_Type()
)
upsCtlOutlet1Powerofftime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCtlOutlet1Powerofftime.setStatus("current")


class _UpsCtlOutlet2Powerofftime_Type(Integer32):
    """Custom type upsCtlOutlet2Powerofftime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 999),
    )


_UpsCtlOutlet2Powerofftime_Type.__name__ = "Integer32"
_UpsCtlOutlet2Powerofftime_Object = MibScalar
upsCtlOutlet2Powerofftime = _UpsCtlOutlet2Powerofftime_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 8, 9),
    _UpsCtlOutlet2Powerofftime_Type()
)
upsCtlOutlet2Powerofftime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCtlOutlet2Powerofftime.setStatus("current")


class _UpsCtlResetConfigure_Type(Integer32):
    """Custom type upsCtlResetConfigure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("reset", 1))
    )


_UpsCtlResetConfigure_Type.__name__ = "Integer32"
_UpsCtlResetConfigure_Object = MibScalar
upsCtlResetConfigure = _UpsCtlResetConfigure_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 8, 10),
    _UpsCtlResetConfigure_Type()
)
upsCtlResetConfigure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCtlResetConfigure.setStatus("current")
_AgentConfig_ObjectIdentity = ObjectIdentity
agentConfig = _AgentConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 9)
)


class _AgentConfigDatetime_Type(DisplayString):
    """Custom type agentConfigDatetime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(19, 19),
    )
    fixed_length = 19


_AgentConfigDatetime_Type.__name__ = "DisplayString"
_AgentConfigDatetime_Object = MibScalar
agentConfigDatetime = _AgentConfigDatetime_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 9, 1),
    _AgentConfigDatetime_Type()
)
agentConfigDatetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentConfigDatetime.setStatus("current")
_CommConfig_ObjectIdentity = ObjectIdentity
commConfig = _CommConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 10)
)


class _CommBaudRate_Type(Integer32):
    """Custom type commBaudRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("B1200", 1),
          ("B2400", 2),
          ("B4800", 3),
          ("B9600", 4),
          ("B19200", 5))
    )


_CommBaudRate_Type.__name__ = "Integer32"
_CommBaudRate_Object = MibScalar
commBaudRate = _CommBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 10, 1),
    _CommBaudRate_Type()
)
commBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commBaudRate.setStatus("current")


class _CommDatabits_Type(Integer32):
    """Custom type commDatabits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 9),
    )


_CommDatabits_Type.__name__ = "Integer32"
_CommDatabits_Object = MibScalar
commDatabits = _CommDatabits_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 10, 2),
    _CommDatabits_Type()
)
commDatabits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commDatabits.setStatus("current")


class _CommStopbits_Type(Integer32):
    """Custom type commStopbits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_CommStopbits_Type.__name__ = "Integer32"
_CommStopbits_Object = MibScalar
commStopbits = _CommStopbits_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 10, 3),
    _CommStopbits_Type()
)
commStopbits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commStopbits.setStatus("current")


class _CommParity_Type(Integer32):
    """Custom type commParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("odd", 1),
          ("even", 2))
    )


_CommParity_Type.__name__ = "Integer32"
_CommParity_Object = MibScalar
commParity = _CommParity_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 10, 4),
    _CommParity_Type()
)
commParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commParity.setStatus("current")


class _CommTimeout_Type(Integer32):
    """Custom type commTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 1000),
    )


_CommTimeout_Type.__name__ = "Integer32"
_CommTimeout_Object = MibScalar
commTimeout = _CommTimeout_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 10, 5),
    _CommTimeout_Type()
)
commTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commTimeout.setStatus("current")
_UpsConfig_ObjectIdentity = ObjectIdentity
upsConfig = _UpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11)
)


class _UpsCfgAlarmbypass_Type(Integer32):
    """Custom type upsCfgAlarmbypass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notsupport", 2))
    )


_UpsCfgAlarmbypass_Type.__name__ = "Integer32"
_UpsCfgAlarmbypass_Object = MibScalar
upsCfgAlarmbypass = _UpsCfgAlarmbypass_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 1),
    _UpsCfgAlarmbypass_Type()
)
upsCfgAlarmbypass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgAlarmbypass.setStatus("current")


class _UpsCfgAlarmbattery_Type(Integer32):
    """Custom type upsCfgAlarmbattery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notsupport", 2))
    )


_UpsCfgAlarmbattery_Type.__name__ = "Integer32"
_UpsCfgAlarmbattery_Object = MibScalar
upsCfgAlarmbattery = _UpsCfgAlarmbattery_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 2),
    _UpsCfgAlarmbattery_Type()
)
upsCfgAlarmbattery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgAlarmbattery.setStatus("current")


class _UpsCfgAutoReboot_Type(Integer32):
    """Custom type upsCfgAutoReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notsupport", 2))
    )


_UpsCfgAutoReboot_Type.__name__ = "Integer32"
_UpsCfgAutoReboot_Object = MibScalar
upsCfgAutoReboot = _UpsCfgAutoReboot_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 3),
    _UpsCfgAutoReboot_Type()
)
upsCfgAutoReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgAutoReboot.setStatus("current")


class _UpsCfgBypasswhenupsoff_Type(Integer32):
    """Custom type upsCfgBypasswhenupsoff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notsupport", 2))
    )


_UpsCfgBypasswhenupsoff_Type.__name__ = "Integer32"
_UpsCfgBypasswhenupsoff_Object = MibScalar
upsCfgBypasswhenupsoff = _UpsCfgBypasswhenupsoff_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 4),
    _UpsCfgBypasswhenupsoff_Type()
)
upsCfgBypasswhenupsoff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgBypasswhenupsoff.setStatus("current")


class _UpsCfgBatterDDP_Type(Integer32):
    """Custom type upsCfgBatterDDP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notsupport", 2))
    )


_UpsCfgBatterDDP_Type.__name__ = "Integer32"
_UpsCfgBatterDDP_Object = MibScalar
upsCfgBatterDDP = _UpsCfgBatterDDP_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 5),
    _UpsCfgBatterDDP_Type()
)
upsCfgBatterDDP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgBatterDDP.setStatus("current")


class _UpsCfgConvertermode_Type(Integer32):
    """Custom type upsCfgConvertermode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notsupport", 2))
    )


_UpsCfgConvertermode_Type.__name__ = "Integer32"
_UpsCfgConvertermode_Object = MibScalar
upsCfgConvertermode = _UpsCfgConvertermode_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 6),
    _UpsCfgConvertermode_Type()
)
upsCfgConvertermode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgConvertermode.setStatus("current")


class _UpsCfgECOmode_Type(Integer32):
    """Custom type upsCfgECOmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notsupport", 2))
    )


_UpsCfgECOmode_Type.__name__ = "Integer32"
_UpsCfgECOmode_Object = MibScalar
upsCfgECOmode = _UpsCfgECOmode_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 7),
    _UpsCfgECOmode_Type()
)
upsCfgECOmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgECOmode.setStatus("current")


class _UpsCfgAdvanceECOmode_Type(Integer32):
    """Custom type upsCfgAdvanceECOmode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notsupport", 2))
    )


_UpsCfgAdvanceECOmode_Type.__name__ = "Integer32"
_UpsCfgAdvanceECOmode_Object = MibScalar
upsCfgAdvanceECOmode = _UpsCfgAdvanceECOmode_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 8),
    _UpsCfgAdvanceECOmode_Type()
)
upsCfgAdvanceECOmode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgAdvanceECOmode.setStatus("current")


class _UpsCfgGreenPowerFunction_Type(Integer32):
    """Custom type upsCfgGreenPowerFunction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notsupport", 2))
    )


_UpsCfgGreenPowerFunction_Type.__name__ = "Integer32"
_UpsCfgGreenPowerFunction_Object = MibScalar
upsCfgGreenPowerFunction = _UpsCfgGreenPowerFunction_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 9),
    _UpsCfgGreenPowerFunction_Type()
)
upsCfgGreenPowerFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgGreenPowerFunction.setStatus("current")


class _UpsCfgBatteryOSC_Type(Integer32):
    """Custom type upsCfgBatteryOSC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notsupport", 2))
    )


_UpsCfgBatteryOSC_Type.__name__ = "Integer32"
_UpsCfgBatteryOSC_Object = MibScalar
upsCfgBatteryOSC = _UpsCfgBatteryOSC_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 10),
    _UpsCfgBatteryOSC_Type()
)
upsCfgBatteryOSC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgBatteryOSC.setStatus("current")


class _UpsCfgAllowShort3times_Type(Integer32):
    """Custom type upsCfgAllowShort3times based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notsupport", 2))
    )


_UpsCfgAllowShort3times_Type.__name__ = "Integer32"
_UpsCfgAllowShort3times_Object = MibScalar
upsCfgAllowShort3times = _UpsCfgAllowShort3times_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 11),
    _UpsCfgAllowShort3times_Type()
)
upsCfgAllowShort3times.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgAllowShort3times.setStatus("current")


class _UpsCfgColdstart_Type(Integer32):
    """Custom type upsCfgColdstart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notsupport", 2))
    )


_UpsCfgColdstart_Type.__name__ = "Integer32"
_UpsCfgColdstart_Object = MibScalar
upsCfgColdstart = _UpsCfgColdstart_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 12),
    _UpsCfgColdstart_Type()
)
upsCfgColdstart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgColdstart.setStatus("current")


class _UpsCfgBypassNotAllowed_Type(Integer32):
    """Custom type upsCfgBypassNotAllowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notsupport", 2))
    )


_UpsCfgBypassNotAllowed_Type.__name__ = "Integer32"
_UpsCfgBypassNotAllowed_Object = MibScalar
upsCfgBypassNotAllowed = _UpsCfgBypassNotAllowed_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 13),
    _UpsCfgBypassNotAllowed_Type()
)
upsCfgBypassNotAllowed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgBypassNotAllowed.setStatus("current")


class _UpsCfgBatterylowprotect_Type(Integer32):
    """Custom type upsCfgBatterylowprotect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notsupport", 2))
    )


_UpsCfgBatterylowprotect_Type.__name__ = "Integer32"
_UpsCfgBatterylowprotect_Object = MibScalar
upsCfgBatterylowprotect = _UpsCfgBatterylowprotect_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 14),
    _UpsCfgBatterylowprotect_Type()
)
upsCfgBatterylowprotect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgBatterylowprotect.setStatus("current")


class _UpsCfgP1progoutletcontrol_Type(Integer32):
    """Custom type upsCfgP1progoutletcontrol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notsupport", 2))
    )


_UpsCfgP1progoutletcontrol_Type.__name__ = "Integer32"
_UpsCfgP1progoutletcontrol_Object = MibScalar
upsCfgP1progoutletcontrol = _UpsCfgP1progoutletcontrol_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 15),
    _UpsCfgP1progoutletcontrol_Type()
)
upsCfgP1progoutletcontrol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgP1progoutletcontrol.setStatus("current")


class _UpsCfgP2progoutletcontrol_Type(Integer32):
    """Custom type upsCfgP2progoutletcontrol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notsupport", 2))
    )


_UpsCfgP2progoutletcontrol_Type.__name__ = "Integer32"
_UpsCfgP2progoutletcontrol_Object = MibScalar
upsCfgP2progoutletcontrol = _UpsCfgP2progoutletcontrol_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 16),
    _UpsCfgP2progoutletcontrol_Type()
)
upsCfgP2progoutletcontrol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgP2progoutletcontrol.setStatus("current")


class _UpsCfgInverterShortClear_Type(Integer32):
    """Custom type upsCfgInverterShortClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notsupport", 2))
    )


_UpsCfgInverterShortClear_Type.__name__ = "Integer32"
_UpsCfgInverterShortClear_Object = MibScalar
upsCfgInverterShortClear = _UpsCfgInverterShortClear_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 17),
    _UpsCfgInverterShortClear_Type()
)
upsCfgInverterShortClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgInverterShortClear.setStatus("current")


class _UpsCfgSitefaildetection_Type(Integer32):
    """Custom type upsCfgSitefaildetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notsupport", 2))
    )


_UpsCfgSitefaildetection_Type.__name__ = "Integer32"
_UpsCfgSitefaildetection_Object = MibScalar
upsCfgSitefaildetection = _UpsCfgSitefaildetection_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 18),
    _UpsCfgSitefaildetection_Type()
)
upsCfgSitefaildetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgSitefaildetection.setStatus("current")


class _UpsCfgBatNumInParallel_Type(Integer32):
    """Custom type upsCfgBatNumInParallel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_UpsCfgBatNumInParallel_Type.__name__ = "Integer32"
_UpsCfgBatNumInParallel_Object = MibScalar
upsCfgBatNumInParallel = _UpsCfgBatNumInParallel_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 19),
    _UpsCfgBatNumInParallel_Type()
)
upsCfgBatNumInParallel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgBatNumInParallel.setStatus("current")


class _UpsCfgBatNumInSeries_Type(Integer32):
    """Custom type upsCfgBatNumInSeries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_UpsCfgBatNumInSeries_Type.__name__ = "Integer32"
_UpsCfgBatNumInSeries_Object = MibScalar
upsCfgBatNumInSeries = _UpsCfgBatNumInSeries_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 20),
    _UpsCfgBatNumInSeries_Type()
)
upsCfgBatNumInSeries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgBatNumInSeries.setStatus("current")


class _UpsCfgBypassmaxvoltage_Type(Integer32):
    """Custom type upsCfgBypassmaxvoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1760, 2760),
    )


_UpsCfgBypassmaxvoltage_Type.__name__ = "Integer32"
_UpsCfgBypassmaxvoltage_Object = MibScalar
upsCfgBypassmaxvoltage = _UpsCfgBypassmaxvoltage_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 21),
    _UpsCfgBypassmaxvoltage_Type()
)
upsCfgBypassmaxvoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgBypassmaxvoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsCfgBypassmaxvoltage.setUnits("0.1 Volts")


class _UpsCfgBypassminvoltage_Type(Integer32):
    """Custom type upsCfgBypassminvoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1760, 2640),
    )


_UpsCfgBypassminvoltage_Type.__name__ = "Integer32"
_UpsCfgBypassminvoltage_Object = MibScalar
upsCfgBypassminvoltage = _UpsCfgBypassminvoltage_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 22),
    _UpsCfgBypassminvoltage_Type()
)
upsCfgBypassminvoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgBypassminvoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsCfgBypassminvoltage.setUnits("0.1 Volts")


class _UpsCfgBypassmaxfrequency_Type(Integer32):
    """Custom type upsCfgBypassmaxfrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(510, 700),
    )


_UpsCfgBypassmaxfrequency_Type.__name__ = "Integer32"
_UpsCfgBypassmaxfrequency_Object = MibScalar
upsCfgBypassmaxfrequency = _UpsCfgBypassmaxfrequency_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 23),
    _UpsCfgBypassmaxfrequency_Type()
)
upsCfgBypassmaxfrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgBypassmaxfrequency.setStatus("current")
if mibBuilder.loadTexts:
    upsCfgBypassmaxfrequency.setUnits("0.1 Hertz")


class _UpsCfgBypassminfrequency_Type(Integer32):
    """Custom type upsCfgBypassminfrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 590),
    )


_UpsCfgBypassminfrequency_Type.__name__ = "Integer32"
_UpsCfgBypassminfrequency_Object = MibScalar
upsCfgBypassminfrequency = _UpsCfgBypassminfrequency_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 24),
    _UpsCfgBypassminfrequency_Type()
)
upsCfgBypassminfrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgBypassminfrequency.setStatus("current")
if mibBuilder.loadTexts:
    upsCfgBypassminfrequency.setUnits("0.1 Hertz")


class _UpsCfgECOmaxvoltage_Type(Integer32):
    """Custom type upsCfgECOmaxvoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3000),
    )


_UpsCfgECOmaxvoltage_Type.__name__ = "Integer32"
_UpsCfgECOmaxvoltage_Object = MibScalar
upsCfgECOmaxvoltage = _UpsCfgECOmaxvoltage_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 25),
    _UpsCfgECOmaxvoltage_Type()
)
upsCfgECOmaxvoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgECOmaxvoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsCfgECOmaxvoltage.setUnits("0.1 Volts")


class _UpsCfgECOminvoltage_Type(Integer32):
    """Custom type upsCfgECOminvoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3000),
    )


_UpsCfgECOminvoltage_Type.__name__ = "Integer32"
_UpsCfgECOminvoltage_Object = MibScalar
upsCfgECOminvoltage = _UpsCfgECOminvoltage_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 26),
    _UpsCfgECOminvoltage_Type()
)
upsCfgECOminvoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgECOminvoltage.setStatus("current")
if mibBuilder.loadTexts:
    upsCfgECOminvoltage.setUnits("0.1 Volts")


class _UpsCfgFreeRunMaxFrequency_Type(Integer32):
    """Custom type upsCfgFreeRunMaxFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 700),
    )


_UpsCfgFreeRunMaxFrequency_Type.__name__ = "Integer32"
_UpsCfgFreeRunMaxFrequency_Object = MibScalar
upsCfgFreeRunMaxFrequency = _UpsCfgFreeRunMaxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 27),
    _UpsCfgFreeRunMaxFrequency_Type()
)
upsCfgFreeRunMaxFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgFreeRunMaxFrequency.setStatus("current")
if mibBuilder.loadTexts:
    upsCfgFreeRunMaxFrequency.setUnits("0.1 Hertz ")


class _UpsCfgFreeRunMinFrequency_Type(Integer32):
    """Custom type upsCfgFreeRunMinFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(400, 700),
    )


_UpsCfgFreeRunMinFrequency_Type.__name__ = "Integer32"
_UpsCfgFreeRunMinFrequency_Object = MibScalar
upsCfgFreeRunMinFrequency = _UpsCfgFreeRunMinFrequency_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 28),
    _UpsCfgFreeRunMinFrequency_Type()
)
upsCfgFreeRunMinFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgFreeRunMinFrequency.setStatus("current")
if mibBuilder.loadTexts:
    upsCfgFreeRunMinFrequency.setUnits("0.1 Hertz ")


class _UpsCfgEPOStatus_Type(Integer32):
    """Custom type upsCfgEPOStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UpsCfgEPOStatus_Type.__name__ = "Integer32"
_UpsCfgEPOStatus_Object = MibScalar
upsCfgEPOStatus = _UpsCfgEPOStatus_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 29),
    _UpsCfgEPOStatus_Type()
)
upsCfgEPOStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsCfgEPOStatus.setStatus("current")


class _UpsCfgQSK1Status_Type(Integer32):
    """Custom type upsCfgQSK1Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UpsCfgQSK1Status_Type.__name__ = "Integer32"
_UpsCfgQSK1Status_Object = MibScalar
upsCfgQSK1Status = _UpsCfgQSK1Status_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 30),
    _UpsCfgQSK1Status_Type()
)
upsCfgQSK1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsCfgQSK1Status.setStatus("current")


class _UpsCfgQSK2Status_Type(Integer32):
    """Custom type upsCfgQSK2Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UpsCfgQSK2Status_Type.__name__ = "Integer32"
_UpsCfgQSK2Status_Object = MibScalar
upsCfgQSK2Status = _UpsCfgQSK2Status_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 31),
    _UpsCfgQSK2Status_Type()
)
upsCfgQSK2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsCfgQSK2Status.setStatus("current")


class _UpsCfgQSKT1Delaytime_Type(Integer32):
    """Custom type upsCfgQSKT1Delaytime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_UpsCfgQSKT1Delaytime_Type.__name__ = "Integer32"
_UpsCfgQSKT1Delaytime_Object = MibScalar
upsCfgQSKT1Delaytime = _UpsCfgQSKT1Delaytime_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 32),
    _UpsCfgQSKT1Delaytime_Type()
)
upsCfgQSKT1Delaytime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsCfgQSKT1Delaytime.setStatus("current")
if mibBuilder.loadTexts:
    upsCfgQSKT1Delaytime.setUnits("minutes ")


class _UpsCfgQSKT2Delaytime_Type(Integer32):
    """Custom type upsCfgQSKT2Delaytime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_UpsCfgQSKT2Delaytime_Type.__name__ = "Integer32"
_UpsCfgQSKT2Delaytime_Object = MibScalar
upsCfgQSKT2Delaytime = _UpsCfgQSKT2Delaytime_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 33),
    _UpsCfgQSKT2Delaytime_Type()
)
upsCfgQSKT2Delaytime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsCfgQSKT2Delaytime.setStatus("current")
if mibBuilder.loadTexts:
    upsCfgQSKT2Delaytime.setUnits("minutes ")


class _UpsCfgConstantPhaseAngle_Type(Integer32):
    """Custom type upsCfgConstantPhaseAngle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_UpsCfgConstantPhaseAngle_Type.__name__ = "Integer32"
_UpsCfgConstantPhaseAngle_Object = MibScalar
upsCfgConstantPhaseAngle = _UpsCfgConstantPhaseAngle_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 34),
    _UpsCfgConstantPhaseAngle_Type()
)
upsCfgConstantPhaseAngle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgConstantPhaseAngle.setStatus("current")


class _UpsCfgInPhaseAngle_Type(Integer32):
    """Custom type upsCfgInPhaseAngle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              120,
              180,
              240)
        )
    )
    namedValues = NamedValues(
        *(("Angle000", 0),
          ("Angle120", 120),
          ("Angle180", 180),
          ("Angle240", 240))
    )


_UpsCfgInPhaseAngle_Type.__name__ = "Integer32"
_UpsCfgInPhaseAngle_Object = MibScalar
upsCfgInPhaseAngle = _UpsCfgInPhaseAngle_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 35),
    _UpsCfgInPhaseAngle_Type()
)
upsCfgInPhaseAngle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsCfgInPhaseAngle.setStatus("current")


class _UpsCfgOutPhaseAngle_Type(Integer32):
    """Custom type upsCfgOutPhaseAngle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              120,
              180,
              240)
        )
    )
    namedValues = NamedValues(
        *(("Angle000", 0),
          ("Angle120", 120),
          ("Angle180", 180),
          ("Angle240", 240))
    )


_UpsCfgOutPhaseAngle_Type.__name__ = "Integer32"
_UpsCfgOutPhaseAngle_Object = MibScalar
upsCfgOutPhaseAngle = _UpsCfgOutPhaseAngle_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 36),
    _UpsCfgOutPhaseAngle_Type()
)
upsCfgOutPhaseAngle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgOutPhaseAngle.setStatus("current")


class _UpsCfgLimiRunOnBatMode_Type(Integer32):
    """Custom type upsCfgLimiRunOnBatMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notsupport", 2))
    )


_UpsCfgLimiRunOnBatMode_Type.__name__ = "Integer32"
_UpsCfgLimiRunOnBatMode_Object = MibScalar
upsCfgLimiRunOnBatMode = _UpsCfgLimiRunOnBatMode_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 37),
    _UpsCfgLimiRunOnBatMode_Type()
)
upsCfgLimiRunOnBatMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgLimiRunOnBatMode.setStatus("current")
_UpsCfgChargingCurrent_Type = Integer32
_UpsCfgChargingCurrent_Object = MibScalar
upsCfgChargingCurrent = _UpsCfgChargingCurrent_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 38),
    _UpsCfgChargingCurrent_Type()
)
upsCfgChargingCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upsCfgChargingCurrent.setStatus("current")
if mibBuilder.loadTexts:
    upsCfgChargingCurrent.setUnits("0.1 Amp DC")


class _UpsCfgBatSeftCheckVolt_Type(Integer32):
    """Custom type upsCfgBatSeftCheckVolt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2400, 2800),
    )


_UpsCfgBatSeftCheckVolt_Type.__name__ = "Integer32"
_UpsCfgBatSeftCheckVolt_Object = MibScalar
upsCfgBatSeftCheckVolt = _UpsCfgBatSeftCheckVolt_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 39),
    _UpsCfgBatSeftCheckVolt_Type()
)
upsCfgBatSeftCheckVolt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgBatSeftCheckVolt.setStatus("current")
if mibBuilder.loadTexts:
    upsCfgBatSeftCheckVolt.setUnits("0.1 Volts")


class _UpsCfgOverChargVolt_Type(Integer32):
    """Custom type upsCfgOverChargVolt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(130, 143),
    )


_UpsCfgOverChargVolt_Type.__name__ = "Integer32"
_UpsCfgOverChargVolt_Object = MibScalar
upsCfgOverChargVolt = _UpsCfgOverChargVolt_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 40),
    _UpsCfgOverChargVolt_Type()
)
upsCfgOverChargVolt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgOverChargVolt.setStatus("current")
if mibBuilder.loadTexts:
    upsCfgOverChargVolt.setUnits("0.1 Volts")


class _UpsCfgBattUnderVolt_Type(Integer32):
    """Custom type upsCfgBattUnderVolt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 2400),
    )


_UpsCfgBattUnderVolt_Type.__name__ = "Integer32"
_UpsCfgBattUnderVolt_Object = MibScalar
upsCfgBattUnderVolt = _UpsCfgBattUnderVolt_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 41),
    _UpsCfgBattUnderVolt_Type()
)
upsCfgBattUnderVolt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgBattUnderVolt.setStatus("current")
if mibBuilder.loadTexts:
    upsCfgBattUnderVolt.setUnits("0.1 Volts")
_UpsCfgBattLowVolt_Type = Integer32
_UpsCfgBattLowVolt_Object = MibScalar
upsCfgBattLowVolt = _UpsCfgBattLowVolt_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 42),
    _UpsCfgBattLowVolt_Type()
)
upsCfgBattLowVolt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgBattLowVolt.setStatus("current")
if mibBuilder.loadTexts:
    upsCfgBattLowVolt.setUnits("0.1 Volts")
_UpsCfgIn1VoltHLoss_Type = Integer32
_UpsCfgIn1VoltHLoss_Object = MibScalar
upsCfgIn1VoltHLoss = _UpsCfgIn1VoltHLoss_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 43),
    _UpsCfgIn1VoltHLoss_Type()
)
upsCfgIn1VoltHLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgIn1VoltHLoss.setStatus("current")
if mibBuilder.loadTexts:
    upsCfgIn1VoltHLoss.setUnits("0.1 Volts")
_UpsCfgIn1VoltLLoss_Type = Integer32
_UpsCfgIn1VoltLLoss_Object = MibScalar
upsCfgIn1VoltLLoss = _UpsCfgIn1VoltLLoss_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 44),
    _UpsCfgIn1VoltLLoss_Type()
)
upsCfgIn1VoltLLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgIn1VoltLLoss.setStatus("current")
if mibBuilder.loadTexts:
    upsCfgIn1VoltLLoss.setUnits("0.1 Volts")
_UpsCfgIn2VoltHLoss_Type = Integer32
_UpsCfgIn2VoltHLoss_Object = MibScalar
upsCfgIn2VoltHLoss = _UpsCfgIn2VoltHLoss_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 45),
    _UpsCfgIn2VoltHLoss_Type()
)
upsCfgIn2VoltHLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgIn2VoltHLoss.setStatus("current")
if mibBuilder.loadTexts:
    upsCfgIn2VoltHLoss.setUnits("0.1 Volts")
_UpsCfgIn2VoltLLoss_Type = Integer32
_UpsCfgIn2VoltLLoss_Object = MibScalar
upsCfgIn2VoltLLoss = _UpsCfgIn2VoltLLoss_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 46),
    _UpsCfgIn2VoltLLoss_Type()
)
upsCfgIn2VoltLLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgIn2VoltLLoss.setStatus("current")
if mibBuilder.loadTexts:
    upsCfgIn2VoltLLoss.setUnits("0.1 Volts")


class _UpsCfgBatteryTurnOn_Type(Integer32):
    """Custom type upsCfgBatteryTurnOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1),
          ("notsupport", 2))
    )


_UpsCfgBatteryTurnOn_Type.__name__ = "Integer32"
_UpsCfgBatteryTurnOn_Object = MibScalar
upsCfgBatteryTurnOn = _UpsCfgBatteryTurnOn_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 11, 47),
    _UpsCfgBatteryTurnOn_Type()
)
upsCfgBatteryTurnOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upsCfgBatteryTurnOn.setStatus("current")
_UpsTraps_ObjectIdentity = ObjectIdentity
upsTraps = _UpsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12)
)


class _Trapleafnodev103_Type(DisplayString):
    """Custom type trapleafnodev103 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_Trapleafnodev103_Type.__name__ = "DisplayString"
_Trapleafnodev103_Object = MibScalar
trapleafnodev103 = _Trapleafnodev103_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 998),
    _Trapleafnodev103_Type()
)
trapleafnodev103.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapleafnodev103.setStatus("current")


class _Trapleafnodev1v2_Type(Integer32):
    """Custom type trapleafnodev1v2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_Trapleafnodev1v2_Type.__name__ = "Integer32"
_Trapleafnodev1v2_Object = MibScalar
trapleafnodev1v2 = _Trapleafnodev1v2_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 999),
    _Trapleafnodev1v2_Type()
)
trapleafnodev1v2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapleafnodev1v2.setStatus("current")
_Extend_ObjectIdentity = ObjectIdentity
extend = _Extend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 13)
)


class _ExtendWorkTemperature_Type(Integer32):
    """Custom type extendWorkTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2200, 2200),
    )


_ExtendWorkTemperature_Type.__name__ = "Integer32"
_ExtendWorkTemperature_Object = MibScalar
extendWorkTemperature = _ExtendWorkTemperature_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 13, 1),
    _ExtendWorkTemperature_Type()
)
extendWorkTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extendWorkTemperature.setStatus("current")
if mibBuilder.loadTexts:
    extendWorkTemperature.setUnits("degrees 0.1 Centigrade")


class _ExtendWorkhumidity_Type(Integer32):
    """Custom type extendWorkhumidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ExtendWorkhumidity_Type.__name__ = "Integer32"
_ExtendWorkhumidity_Object = MibScalar
extendWorkhumidity = _ExtendWorkhumidity_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 13, 2),
    _ExtendWorkhumidity_Type()
)
extendWorkhumidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extendWorkhumidity.setStatus("current")
if mibBuilder.loadTexts:
    extendWorkhumidity.setUnits("percent")


class _ExtendSmokeScope_Type(Integer32):
    """Custom type extendSmokeScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_ExtendSmokeScope_Type.__name__ = "Integer32"
_ExtendSmokeScope_Object = MibScalar
extendSmokeScope = _ExtendSmokeScope_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 13, 3),
    _ExtendSmokeScope_Type()
)
extendSmokeScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extendSmokeScope.setStatus("current")
if mibBuilder.loadTexts:
    extendSmokeScope.setUnits("%/FOOT")


class _ExtendEMDAlarm1_Type(Integer32):
    """Custom type extendEMDAlarm1 based on Integer32"""
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


_ExtendEMDAlarm1_Type.__name__ = "Integer32"
_ExtendEMDAlarm1_Object = MibScalar
extendEMDAlarm1 = _ExtendEMDAlarm1_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 13, 4),
    _ExtendEMDAlarm1_Type()
)
extendEMDAlarm1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extendEMDAlarm1.setStatus("current")


class _ExtendEMDAlarm2_Type(Integer32):
    """Custom type extendEMDAlarm2 based on Integer32"""
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


_ExtendEMDAlarm2_Type.__name__ = "Integer32"
_ExtendEMDAlarm2_Object = MibScalar
extendEMDAlarm2 = _ExtendEMDAlarm2_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 13, 5),
    _ExtendEMDAlarm2_Type()
)
extendEMDAlarm2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extendEMDAlarm2.setStatus("current")


class _ExtendEMDAlarm3_Type(Integer32):
    """Custom type extendEMDAlarm3 based on Integer32"""
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


_ExtendEMDAlarm3_Type.__name__ = "Integer32"
_ExtendEMDAlarm3_Object = MibScalar
extendEMDAlarm3 = _ExtendEMDAlarm3_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 13, 6),
    _ExtendEMDAlarm3_Type()
)
extendEMDAlarm3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extendEMDAlarm3.setStatus("current")


class _ExtendEMDAlarm4_Type(Integer32):
    """Custom type extendEMDAlarm4 based on Integer32"""
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


_ExtendEMDAlarm4_Type.__name__ = "Integer32"
_ExtendEMDAlarm4_Object = MibScalar
extendEMDAlarm4 = _ExtendEMDAlarm4_Object(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 13, 7),
    _ExtendEMDAlarm4_Type()
)
extendEMDAlarm4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extendEMDAlarm4.setStatus("current")
_Inverter_ObjectIdentity = ObjectIdentity
inverter = _Inverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 2)
)
_SolarIdent_ObjectIdentity = ObjectIdentity
solarIdent = _SolarIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 2, 1)
)
_SolarRating_ObjectIdentity = ObjectIdentity
solarRating = _SolarRating_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 2, 2)
)
_SolarBattery_ObjectIdentity = ObjectIdentity
solarBattery = _SolarBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 2, 3)
)
_SolarGrid_ObjectIdentity = ObjectIdentity
solarGrid = _SolarGrid_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 2, 4)
)
_SolarACOutput_ObjectIdentity = ObjectIdentity
solarACOutput = _SolarACOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 2, 5)
)
_SolarPV_ObjectIdentity = ObjectIdentity
solarPV = _SolarPV_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 2, 6)
)
_SolarEnergy_ObjectIdentity = ObjectIdentity
solarEnergy = _SolarEnergy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 2, 7)
)
_SolarTest_ObjectIdentity = ObjectIdentity
solarTest = _SolarTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 2, 8)
)
_SolarDefValue_ObjectIdentity = ObjectIdentity
solarDefValue = _SolarDefValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 2, 9)
)
_SolarFaultInfo_ObjectIdentity = ObjectIdentity
solarFaultInfo = _SolarFaultInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 2, 10)
)
_SolarControl_ObjectIdentity = ObjectIdentity
solarControl = _SolarControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 2, 11)
)
_SolarAgentConfig_ObjectIdentity = ObjectIdentity
solarAgentConfig = _SolarAgentConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 2, 12)
)
_SolarCommConfig_ObjectIdentity = ObjectIdentity
solarCommConfig = _SolarCommConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 2, 13)
)
_SolarConfig_ObjectIdentity = ObjectIdentity
solarConfig = _SolarConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 2, 14)
)
_SolarTraps_ObjectIdentity = ObjectIdentity
solarTraps = _SolarTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 2, 15)
)
_SolarExtend_ObjectIdentity = ObjectIdentity
solarExtend = _SolarExtend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 2, 16)
)
_Charger_ObjectIdentity = ObjectIdentity
charger = _Charger_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 3)
)
_ATS_ObjectIdentity = ObjectIdentity
ATS = _ATS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 4)
)
_ATSIdent_ObjectIdentity = ObjectIdentity
ATSIdent = _ATSIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 4, 1)
)
_ATSRating_ObjectIdentity = ObjectIdentity
ATSRating = _ATSRating_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 4, 2)
)
_ATSInformation_ObjectIdentity = ObjectIdentity
ATSInformation = _ATSInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 4, 3)
)
_ATSControl_ObjectIdentity = ObjectIdentity
ATSControl = _ATSControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 4, 4)
)
_ATSAgentConfig_ObjectIdentity = ObjectIdentity
ATSAgentConfig = _ATSAgentConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 4, 5)
)
_ATSCommConfig_ObjectIdentity = ObjectIdentity
ATSCommConfig = _ATSCommConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 4, 6)
)
_ATSConfig_ObjectIdentity = ObjectIdentity
ATSConfig = _ATSConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 4, 7)
)
_ATSTraps_ObjectIdentity = ObjectIdentity
ATSTraps = _ATSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 4, 8)
)
_ATSExtend_ObjectIdentity = ObjectIdentity
ATSExtend = _ATSExtend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 43943, 1, 4, 9)
)

# Managed Objects groups


# Notification objects

cmpACFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 1)
)
if mibBuilder.loadTexts:
    cmpACFailure.setStatus(
        ""
    )

cmpFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 2)
)
if mibBuilder.loadTexts:
    cmpFanFailure.setStatus(
        ""
    )

cmpUPSFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 3)
)
if mibBuilder.loadTexts:
    cmpUPSFailure.setStatus(
        ""
    )

cmpChargerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 4)
)
if mibBuilder.loadTexts:
    cmpChargerFailure.setStatus(
        ""
    )

cmpOverloadFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 5)
)
if mibBuilder.loadTexts:
    cmpOverloadFailure.setStatus(
        ""
    )

cmpOvertempFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 6)
)
if mibBuilder.loadTexts:
    cmpOvertempFailure.setStatus(
        ""
    )

cmpInvertershortcircuited = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 7)
)
if mibBuilder.loadTexts:
    cmpInvertershortcircuited.setStatus(
        ""
    )

cmpbatteryfusebeingoc = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 8)
)
if mibBuilder.loadTexts:
    cmpbatteryfusebeingoc.setStatus(
        ""
    )

cmpLowbattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 9)
)
if mibBuilder.loadTexts:
    cmpLowbattery.setStatus(
        ""
    )

cmpSysgotoshutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 10)
)
if mibBuilder.loadTexts:
    cmpSysgotoshutdown.setStatus(
        ""
    )

cmpSitefault = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 11)
)
if mibBuilder.loadTexts:
    cmpSitefault.setStatus(
        ""
    )

cmpPhasesequenceincorrect = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 12)
)
if mibBuilder.loadTexts:
    cmpPhasesequenceincorrect.setStatus(
        ""
    )

cmpPhasesequenceincorrectbypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 13)
)
if mibBuilder.loadTexts:
    cmpPhasesequenceincorrectbypass.setStatus(
        ""
    )

cmpFanalarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 14)
)
if mibBuilder.loadTexts:
    cmpFanalarm.setStatus(
        ""
    )

cmpEPOenabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 15)
)
if mibBuilder.loadTexts:
    cmpEPOenabled.setStatus(
        ""
    )

cmpUnabletotrunonUPS = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 16)
)
if mibBuilder.loadTexts:
    cmpUnabletotrunonUPS.setStatus(
        ""
    )

cmpOvertemperaturealarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 17)
)
if mibBuilder.loadTexts:
    cmpOvertemperaturealarm.setStatus(
        ""
    )

cmpInputfrequnstablebypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 18)
)
if mibBuilder.loadTexts:
    cmpInputfrequnstablebypass.setStatus(
        ""
    )

cmpChargeralarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 19)
)
if mibBuilder.loadTexts:
    cmpChargeralarm.setStatus(
        ""
    )

cmpL1inputfusenotwork = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 20)
)
if mibBuilder.loadTexts:
    cmpL1inputfusenotwork.setStatus(
        ""
    )

cmpNeutralnotConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 21)
)
if mibBuilder.loadTexts:
    cmpNeutralnotConnected.setStatus(
        ""
    )

cmpL2inputfusenotwork = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 22)
)
if mibBuilder.loadTexts:
    cmpL2inputfusenotwork.setStatus(
        ""
    )

cmpL3inputfusenotwork = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 23)
)
if mibBuilder.loadTexts:
    cmpL3inputfusenotwork.setStatus(
        ""
    )

cmpPositivePFCabnormalL1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 24)
)
if mibBuilder.loadTexts:
    cmpPositivePFCabnormalL1.setStatus(
        ""
    )

cmpNegativePFCabnormalL1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 25)
)
if mibBuilder.loadTexts:
    cmpNegativePFCabnormalL1.setStatus(
        ""
    )

cmpPositivePFCabnormalL2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 26)
)
if mibBuilder.loadTexts:
    cmpPositivePFCabnormalL2.setStatus(
        ""
    )

cmpNegativePFCabnormalL2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 27)
)
if mibBuilder.loadTexts:
    cmpNegativePFCabnormalL2.setStatus(
        ""
    )

cmpPositivePFCabnormalL3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 28)
)
if mibBuilder.loadTexts:
    cmpPositivePFCabnormalL3.setStatus(
        ""
    )

cmpNegativePFCabnormalL3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 29)
)
if mibBuilder.loadTexts:
    cmpNegativePFCabnormalL3.setStatus(
        ""
    )

cmpBusvoltagenotwds = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 30)
)
if mibBuilder.loadTexts:
    cmpBusvoltagenotwds.setStatus(
        ""
    )

cmpBusvoltageovermaxvalue = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 31)
)
if mibBuilder.loadTexts:
    cmpBusvoltageovermaxvalue.setStatus(
        ""
    )

cmpBusvoltagebelowminvalue = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 32)
)
if mibBuilder.loadTexts:
    cmpBusvoltagebelowminvalue.setStatus(
        ""
    )

cmpBusvoltagediffoutofrange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 33)
)
if mibBuilder.loadTexts:
    cmpBusvoltagediffoutofrange.setStatus(
        ""
    )

cmpBusvoltageofsloperatetoofast = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 34)
)
if mibBuilder.loadTexts:
    cmpBusvoltageofsloperatetoofast.setStatus(
        ""
    )

cmpOvercurrentinPFCII = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 35)
)
if mibBuilder.loadTexts:
    cmpOvercurrentinPFCII.setStatus(
        ""
    )

cmpInvertervoloutofrange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 36)
)
if mibBuilder.loadTexts:
    cmpInvertervoloutofrange.setStatus(
        ""
    )

cmpInvertervolovermaxvalue = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 37)
)
if mibBuilder.loadTexts:
    cmpInvertervolovermaxvalue.setStatus(
        ""
    )

cmpInvertervolbelowminvalue = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 38)
)
if mibBuilder.loadTexts:
    cmpInvertervolbelowminvalue.setStatus(
        ""
    )

cmpBatteryoppositelyconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 39)
)
if mibBuilder.loadTexts:
    cmpBatteryoppositelyconnected.setStatus(
        ""
    )

cmpL2phaseshortcicuited = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 40)
)
if mibBuilder.loadTexts:
    cmpL2phaseshortcicuited.setStatus(
        ""
    )

cmpL3phaseshortcicuited = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 41)
)
if mibBuilder.loadTexts:
    cmpL3phaseshortcicuited.setStatus(
        ""
    )

cmpL1L2invertershortcicuited = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 42)
)
if mibBuilder.loadTexts:
    cmpL1L2invertershortcicuited.setStatus(
        ""
    )

cmpL2L3invertershortcicuited = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 43)
)
if mibBuilder.loadTexts:
    cmpL2L3invertershortcicuited.setStatus(
        ""
    )

cmpL3L1invertershortcicuited = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 44)
)
if mibBuilder.loadTexts:
    cmpL3L1invertershortcicuited.setStatus(
        ""
    )

cmpL1negativepoweroutofrange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 45)
)
if mibBuilder.loadTexts:
    cmpL1negativepoweroutofrange.setStatus(
        ""
    )

cmpL2negativepoweroutofrange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 46)
)
if mibBuilder.loadTexts:
    cmpL2negativepoweroutofrange.setStatus(
        ""
    )

cmpL3negativepoweroutofrange = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 47)
)
if mibBuilder.loadTexts:
    cmpL3negativepoweroutofrange.setStatus(
        ""
    )

cmpBatterySCRshortcircuited = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 48)
)
if mibBuilder.loadTexts:
    cmpBatterySCRshortcircuited.setStatus(
        ""
    )

cmpLineSCRshortcircuited = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 49)
)
if mibBuilder.loadTexts:
    cmpLineSCRshortcircuited.setStatus(
        ""
    )

cmpInverterrelayopenfault = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 50)
)
if mibBuilder.loadTexts:
    cmpInverterrelayopenfault.setStatus(
        ""
    )

cmpInverterrelayshortcircuited = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 51)
)
if mibBuilder.loadTexts:
    cmpInverterrelayshortcircuited.setStatus(
        ""
    )

cmpInoutwiresoppositelyconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 52)
)
if mibBuilder.loadTexts:
    cmpInoutwiresoppositelyconnected.setStatus(
        ""
    )

cmpabnormalcanbuscommunication = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 53)
)
if mibBuilder.loadTexts:
    cmpabnormalcanbuscommunication.setStatus(
        ""
    )

cmpcommfailurebcupsboard = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 54)
)
if mibBuilder.loadTexts:
    cmpcommfailurebcupsboard.setStatus(
        ""
    )

cmpabnormalsyncsignalcircuit = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 55)
)
if mibBuilder.loadTexts:
    cmpabnormalsyncsignalcircuit.setStatus(
        ""
    )

cmpabnormalsyncpulsesignalcircuit = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 56)
)
if mibBuilder.loadTexts:
    cmpabnormalsyncpulsesignalcircuit.setStatus(
        ""
    )

cmpcurrent3punbalancedetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 57)
)
if mibBuilder.loadTexts:
    cmpcurrent3punbalancedetected.setStatus(
        ""
    )

cmpbatteryselftestfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 58)
)
if mibBuilder.loadTexts:
    cmpbatteryselftestfailure.setStatus(
        ""
    )

cmpintercurrentunbalance = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 59)
)
if mibBuilder.loadTexts:
    cmpintercurrentunbalance.setStatus(
        ""
    )

cmpbatterydisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 60)
)
if mibBuilder.loadTexts:
    cmpbatterydisconnected.setStatus(
        ""
    )

cmpabnormalhostsignalcircuit = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 61)
)
if mibBuilder.loadTexts:
    cmpabnormalhostsignalcircuit.setStatus(
        ""
    )

cmpbatteryovercharged = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 62)
)
if mibBuilder.loadTexts:
    cmpbatteryovercharged.setStatus(
        ""
    )

cmpbatteryvoltoohigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 63)
)
if mibBuilder.loadTexts:
    cmpbatteryvoltoohigh.setStatus(
        ""
    )

cmpbatteryvoltoolow = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 64)
)
if mibBuilder.loadTexts:
    cmpbatteryvoltoolow.setStatus(
        ""
    )

cmpfemaleconnectornotconnwell = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 65)
)
if mibBuilder.loadTexts:
    cmpfemaleconnectornotconnwell.setStatus(
        ""
    )

cmpmaleconnectornotconnwell = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 66)
)
if mibBuilder.loadTexts:
    cmpmaleconnectornotconnwell.setStatus(
        ""
    )

cmplockingbypassA3COW30M = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 67)
)
if mibBuilder.loadTexts:
    cmplockingbypassA3COW30M.setStatus(
        ""
    )

cmpparallelcabledisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 68)
)
if mibBuilder.loadTexts:
    cmpparallelcabledisconnected.setStatus(
        ""
    )

cmpsyncpulsecircuitfault = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 69)
)
if mibBuilder.loadTexts:
    cmpsyncpulsecircuitfault.setStatus(
        ""
    )

cmpsyncsignalcircuitfalt = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 70)
)
if mibBuilder.loadTexts:
    cmpsyncsignalcircuitfalt.setStatus(
        ""
    )

cmphostsignalcircuitfault = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 71)
)
if mibBuilder.loadTexts:
    cmphostsignalcircuitfault.setStatus(
        ""
    )

cmpcanbuscommunicationfault = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 72)
)
if mibBuilder.loadTexts:
    cmpcanbuscommunicationfault.setStatus(
        ""
    )

cmplowlosspointforvolinACmode = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 73)
)
if mibBuilder.loadTexts:
    cmplowlosspointforvolinACmode.setStatus(
        ""
    )

cmphighlosspointforvolinACmode = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 74)
)
if mibBuilder.loadTexts:
    cmphighlosspointforvolinACmode.setStatus(
        ""
    )

cmplowlosspointforfreqinACmode = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 75)
)
if mibBuilder.loadTexts:
    cmplowlosspointforfreqinACmode.setStatus(
        ""
    )

cmphighlosspointforfreqinACmode = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 76)
)
if mibBuilder.loadTexts:
    cmphighlosspointforfreqinACmode.setStatus(
        ""
    )

cmplowlosspointforvolinbypassmode = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 77)
)
if mibBuilder.loadTexts:
    cmplowlosspointforvolinbypassmode.setStatus(
        ""
    )

cmphighlosspointforvolinbypassmode = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 78)
)
if mibBuilder.loadTexts:
    cmphighlosspointforvolinbypassmode.setStatus(
        ""
    )

cmplowlosspointforfreqinbypassmode = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 79)
)
if mibBuilder.loadTexts:
    cmplowlosspointforfreqinbypassmode.setStatus(
        ""
    )

cmphighlosspointforfreqinbypassmode = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 80)
)
if mibBuilder.loadTexts:
    cmphighlosspointforfreqinbypassmode.setStatus(
        ""
    )

cmploadunbalanced = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 81)
)
if mibBuilder.loadTexts:
    cmploadunbalanced.setStatus(
        ""
    )

cmpoverloadalarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 82)
)
if mibBuilder.loadTexts:
    cmpoverloadalarm.setStatus(
        ""
    )

cmpparallelnotconnectedwell = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 83)
)
if mibBuilder.loadTexts:
    cmpparallelnotconnectedwell.setStatus(
        ""
    )

cmpcommunicationlost = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 84)
)
if mibBuilder.loadTexts:
    cmpcommunicationlost.setStatus(
        ""
    )

cmpbatteryconnnotsonsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 85)
)
if mibBuilder.loadTexts:
    cmpbatteryconnnotsonsistent.setStatus(
        ""
    )

cmpconverternotconsisstent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 86)
)
if mibBuilder.loadTexts:
    cmpconverternotconsisstent.setStatus(
        ""
    )

cmpbypassnotallownotconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 87)
)
if mibBuilder.loadTexts:
    cmpbypassnotallownotconsistent.setStatus(
        ""
    )

cmpACconnnotconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 88)
)
if mibBuilder.loadTexts:
    cmpACconnnotconsistent.setStatus(
        ""
    )

cmpinput3pcurrentunbalance = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 89)
)
if mibBuilder.loadTexts:
    cmpinput3pcurrentunbalance.setStatus(
        ""
    )

cmpbypassconnnotconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 90)
)
if mibBuilder.loadTexts:
    cmpbypassconnnotconsistent.setStatus(
        ""
    )

cmpbatteryprotectionnotconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 91)
)
if mibBuilder.loadTexts:
    cmpbatteryprotectionnotconsistent.setStatus(
        ""
    )

cmpbatterydetectionnotconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 92)
)
if mibBuilder.loadTexts:
    cmpbatterydetectionnotconsistent.setStatus(
        ""
    )

cmpupsmodeltypesnotconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 93)
)
if mibBuilder.loadTexts:
    cmpupsmodeltypesnotconsistent.setStatus(
        ""
    )

cmpbypassnotconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 94)
)
if mibBuilder.loadTexts:
    cmpbypassnotconsistent.setStatus(
        ""
    )

cmpcapacitynotconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 95)
)
if mibBuilder.loadTexts:
    cmpcapacitynotconsistent.setStatus(
        ""
    )

cmpautorestartnotconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 96)
)
if mibBuilder.loadTexts:
    cmpautorestartnotconsistent.setStatus(
        ""
    )

cmpBatteryReplace = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 97)
)
if mibBuilder.loadTexts:
    cmpBatteryReplace.setStatus(
        ""
    )

cmpACNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 100)
)
if mibBuilder.loadTexts:
    cmpACNormal.setStatus(
        ""
    )

cmpOutputBadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 103)
)
if mibBuilder.loadTexts:
    cmpOutputBadAlarm.setStatus(
        ""
    )

cmpBypassBadAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 104)
)
if mibBuilder.loadTexts:
    cmpBypassBadAlarm.setStatus(
        ""
    )

cmpOutputOffAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 105)
)
if mibBuilder.loadTexts:
    cmpOutputOffAlarm.setStatus(
        ""
    )

cmpUPSShutAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 106)
)
if mibBuilder.loadTexts:
    cmpUPSShutAlarm.setStatus(
        ""
    )

cmpSystemOffAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 107)
)
if mibBuilder.loadTexts:
    cmpSystemOffAlarm.setStatus(
        ""
    )

cmpFuseFailureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 108)
)
if mibBuilder.loadTexts:
    cmpFuseFailureAlarm.setStatus(
        ""
    )

cmpGenFailureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 109)
)
if mibBuilder.loadTexts:
    cmpGenFailureAlarm.setStatus(
        ""
    )

cmpAwaitPowerAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 110)
)
if mibBuilder.loadTexts:
    cmpAwaitPowerAlarm.setStatus(
        ""
    )

cmpShutPendingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 111)
)
if mibBuilder.loadTexts:
    cmpShutPendingAlarm.setStatus(
        ""
    )

cmpBatDepleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 112)
)
if mibBuilder.loadTexts:
    cmpBatDepleted.setStatus(
        ""
    )

cmpUnknowStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 113)
)
if mibBuilder.loadTexts:
    cmpUnknowStatus.setStatus(
        ""
    )

cmpOutputOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 114)
)
if mibBuilder.loadTexts:
    cmpOutputOn.setStatus(
        ""
    )

cmpTurntobypass = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 115)
)
if mibBuilder.loadTexts:
    cmpTurntobypass.setStatus(
        ""
    )

cmpTurntobattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 116)
)
if mibBuilder.loadTexts:
    cmpTurntobattery.setStatus(
        ""
    )

cmpOutBooster = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 117)
)
if mibBuilder.loadTexts:
    cmpOutBooster.setStatus(
        ""
    )

cmpOutReducer = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 118)
)
if mibBuilder.loadTexts:
    cmpOutReducer.setStatus(
        ""
    )

cmpOutBattest = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 119)
)
if mibBuilder.loadTexts:
    cmpOutBattest.setStatus(
        ""
    )

cmpOtherSource = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 120)
)
if mibBuilder.loadTexts:
    cmpOtherSource.setStatus(
        ""
    )

cmpBatfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 121)
)
if mibBuilder.loadTexts:
    cmpBatfailure.setStatus(
        ""
    )

cmpBatTestDonePassed = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 122)
)
if mibBuilder.loadTexts:
    cmpBatTestDonePassed.setStatus(
        ""
    )

cmpBatTestDoneWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 123)
)
if mibBuilder.loadTexts:
    cmpBatTestDoneWarning.setStatus(
        ""
    )

cmpBatTestDoneAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 124)
)
if mibBuilder.loadTexts:
    cmpBatTestDoneAborted.setStatus(
        ""
    )

cmpBatteryNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 125)
)
if mibBuilder.loadTexts:
    cmpBatteryNormal.setStatus(
        ""
    )

cmpBatteryDischarging = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 126)
)
if mibBuilder.loadTexts:
    cmpBatteryDischarging.setStatus(
        ""
    )

cmpP1cutoffprealarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 127)
)
if mibBuilder.loadTexts:
    cmpP1cutoffprealarm.setStatus(
        ""
    )

cmpInputPhaseError = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 128)
)
if mibBuilder.loadTexts:
    cmpInputPhaseError.setStatus(
        ""
    )

cmpMaintainSwitchOpenalarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 129)
)
if mibBuilder.loadTexts:
    cmpMaintainSwitchOpenalarm.setStatus(
        ""
    )

cmpEMDChAbnormal1 = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 130)
)
if mibBuilder.loadTexts:
    cmpEMDChAbnormal1.setStatus(
        ""
    )

cmpEMDChAbnormal2 = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 131)
)
if mibBuilder.loadTexts:
    cmpEMDChAbnormal2.setStatus(
        ""
    )

cmpEMDChAbnormal3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 132)
)
if mibBuilder.loadTexts:
    cmpEMDChAbnormal3.setStatus(
        ""
    )

cmpEMDChAbnormal4 = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 133)
)
if mibBuilder.loadTexts:
    cmpEMDChAbnormal4.setStatus(
        ""
    )

cmpEMDChAbnormal5 = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 134)
)
if mibBuilder.loadTexts:
    cmpEMDChAbnormal5.setStatus(
        ""
    )

cmpEMDChAbnormal6 = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 135)
)
if mibBuilder.loadTexts:
    cmpEMDChAbnormal6.setStatus(
        ""
    )

cmpEMDChAbnormal7 = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 136)
)
if mibBuilder.loadTexts:
    cmpEMDChAbnormal7.setStatus(
        ""
    )

cmpEMDChAbnormal8 = NotificationType(
    (1, 3, 6, 1, 4, 1, 43943, 1, 1, 12, 0, 137)
)
if mibBuilder.loadTexts:
    cmpEMDChAbnormal8.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VoltronicMIB",
    **{"voltronicMIB": voltronicMIB,
       "products": products,
       "ups": ups,
       "upsIdent": upsIdent,
       "upsIdManufacturer": upsIdManufacturer,
       "upsIdProtocol": upsIdProtocol,
       "upsIdModelName": upsIdModelName,
       "upsIdSerialNumber": upsIdSerialNumber,
       "upsIdName": upsIdName,
       "upsIdFWVersion": upsIdFWVersion,
       "upsIdUPSType": upsIdUPSType,
       "upsRating": upsRating,
       "upsRatinVoltage": upsRatinVoltage,
       "upsRatoutVoltage": upsRatoutVoltage,
       "upsRatoutFrequency": upsRatoutFrequency,
       "upsRatoutCurrent": upsRatoutCurrent,
       "upsRatoutApparentPower": upsRatoutApparentPower,
       "upsRatoutTruePower": upsRatoutTruePower,
       "upsRatBatVoltage": upsRatBatVoltage,
       "upsBattery": upsBattery,
       "upsBatStatus": upsBatStatus,
       "upsBatSecondsOnBattery": upsBatSecondsOnBattery,
       "upsBatEstMinutesRemaining": upsBatEstMinutesRemaining,
       "upsBatEstChargeRemaining": upsBatEstChargeRemaining,
       "upsBatPBatVoltage": upsBatPBatVoltage,
       "upsBatNBatVoltage": upsBatNBatVoltage,
       "upsBatPBatCurrent": upsBatPBatCurrent,
       "upsBatNBatCurrent": upsBatNBatCurrent,
       "upsBatPBatChargCurrent": upsBatPBatChargCurrent,
       "upsBatNBatchargCurrent": upsBatNBatchargCurrent,
       "upsBatPBatDischargCurrent": upsBatPBatDischargCurrent,
       "upsBatNBatDischargCurrent": upsBatNBatDischargCurrent,
       "upsBatTemperature": upsBatTemperature,
       "upsBatNumberInSeries": upsBatNumberInSeries,
       "upsBatNumberInParallel": upsBatNumberInParallel,
       "upsBatPBatDischargCurrent2": upsBatPBatDischargCurrent2,
       "upsInput": upsInput,
       "upsInLineBads": upsInLineBads,
       "upsInTtlApparentPower": upsInTtlApparentPower,
       "upsInTtlTruePower": upsInTtlTruePower,
       "upsInNumLines": upsInNumLines,
       "upsInTable": upsInTable,
       "upsInEntry": upsInEntry,
       "upsInLineIndex": upsInLineIndex,
       "upsInFrequency": upsInFrequency,
       "upsInVoltage": upsInVoltage,
       "upsInCurrent": upsInCurrent,
       "upsInApparentPower": upsInApparentPower,
       "upsInTruePower": upsInTruePower,
       "upsInPowerFactor": upsInPowerFactor,
       "upsInLineVoltage": upsInLineVoltage,
       "upsInTtlVoltage": upsInTtlVoltage,
       "upsInTtlCurrent": upsInTtlCurrent,
       "upsOutput": upsOutput,
       "upsOutSource": upsOutSource,
       "upsOutFreq": upsOutFreq,
       "upsOutTtlApparentPower": upsOutTtlApparentPower,
       "upsOutTtlTruePower": upsOutTtlTruePower,
       "upsOutTtlPercentLoad": upsOutTtlPercentLoad,
       "upsOutNumLines": upsOutNumLines,
       "upsOutTable": upsOutTable,
       "upsOutEntry": upsOutEntry,
       "upsOutLineIndex": upsOutLineIndex,
       "upsOutVoltage": upsOutVoltage,
       "upsOutCurrent": upsOutCurrent,
       "upsOutApparentPower": upsOutApparentPower,
       "upsOutTruePower": upsOutTruePower,
       "upsOutPowerFactor": upsOutPowerFactor,
       "upsOutPercentLoad": upsOutPercentLoad,
       "upsOutLineVoltage": upsOutLineVoltage,
       "upsOutFrequency": upsOutFrequency,
       "upsOutTtlVoltage": upsOutTtlVoltage,
       "upsOutTtlCurrent": upsOutTtlCurrent,
       "upsOutStatus": upsOutStatus,
       "upsOutSource2": upsOutSource2,
       "upsBypass": upsBypass,
       "upsByFrequency": upsByFrequency,
       "upsByNumLines": upsByNumLines,
       "upsByTable": upsByTable,
       "upsByEntry": upsByEntry,
       "upsByLineIndex": upsByLineIndex,
       "upsByVoltage": upsByVoltage,
       "upsByCurrent": upsByCurrent,
       "upsByPower": upsByPower,
       "upsByLineVoltage": upsByLineVoltage,
       "upsTest": upsTest,
       "upsTstBatteryTest": upsTstBatteryTest,
       "upsTstBatteryTestResult": upsTstBatteryTestResult,
       "upsTstBatteryTestStartTime": upsTstBatteryTestStartTime,
       "upsTstBatterySettingTime": upsTstBatterySettingTime,
       "upsControl": upsControl,
       "upsCtlShutdownDelay": upsCtlShutdownDelay,
       "upsCtlSleepTime": upsCtlSleepTime,
       "upsCtlStartupAfterDelay": upsCtlStartupAfterDelay,
       "upsCtlbuzzer": upsCtlbuzzer,
       "upsCtlRemoteControlUPS": upsCtlRemoteControlUPS,
       "upsCtloutletPoweron": upsCtloutletPoweron,
       "upsCtloutletPoweroff": upsCtloutletPoweroff,
       "upsCtlOutlet1Powerofftime": upsCtlOutlet1Powerofftime,
       "upsCtlOutlet2Powerofftime": upsCtlOutlet2Powerofftime,
       "upsCtlResetConfigure": upsCtlResetConfigure,
       "agentConfig": agentConfig,
       "agentConfigDatetime": agentConfigDatetime,
       "commConfig": commConfig,
       "commBaudRate": commBaudRate,
       "commDatabits": commDatabits,
       "commStopbits": commStopbits,
       "commParity": commParity,
       "commTimeout": commTimeout,
       "upsConfig": upsConfig,
       "upsCfgAlarmbypass": upsCfgAlarmbypass,
       "upsCfgAlarmbattery": upsCfgAlarmbattery,
       "upsCfgAutoReboot": upsCfgAutoReboot,
       "upsCfgBypasswhenupsoff": upsCfgBypasswhenupsoff,
       "upsCfgBatterDDP": upsCfgBatterDDP,
       "upsCfgConvertermode": upsCfgConvertermode,
       "upsCfgECOmode": upsCfgECOmode,
       "upsCfgAdvanceECOmode": upsCfgAdvanceECOmode,
       "upsCfgGreenPowerFunction": upsCfgGreenPowerFunction,
       "upsCfgBatteryOSC": upsCfgBatteryOSC,
       "upsCfgAllowShort3times": upsCfgAllowShort3times,
       "upsCfgColdstart": upsCfgColdstart,
       "upsCfgBypassNotAllowed": upsCfgBypassNotAllowed,
       "upsCfgBatterylowprotect": upsCfgBatterylowprotect,
       "upsCfgP1progoutletcontrol": upsCfgP1progoutletcontrol,
       "upsCfgP2progoutletcontrol": upsCfgP2progoutletcontrol,
       "upsCfgInverterShortClear": upsCfgInverterShortClear,
       "upsCfgSitefaildetection": upsCfgSitefaildetection,
       "upsCfgBatNumInParallel": upsCfgBatNumInParallel,
       "upsCfgBatNumInSeries": upsCfgBatNumInSeries,
       "upsCfgBypassmaxvoltage": upsCfgBypassmaxvoltage,
       "upsCfgBypassminvoltage": upsCfgBypassminvoltage,
       "upsCfgBypassmaxfrequency": upsCfgBypassmaxfrequency,
       "upsCfgBypassminfrequency": upsCfgBypassminfrequency,
       "upsCfgECOmaxvoltage": upsCfgECOmaxvoltage,
       "upsCfgECOminvoltage": upsCfgECOminvoltage,
       "upsCfgFreeRunMaxFrequency": upsCfgFreeRunMaxFrequency,
       "upsCfgFreeRunMinFrequency": upsCfgFreeRunMinFrequency,
       "upsCfgEPOStatus": upsCfgEPOStatus,
       "upsCfgQSK1Status": upsCfgQSK1Status,
       "upsCfgQSK2Status": upsCfgQSK2Status,
       "upsCfgQSKT1Delaytime": upsCfgQSKT1Delaytime,
       "upsCfgQSKT2Delaytime": upsCfgQSKT2Delaytime,
       "upsCfgConstantPhaseAngle": upsCfgConstantPhaseAngle,
       "upsCfgInPhaseAngle": upsCfgInPhaseAngle,
       "upsCfgOutPhaseAngle": upsCfgOutPhaseAngle,
       "upsCfgLimiRunOnBatMode": upsCfgLimiRunOnBatMode,
       "upsCfgChargingCurrent": upsCfgChargingCurrent,
       "upsCfgBatSeftCheckVolt": upsCfgBatSeftCheckVolt,
       "upsCfgOverChargVolt": upsCfgOverChargVolt,
       "upsCfgBattUnderVolt": upsCfgBattUnderVolt,
       "upsCfgBattLowVolt": upsCfgBattLowVolt,
       "upsCfgIn1VoltHLoss": upsCfgIn1VoltHLoss,
       "upsCfgIn1VoltLLoss": upsCfgIn1VoltLLoss,
       "upsCfgIn2VoltHLoss": upsCfgIn2VoltHLoss,
       "upsCfgIn2VoltLLoss": upsCfgIn2VoltLLoss,
       "upsCfgBatteryTurnOn": upsCfgBatteryTurnOn,
       "upsTraps": upsTraps,
       "cmpACFailure": cmpACFailure,
       "cmpFanFailure": cmpFanFailure,
       "cmpUPSFailure": cmpUPSFailure,
       "cmpChargerFailure": cmpChargerFailure,
       "cmpOverloadFailure": cmpOverloadFailure,
       "cmpOvertempFailure": cmpOvertempFailure,
       "cmpInvertershortcircuited": cmpInvertershortcircuited,
       "cmpbatteryfusebeingoc": cmpbatteryfusebeingoc,
       "cmpLowbattery": cmpLowbattery,
       "cmpSysgotoshutdown": cmpSysgotoshutdown,
       "cmpSitefault": cmpSitefault,
       "cmpPhasesequenceincorrect": cmpPhasesequenceincorrect,
       "cmpPhasesequenceincorrectbypass": cmpPhasesequenceincorrectbypass,
       "cmpFanalarm": cmpFanalarm,
       "cmpEPOenabled": cmpEPOenabled,
       "cmpUnabletotrunonUPS": cmpUnabletotrunonUPS,
       "cmpOvertemperaturealarm": cmpOvertemperaturealarm,
       "cmpInputfrequnstablebypass": cmpInputfrequnstablebypass,
       "cmpChargeralarm": cmpChargeralarm,
       "cmpL1inputfusenotwork": cmpL1inputfusenotwork,
       "cmpNeutralnotConnected": cmpNeutralnotConnected,
       "cmpL2inputfusenotwork": cmpL2inputfusenotwork,
       "cmpL3inputfusenotwork": cmpL3inputfusenotwork,
       "cmpPositivePFCabnormalL1": cmpPositivePFCabnormalL1,
       "cmpNegativePFCabnormalL1": cmpNegativePFCabnormalL1,
       "cmpPositivePFCabnormalL2": cmpPositivePFCabnormalL2,
       "cmpNegativePFCabnormalL2": cmpNegativePFCabnormalL2,
       "cmpPositivePFCabnormalL3": cmpPositivePFCabnormalL3,
       "cmpNegativePFCabnormalL3": cmpNegativePFCabnormalL3,
       "cmpBusvoltagenotwds": cmpBusvoltagenotwds,
       "cmpBusvoltageovermaxvalue": cmpBusvoltageovermaxvalue,
       "cmpBusvoltagebelowminvalue": cmpBusvoltagebelowminvalue,
       "cmpBusvoltagediffoutofrange": cmpBusvoltagediffoutofrange,
       "cmpBusvoltageofsloperatetoofast": cmpBusvoltageofsloperatetoofast,
       "cmpOvercurrentinPFCII": cmpOvercurrentinPFCII,
       "cmpInvertervoloutofrange": cmpInvertervoloutofrange,
       "cmpInvertervolovermaxvalue": cmpInvertervolovermaxvalue,
       "cmpInvertervolbelowminvalue": cmpInvertervolbelowminvalue,
       "cmpBatteryoppositelyconnected": cmpBatteryoppositelyconnected,
       "cmpL2phaseshortcicuited": cmpL2phaseshortcicuited,
       "cmpL3phaseshortcicuited": cmpL3phaseshortcicuited,
       "cmpL1L2invertershortcicuited": cmpL1L2invertershortcicuited,
       "cmpL2L3invertershortcicuited": cmpL2L3invertershortcicuited,
       "cmpL3L1invertershortcicuited": cmpL3L1invertershortcicuited,
       "cmpL1negativepoweroutofrange": cmpL1negativepoweroutofrange,
       "cmpL2negativepoweroutofrange": cmpL2negativepoweroutofrange,
       "cmpL3negativepoweroutofrange": cmpL3negativepoweroutofrange,
       "cmpBatterySCRshortcircuited": cmpBatterySCRshortcircuited,
       "cmpLineSCRshortcircuited": cmpLineSCRshortcircuited,
       "cmpInverterrelayopenfault": cmpInverterrelayopenfault,
       "cmpInverterrelayshortcircuited": cmpInverterrelayshortcircuited,
       "cmpInoutwiresoppositelyconnected": cmpInoutwiresoppositelyconnected,
       "cmpabnormalcanbuscommunication": cmpabnormalcanbuscommunication,
       "cmpcommfailurebcupsboard": cmpcommfailurebcupsboard,
       "cmpabnormalsyncsignalcircuit": cmpabnormalsyncsignalcircuit,
       "cmpabnormalsyncpulsesignalcircuit": cmpabnormalsyncpulsesignalcircuit,
       "cmpcurrent3punbalancedetected": cmpcurrent3punbalancedetected,
       "cmpbatteryselftestfailure": cmpbatteryselftestfailure,
       "cmpintercurrentunbalance": cmpintercurrentunbalance,
       "cmpbatterydisconnected": cmpbatterydisconnected,
       "cmpabnormalhostsignalcircuit": cmpabnormalhostsignalcircuit,
       "cmpbatteryovercharged": cmpbatteryovercharged,
       "cmpbatteryvoltoohigh": cmpbatteryvoltoohigh,
       "cmpbatteryvoltoolow": cmpbatteryvoltoolow,
       "cmpfemaleconnectornotconnwell": cmpfemaleconnectornotconnwell,
       "cmpmaleconnectornotconnwell": cmpmaleconnectornotconnwell,
       "cmplockingbypassA3COW30M": cmplockingbypassA3COW30M,
       "cmpparallelcabledisconnected": cmpparallelcabledisconnected,
       "cmpsyncpulsecircuitfault": cmpsyncpulsecircuitfault,
       "cmpsyncsignalcircuitfalt": cmpsyncsignalcircuitfalt,
       "cmphostsignalcircuitfault": cmphostsignalcircuitfault,
       "cmpcanbuscommunicationfault": cmpcanbuscommunicationfault,
       "cmplowlosspointforvolinACmode": cmplowlosspointforvolinACmode,
       "cmphighlosspointforvolinACmode": cmphighlosspointforvolinACmode,
       "cmplowlosspointforfreqinACmode": cmplowlosspointforfreqinACmode,
       "cmphighlosspointforfreqinACmode": cmphighlosspointforfreqinACmode,
       "cmplowlosspointforvolinbypassmode": cmplowlosspointforvolinbypassmode,
       "cmphighlosspointforvolinbypassmode": cmphighlosspointforvolinbypassmode,
       "cmplowlosspointforfreqinbypassmode": cmplowlosspointforfreqinbypassmode,
       "cmphighlosspointforfreqinbypassmode": cmphighlosspointforfreqinbypassmode,
       "cmploadunbalanced": cmploadunbalanced,
       "cmpoverloadalarm": cmpoverloadalarm,
       "cmpparallelnotconnectedwell": cmpparallelnotconnectedwell,
       "cmpcommunicationlost": cmpcommunicationlost,
       "cmpbatteryconnnotsonsistent": cmpbatteryconnnotsonsistent,
       "cmpconverternotconsisstent": cmpconverternotconsisstent,
       "cmpbypassnotallownotconsistent": cmpbypassnotallownotconsistent,
       "cmpACconnnotconsistent": cmpACconnnotconsistent,
       "cmpinput3pcurrentunbalance": cmpinput3pcurrentunbalance,
       "cmpbypassconnnotconsistent": cmpbypassconnnotconsistent,
       "cmpbatteryprotectionnotconsistent": cmpbatteryprotectionnotconsistent,
       "cmpbatterydetectionnotconsistent": cmpbatterydetectionnotconsistent,
       "cmpupsmodeltypesnotconsistent": cmpupsmodeltypesnotconsistent,
       "cmpbypassnotconsistent": cmpbypassnotconsistent,
       "cmpcapacitynotconsistent": cmpcapacitynotconsistent,
       "cmpautorestartnotconsistent": cmpautorestartnotconsistent,
       "cmpBatteryReplace": cmpBatteryReplace,
       "cmpACNormal": cmpACNormal,
       "cmpOutputBadAlarm": cmpOutputBadAlarm,
       "cmpBypassBadAlarm": cmpBypassBadAlarm,
       "cmpOutputOffAlarm": cmpOutputOffAlarm,
       "cmpUPSShutAlarm": cmpUPSShutAlarm,
       "cmpSystemOffAlarm": cmpSystemOffAlarm,
       "cmpFuseFailureAlarm": cmpFuseFailureAlarm,
       "cmpGenFailureAlarm": cmpGenFailureAlarm,
       "cmpAwaitPowerAlarm": cmpAwaitPowerAlarm,
       "cmpShutPendingAlarm": cmpShutPendingAlarm,
       "cmpBatDepleted": cmpBatDepleted,
       "cmpUnknowStatus": cmpUnknowStatus,
       "cmpOutputOn": cmpOutputOn,
       "cmpTurntobypass": cmpTurntobypass,
       "cmpTurntobattery": cmpTurntobattery,
       "cmpOutBooster": cmpOutBooster,
       "cmpOutReducer": cmpOutReducer,
       "cmpOutBattest": cmpOutBattest,
       "cmpOtherSource": cmpOtherSource,
       "cmpBatfailure": cmpBatfailure,
       "cmpBatTestDonePassed": cmpBatTestDonePassed,
       "cmpBatTestDoneWarning": cmpBatTestDoneWarning,
       "cmpBatTestDoneAborted": cmpBatTestDoneAborted,
       "cmpBatteryNormal": cmpBatteryNormal,
       "cmpBatteryDischarging": cmpBatteryDischarging,
       "cmpP1cutoffprealarm": cmpP1cutoffprealarm,
       "cmpInputPhaseError": cmpInputPhaseError,
       "cmpMaintainSwitchOpenalarm": cmpMaintainSwitchOpenalarm,
       "cmpEMDChAbnormal1": cmpEMDChAbnormal1,
       "cmpEMDChAbnormal2": cmpEMDChAbnormal2,
       "cmpEMDChAbnormal3": cmpEMDChAbnormal3,
       "cmpEMDChAbnormal4": cmpEMDChAbnormal4,
       "cmpEMDChAbnormal5": cmpEMDChAbnormal5,
       "cmpEMDChAbnormal6": cmpEMDChAbnormal6,
       "cmpEMDChAbnormal7": cmpEMDChAbnormal7,
       "cmpEMDChAbnormal8": cmpEMDChAbnormal8,
       "trapleafnodev103": trapleafnodev103,
       "trapleafnodev1v2": trapleafnodev1v2,
       "extend": extend,
       "extendWorkTemperature": extendWorkTemperature,
       "extendWorkhumidity": extendWorkhumidity,
       "extendSmokeScope": extendSmokeScope,
       "extendEMDAlarm1": extendEMDAlarm1,
       "extendEMDAlarm2": extendEMDAlarm2,
       "extendEMDAlarm3": extendEMDAlarm3,
       "extendEMDAlarm4": extendEMDAlarm4,
       "inverter": inverter,
       "solarIdent": solarIdent,
       "solarRating": solarRating,
       "solarBattery": solarBattery,
       "solarGrid": solarGrid,
       "solarACOutput": solarACOutput,
       "solarPV": solarPV,
       "solarEnergy": solarEnergy,
       "solarTest": solarTest,
       "solarDefValue": solarDefValue,
       "solarFaultInfo": solarFaultInfo,
       "solarControl": solarControl,
       "solarAgentConfig": solarAgentConfig,
       "solarCommConfig": solarCommConfig,
       "solarConfig": solarConfig,
       "solarTraps": solarTraps,
       "solarExtend": solarExtend,
       "charger": charger,
       "ATS": ATS,
       "ATSIdent": ATSIdent,
       "ATSRating": ATSRating,
       "ATSInformation": ATSInformation,
       "ATSControl": ATSControl,
       "ATSAgentConfig": ATSAgentConfig,
       "ATSCommConfig": ATSCommConfig,
       "ATSConfig": ATSConfig,
       "ATSTraps": ATSTraps,
       "ATSExtend": ATSExtend}
)
