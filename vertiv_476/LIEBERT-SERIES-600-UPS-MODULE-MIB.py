# SNMP MIB module (LIEBERT-SERIES-600-UPS-MODULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/vertiv_476/LIEBERT-SERIES-600-UPS-MODULE-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 20:21:43 2025
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

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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

_Emerson_ObjectIdentity = ObjectIdentity
emerson = _Emerson_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476)
)
_LiebertCorp_ObjectIdentity = ObjectIdentity
liebertCorp = _LiebertCorp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1)
)
_LiebertUps_ObjectIdentity = ObjectIdentity
liebertUps = _LiebertUps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1)
)
_LuExtensions_ObjectIdentity = ObjectIdentity
luExtensions = _LuExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1)
)
_LuCore_ObjectIdentity = ObjectIdentity
luCore = _LuCore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1)
)
_LcUpsIdent_ObjectIdentity = ObjectIdentity
lcUpsIdent = _LcUpsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1)
)


class _LcUpsIdentManufacturer_Type(DisplayString):
    """Custom type lcUpsIdentManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_LcUpsIdentManufacturer_Type.__name__ = "DisplayString"
_LcUpsIdentManufacturer_Object = MibScalar
lcUpsIdentManufacturer = _LcUpsIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1, 1),
    _LcUpsIdentManufacturer_Type()
)
lcUpsIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsIdentManufacturer.setStatus("optional")


class _LcUpsIdentModel_Type(DisplayString):
    """Custom type lcUpsIdentModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_LcUpsIdentModel_Type.__name__ = "DisplayString"
_LcUpsIdentModel_Object = MibScalar
lcUpsIdentModel = _LcUpsIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1, 2),
    _LcUpsIdentModel_Type()
)
lcUpsIdentModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsIdentModel.setStatus("optional")


class _LcUpsIdentSoftwareVersion_Type(DisplayString):
    """Custom type lcUpsIdentSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_LcUpsIdentSoftwareVersion_Type.__name__ = "DisplayString"
_LcUpsIdentSoftwareVersion_Object = MibScalar
lcUpsIdentSoftwareVersion = _LcUpsIdentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1, 3),
    _LcUpsIdentSoftwareVersion_Type()
)
lcUpsIdentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsIdentSoftwareVersion.setStatus("optional")
_LcUpsIdentSpecific_Type = ObjectIdentifier
_LcUpsIdentSpecific_Object = MibScalar
lcUpsIdentSpecific = _LcUpsIdentSpecific_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1, 4),
    _LcUpsIdentSpecific_Type()
)
lcUpsIdentSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsIdentSpecific.setStatus("optional")


class _LcUpsIdentFirmwareVersion_Type(DisplayString):
    """Custom type lcUpsIdentFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_LcUpsIdentFirmwareVersion_Type.__name__ = "DisplayString"
_LcUpsIdentFirmwareVersion_Object = MibScalar
lcUpsIdentFirmwareVersion = _LcUpsIdentFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1, 5),
    _LcUpsIdentFirmwareVersion_Type()
)
lcUpsIdentFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsIdentFirmwareVersion.setStatus("optional")


class _LcUpsIdentSerialNumber_Type(DisplayString):
    """Custom type lcUpsIdentSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_LcUpsIdentSerialNumber_Type.__name__ = "DisplayString"
_LcUpsIdentSerialNumber_Object = MibScalar
lcUpsIdentSerialNumber = _LcUpsIdentSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1, 6),
    _LcUpsIdentSerialNumber_Type()
)
lcUpsIdentSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsIdentSerialNumber.setStatus("optional")
_LcUpsBattery_ObjectIdentity = ObjectIdentity
lcUpsBattery = _LcUpsBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2)
)


class _LcUpsBatTimeRemaining_Type(Integer32):
    """Custom type lcUpsBatTimeRemaining based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcUpsBatTimeRemaining_Type.__name__ = "Integer32"
_LcUpsBatTimeRemaining_Object = MibScalar
lcUpsBatTimeRemaining = _LcUpsBatTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 1),
    _LcUpsBatTimeRemaining_Type()
)
lcUpsBatTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBatTimeRemaining.setStatus("optional")


class _LcUpsBatTemperature_Type(Integer32):
    """Custom type lcUpsBatTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_LcUpsBatTemperature_Type.__name__ = "Integer32"
_LcUpsBatTemperature_Object = MibScalar
lcUpsBatTemperature = _LcUpsBatTemperature_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 2),
    _LcUpsBatTemperature_Type()
)
lcUpsBatTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBatTemperature.setStatus("optional")


class _LcUpsBatVoltage_Type(Integer32):
    """Custom type lcUpsBatVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_LcUpsBatVoltage_Type.__name__ = "Integer32"
_LcUpsBatVoltage_Object = MibScalar
lcUpsBatVoltage = _LcUpsBatVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 3),
    _LcUpsBatVoltage_Type()
)
lcUpsBatVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBatVoltage.setStatus("optional")


class _LcUpsBatCurrent_Type(Integer32):
    """Custom type lcUpsBatCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_LcUpsBatCurrent_Type.__name__ = "Integer32"
_LcUpsBatCurrent_Object = MibScalar
lcUpsBatCurrent = _LcUpsBatCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 4),
    _LcUpsBatCurrent_Type()
)
lcUpsBatCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBatCurrent.setStatus("optional")


class _LcUpsBatCapacity_Type(Integer32):
    """Custom type lcUpsBatCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LcUpsBatCapacity_Type.__name__ = "Integer32"
_LcUpsBatCapacity_Object = MibScalar
lcUpsBatCapacity = _LcUpsBatCapacity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 6),
    _LcUpsBatCapacity_Type()
)
lcUpsBatCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBatCapacity.setStatus("optional")
_LcUpsBatTotalDischCounts_Type = Counter32
_LcUpsBatTotalDischCounts_Object = MibScalar
lcUpsBatTotalDischCounts = _LcUpsBatTotalDischCounts_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 7),
    _LcUpsBatTotalDischCounts_Type()
)
lcUpsBatTotalDischCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBatTotalDischCounts.setStatus("optional")
_LcUpsBatCycleDurationInSeconds_Type = Counter32
_LcUpsBatCycleDurationInSeconds_Object = MibScalar
lcUpsBatCycleDurationInSeconds = _LcUpsBatCycleDurationInSeconds_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 8),
    _LcUpsBatCycleDurationInSeconds_Type()
)
lcUpsBatCycleDurationInSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBatCycleDurationInSeconds.setStatus("optional")
_LcUpsBatAmpHours_Type = Counter32
_LcUpsBatAmpHours_Object = MibScalar
lcUpsBatAmpHours = _LcUpsBatAmpHours_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 9),
    _LcUpsBatAmpHours_Type()
)
lcUpsBatAmpHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBatAmpHours.setStatus("optional")
_LcUpsBatKWhours_Type = Counter32
_LcUpsBatKWhours_Object = MibScalar
lcUpsBatKWhours = _LcUpsBatKWhours_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 10),
    _LcUpsBatKWhours_Type()
)
lcUpsBatKWhours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBatKWhours.setStatus("optional")
_LcUpsBatWattHours_Type = Counter32
_LcUpsBatWattHours_Object = MibScalar
lcUpsBatWattHours = _LcUpsBatWattHours_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 2, 11),
    _LcUpsBatWattHours_Type()
)
lcUpsBatWattHours.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBatWattHours.setStatus("optional")
_LcUpsInput_ObjectIdentity = ObjectIdentity
lcUpsInput = _LcUpsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3)
)


class _LcUpsInputNumLines_Type(Integer32):
    """Custom type lcUpsInputNumLines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_LcUpsInputNumLines_Type.__name__ = "Integer32"
_LcUpsInputNumLines_Object = MibScalar
lcUpsInputNumLines = _LcUpsInputNumLines_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 5),
    _LcUpsInputNumLines_Type()
)
lcUpsInputNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsInputNumLines.setStatus("optional")
_LcUpsInputTable_Object = MibTable
lcUpsInputTable = _LcUpsInputTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 6)
)
if mibBuilder.loadTexts:
    lcUpsInputTable.setStatus("optional")
_LcUpsInputEntry_Object = MibTableRow
lcUpsInputEntry = _LcUpsInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 6, 1)
)
lcUpsInputEntry.setIndexNames(
    (0, "LIEBERT-SERIES-600-UPS-MODULE-MIB", "lcUpsInputLine"),
)
if mibBuilder.loadTexts:
    lcUpsInputEntry.setStatus("optional")


class _LcUpsInputLine_Type(Integer32):
    """Custom type lcUpsInputLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_LcUpsInputLine_Type.__name__ = "Integer32"
_LcUpsInputLine_Object = MibTableColumn
lcUpsInputLine = _LcUpsInputLine_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 6, 1, 1),
    _LcUpsInputLine_Type()
)
lcUpsInputLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsInputLine.setStatus("optional")


class _LcUpsInputVoltage_Type(Integer32):
    """Custom type lcUpsInputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsInputVoltage_Type.__name__ = "Integer32"
_LcUpsInputVoltage_Object = MibTableColumn
lcUpsInputVoltage = _LcUpsInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 6, 1, 2),
    _LcUpsInputVoltage_Type()
)
lcUpsInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsInputVoltage.setStatus("optional")


class _LcUpsInputCurrent_Type(Integer32):
    """Custom type lcUpsInputCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsInputCurrent_Type.__name__ = "Integer32"
_LcUpsInputCurrent_Object = MibTableColumn
lcUpsInputCurrent = _LcUpsInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 6, 1, 3),
    _LcUpsInputCurrent_Type()
)
lcUpsInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsInputCurrent.setStatus("optional")
_LcUpsOutput_ObjectIdentity = ObjectIdentity
lcUpsOutput = _LcUpsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4)
)


class _LcUpsOutputFrequency_Type(Integer32):
    """Custom type lcUpsOutputFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsOutputFrequency_Type.__name__ = "Integer32"
_LcUpsOutputFrequency_Object = MibScalar
lcUpsOutputFrequency = _LcUpsOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 1),
    _LcUpsOutputFrequency_Type()
)
lcUpsOutputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsOutputFrequency.setStatus("optional")


class _LcUpsOutputLoad_Type(Integer32):
    """Custom type lcUpsOutputLoad based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_LcUpsOutputLoad_Type.__name__ = "Integer32"
_LcUpsOutputLoad_Object = MibScalar
lcUpsOutputLoad = _LcUpsOutputLoad_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 2),
    _LcUpsOutputLoad_Type()
)
lcUpsOutputLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsOutputLoad.setStatus("optional")


class _LcUpsOutputNumLines_Type(Integer32):
    """Custom type lcUpsOutputNumLines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_LcUpsOutputNumLines_Type.__name__ = "Integer32"
_LcUpsOutputNumLines_Object = MibScalar
lcUpsOutputNumLines = _LcUpsOutputNumLines_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 3),
    _LcUpsOutputNumLines_Type()
)
lcUpsOutputNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsOutputNumLines.setStatus("optional")
_LcUpsOutputTable_Object = MibTable
lcUpsOutputTable = _LcUpsOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 4)
)
if mibBuilder.loadTexts:
    lcUpsOutputTable.setStatus("optional")
_LcUpsOutputEntry_Object = MibTableRow
lcUpsOutputEntry = _LcUpsOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 4, 1)
)
lcUpsOutputEntry.setIndexNames(
    (0, "LIEBERT-SERIES-600-UPS-MODULE-MIB", "lcUpsOutputLine"),
)
if mibBuilder.loadTexts:
    lcUpsOutputEntry.setStatus("optional")


class _LcUpsOutputLine_Type(Integer32):
    """Custom type lcUpsOutputLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_LcUpsOutputLine_Type.__name__ = "Integer32"
_LcUpsOutputLine_Object = MibTableColumn
lcUpsOutputLine = _LcUpsOutputLine_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 4, 1, 1),
    _LcUpsOutputLine_Type()
)
lcUpsOutputLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsOutputLine.setStatus("optional")


class _LcUpsOutputVoltage_Type(Integer32):
    """Custom type lcUpsOutputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsOutputVoltage_Type.__name__ = "Integer32"
_LcUpsOutputVoltage_Object = MibTableColumn
lcUpsOutputVoltage = _LcUpsOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 4, 1, 2),
    _LcUpsOutputVoltage_Type()
)
lcUpsOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsOutputVoltage.setStatus("optional")


class _LcUpsOutputCurrent_Type(Integer32):
    """Custom type lcUpsOutputCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsOutputCurrent_Type.__name__ = "Integer32"
_LcUpsOutputCurrent_Object = MibTableColumn
lcUpsOutputCurrent = _LcUpsOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 4, 1, 3),
    _LcUpsOutputCurrent_Type()
)
lcUpsOutputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsOutputCurrent.setStatus("optional")


class _LcUpsOutputWatts_Type(Integer32):
    """Custom type lcUpsOutputWatts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsOutputWatts_Type.__name__ = "Integer32"
_LcUpsOutputWatts_Object = MibScalar
lcUpsOutputWatts = _LcUpsOutputWatts_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 5),
    _LcUpsOutputWatts_Type()
)
lcUpsOutputWatts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsOutputWatts.setStatus("optional")
_LcUpsInverter_ObjectIdentity = ObjectIdentity
lcUpsInverter = _LcUpsInverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 5)
)


class _LcUpsInverterStatus_Type(Integer32):
    """Custom type lcUpsInverterStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("on", 2),
          ("off", 3))
    )


_LcUpsInverterStatus_Type.__name__ = "Integer32"
_LcUpsInverterStatus_Object = MibScalar
lcUpsInverterStatus = _LcUpsInverterStatus_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 5, 1),
    _LcUpsInverterStatus_Type()
)
lcUpsInverterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsInverterStatus.setStatus("optional")
_LcUpsAlarm_ObjectIdentity = ObjectIdentity
lcUpsAlarm = _LcUpsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6)
)
_LcUpsAlarms_Type = Gauge32
_LcUpsAlarms_Object = MibScalar
lcUpsAlarms = _LcUpsAlarms_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 1),
    _LcUpsAlarms_Type()
)
lcUpsAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsAlarms.setStatus("optional")
_LcUpsAlarmTable_Object = MibTable
lcUpsAlarmTable = _LcUpsAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 2)
)
if mibBuilder.loadTexts:
    lcUpsAlarmTable.setStatus("optional")
_LcUpsAlarmEntry_Object = MibTableRow
lcUpsAlarmEntry = _LcUpsAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 2, 1)
)
lcUpsAlarmEntry.setIndexNames(
    (0, "LIEBERT-SERIES-600-UPS-MODULE-MIB", "lcUpsAlarmId"),
)
if mibBuilder.loadTexts:
    lcUpsAlarmEntry.setStatus("optional")


class _LcUpsAlarmId_Type(Integer32):
    """Custom type lcUpsAlarmId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsAlarmId_Type.__name__ = "Integer32"
_LcUpsAlarmId_Object = MibTableColumn
lcUpsAlarmId = _LcUpsAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 2, 1, 1),
    _LcUpsAlarmId_Type()
)
lcUpsAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsAlarmId.setStatus("optional")
_LcUpsAlarmDescr_Type = ObjectIdentifier
_LcUpsAlarmDescr_Object = MibTableColumn
lcUpsAlarmDescr = _LcUpsAlarmDescr_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 2, 1, 2),
    _LcUpsAlarmDescr_Type()
)
lcUpsAlarmDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsAlarmDescr.setStatus("optional")
_LcUpsAlarmTime_Type = TimeTicks
_LcUpsAlarmTime_Object = MibTableColumn
lcUpsAlarmTime = _LcUpsAlarmTime_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 2, 1, 3),
    _LcUpsAlarmTime_Type()
)
lcUpsAlarmTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsAlarmTime.setStatus("optional")
_LcUpsAlarmConditions_ObjectIdentity = ObjectIdentity
lcUpsAlarmConditions = _LcUpsAlarmConditions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3)
)
_LcUpsAlarmLowBatteryWarning_ObjectIdentity = ObjectIdentity
lcUpsAlarmLowBatteryWarning = _LcUpsAlarmLowBatteryWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 1)
)
_LcUpsAlarmLowBatteryShutdown_ObjectIdentity = ObjectIdentity
lcUpsAlarmLowBatteryShutdown = _LcUpsAlarmLowBatteryShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 2)
)
_LcUpsAlarmUtilFailed_ObjectIdentity = ObjectIdentity
lcUpsAlarmUtilFailed = _LcUpsAlarmUtilFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 3)
)
_LcUpsAlarmOverTempWarning_ObjectIdentity = ObjectIdentity
lcUpsAlarmOverTempWarning = _LcUpsAlarmOverTempWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 4)
)
_LcUpsAlarmOverTempShutdown_ObjectIdentity = ObjectIdentity
lcUpsAlarmOverTempShutdown = _LcUpsAlarmOverTempShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 5)
)
_LcUpsAlarmOutputOverloadWarning_ObjectIdentity = ObjectIdentity
lcUpsAlarmOutputOverloadWarning = _LcUpsAlarmOutputOverloadWarning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 6)
)
_LcUpsAlarmOnBattery_ObjectIdentity = ObjectIdentity
lcUpsAlarmOnBattery = _LcUpsAlarmOnBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 10)
)
_LcUpsAlarmOutputUnderVoltage_ObjectIdentity = ObjectIdentity
lcUpsAlarmOutputUnderVoltage = _LcUpsAlarmOutputUnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 15)
)
_LcUpsAlarmOutputOverVoltage_ObjectIdentity = ObjectIdentity
lcUpsAlarmOutputOverVoltage = _LcUpsAlarmOutputOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 16)
)
_LcUpsBadBypassPower_ObjectIdentity = ObjectIdentity
lcUpsBadBypassPower = _LcUpsBadBypassPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 17)
)
_LcUpsAlarmDCOverVoltageShutdown_ObjectIdentity = ObjectIdentity
lcUpsAlarmDCOverVoltageShutdown = _LcUpsAlarmDCOverVoltageShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 18)
)
_LcUpsAlarmHardwareShutdown_ObjectIdentity = ObjectIdentity
lcUpsAlarmHardwareShutdown = _LcUpsAlarmHardwareShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 23)
)
_LcUpsAlarmEmergencyXferToBypass_ObjectIdentity = ObjectIdentity
lcUpsAlarmEmergencyXferToBypass = _LcUpsAlarmEmergencyXferToBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 24)
)
_LcUpsAlarmInverterFault_ObjectIdentity = ObjectIdentity
lcUpsAlarmInverterFault = _LcUpsAlarmInverterFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 25)
)
_LcUpsAlarmPhaseRotationError_ObjectIdentity = ObjectIdentity
lcUpsAlarmPhaseRotationError = _LcUpsAlarmPhaseRotationError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 26)
)
_LcUpsAlarmFuseBlown_ObjectIdentity = ObjectIdentity
lcUpsAlarmFuseBlown = _LcUpsAlarmFuseBlown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 28)
)
_LcUpsAlarmAmbientOverTemp_ObjectIdentity = ObjectIdentity
lcUpsAlarmAmbientOverTemp = _LcUpsAlarmAmbientOverTemp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 29)
)
_LcUpsAlarmEmergencyPowerOff_ObjectIdentity = ObjectIdentity
lcUpsAlarmEmergencyPowerOff = _LcUpsAlarmEmergencyPowerOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 30)
)
_LcUpsAlarmFanFailed_ObjectIdentity = ObjectIdentity
lcUpsAlarmFanFailed = _LcUpsAlarmFanFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 31)
)
_LcUpsAlarmControlPowerFailed_ObjectIdentity = ObjectIdentity
lcUpsAlarmControlPowerFailed = _LcUpsAlarmControlPowerFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 32)
)
_LcUpsAlarmReversePower_ObjectIdentity = ObjectIdentity
lcUpsAlarmReversePower = _LcUpsAlarmReversePower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 33)
)
_LcUpsAlarmDCgroundFault_ObjectIdentity = ObjectIdentity
lcUpsAlarmDCgroundFault = _LcUpsAlarmDCgroundFault_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 34)
)
_LcUpsAlarmLoadOnBypass_ObjectIdentity = ObjectIdentity
lcUpsAlarmLoadOnBypass = _LcUpsAlarmLoadOnBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 35)
)
_LcUpsAlarmBatteryCbOpen_ObjectIdentity = ObjectIdentity
lcUpsAlarmBatteryCbOpen = _LcUpsAlarmBatteryCbOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 37)
)
_LcUpsAlarmInputCbOpen_ObjectIdentity = ObjectIdentity
lcUpsAlarmInputCbOpen = _LcUpsAlarmInputCbOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 38)
)
_LcUpsAlarmOutputCbOpen_ObjectIdentity = ObjectIdentity
lcUpsAlarmOutputCbOpen = _LcUpsAlarmOutputCbOpen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 39)
)
_LcUpsAlarmOutputFreqError_ObjectIdentity = ObjectIdentity
lcUpsAlarmOutputFreqError = _LcUpsAlarmOutputFreqError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 40)
)
_LcUpsAlarmStaticSwUnable_ObjectIdentity = ObjectIdentity
lcUpsAlarmStaticSwUnable = _LcUpsAlarmStaticSwUnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 41)
)
_LcUpsAlarmManualResetXfer_ObjectIdentity = ObjectIdentity
lcUpsAlarmManualResetXfer = _LcUpsAlarmManualResetXfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 42)
)
_LcUpsAlarmAutoRexferPrimed_ObjectIdentity = ObjectIdentity
lcUpsAlarmAutoRexferPrimed = _LcUpsAlarmAutoRexferPrimed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 43)
)
_LcUpsAlarmBattCycleBuffWarn_ObjectIdentity = ObjectIdentity
lcUpsAlarmBattCycleBuffWarn = _LcUpsAlarmBattCycleBuffWarn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 44)
)
_LcUpsControl_ObjectIdentity = ObjectIdentity
lcUpsControl = _LcUpsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8)
)


class _LcUpsControlRebootAgentDelay_Type(Integer32):
    """Custom type lcUpsControlRebootAgentDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsControlRebootAgentDelay_Type.__name__ = "Integer32"
_LcUpsControlRebootAgentDelay_Object = MibScalar
lcUpsControlRebootAgentDelay = _LcUpsControlRebootAgentDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 8),
    _LcUpsControlRebootAgentDelay_Type()
)
lcUpsControlRebootAgentDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsControlRebootAgentDelay.setStatus("optional")
_LcUpsNominal_ObjectIdentity = ObjectIdentity
lcUpsNominal = _LcUpsNominal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9)
)


class _LcUpsNominalOutputVoltage_Type(Integer32):
    """Custom type lcUpsNominalOutputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsNominalOutputVoltage_Type.__name__ = "Integer32"
_LcUpsNominalOutputVoltage_Object = MibScalar
lcUpsNominalOutputVoltage = _LcUpsNominalOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 1),
    _LcUpsNominalOutputVoltage_Type()
)
lcUpsNominalOutputVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsNominalOutputVoltage.setStatus("optional")


class _LcUpsNominalInputVoltage_Type(Integer32):
    """Custom type lcUpsNominalInputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsNominalInputVoltage_Type.__name__ = "Integer32"
_LcUpsNominalInputVoltage_Object = MibScalar
lcUpsNominalInputVoltage = _LcUpsNominalInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 2),
    _LcUpsNominalInputVoltage_Type()
)
lcUpsNominalInputVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsNominalInputVoltage.setStatus("optional")


class _LcUpsNominalOutputFreq_Type(Integer32):
    """Custom type lcUpsNominalOutputFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsNominalOutputFreq_Type.__name__ = "Integer32"
_LcUpsNominalOutputFreq_Object = MibScalar
lcUpsNominalOutputFreq = _LcUpsNominalOutputFreq_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 5),
    _LcUpsNominalOutputFreq_Type()
)
lcUpsNominalOutputFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsNominalOutputFreq.setStatus("optional")


class _LcUpsNominalOutputVaRating_Type(Integer32):
    """Custom type lcUpsNominalOutputVaRating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsNominalOutputVaRating_Type.__name__ = "Integer32"
_LcUpsNominalOutputVaRating_Object = MibScalar
lcUpsNominalOutputVaRating = _LcUpsNominalOutputVaRating_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 7),
    _LcUpsNominalOutputVaRating_Type()
)
lcUpsNominalOutputVaRating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsNominalOutputVaRating.setStatus("optional")


class _LcUpsNominalOutputWattsRating_Type(Integer32):
    """Custom type lcUpsNominalOutputWattsRating based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsNominalOutputWattsRating_Type.__name__ = "Integer32"
_LcUpsNominalOutputWattsRating_Object = MibScalar
lcUpsNominalOutputWattsRating = _LcUpsNominalOutputWattsRating_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 8),
    _LcUpsNominalOutputWattsRating_Type()
)
lcUpsNominalOutputWattsRating.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsNominalOutputWattsRating.setStatus("optional")
_LcUpsTraps_ObjectIdentity = ObjectIdentity
lcUpsTraps = _LcUpsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11)
)
_LcUpsBypass_ObjectIdentity = ObjectIdentity
lcUpsBypass = _LcUpsBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 13)
)


class _LcUpsOnBypass_Type(Integer32):
    """Custom type lcUpsOnBypass based on Integer32"""
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
        *(("unknown", 1),
          ("yes", 2),
          ("no", 3),
          ("maintenance", 4))
    )


_LcUpsOnBypass_Type.__name__ = "Integer32"
_LcUpsOnBypass_Object = MibScalar
lcUpsOnBypass = _LcUpsOnBypass_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 13, 1),
    _LcUpsOnBypass_Type()
)
lcUpsOnBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsOnBypass.setStatus("optional")


class _LcUpsBypassFrequency_Type(Integer32):
    """Custom type lcUpsBypassFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsBypassFrequency_Type.__name__ = "Integer32"
_LcUpsBypassFrequency_Object = MibScalar
lcUpsBypassFrequency = _LcUpsBypassFrequency_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 13, 2),
    _LcUpsBypassFrequency_Type()
)
lcUpsBypassFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBypassFrequency.setStatus("optional")


class _LcUpsBypassNumLines_Type(Integer32):
    """Custom type lcUpsBypassNumLines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_LcUpsBypassNumLines_Type.__name__ = "Integer32"
_LcUpsBypassNumLines_Object = MibScalar
lcUpsBypassNumLines = _LcUpsBypassNumLines_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 13, 3),
    _LcUpsBypassNumLines_Type()
)
lcUpsBypassNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBypassNumLines.setStatus("optional")
_LcUpsBypassTable_Object = MibTable
lcUpsBypassTable = _LcUpsBypassTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 13, 4)
)
if mibBuilder.loadTexts:
    lcUpsBypassTable.setStatus("optional")
_LcUpsBypassEntry_Object = MibTableRow
lcUpsBypassEntry = _LcUpsBypassEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 13, 4, 1)
)
lcUpsBypassEntry.setIndexNames(
    (0, "LIEBERT-SERIES-600-UPS-MODULE-MIB", "lcUpsBypassLine"),
)
if mibBuilder.loadTexts:
    lcUpsBypassEntry.setStatus("optional")


class _LcUpsBypassLine_Type(Integer32):
    """Custom type lcUpsBypassLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_LcUpsBypassLine_Type.__name__ = "Integer32"
_LcUpsBypassLine_Object = MibTableColumn
lcUpsBypassLine = _LcUpsBypassLine_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 13, 4, 1, 1),
    _LcUpsBypassLine_Type()
)
lcUpsBypassLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBypassLine.setStatus("optional")


class _LcUpsBypassVoltage_Type(Integer32):
    """Custom type lcUpsBypassVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsBypassVoltage_Type.__name__ = "Integer32"
_LcUpsBypassVoltage_Object = MibTableColumn
lcUpsBypassVoltage = _LcUpsBypassVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 13, 4, 1, 2),
    _LcUpsBypassVoltage_Type()
)
lcUpsBypassVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBypassVoltage.setStatus("optional")


class _LcUpsBypassCurrent_Type(Integer32):
    """Custom type lcUpsBypassCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsBypassCurrent_Type.__name__ = "Integer32"
_LcUpsBypassCurrent_Object = MibTableColumn
lcUpsBypassCurrent = _LcUpsBypassCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 13, 4, 1, 3),
    _LcUpsBypassCurrent_Type()
)
lcUpsBypassCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsBypassCurrent.setStatus("optional")
_LcUpsConfig_ObjectIdentity = ObjectIdentity
lcUpsConfig = _LcUpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 14)
)


class _LcUpsConfigType_Type(Integer32):
    """Custom type lcUpsConfigType based on Integer32"""
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
        *(("unknown", 1),
          ("online", 2),
          ("offline", 3),
          ("lineinteractive", 4))
    )


_LcUpsConfigType_Type.__name__ = "Integer32"
_LcUpsConfigType_Object = MibScalar
lcUpsConfigType = _LcUpsConfigType_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 14, 1),
    _LcUpsConfigType_Type()
)
lcUpsConfigType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsConfigType.setStatus("optional")


class _LcUpsConfigBypassInstalled_Type(Integer32):
    """Custom type lcUpsConfigBypassInstalled based on Integer32"""
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
        *(("unknown", 1),
          ("yes", 2),
          ("no", 3),
          ("dualinput", 4))
    )


_LcUpsConfigBypassInstalled_Type.__name__ = "Integer32"
_LcUpsConfigBypassInstalled_Object = MibScalar
lcUpsConfigBypassInstalled = _LcUpsConfigBypassInstalled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 14, 2),
    _LcUpsConfigBypassInstalled_Type()
)
lcUpsConfigBypassInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsConfigBypassInstalled.setStatus("optional")
_LuUpsModule_ObjectIdentity = ObjectIdentity
luUpsModule = _LuUpsModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 11)
)
_LuExperimental_ObjectIdentity = ObjectIdentity
luExperimental = _LuExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 2)
)
_LuPrivate_ObjectIdentity = ObjectIdentity
luPrivate = _LuPrivate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 3)
)

# Managed Objects groups


# Notification objects

lcUpsOverloadWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 1)
)
lcUpsOverloadWarningTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOverloadWarningTrap.setStatus(
        ""
    )

lcUpsOverloadShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 2)
)
lcUpsOverloadShutdownTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOverloadShutdownTrap.setStatus(
        ""
    )

lcUpsOnBatteryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 3)
)
lcUpsOnBatteryTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOnBatteryTrap.setStatus(
        ""
    )

lcUpsLowBatteryWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 4)
)
lcUpsLowBatteryWarningTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsLowBatteryWarningTrap.setStatus(
        ""
    )

lcUpsLowBatteryShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 5)
)
lcUpsLowBatteryShutdownTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsLowBatteryShutdownTrap.setStatus(
        ""
    )

lcUpsUtilPowerFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 6)
)
lcUpsUtilPowerFailedTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsUtilPowerFailedTrap.setStatus(
        ""
    )

lcUpsUtilPowerRestoredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 7)
)
lcUpsUtilPowerRestoredTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsUtilPowerRestoredTrap.setStatus(
        ""
    )

lcUpsInputOverVoltageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 8)
)
lcUpsInputOverVoltageTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsInputOverVoltageTrap.setStatus(
        ""
    )

lcUpsOverTempWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 9)
)
lcUpsOverTempWarningTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOverTempWarningTrap.setStatus(
        ""
    )

lcUpsOverTempShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 10)
)
lcUpsOverTempShutdownTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOverTempShutdownTrap.setStatus(
        ""
    )

lcUpsAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 11)
)
lcUpsAlarmTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsAlarmTrap.setStatus(
        ""
    )

lcUpsOutputOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 12)
)
lcUpsOutputOffTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOutputOffTrap.setStatus(
        ""
    )

lcUpsOutputOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 14)
)
lcUpsOutputOnTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOutputOnTrap.setStatus(
        ""
    )

lcUpsDCOverVoltageShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 23)
)
lcUpsDCOverVoltageShutdownTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsDCOverVoltageShutdownTrap.setStatus(
        ""
    )

lcUpsOutputOverVoltageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 24)
)
lcUpsOutputOverVoltageTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOutputOverVoltageTrap.setStatus(
        ""
    )

lcUpsFuseBlownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 25)
)
lcUpsFuseBlownTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsFuseBlownTrap.setStatus(
        ""
    )

lcUpsEmergencyPowerOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 26)
)
lcUpsEmergencyPowerOffTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsEmergencyPowerOffTrap.setStatus(
        ""
    )

lcUpsControlPowerFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 27)
)
lcUpsControlPowerFailureTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsControlPowerFailureTrap.setStatus(
        ""
    )

lcUpsReversePowerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 28)
)
lcUpsReversePowerTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsReversePowerTrap.setStatus(
        ""
    )

lcUpsPhaseRotationErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 29)
)
lcUpsPhaseRotationErrorTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsPhaseRotationErrorTrap.setStatus(
        ""
    )

lcUpsLoadOnBypassTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 30)
)
lcUpsLoadOnBypassTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsLoadOnBypassTrap.setStatus(
        ""
    )

lcUpsEmergencyXferToBypassTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 31)
)
lcUpsEmergencyXferToBypassTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsEmergencyXferToBypassTrap.setStatus(
        ""
    )

lcUpsInverterFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 34)
)
lcUpsInverterFaultTrap.setObjects(
    ("SNMPv2-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsInverterFaultTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIEBERT-SERIES-600-UPS-MODULE-MIB",
    **{"emerson": emerson,
       "liebertCorp": liebertCorp,
       "liebertUps": liebertUps,
       "luExtensions": luExtensions,
       "luCore": luCore,
       "lcUpsIdent": lcUpsIdent,
       "lcUpsIdentManufacturer": lcUpsIdentManufacturer,
       "lcUpsIdentModel": lcUpsIdentModel,
       "lcUpsIdentSoftwareVersion": lcUpsIdentSoftwareVersion,
       "lcUpsIdentSpecific": lcUpsIdentSpecific,
       "lcUpsIdentFirmwareVersion": lcUpsIdentFirmwareVersion,
       "lcUpsIdentSerialNumber": lcUpsIdentSerialNumber,
       "lcUpsBattery": lcUpsBattery,
       "lcUpsBatTimeRemaining": lcUpsBatTimeRemaining,
       "lcUpsBatTemperature": lcUpsBatTemperature,
       "lcUpsBatVoltage": lcUpsBatVoltage,
       "lcUpsBatCurrent": lcUpsBatCurrent,
       "lcUpsBatCapacity": lcUpsBatCapacity,
       "lcUpsBatTotalDischCounts": lcUpsBatTotalDischCounts,
       "lcUpsBatCycleDurationInSeconds": lcUpsBatCycleDurationInSeconds,
       "lcUpsBatAmpHours": lcUpsBatAmpHours,
       "lcUpsBatKWhours": lcUpsBatKWhours,
       "lcUpsBatWattHours": lcUpsBatWattHours,
       "lcUpsInput": lcUpsInput,
       "lcUpsInputNumLines": lcUpsInputNumLines,
       "lcUpsInputTable": lcUpsInputTable,
       "lcUpsInputEntry": lcUpsInputEntry,
       "lcUpsInputLine": lcUpsInputLine,
       "lcUpsInputVoltage": lcUpsInputVoltage,
       "lcUpsInputCurrent": lcUpsInputCurrent,
       "lcUpsOutput": lcUpsOutput,
       "lcUpsOutputFrequency": lcUpsOutputFrequency,
       "lcUpsOutputLoad": lcUpsOutputLoad,
       "lcUpsOutputNumLines": lcUpsOutputNumLines,
       "lcUpsOutputTable": lcUpsOutputTable,
       "lcUpsOutputEntry": lcUpsOutputEntry,
       "lcUpsOutputLine": lcUpsOutputLine,
       "lcUpsOutputVoltage": lcUpsOutputVoltage,
       "lcUpsOutputCurrent": lcUpsOutputCurrent,
       "lcUpsOutputWatts": lcUpsOutputWatts,
       "lcUpsInverter": lcUpsInverter,
       "lcUpsInverterStatus": lcUpsInverterStatus,
       "lcUpsAlarm": lcUpsAlarm,
       "lcUpsAlarms": lcUpsAlarms,
       "lcUpsAlarmTable": lcUpsAlarmTable,
       "lcUpsAlarmEntry": lcUpsAlarmEntry,
       "lcUpsAlarmId": lcUpsAlarmId,
       "lcUpsAlarmDescr": lcUpsAlarmDescr,
       "lcUpsAlarmTime": lcUpsAlarmTime,
       "lcUpsAlarmConditions": lcUpsAlarmConditions,
       "lcUpsAlarmLowBatteryWarning": lcUpsAlarmLowBatteryWarning,
       "lcUpsAlarmLowBatteryShutdown": lcUpsAlarmLowBatteryShutdown,
       "lcUpsAlarmUtilFailed": lcUpsAlarmUtilFailed,
       "lcUpsAlarmOverTempWarning": lcUpsAlarmOverTempWarning,
       "lcUpsAlarmOverTempShutdown": lcUpsAlarmOverTempShutdown,
       "lcUpsAlarmOutputOverloadWarning": lcUpsAlarmOutputOverloadWarning,
       "lcUpsAlarmOnBattery": lcUpsAlarmOnBattery,
       "lcUpsAlarmOutputUnderVoltage": lcUpsAlarmOutputUnderVoltage,
       "lcUpsAlarmOutputOverVoltage": lcUpsAlarmOutputOverVoltage,
       "lcUpsBadBypassPower": lcUpsBadBypassPower,
       "lcUpsAlarmDCOverVoltageShutdown": lcUpsAlarmDCOverVoltageShutdown,
       "lcUpsAlarmHardwareShutdown": lcUpsAlarmHardwareShutdown,
       "lcUpsAlarmEmergencyXferToBypass": lcUpsAlarmEmergencyXferToBypass,
       "lcUpsAlarmInverterFault": lcUpsAlarmInverterFault,
       "lcUpsAlarmPhaseRotationError": lcUpsAlarmPhaseRotationError,
       "lcUpsAlarmFuseBlown": lcUpsAlarmFuseBlown,
       "lcUpsAlarmAmbientOverTemp": lcUpsAlarmAmbientOverTemp,
       "lcUpsAlarmEmergencyPowerOff": lcUpsAlarmEmergencyPowerOff,
       "lcUpsAlarmFanFailed": lcUpsAlarmFanFailed,
       "lcUpsAlarmControlPowerFailed": lcUpsAlarmControlPowerFailed,
       "lcUpsAlarmReversePower": lcUpsAlarmReversePower,
       "lcUpsAlarmDCgroundFault": lcUpsAlarmDCgroundFault,
       "lcUpsAlarmLoadOnBypass": lcUpsAlarmLoadOnBypass,
       "lcUpsAlarmBatteryCbOpen": lcUpsAlarmBatteryCbOpen,
       "lcUpsAlarmInputCbOpen": lcUpsAlarmInputCbOpen,
       "lcUpsAlarmOutputCbOpen": lcUpsAlarmOutputCbOpen,
       "lcUpsAlarmOutputFreqError": lcUpsAlarmOutputFreqError,
       "lcUpsAlarmStaticSwUnable": lcUpsAlarmStaticSwUnable,
       "lcUpsAlarmManualResetXfer": lcUpsAlarmManualResetXfer,
       "lcUpsAlarmAutoRexferPrimed": lcUpsAlarmAutoRexferPrimed,
       "lcUpsAlarmBattCycleBuffWarn": lcUpsAlarmBattCycleBuffWarn,
       "lcUpsControl": lcUpsControl,
       "lcUpsControlRebootAgentDelay": lcUpsControlRebootAgentDelay,
       "lcUpsNominal": lcUpsNominal,
       "lcUpsNominalOutputVoltage": lcUpsNominalOutputVoltage,
       "lcUpsNominalInputVoltage": lcUpsNominalInputVoltage,
       "lcUpsNominalOutputFreq": lcUpsNominalOutputFreq,
       "lcUpsNominalOutputVaRating": lcUpsNominalOutputVaRating,
       "lcUpsNominalOutputWattsRating": lcUpsNominalOutputWattsRating,
       "lcUpsTraps": lcUpsTraps,
       "lcUpsOverloadWarningTrap": lcUpsOverloadWarningTrap,
       "lcUpsOverloadShutdownTrap": lcUpsOverloadShutdownTrap,
       "lcUpsOnBatteryTrap": lcUpsOnBatteryTrap,
       "lcUpsLowBatteryWarningTrap": lcUpsLowBatteryWarningTrap,
       "lcUpsLowBatteryShutdownTrap": lcUpsLowBatteryShutdownTrap,
       "lcUpsUtilPowerFailedTrap": lcUpsUtilPowerFailedTrap,
       "lcUpsUtilPowerRestoredTrap": lcUpsUtilPowerRestoredTrap,
       "lcUpsInputOverVoltageTrap": lcUpsInputOverVoltageTrap,
       "lcUpsOverTempWarningTrap": lcUpsOverTempWarningTrap,
       "lcUpsOverTempShutdownTrap": lcUpsOverTempShutdownTrap,
       "lcUpsAlarmTrap": lcUpsAlarmTrap,
       "lcUpsOutputOffTrap": lcUpsOutputOffTrap,
       "lcUpsOutputOnTrap": lcUpsOutputOnTrap,
       "lcUpsDCOverVoltageShutdownTrap": lcUpsDCOverVoltageShutdownTrap,
       "lcUpsOutputOverVoltageTrap": lcUpsOutputOverVoltageTrap,
       "lcUpsFuseBlownTrap": lcUpsFuseBlownTrap,
       "lcUpsEmergencyPowerOffTrap": lcUpsEmergencyPowerOffTrap,
       "lcUpsControlPowerFailureTrap": lcUpsControlPowerFailureTrap,
       "lcUpsReversePowerTrap": lcUpsReversePowerTrap,
       "lcUpsPhaseRotationErrorTrap": lcUpsPhaseRotationErrorTrap,
       "lcUpsLoadOnBypassTrap": lcUpsLoadOnBypassTrap,
       "lcUpsEmergencyXferToBypassTrap": lcUpsEmergencyXferToBypassTrap,
       "lcUpsInverterFaultTrap": lcUpsInverterFaultTrap,
       "lcUpsBypass": lcUpsBypass,
       "lcUpsOnBypass": lcUpsOnBypass,
       "lcUpsBypassFrequency": lcUpsBypassFrequency,
       "lcUpsBypassNumLines": lcUpsBypassNumLines,
       "lcUpsBypassTable": lcUpsBypassTable,
       "lcUpsBypassEntry": lcUpsBypassEntry,
       "lcUpsBypassLine": lcUpsBypassLine,
       "lcUpsBypassVoltage": lcUpsBypassVoltage,
       "lcUpsBypassCurrent": lcUpsBypassCurrent,
       "lcUpsConfig": lcUpsConfig,
       "lcUpsConfigType": lcUpsConfigType,
       "lcUpsConfigBypassInstalled": lcUpsConfigBypassInstalled,
       "luUpsModule": luUpsModule,
       "luExperimental": luExperimental,
       "luPrivate": luPrivate}
)
