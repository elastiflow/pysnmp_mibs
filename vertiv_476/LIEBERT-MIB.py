# SNMP MIB module (LIEBERT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/vertiv_476/LIEBERT-MIB.mib
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

(Bits,
 Counter32,
 Counter64,
 DisplayString,
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
 TruthValue,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "DisplayString",
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
    "TruthValue",
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


class _LcUpsIdentManufactureDate_Type(DisplayString):
    """Custom type lcUpsIdentManufactureDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_LcUpsIdentManufactureDate_Type.__name__ = "DisplayString"
_LcUpsIdentManufactureDate_Object = MibScalar
lcUpsIdentManufactureDate = _LcUpsIdentManufactureDate_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 1, 7),
    _LcUpsIdentManufactureDate_Type()
)
lcUpsIdentManufactureDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsIdentManufactureDate.setStatus("optional")
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


class _LcUpsInputFrequency_Type(Integer32):
    """Custom type lcUpsInputFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsInputFrequency_Type.__name__ = "Integer32"
_LcUpsInputFrequency_Object = MibScalar
lcUpsInputFrequency = _LcUpsInputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 1),
    _LcUpsInputFrequency_Type()
)
lcUpsInputFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsInputFrequency.setStatus("optional")
_LcUpsInputBrownOuts_Type = Counter32
_LcUpsInputBrownOuts_Object = MibScalar
lcUpsInputBrownOuts = _LcUpsInputBrownOuts_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 2),
    _LcUpsInputBrownOuts_Type()
)
lcUpsInputBrownOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsInputBrownOuts.setStatus("optional")
_LcUpsInputBlackOuts_Type = Counter32
_LcUpsInputBlackOuts_Object = MibScalar
lcUpsInputBlackOuts = _LcUpsInputBlackOuts_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 3),
    _LcUpsInputBlackOuts_Type()
)
lcUpsInputBlackOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsInputBlackOuts.setStatus("optional")
_LcUpsInputTransients_Type = Counter32
_LcUpsInputTransients_Object = MibScalar
lcUpsInputTransients = _LcUpsInputTransients_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 4),
    _LcUpsInputTransients_Type()
)
lcUpsInputTransients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsInputTransients.setStatus("optional")


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
    (0, "LIEBERT-MIB", "lcUpsInputLine"),
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


class _LcUpsInputVA_Type(Integer32):
    """Custom type lcUpsInputVA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsInputVA_Type.__name__ = "Integer32"
_LcUpsInputVA_Object = MibTableColumn
lcUpsInputVA = _LcUpsInputVA_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 3, 6, 1, 4),
    _LcUpsInputVA_Type()
)
lcUpsInputVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsInputVA.setStatus("optional")
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
    (0, "LIEBERT-MIB", "lcUpsOutputLine"),
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


class _LcUpsOutputVA_Type(Integer32):
    """Custom type lcUpsOutputVA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsOutputVA_Type.__name__ = "Integer32"
_LcUpsOutputVA_Object = MibTableColumn
lcUpsOutputVA = _LcUpsOutputVA_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 4, 4, 1, 4),
    _LcUpsOutputVA_Type()
)
lcUpsOutputVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsOutputVA.setStatus("optional")


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


class _LcUpsInverterTemp_Type(Integer32):
    """Custom type lcUpsInverterTemp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_LcUpsInverterTemp_Type.__name__ = "Integer32"
_LcUpsInverterTemp_Object = MibScalar
lcUpsInverterTemp = _LcUpsInverterTemp_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 5, 2),
    _LcUpsInverterTemp_Type()
)
lcUpsInverterTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsInverterTemp.setStatus("optional")
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
    (0, "LIEBERT-MIB", "lcUpsAlarmId"),
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
_LcUpsAlarmOutputOverloadShutdown_ObjectIdentity = ObjectIdentity
lcUpsAlarmOutputOverloadShutdown = _LcUpsAlarmOutputOverloadShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 7)
)
_LcUpsAlarmInputOverVoltage_ObjectIdentity = ObjectIdentity
lcUpsAlarmInputOverVoltage = _LcUpsAlarmInputOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 8)
)
_LcUpsAlarmBatteryBad_ObjectIdentity = ObjectIdentity
lcUpsAlarmBatteryBad = _LcUpsAlarmBatteryBad_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 9)
)
_LcUpsAlarmOnBattery_ObjectIdentity = ObjectIdentity
lcUpsAlarmOnBattery = _LcUpsAlarmOnBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 10)
)
_LcUpsAlarmStopNoticeIssued_ObjectIdentity = ObjectIdentity
lcUpsAlarmStopNoticeIssued = _LcUpsAlarmStopNoticeIssued_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 11)
)
_LcUpsAlarmUpsOff_ObjectIdentity = ObjectIdentity
lcUpsAlarmUpsOff = _LcUpsAlarmUpsOff_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 12)
)
_LcUpsAlarmInputFreqError_ObjectIdentity = ObjectIdentity
lcUpsAlarmInputFreqError = _LcUpsAlarmInputFreqError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 13)
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
_LcUpsAlarmModuleSummary_ObjectIdentity = ObjectIdentity
lcUpsAlarmModuleSummary = _LcUpsAlarmModuleSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 45)
)
_LcUpsLineCorrectionActive_ObjectIdentity = ObjectIdentity
lcUpsLineCorrectionActive = _LcUpsLineCorrectionActive_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 6, 3, 46)
)
_LcUpsTest_ObjectIdentity = ObjectIdentity
lcUpsTest = _LcUpsTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 7)
)


class _LcUpsTestBattery_Type(Integer32):
    """Custom type lcUpsTestBattery based on Integer32"""
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
          ("start", 2),
          ("abort", 3))
    )


_LcUpsTestBattery_Type.__name__ = "Integer32"
_LcUpsTestBattery_Object = MibScalar
lcUpsTestBattery = _LcUpsTestBattery_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 7, 1),
    _LcUpsTestBattery_Type()
)
lcUpsTestBattery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsTestBattery.setStatus("optional")


class _LcUpsTestBatteryStatus_Type(Integer32):
    """Custom type lcUpsTestBatteryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("passed", 2),
          ("failed", 3),
          ("inProgress", 4),
          ("sysFailure", 5),
          ("notSupported", 6),
          ("inhibited", 7))
    )


_LcUpsTestBatteryStatus_Type.__name__ = "Integer32"
_LcUpsTestBatteryStatus_Object = MibScalar
lcUpsTestBatteryStatus = _LcUpsTestBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 7, 2),
    _LcUpsTestBatteryStatus_Type()
)
lcUpsTestBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsTestBatteryStatus.setStatus("optional")


class _LcUpsTestDiag_Type(Integer32):
    """Custom type lcUpsTestDiag based on Integer32"""
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
          ("start", 2),
          ("abort", 3))
    )


_LcUpsTestDiag_Type.__name__ = "Integer32"
_LcUpsTestDiag_Object = MibScalar
lcUpsTestDiag = _LcUpsTestDiag_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 7, 3),
    _LcUpsTestDiag_Type()
)
lcUpsTestDiag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsTestDiag.setStatus("optional")


class _LcUpsTestDiagStatus_Type(Integer32):
    """Custom type lcUpsTestDiagStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("passed", 2),
          ("failed", 3),
          ("inProgress", 4),
          ("sysFailure", 5),
          ("notSupported", 6),
          ("inhibited", 7))
    )


_LcUpsTestDiagStatus_Type.__name__ = "Integer32"
_LcUpsTestDiagStatus_Object = MibScalar
lcUpsTestDiagStatus = _LcUpsTestDiagStatus_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 7, 4),
    _LcUpsTestDiagStatus_Type()
)
lcUpsTestDiagStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsTestDiagStatus.setStatus("optional")
_LcUpsControl_ObjectIdentity = ObjectIdentity
lcUpsControl = _LcUpsControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8)
)


class _LcUpsControlOutputOffDelay_Type(Integer32):
    """Custom type lcUpsControlOutputOffDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsControlOutputOffDelay_Type.__name__ = "Integer32"
_LcUpsControlOutputOffDelay_Object = MibScalar
lcUpsControlOutputOffDelay = _LcUpsControlOutputOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 1),
    _LcUpsControlOutputOffDelay_Type()
)
lcUpsControlOutputOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsControlOutputOffDelay.setStatus("optional")


class _LcUpsControlOutputOnDelay_Type(Integer32):
    """Custom type lcUpsControlOutputOnDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsControlOutputOnDelay_Type.__name__ = "Integer32"
_LcUpsControlOutputOnDelay_Object = MibScalar
lcUpsControlOutputOnDelay = _LcUpsControlOutputOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 2),
    _LcUpsControlOutputOnDelay_Type()
)
lcUpsControlOutputOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsControlOutputOnDelay.setStatus("optional")


class _LcUpsControlOutputOffTrapDelay_Type(Integer32):
    """Custom type lcUpsControlOutputOffTrapDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsControlOutputOffTrapDelay_Type.__name__ = "Integer32"
_LcUpsControlOutputOffTrapDelay_Object = MibScalar
lcUpsControlOutputOffTrapDelay = _LcUpsControlOutputOffTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 3),
    _LcUpsControlOutputOffTrapDelay_Type()
)
lcUpsControlOutputOffTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsControlOutputOffTrapDelay.setStatus("optional")


class _LcUpsControlOutputOnTrapDelay_Type(Integer32):
    """Custom type lcUpsControlOutputOnTrapDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsControlOutputOnTrapDelay_Type.__name__ = "Integer32"
_LcUpsControlOutputOnTrapDelay_Object = MibScalar
lcUpsControlOutputOnTrapDelay = _LcUpsControlOutputOnTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 4),
    _LcUpsControlOutputOnTrapDelay_Type()
)
lcUpsControlOutputOnTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsControlOutputOnTrapDelay.setStatus("optional")


class _LcUpsControlUnixShutdownDelay_Type(Integer32):
    """Custom type lcUpsControlUnixShutdownDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsControlUnixShutdownDelay_Type.__name__ = "Integer32"
_LcUpsControlUnixShutdownDelay_Object = MibScalar
lcUpsControlUnixShutdownDelay = _LcUpsControlUnixShutdownDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 5),
    _LcUpsControlUnixShutdownDelay_Type()
)
lcUpsControlUnixShutdownDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsControlUnixShutdownDelay.setStatus("optional")


class _LcUpsControlUnixShutdownTrapDelay_Type(Integer32):
    """Custom type lcUpsControlUnixShutdownTrapDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsControlUnixShutdownTrapDelay_Type.__name__ = "Integer32"
_LcUpsControlUnixShutdownTrapDelay_Object = MibScalar
lcUpsControlUnixShutdownTrapDelay = _LcUpsControlUnixShutdownTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 6),
    _LcUpsControlUnixShutdownTrapDelay_Type()
)
lcUpsControlUnixShutdownTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsControlUnixShutdownTrapDelay.setStatus("optional")


class _LcUpsControlCancelCommands_Type(Integer32):
    """Custom type lcUpsControlCancelCommands based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("cancel", 2))
    )


_LcUpsControlCancelCommands_Type.__name__ = "Integer32"
_LcUpsControlCancelCommands_Object = MibScalar
lcUpsControlCancelCommands = _LcUpsControlCancelCommands_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 8, 7),
    _LcUpsControlCancelCommands_Type()
)
lcUpsControlCancelCommands.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsControlCancelCommands.setStatus("optional")


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


class _LcUpsNominalOutputVA_Type(Integer32):
    """Custom type lcUpsNominalOutputVA based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsNominalOutputVA_Type.__name__ = "Integer32"
_LcUpsNominalOutputVA_Object = MibScalar
lcUpsNominalOutputVA = _LcUpsNominalOutputVA_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 3),
    _LcUpsNominalOutputVA_Type()
)
lcUpsNominalOutputVA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsNominalOutputVA.setStatus("optional")


class _LcUpsNominalOutputWatts_Type(Integer32):
    """Custom type lcUpsNominalOutputWatts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsNominalOutputWatts_Type.__name__ = "Integer32"
_LcUpsNominalOutputWatts_Object = MibScalar
lcUpsNominalOutputWatts = _LcUpsNominalOutputWatts_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 4),
    _LcUpsNominalOutputWatts_Type()
)
lcUpsNominalOutputWatts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsNominalOutputWatts.setStatus("optional")


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


class _LcUpsNominalInputFreq_Type(Integer32):
    """Custom type lcUpsNominalInputFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LcUpsNominalInputFreq_Type.__name__ = "Integer32"
_LcUpsNominalInputFreq_Object = MibScalar
lcUpsNominalInputFreq = _LcUpsNominalInputFreq_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 9, 6),
    _LcUpsNominalInputFreq_Type()
)
lcUpsNominalInputFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsNominalInputFreq.setStatus("optional")


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
_LcUpsSwitchedReceptacles_ObjectIdentity = ObjectIdentity
lcUpsSwitchedReceptacles = _LcUpsSwitchedReceptacles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 12)
)


class _LcUpsSwitchedReceptMaxNum_Type(Integer32):
    """Custom type lcUpsSwitchedReceptMaxNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_LcUpsSwitchedReceptMaxNum_Type.__name__ = "Integer32"
_LcUpsSwitchedReceptMaxNum_Object = MibScalar
lcUpsSwitchedReceptMaxNum = _LcUpsSwitchedReceptMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 12, 1),
    _LcUpsSwitchedReceptMaxNum_Type()
)
lcUpsSwitchedReceptMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsSwitchedReceptMaxNum.setStatus("optional")
_LcUpsSwitchedReceptTable_Object = MibTable
lcUpsSwitchedReceptTable = _LcUpsSwitchedReceptTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 12, 2)
)
if mibBuilder.loadTexts:
    lcUpsSwitchedReceptTable.setStatus("optional")
_LcUpsSwitchedReceptEntry_Object = MibTableRow
lcUpsSwitchedReceptEntry = _LcUpsSwitchedReceptEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 12, 2, 1)
)
lcUpsSwitchedReceptEntry.setIndexNames(
    (0, "LIEBERT-MIB", "lcUpsSwitchedReceptIndex"),
)
if mibBuilder.loadTexts:
    lcUpsSwitchedReceptEntry.setStatus("optional")
_LcUpsSwitchedReceptIndex_Type = Integer32
_LcUpsSwitchedReceptIndex_Object = MibTableColumn
lcUpsSwitchedReceptIndex = _LcUpsSwitchedReceptIndex_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 12, 2, 1, 1),
    _LcUpsSwitchedReceptIndex_Type()
)
lcUpsSwitchedReceptIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsSwitchedReceptIndex.setStatus("optional")


class _LcUpsSwitchedReceptOnDelay_Type(Integer32):
    """Custom type lcUpsSwitchedReceptOnDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsSwitchedReceptOnDelay_Type.__name__ = "Integer32"
_LcUpsSwitchedReceptOnDelay_Object = MibTableColumn
lcUpsSwitchedReceptOnDelay = _LcUpsSwitchedReceptOnDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 12, 2, 1, 2),
    _LcUpsSwitchedReceptOnDelay_Type()
)
lcUpsSwitchedReceptOnDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsSwitchedReceptOnDelay.setStatus("optional")


class _LcUpsSwitchedReceptOnTrapDelay_Type(Integer32):
    """Custom type lcUpsSwitchedReceptOnTrapDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsSwitchedReceptOnTrapDelay_Type.__name__ = "Integer32"
_LcUpsSwitchedReceptOnTrapDelay_Object = MibTableColumn
lcUpsSwitchedReceptOnTrapDelay = _LcUpsSwitchedReceptOnTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 12, 2, 1, 3),
    _LcUpsSwitchedReceptOnTrapDelay_Type()
)
lcUpsSwitchedReceptOnTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsSwitchedReceptOnTrapDelay.setStatus("optional")


class _LcUpsSwitchedReceptOffDelay_Type(Integer32):
    """Custom type lcUpsSwitchedReceptOffDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsSwitchedReceptOffDelay_Type.__name__ = "Integer32"
_LcUpsSwitchedReceptOffDelay_Object = MibTableColumn
lcUpsSwitchedReceptOffDelay = _LcUpsSwitchedReceptOffDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 12, 2, 1, 4),
    _LcUpsSwitchedReceptOffDelay_Type()
)
lcUpsSwitchedReceptOffDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsSwitchedReceptOffDelay.setStatus("optional")


class _LcUpsSwitchedReceptOffTrapDelay_Type(Integer32):
    """Custom type lcUpsSwitchedReceptOffTrapDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_LcUpsSwitchedReceptOffTrapDelay_Type.__name__ = "Integer32"
_LcUpsSwitchedReceptOffTrapDelay_Object = MibTableColumn
lcUpsSwitchedReceptOffTrapDelay = _LcUpsSwitchedReceptOffTrapDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 12, 2, 1, 5),
    _LcUpsSwitchedReceptOffTrapDelay_Type()
)
lcUpsSwitchedReceptOffTrapDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsSwitchedReceptOffTrapDelay.setStatus("optional")


class _LcUpsSwitchedReceptStatus_Type(Integer32):
    """Custom type lcUpsSwitchedReceptStatus based on Integer32"""
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


_LcUpsSwitchedReceptStatus_Type.__name__ = "Integer32"
_LcUpsSwitchedReceptStatus_Object = MibTableColumn
lcUpsSwitchedReceptStatus = _LcUpsSwitchedReceptStatus_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 12, 2, 1, 6),
    _LcUpsSwitchedReceptStatus_Type()
)
lcUpsSwitchedReceptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsSwitchedReceptStatus.setStatus("optional")


class _LcUpsSwitchedReceptLabel_Type(DisplayString):
    """Custom type lcUpsSwitchedReceptLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_LcUpsSwitchedReceptLabel_Type.__name__ = "DisplayString"
_LcUpsSwitchedReceptLabel_Object = MibTableColumn
lcUpsSwitchedReceptLabel = _LcUpsSwitchedReceptLabel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 12, 2, 1, 7),
    _LcUpsSwitchedReceptLabel_Type()
)
lcUpsSwitchedReceptLabel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsSwitchedReceptLabel.setStatus("optional")
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
    (0, "LIEBERT-MIB", "lcUpsBypassLine"),
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


class _LcUpsConfigModuleCount_Type(Integer32):
    """Custom type lcUpsConfigModuleCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_LcUpsConfigModuleCount_Type.__name__ = "Integer32"
_LcUpsConfigModuleCount_Object = MibScalar
lcUpsConfigModuleCount = _LcUpsConfigModuleCount_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 14, 3),
    _LcUpsConfigModuleCount_Type()
)
lcUpsConfigModuleCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lcUpsConfigModuleCount.setStatus("optional")


class _LcUpsConfigCurrentModule_Type(Integer32):
    """Custom type lcUpsConfigCurrentModule based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_LcUpsConfigCurrentModule_Type.__name__ = "Integer32"
_LcUpsConfigCurrentModule_Object = MibScalar
lcUpsConfigCurrentModule = _LcUpsConfigCurrentModule_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 14, 4),
    _LcUpsConfigCurrentModule_Type()
)
lcUpsConfigCurrentModule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsConfigCurrentModule.setStatus("optional")


class _LcUpsConfigAudibleStatus_Type(Integer32):
    """Custom type lcUpsConfigAudibleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("muted", 3))
    )


_LcUpsConfigAudibleStatus_Type.__name__ = "Integer32"
_LcUpsConfigAudibleStatus_Object = MibScalar
lcUpsConfigAudibleStatus = _LcUpsConfigAudibleStatus_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 14, 5),
    _LcUpsConfigAudibleStatus_Type()
)
lcUpsConfigAudibleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsConfigAudibleStatus.setStatus("optional")


class _LcUpsConfigLowBattTime_Type(Integer32):
    """Custom type lcUpsConfigLowBattTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_LcUpsConfigLowBattTime_Type.__name__ = "Integer32"
_LcUpsConfigLowBattTime_Object = MibScalar
lcUpsConfigLowBattTime = _LcUpsConfigLowBattTime_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 14, 6),
    _LcUpsConfigLowBattTime_Type()
)
lcUpsConfigLowBattTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsConfigLowBattTime.setStatus("optional")


class _LcUpsConfigAutoRestart_Type(Integer32):
    """Custom type lcUpsConfigAutoRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 32767),
    )


_LcUpsConfigAutoRestart_Type.__name__ = "Integer32"
_LcUpsConfigAutoRestart_Object = MibScalar
lcUpsConfigAutoRestart = _LcUpsConfigAutoRestart_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 14, 7),
    _LcUpsConfigAutoRestart_Type()
)
lcUpsConfigAutoRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lcUpsConfigAutoRestart.setStatus("optional")
_LuUPStationS_ObjectIdentity = ObjectIdentity
luUPStationS = _LuUPStationS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2)
)
_LsUpsIdent_ObjectIdentity = ObjectIdentity
lsUpsIdent = _LsUpsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 1)
)


class _LsUpsIdentFirmwareVersion_Type(DisplayString):
    """Custom type lsUpsIdentFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_LsUpsIdentFirmwareVersion_Type.__name__ = "DisplayString"
_LsUpsIdentFirmwareVersion_Object = MibScalar
lsUpsIdentFirmwareVersion = _LsUpsIdentFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 1, 1),
    _LsUpsIdentFirmwareVersion_Type()
)
lsUpsIdentFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsUpsIdentFirmwareVersion.setStatus("optional")
_LsUpsAlarm_ObjectIdentity = ObjectIdentity
lsUpsAlarm = _LsUpsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 6)
)
_LsUpsAlarmConditions_ObjectIdentity = ObjectIdentity
lsUpsAlarmConditions = _LsUpsAlarmConditions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 6, 1)
)
_LsUpsAlarmCheckAirFilter_ObjectIdentity = ObjectIdentity
lsUpsAlarmCheckAirFilter = _LsUpsAlarmCheckAirFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 6, 1, 1)
)
_LsUpsTraps_ObjectIdentity = ObjectIdentity
lsUpsTraps = _LsUpsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 11)
)
_LsUpsConfig_ObjectIdentity = ObjectIdentity
lsUpsConfig = _LsUpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 12)
)


class _LsUpsConfigBypassInstalled_Type(Integer32):
    """Custom type lsUpsConfigBypassInstalled based on Integer32"""
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
          ("yes", 2),
          ("no", 3))
    )


_LsUpsConfigBypassInstalled_Type.__name__ = "Integer32"
_LsUpsConfigBypassInstalled_Object = MibScalar
lsUpsConfigBypassInstalled = _LsUpsConfigBypassInstalled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 12, 1),
    _LsUpsConfigBypassInstalled_Type()
)
lsUpsConfigBypassInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsUpsConfigBypassInstalled.setStatus("optional")
_LsUpsBypass_ObjectIdentity = ObjectIdentity
lsUpsBypass = _LsUpsBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 13)
)


class _LsUpsOnBypass_Type(Integer32):
    """Custom type lsUpsOnBypass based on Integer32"""
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
          ("yes", 2),
          ("no", 3))
    )


_LsUpsOnBypass_Type.__name__ = "Integer32"
_LsUpsOnBypass_Object = MibScalar
lsUpsOnBypass = _LsUpsOnBypass_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 13, 1),
    _LsUpsOnBypass_Type()
)
lsUpsOnBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsUpsOnBypass.setStatus("optional")


class _LsUpsBypassFrequency_Type(Integer32):
    """Custom type lsUpsBypassFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LsUpsBypassFrequency_Type.__name__ = "Integer32"
_LsUpsBypassFrequency_Object = MibScalar
lsUpsBypassFrequency = _LsUpsBypassFrequency_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 13, 2),
    _LsUpsBypassFrequency_Type()
)
lsUpsBypassFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsUpsBypassFrequency.setStatus("optional")


class _LsUpsBypassNumLines_Type(Integer32):
    """Custom type lsUpsBypassNumLines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_LsUpsBypassNumLines_Type.__name__ = "Integer32"
_LsUpsBypassNumLines_Object = MibScalar
lsUpsBypassNumLines = _LsUpsBypassNumLines_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 13, 3),
    _LsUpsBypassNumLines_Type()
)
lsUpsBypassNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsUpsBypassNumLines.setStatus("optional")
_LsUpsBypassTable_Object = MibTable
lsUpsBypassTable = _LsUpsBypassTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 13, 4)
)
if mibBuilder.loadTexts:
    lsUpsBypassTable.setStatus("optional")
_LsUpsBypassEntry_Object = MibTableRow
lsUpsBypassEntry = _LsUpsBypassEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 13, 4, 1)
)
lsUpsBypassEntry.setIndexNames(
    (0, "LIEBERT-MIB", "lsUpsBypassLine"),
)
if mibBuilder.loadTexts:
    lsUpsBypassEntry.setStatus("optional")


class _LsUpsBypassLine_Type(Integer32):
    """Custom type lsUpsBypassLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_LsUpsBypassLine_Type.__name__ = "Integer32"
_LsUpsBypassLine_Object = MibTableColumn
lsUpsBypassLine = _LsUpsBypassLine_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 13, 4, 1, 1),
    _LsUpsBypassLine_Type()
)
lsUpsBypassLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsUpsBypassLine.setStatus("optional")


class _LsUpsBypassVoltage_Type(Integer32):
    """Custom type lsUpsBypassVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LsUpsBypassVoltage_Type.__name__ = "Integer32"
_LsUpsBypassVoltage_Object = MibTableColumn
lsUpsBypassVoltage = _LsUpsBypassVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 13, 4, 1, 2),
    _LsUpsBypassVoltage_Type()
)
lsUpsBypassVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsUpsBypassVoltage.setStatus("optional")


class _LsUpsBypassCurrent_Type(Integer32):
    """Custom type lsUpsBypassCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LsUpsBypassCurrent_Type.__name__ = "Integer32"
_LsUpsBypassCurrent_Object = MibTableColumn
lsUpsBypassCurrent = _LsUpsBypassCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 13, 4, 1, 3),
    _LsUpsBypassCurrent_Type()
)
lsUpsBypassCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lsUpsBypassCurrent.setStatus("optional")
_LuUPStationD_ObjectIdentity = ObjectIdentity
luUPStationD = _LuUPStationD_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3)
)
_LdUpsInput_ObjectIdentity = ObjectIdentity
ldUpsInput = _LdUpsInput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 3)
)


class _LdUpsInputMaxVoltsSinceLastPoll_Type(Integer32):
    """Custom type ldUpsInputMaxVoltsSinceLastPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LdUpsInputMaxVoltsSinceLastPoll_Type.__name__ = "Integer32"
_LdUpsInputMaxVoltsSinceLastPoll_Object = MibScalar
ldUpsInputMaxVoltsSinceLastPoll = _LdUpsInputMaxVoltsSinceLastPoll_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 3, 1),
    _LdUpsInputMaxVoltsSinceLastPoll_Type()
)
ldUpsInputMaxVoltsSinceLastPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldUpsInputMaxVoltsSinceLastPoll.setStatus("optional")


class _LdUpsInputMinVoltsSinceLastPoll_Type(Integer32):
    """Custom type ldUpsInputMinVoltsSinceLastPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LdUpsInputMinVoltsSinceLastPoll_Type.__name__ = "Integer32"
_LdUpsInputMinVoltsSinceLastPoll_Object = MibScalar
ldUpsInputMinVoltsSinceLastPoll = _LdUpsInputMinVoltsSinceLastPoll_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 3, 2),
    _LdUpsInputMinVoltsSinceLastPoll_Type()
)
ldUpsInputMinVoltsSinceLastPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldUpsInputMinVoltsSinceLastPoll.setStatus("optional")
_LdUpsOutput_ObjectIdentity = ObjectIdentity
ldUpsOutput = _LdUpsOutput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 4)
)


class _LdUpsOutputMaxVoltsSinceLastPoll_Type(Integer32):
    """Custom type ldUpsOutputMaxVoltsSinceLastPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LdUpsOutputMaxVoltsSinceLastPoll_Type.__name__ = "Integer32"
_LdUpsOutputMaxVoltsSinceLastPoll_Object = MibScalar
ldUpsOutputMaxVoltsSinceLastPoll = _LdUpsOutputMaxVoltsSinceLastPoll_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 4, 1),
    _LdUpsOutputMaxVoltsSinceLastPoll_Type()
)
ldUpsOutputMaxVoltsSinceLastPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldUpsOutputMaxVoltsSinceLastPoll.setStatus("optional")


class _LdUpsOutputMinVoltsSinceLastPoll_Type(Integer32):
    """Custom type ldUpsOutputMinVoltsSinceLastPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LdUpsOutputMinVoltsSinceLastPoll_Type.__name__ = "Integer32"
_LdUpsOutputMinVoltsSinceLastPoll_Object = MibScalar
ldUpsOutputMinVoltsSinceLastPoll = _LdUpsOutputMinVoltsSinceLastPoll_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 4, 2),
    _LdUpsOutputMinVoltsSinceLastPoll_Type()
)
ldUpsOutputMinVoltsSinceLastPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ldUpsOutputMinVoltsSinceLastPoll.setStatus("optional")
_LdUpsAlarm_ObjectIdentity = ObjectIdentity
ldUpsAlarm = _LdUpsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 6)
)
_LdUpsAlarmConditions_ObjectIdentity = ObjectIdentity
ldUpsAlarmConditions = _LdUpsAlarmConditions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 6, 1)
)
_LdUpsAlarmDCOverVoltageShutdown_ObjectIdentity = ObjectIdentity
ldUpsAlarmDCOverVoltageShutdown = _LdUpsAlarmDCOverVoltageShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 6, 1, 1)
)
_LdUpsAlarmOutputShortShutdown_ObjectIdentity = ObjectIdentity
ldUpsAlarmOutputShortShutdown = _LdUpsAlarmOutputShortShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 6, 1, 2)
)
_LdUpsAlarmLNReversedShutdown_ObjectIdentity = ObjectIdentity
ldUpsAlarmLNReversedShutdown = _LdUpsAlarmLNReversedShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 6, 1, 3)
)
_LdUpsAlarmImminentShutdown_ObjectIdentity = ObjectIdentity
ldUpsAlarmImminentShutdown = _LdUpsAlarmImminentShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 6, 1, 4)
)
_LdUpsAlarmInputFreqError_ObjectIdentity = ObjectIdentity
ldUpsAlarmInputFreqError = _LdUpsAlarmInputFreqError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 6, 1, 5)
)
_LdUpsAlarmBoostOn_ObjectIdentity = ObjectIdentity
ldUpsAlarmBoostOn = _LdUpsAlarmBoostOn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 6, 1, 6)
)
_LdUpsAlarmReplaceBattery_ObjectIdentity = ObjectIdentity
ldUpsAlarmReplaceBattery = _LdUpsAlarmReplaceBattery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 6, 1, 7)
)
_LdUpsAlarmOutputOverVoltage_ObjectIdentity = ObjectIdentity
ldUpsAlarmOutputOverVoltage = _LdUpsAlarmOutputOverVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 6, 1, 8)
)
_LdUpsAlarmOutputUnderVoltage_ObjectIdentity = ObjectIdentity
ldUpsAlarmOutputUnderVoltage = _LdUpsAlarmOutputUnderVoltage_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 6, 1, 9)
)
_LdUpsAlarmChargerFailed_ObjectIdentity = ObjectIdentity
ldUpsAlarmChargerFailed = _LdUpsAlarmChargerFailed_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 6, 1, 10)
)
_LdUpsTraps_ObjectIdentity = ObjectIdentity
ldUpsTraps = _LdUpsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 11)
)
_LuUPStationG_ObjectIdentity = ObjectIdentity
luUPStationG = _LuUPStationG_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4)
)
_LgUpsAlarm_ObjectIdentity = ObjectIdentity
lgUpsAlarm = _LgUpsAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 6)
)
_LgUpsAlarmConditions_ObjectIdentity = ObjectIdentity
lgUpsAlarmConditions = _LgUpsAlarmConditions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 6, 1)
)
_LgUpsAlarmDCOverVoltageShutdown_ObjectIdentity = ObjectIdentity
lgUpsAlarmDCOverVoltageShutdown = _LgUpsAlarmDCOverVoltageShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 6, 1, 1)
)
_LgUpsAlarmOutputShortShutdown_ObjectIdentity = ObjectIdentity
lgUpsAlarmOutputShortShutdown = _LgUpsAlarmOutputShortShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 6, 1, 2)
)
_LgUpsAlarmLNReversedShutdown_ObjectIdentity = ObjectIdentity
lgUpsAlarmLNReversedShutdown = _LgUpsAlarmLNReversedShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 6, 1, 3)
)
_LgUpsAlarmRemoteShutdown_ObjectIdentity = ObjectIdentity
lgUpsAlarmRemoteShutdown = _LgUpsAlarmRemoteShutdown_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 6, 1, 4)
)
_LgUpsAlarmInputUVOnStartup_ObjectIdentity = ObjectIdentity
lgUpsAlarmInputUVOnStartup = _LgUpsAlarmInputUVOnStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 6, 1, 5)
)
_LgUpsAlarmPFCFailedOnStartup_ObjectIdentity = ObjectIdentity
lgUpsAlarmPFCFailedOnStartup = _LgUpsAlarmPFCFailedOnStartup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 6, 1, 6)
)
_LgUpsTraps_ObjectIdentity = ObjectIdentity
lgUpsTraps = _LgUpsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 11)
)
_LuSeries300_ObjectIdentity = ObjectIdentity
luSeries300 = _LuSeries300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 5)
)
_LuExternal_ObjectIdentity = ObjectIdentity
luExternal = _LuExternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 6)
)
_LuUPStationS3_ObjectIdentity = ObjectIdentity
luUPStationS3 = _LuUPStationS3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 7)
)
_LuSeries200_ObjectIdentity = ObjectIdentity
luSeries200 = _LuSeries200_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8)
)
_LuSeries200Input_ObjectIdentity = ObjectIdentity
luSeries200Input = _LuSeries200Input_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 3)
)


class _LuSeries200InputMaxVoltsSinceLastPoll_Type(Integer32):
    """Custom type luSeries200InputMaxVoltsSinceLastPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LuSeries200InputMaxVoltsSinceLastPoll_Type.__name__ = "Integer32"
_LuSeries200InputMaxVoltsSinceLastPoll_Object = MibScalar
luSeries200InputMaxVoltsSinceLastPoll = _LuSeries200InputMaxVoltsSinceLastPoll_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 3, 1),
    _LuSeries200InputMaxVoltsSinceLastPoll_Type()
)
luSeries200InputMaxVoltsSinceLastPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luSeries200InputMaxVoltsSinceLastPoll.setStatus("optional")


class _LuSeries200InputMinVoltsSinceLastPoll_Type(Integer32):
    """Custom type luSeries200InputMinVoltsSinceLastPoll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_LuSeries200InputMinVoltsSinceLastPoll_Type.__name__ = "Integer32"
_LuSeries200InputMinVoltsSinceLastPoll_Object = MibScalar
luSeries200InputMinVoltsSinceLastPoll = _LuSeries200InputMinVoltsSinceLastPoll_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 3, 2),
    _LuSeries200InputMinVoltsSinceLastPoll_Type()
)
luSeries200InputMinVoltsSinceLastPoll.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luSeries200InputMinVoltsSinceLastPoll.setStatus("optional")
_LuSeries200Alarm_ObjectIdentity = ObjectIdentity
luSeries200Alarm = _LuSeries200Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 6)
)
_LuSeries200AlarmConditions_ObjectIdentity = ObjectIdentity
luSeries200AlarmConditions = _LuSeries200AlarmConditions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 6, 1)
)
_LuSeries200AlarmInputFreqError_ObjectIdentity = ObjectIdentity
luSeries200AlarmInputFreqError = _LuSeries200AlarmInputFreqError_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 6, 1, 1)
)
_LuSeries200Config_ObjectIdentity = ObjectIdentity
luSeries200Config = _LuSeries200Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 12)
)


class _LuSeries200ConfigBypassInstalled_Type(Integer32):
    """Custom type luSeries200ConfigBypassInstalled based on Integer32"""
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
          ("yes", 2),
          ("no", 3))
    )


_LuSeries200ConfigBypassInstalled_Type.__name__ = "Integer32"
_LuSeries200ConfigBypassInstalled_Object = MibScalar
luSeries200ConfigBypassInstalled = _LuSeries200ConfigBypassInstalled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 12, 1),
    _LuSeries200ConfigBypassInstalled_Type()
)
luSeries200ConfigBypassInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luSeries200ConfigBypassInstalled.setStatus("optional")


class _LuSeries200ConfigFrequencyChangerModel_Type(Integer32):
    """Custom type luSeries200ConfigFrequencyChangerModel based on Integer32"""
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
          ("yes", 2),
          ("no", 3))
    )


_LuSeries200ConfigFrequencyChangerModel_Type.__name__ = "Integer32"
_LuSeries200ConfigFrequencyChangerModel_Object = MibScalar
luSeries200ConfigFrequencyChangerModel = _LuSeries200ConfigFrequencyChangerModel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 12, 2),
    _LuSeries200ConfigFrequencyChangerModel_Type()
)
luSeries200ConfigFrequencyChangerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luSeries200ConfigFrequencyChangerModel.setStatus("optional")
_LuSeries200Bypass_ObjectIdentity = ObjectIdentity
luSeries200Bypass = _LuSeries200Bypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 13)
)


class _LuSeries200OnBypass_Type(Integer32):
    """Custom type luSeries200OnBypass based on Integer32"""
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
          ("yes", 2),
          ("no", 3))
    )


_LuSeries200OnBypass_Type.__name__ = "Integer32"
_LuSeries200OnBypass_Object = MibScalar
luSeries200OnBypass = _LuSeries200OnBypass_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 8, 13, 1),
    _LuSeries200OnBypass_Type()
)
luSeries200OnBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    luSeries200OnBypass.setStatus("optional")
_LuSeries4300_ObjectIdentity = ObjectIdentity
luSeries4300 = _LuSeries4300_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10)
)
_Ls43cUpsIdent_ObjectIdentity = ObjectIdentity
ls43cUpsIdent = _Ls43cUpsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10, 1)
)


class _Ls43cUpsIdentFirmwareVersion_Type(DisplayString):
    """Custom type ls43cUpsIdentFirmwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )
    fixed_length = 255


_Ls43cUpsIdentFirmwareVersion_Type.__name__ = "DisplayString"
_Ls43cUpsIdentFirmwareVersion_Object = MibScalar
ls43cUpsIdentFirmwareVersion = _Ls43cUpsIdentFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10, 1, 1),
    _Ls43cUpsIdentFirmwareVersion_Type()
)
ls43cUpsIdentFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls43cUpsIdentFirmwareVersion.setStatus("optional")
_Ls43cUpsConfig_ObjectIdentity = ObjectIdentity
ls43cUpsConfig = _Ls43cUpsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10, 12)
)


class _Ls43cUpsConfigBypassInstalled_Type(Integer32):
    """Custom type ls43cUpsConfigBypassInstalled based on Integer32"""
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
          ("yes", 2),
          ("no", 3))
    )


_Ls43cUpsConfigBypassInstalled_Type.__name__ = "Integer32"
_Ls43cUpsConfigBypassInstalled_Object = MibScalar
ls43cUpsConfigBypassInstalled = _Ls43cUpsConfigBypassInstalled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10, 12, 1),
    _Ls43cUpsConfigBypassInstalled_Type()
)
ls43cUpsConfigBypassInstalled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls43cUpsConfigBypassInstalled.setStatus("optional")
_Ls43cUpsBypass_ObjectIdentity = ObjectIdentity
ls43cUpsBypass = _Ls43cUpsBypass_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10, 13)
)


class _Ls43cUpsOnBypass_Type(Integer32):
    """Custom type ls43cUpsOnBypass based on Integer32"""
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
          ("yes", 2),
          ("no", 3))
    )


_Ls43cUpsOnBypass_Type.__name__ = "Integer32"
_Ls43cUpsOnBypass_Object = MibScalar
ls43cUpsOnBypass = _Ls43cUpsOnBypass_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10, 13, 1),
    _Ls43cUpsOnBypass_Type()
)
ls43cUpsOnBypass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls43cUpsOnBypass.setStatus("optional")


class _Ls43cUpsBypassFrequency_Type(Integer32):
    """Custom type ls43cUpsBypassFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Ls43cUpsBypassFrequency_Type.__name__ = "Integer32"
_Ls43cUpsBypassFrequency_Object = MibScalar
ls43cUpsBypassFrequency = _Ls43cUpsBypassFrequency_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10, 13, 2),
    _Ls43cUpsBypassFrequency_Type()
)
ls43cUpsBypassFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls43cUpsBypassFrequency.setStatus("optional")


class _Ls43cUpsBypassNumLines_Type(Integer32):
    """Custom type ls43cUpsBypassNumLines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Ls43cUpsBypassNumLines_Type.__name__ = "Integer32"
_Ls43cUpsBypassNumLines_Object = MibScalar
ls43cUpsBypassNumLines = _Ls43cUpsBypassNumLines_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10, 13, 3),
    _Ls43cUpsBypassNumLines_Type()
)
ls43cUpsBypassNumLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls43cUpsBypassNumLines.setStatus("optional")
_Ls43cUpsBypassTable_Object = MibTable
ls43cUpsBypassTable = _Ls43cUpsBypassTable_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10, 13, 4)
)
if mibBuilder.loadTexts:
    ls43cUpsBypassTable.setStatus("optional")
_Ls43cUpsBypassEntry_Object = MibTableRow
ls43cUpsBypassEntry = _Ls43cUpsBypassEntry_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10, 13, 4, 1)
)
ls43cUpsBypassEntry.setIndexNames(
    (0, "LIEBERT-MIB", "ls43cUpsBypassLine"),
)
if mibBuilder.loadTexts:
    ls43cUpsBypassEntry.setStatus("optional")


class _Ls43cUpsBypassLine_Type(Integer32):
    """Custom type ls43cUpsBypassLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Ls43cUpsBypassLine_Type.__name__ = "Integer32"
_Ls43cUpsBypassLine_Object = MibTableColumn
ls43cUpsBypassLine = _Ls43cUpsBypassLine_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10, 13, 4, 1, 1),
    _Ls43cUpsBypassLine_Type()
)
ls43cUpsBypassLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls43cUpsBypassLine.setStatus("optional")


class _Ls43cUpsBypassVoltage_Type(Integer32):
    """Custom type ls43cUpsBypassVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Ls43cUpsBypassVoltage_Type.__name__ = "Integer32"
_Ls43cUpsBypassVoltage_Object = MibTableColumn
ls43cUpsBypassVoltage = _Ls43cUpsBypassVoltage_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10, 13, 4, 1, 2),
    _Ls43cUpsBypassVoltage_Type()
)
ls43cUpsBypassVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls43cUpsBypassVoltage.setStatus("optional")


class _Ls43cUpsBypassCurrent_Type(Integer32):
    """Custom type ls43cUpsBypassCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_Ls43cUpsBypassCurrent_Type.__name__ = "Integer32"
_Ls43cUpsBypassCurrent_Object = MibTableColumn
ls43cUpsBypassCurrent = _Ls43cUpsBypassCurrent_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 10, 13, 4, 1, 3),
    _Ls43cUpsBypassCurrent_Type()
)
ls43cUpsBypassCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ls43cUpsBypassCurrent.setStatus("optional")
_LuUpsModule_ObjectIdentity = ObjectIdentity
luUpsModule = _LuUpsModule_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 11)
)
_LuSystemCabinet_ObjectIdentity = ObjectIdentity
luSystemCabinet = _LuSystemCabinet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 12)
)
_LuUPStationGxt_ObjectIdentity = ObjectIdentity
luUPStationGxt = _LuUPStationGxt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 14)
)
_LuPowerSure_ObjectIdentity = ObjectIdentity
luPowerSure = _LuPowerSure_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 15)
)
_LuExperimental_ObjectIdentity = ObjectIdentity
luExperimental = _LuExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 2)
)
_LuPrivate_ObjectIdentity = ObjectIdentity
luPrivate = _LuPrivate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 3)
)
_LiebertEnvironment_ObjectIdentity = ObjectIdentity
liebertEnvironment = _LiebertEnvironment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2)
)
_LeExtensions_ObjectIdentity = ObjectIdentity
leExtensions = _LeExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1)
)
_LeSiteNet01_ObjectIdentity = ObjectIdentity
leSiteNet01 = _LeSiteNet01_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1)
)
_EnvMIB_ObjectIdentity = ObjectIdentity
envMIB = _EnvMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1)
)
_EnvIdent_ObjectIdentity = ObjectIdentity
envIdent = _EnvIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 1)
)
_EnvIdentManufacturer_Type = DisplayString
_EnvIdentManufacturer_Object = MibScalar
envIdentManufacturer = _EnvIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 1, 1),
    _EnvIdentManufacturer_Type()
)
envIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envIdentManufacturer.setStatus("mandatory")
_EnvIdentModel_Type = DisplayString
_EnvIdentModel_Object = MibScalar
envIdentModel = _EnvIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 1, 2),
    _EnvIdentModel_Type()
)
envIdentModel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envIdentModel.setStatus("mandatory")
_EnvIdentSoftwareVersion_Type = DisplayString
_EnvIdentSoftwareVersion_Object = MibScalar
envIdentSoftwareVersion = _EnvIdentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 1, 3),
    _EnvIdentSoftwareVersion_Type()
)
envIdentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envIdentSoftwareVersion.setStatus("mandatory")
_EnvIdentSpecific_Type = ObjectIdentifier
_EnvIdentSpecific_Object = MibScalar
envIdentSpecific = _EnvIdentSpecific_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 1, 4),
    _EnvIdentSpecific_Type()
)
envIdentSpecific.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envIdentSpecific.setStatus("mandatory")
_EnvDigitalInputs_ObjectIdentity = ObjectIdentity
envDigitalInputs = _EnvDigitalInputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2)
)
_EnvDigInput1_ObjectIdentity = ObjectIdentity
envDigInput1 = _EnvDigInput1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 1)
)


class _EnvDigInput1State_Type(Integer32):
    """Custom type envDigInput1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("notInstalled", 3))
    )


_EnvDigInput1State_Type.__name__ = "Integer32"
_EnvDigInput1State_Object = MibScalar
envDigInput1State = _EnvDigInput1State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 1, 1),
    _EnvDigInput1State_Type()
)
envDigInput1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envDigInput1State.setStatus("mandatory")
_EnvDigInput1Label_Type = DisplayString
_EnvDigInput1Label_Object = MibScalar
envDigInput1Label = _EnvDigInput1Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 1, 2),
    _EnvDigInput1Label_Type()
)
envDigInput1Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput1Label.setStatus("mandatory")


class _EnvDigInput1Polarity_Type(Integer32):
    """Custom type envDigInput1Polarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeHigh", 1),
          ("activeLow", 2),
          ("notDefined", 3))
    )


_EnvDigInput1Polarity_Type.__name__ = "Integer32"
_EnvDigInput1Polarity_Object = MibScalar
envDigInput1Polarity = _EnvDigInput1Polarity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 1, 3),
    _EnvDigInput1Polarity_Type()
)
envDigInput1Polarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput1Polarity.setStatus("mandatory")
_EnvDigInput1TrapEnabled_Type = TruthValue
_EnvDigInput1TrapEnabled_Object = MibScalar
envDigInput1TrapEnabled = _EnvDigInput1TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 1, 4),
    _EnvDigInput1TrapEnabled_Type()
)
envDigInput1TrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput1TrapEnabled.setStatus("mandatory")
_EnvDigInput2_ObjectIdentity = ObjectIdentity
envDigInput2 = _EnvDigInput2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 2)
)


class _EnvDigInput2State_Type(Integer32):
    """Custom type envDigInput2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("notInstalled", 3))
    )


_EnvDigInput2State_Type.__name__ = "Integer32"
_EnvDigInput2State_Object = MibScalar
envDigInput2State = _EnvDigInput2State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 2, 1),
    _EnvDigInput2State_Type()
)
envDigInput2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envDigInput2State.setStatus("mandatory")
_EnvDigInput2Label_Type = DisplayString
_EnvDigInput2Label_Object = MibScalar
envDigInput2Label = _EnvDigInput2Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 2, 2),
    _EnvDigInput2Label_Type()
)
envDigInput2Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput2Label.setStatus("mandatory")


class _EnvDigInput2Polarity_Type(Integer32):
    """Custom type envDigInput2Polarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeHigh", 1),
          ("activeLow", 2),
          ("notDefined", 3))
    )


_EnvDigInput2Polarity_Type.__name__ = "Integer32"
_EnvDigInput2Polarity_Object = MibScalar
envDigInput2Polarity = _EnvDigInput2Polarity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 2, 3),
    _EnvDigInput2Polarity_Type()
)
envDigInput2Polarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput2Polarity.setStatus("mandatory")
_EnvDigInput2TrapEnabled_Type = TruthValue
_EnvDigInput2TrapEnabled_Object = MibScalar
envDigInput2TrapEnabled = _EnvDigInput2TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 2, 4),
    _EnvDigInput2TrapEnabled_Type()
)
envDigInput2TrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput2TrapEnabled.setStatus("mandatory")
_EnvDigInput3_ObjectIdentity = ObjectIdentity
envDigInput3 = _EnvDigInput3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 3)
)


class _EnvDigInput3State_Type(Integer32):
    """Custom type envDigInput3State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("notInstalled", 3))
    )


_EnvDigInput3State_Type.__name__ = "Integer32"
_EnvDigInput3State_Object = MibScalar
envDigInput3State = _EnvDigInput3State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 3, 1),
    _EnvDigInput3State_Type()
)
envDigInput3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envDigInput3State.setStatus("mandatory")
_EnvDigInput3Label_Type = DisplayString
_EnvDigInput3Label_Object = MibScalar
envDigInput3Label = _EnvDigInput3Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 3, 2),
    _EnvDigInput3Label_Type()
)
envDigInput3Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput3Label.setStatus("mandatory")


class _EnvDigInput3Polarity_Type(Integer32):
    """Custom type envDigInput3Polarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeHigh", 1),
          ("activeLow", 2),
          ("notDefined", 3))
    )


_EnvDigInput3Polarity_Type.__name__ = "Integer32"
_EnvDigInput3Polarity_Object = MibScalar
envDigInput3Polarity = _EnvDigInput3Polarity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 3, 3),
    _EnvDigInput3Polarity_Type()
)
envDigInput3Polarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput3Polarity.setStatus("mandatory")
_EnvDigInput3TrapEnabled_Type = TruthValue
_EnvDigInput3TrapEnabled_Object = MibScalar
envDigInput3TrapEnabled = _EnvDigInput3TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 3, 4),
    _EnvDigInput3TrapEnabled_Type()
)
envDigInput3TrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput3TrapEnabled.setStatus("mandatory")
_EnvDigInput4_ObjectIdentity = ObjectIdentity
envDigInput4 = _EnvDigInput4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 4)
)


class _EnvDigInput4State_Type(Integer32):
    """Custom type envDigInput4State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("notInstalled", 3))
    )


_EnvDigInput4State_Type.__name__ = "Integer32"
_EnvDigInput4State_Object = MibScalar
envDigInput4State = _EnvDigInput4State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 4, 1),
    _EnvDigInput4State_Type()
)
envDigInput4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envDigInput4State.setStatus("mandatory")
_EnvDigInput4Label_Type = DisplayString
_EnvDigInput4Label_Object = MibScalar
envDigInput4Label = _EnvDigInput4Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 4, 2),
    _EnvDigInput4Label_Type()
)
envDigInput4Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput4Label.setStatus("mandatory")


class _EnvDigInput4Polarity_Type(Integer32):
    """Custom type envDigInput4Polarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeHigh", 1),
          ("activeLow", 2),
          ("notDefined", 3))
    )


_EnvDigInput4Polarity_Type.__name__ = "Integer32"
_EnvDigInput4Polarity_Object = MibScalar
envDigInput4Polarity = _EnvDigInput4Polarity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 4, 3),
    _EnvDigInput4Polarity_Type()
)
envDigInput4Polarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput4Polarity.setStatus("mandatory")
_EnvDigInput4TrapEnabled_Type = TruthValue
_EnvDigInput4TrapEnabled_Object = MibScalar
envDigInput4TrapEnabled = _EnvDigInput4TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 4, 4),
    _EnvDigInput4TrapEnabled_Type()
)
envDigInput4TrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput4TrapEnabled.setStatus("mandatory")
_EnvDigInput5_ObjectIdentity = ObjectIdentity
envDigInput5 = _EnvDigInput5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 5)
)


class _EnvDigInput5State_Type(Integer32):
    """Custom type envDigInput5State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("notInstalled", 3))
    )


_EnvDigInput5State_Type.__name__ = "Integer32"
_EnvDigInput5State_Object = MibScalar
envDigInput5State = _EnvDigInput5State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 5, 1),
    _EnvDigInput5State_Type()
)
envDigInput5State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envDigInput5State.setStatus("mandatory")
_EnvDigInput5Label_Type = DisplayString
_EnvDigInput5Label_Object = MibScalar
envDigInput5Label = _EnvDigInput5Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 5, 2),
    _EnvDigInput5Label_Type()
)
envDigInput5Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput5Label.setStatus("mandatory")


class _EnvDigInput5Polarity_Type(Integer32):
    """Custom type envDigInput5Polarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeHigh", 1),
          ("activeLow", 2),
          ("notDefined", 3))
    )


_EnvDigInput5Polarity_Type.__name__ = "Integer32"
_EnvDigInput5Polarity_Object = MibScalar
envDigInput5Polarity = _EnvDigInput5Polarity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 5, 3),
    _EnvDigInput5Polarity_Type()
)
envDigInput5Polarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput5Polarity.setStatus("mandatory")
_EnvDigInput5TrapEnabled_Type = TruthValue
_EnvDigInput5TrapEnabled_Object = MibScalar
envDigInput5TrapEnabled = _EnvDigInput5TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 5, 4),
    _EnvDigInput5TrapEnabled_Type()
)
envDigInput5TrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput5TrapEnabled.setStatus("mandatory")
_EnvDigInput6_ObjectIdentity = ObjectIdentity
envDigInput6 = _EnvDigInput6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 6)
)


class _EnvDigInput6State_Type(Integer32):
    """Custom type envDigInput6State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("notInstalled", 3))
    )


_EnvDigInput6State_Type.__name__ = "Integer32"
_EnvDigInput6State_Object = MibScalar
envDigInput6State = _EnvDigInput6State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 6, 1),
    _EnvDigInput6State_Type()
)
envDigInput6State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envDigInput6State.setStatus("mandatory")
_EnvDigInput6Label_Type = DisplayString
_EnvDigInput6Label_Object = MibScalar
envDigInput6Label = _EnvDigInput6Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 6, 2),
    _EnvDigInput6Label_Type()
)
envDigInput6Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput6Label.setStatus("mandatory")


class _EnvDigInput6Polarity_Type(Integer32):
    """Custom type envDigInput6Polarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeHigh", 1),
          ("activeLow", 2),
          ("notDefined", 3))
    )


_EnvDigInput6Polarity_Type.__name__ = "Integer32"
_EnvDigInput6Polarity_Object = MibScalar
envDigInput6Polarity = _EnvDigInput6Polarity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 6, 3),
    _EnvDigInput6Polarity_Type()
)
envDigInput6Polarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput6Polarity.setStatus("mandatory")
_EnvDigInput6TrapEnabled_Type = TruthValue
_EnvDigInput6TrapEnabled_Object = MibScalar
envDigInput6TrapEnabled = _EnvDigInput6TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 6, 4),
    _EnvDigInput6TrapEnabled_Type()
)
envDigInput6TrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput6TrapEnabled.setStatus("mandatory")
_EnvDigInput7_ObjectIdentity = ObjectIdentity
envDigInput7 = _EnvDigInput7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 7)
)


class _EnvDigInput7State_Type(Integer32):
    """Custom type envDigInput7State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("notInstalled", 3))
    )


_EnvDigInput7State_Type.__name__ = "Integer32"
_EnvDigInput7State_Object = MibScalar
envDigInput7State = _EnvDigInput7State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 7, 1),
    _EnvDigInput7State_Type()
)
envDigInput7State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envDigInput7State.setStatus("mandatory")
_EnvDigInput7Label_Type = DisplayString
_EnvDigInput7Label_Object = MibScalar
envDigInput7Label = _EnvDigInput7Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 7, 2),
    _EnvDigInput7Label_Type()
)
envDigInput7Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput7Label.setStatus("mandatory")


class _EnvDigInput7Polarity_Type(Integer32):
    """Custom type envDigInput7Polarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeHigh", 1),
          ("activeLow", 2),
          ("notDefined", 3))
    )


_EnvDigInput7Polarity_Type.__name__ = "Integer32"
_EnvDigInput7Polarity_Object = MibScalar
envDigInput7Polarity = _EnvDigInput7Polarity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 7, 3),
    _EnvDigInput7Polarity_Type()
)
envDigInput7Polarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput7Polarity.setStatus("mandatory")
_EnvDigInput7TrapEnabled_Type = TruthValue
_EnvDigInput7TrapEnabled_Object = MibScalar
envDigInput7TrapEnabled = _EnvDigInput7TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 7, 4),
    _EnvDigInput7TrapEnabled_Type()
)
envDigInput7TrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput7TrapEnabled.setStatus("mandatory")
_EnvDigInput8_ObjectIdentity = ObjectIdentity
envDigInput8 = _EnvDigInput8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 8)
)


class _EnvDigInput8State_Type(Integer32):
    """Custom type envDigInput8State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("notInstalled", 3))
    )


_EnvDigInput8State_Type.__name__ = "Integer32"
_EnvDigInput8State_Object = MibScalar
envDigInput8State = _EnvDigInput8State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 8, 1),
    _EnvDigInput8State_Type()
)
envDigInput8State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envDigInput8State.setStatus("mandatory")
_EnvDigInput8Label_Type = DisplayString
_EnvDigInput8Label_Object = MibScalar
envDigInput8Label = _EnvDigInput8Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 8, 2),
    _EnvDigInput8Label_Type()
)
envDigInput8Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput8Label.setStatus("mandatory")


class _EnvDigInput8Polarity_Type(Integer32):
    """Custom type envDigInput8Polarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeHigh", 1),
          ("activeLow", 2),
          ("notDefined", 3))
    )


_EnvDigInput8Polarity_Type.__name__ = "Integer32"
_EnvDigInput8Polarity_Object = MibScalar
envDigInput8Polarity = _EnvDigInput8Polarity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 8, 3),
    _EnvDigInput8Polarity_Type()
)
envDigInput8Polarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput8Polarity.setStatus("mandatory")
_EnvDigInput8TrapEnabled_Type = TruthValue
_EnvDigInput8TrapEnabled_Object = MibScalar
envDigInput8TrapEnabled = _EnvDigInput8TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 8, 4),
    _EnvDigInput8TrapEnabled_Type()
)
envDigInput8TrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput8TrapEnabled.setStatus("mandatory")
_EnvDigInput9_ObjectIdentity = ObjectIdentity
envDigInput9 = _EnvDigInput9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 9)
)


class _EnvDigInput9State_Type(Integer32):
    """Custom type envDigInput9State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("notInstalled", 3))
    )


_EnvDigInput9State_Type.__name__ = "Integer32"
_EnvDigInput9State_Object = MibScalar
envDigInput9State = _EnvDigInput9State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 9, 1),
    _EnvDigInput9State_Type()
)
envDigInput9State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envDigInput9State.setStatus("mandatory")
_EnvDigInput9Label_Type = DisplayString
_EnvDigInput9Label_Object = MibScalar
envDigInput9Label = _EnvDigInput9Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 9, 2),
    _EnvDigInput9Label_Type()
)
envDigInput9Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput9Label.setStatus("mandatory")


class _EnvDigInput9Polarity_Type(Integer32):
    """Custom type envDigInput9Polarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeHigh", 1),
          ("activeLow", 2),
          ("notDefined", 3))
    )


_EnvDigInput9Polarity_Type.__name__ = "Integer32"
_EnvDigInput9Polarity_Object = MibScalar
envDigInput9Polarity = _EnvDigInput9Polarity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 9, 3),
    _EnvDigInput9Polarity_Type()
)
envDigInput9Polarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput9Polarity.setStatus("mandatory")
_EnvDigInput9TrapEnabled_Type = TruthValue
_EnvDigInput9TrapEnabled_Object = MibScalar
envDigInput9TrapEnabled = _EnvDigInput9TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 9, 4),
    _EnvDigInput9TrapEnabled_Type()
)
envDigInput9TrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput9TrapEnabled.setStatus("mandatory")
_EnvDigInput10_ObjectIdentity = ObjectIdentity
envDigInput10 = _EnvDigInput10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 10)
)


class _EnvDigInput10State_Type(Integer32):
    """Custom type envDigInput10State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("notInstalled", 3))
    )


_EnvDigInput10State_Type.__name__ = "Integer32"
_EnvDigInput10State_Object = MibScalar
envDigInput10State = _EnvDigInput10State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 10, 1),
    _EnvDigInput10State_Type()
)
envDigInput10State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envDigInput10State.setStatus("mandatory")
_EnvDigInput10Label_Type = DisplayString
_EnvDigInput10Label_Object = MibScalar
envDigInput10Label = _EnvDigInput10Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 10, 2),
    _EnvDigInput10Label_Type()
)
envDigInput10Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput10Label.setStatus("mandatory")


class _EnvDigInput10Polarity_Type(Integer32):
    """Custom type envDigInput10Polarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("activeHigh", 1),
          ("activeLow", 2),
          ("notDefined", 3))
    )


_EnvDigInput10Polarity_Type.__name__ = "Integer32"
_EnvDigInput10Polarity_Object = MibScalar
envDigInput10Polarity = _EnvDigInput10Polarity_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 10, 3),
    _EnvDigInput10Polarity_Type()
)
envDigInput10Polarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput10Polarity.setStatus("mandatory")
_EnvDigInput10TrapEnabled_Type = TruthValue
_EnvDigInput10TrapEnabled_Object = MibScalar
envDigInput10TrapEnabled = _EnvDigInput10TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 2, 10, 4),
    _EnvDigInput10TrapEnabled_Type()
)
envDigInput10TrapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envDigInput10TrapEnabled.setStatus("mandatory")
_EnvRelays_ObjectIdentity = ObjectIdentity
envRelays = _EnvRelays_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 3)
)
_EnvRelay1_ObjectIdentity = ObjectIdentity
envRelay1 = _EnvRelay1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 3, 1)
)


class _EnvRelay1State_Type(Integer32):
    """Custom type envRelay1State based on Integer32"""
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


_EnvRelay1State_Type.__name__ = "Integer32"
_EnvRelay1State_Object = MibScalar
envRelay1State = _EnvRelay1State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 3, 1, 1),
    _EnvRelay1State_Type()
)
envRelay1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envRelay1State.setStatus("mandatory")
_EnvRelay1Label_Type = DisplayString
_EnvRelay1Label_Object = MibScalar
envRelay1Label = _EnvRelay1Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 3, 1, 2),
    _EnvRelay1Label_Type()
)
envRelay1Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envRelay1Label.setStatus("mandatory")


class _EnvRelay1Control_Type(Integer32):
    """Custom type envRelay1Control based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvRelay1Control_Type.__name__ = "Integer32"
_EnvRelay1Control_Object = MibScalar
envRelay1Control = _EnvRelay1Control_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 3, 1, 3),
    _EnvRelay1Control_Type()
)
envRelay1Control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envRelay1Control.setStatus("mandatory")
_EnvRelay2_ObjectIdentity = ObjectIdentity
envRelay2 = _EnvRelay2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 3, 2)
)


class _EnvRelay2State_Type(Integer32):
    """Custom type envRelay2State based on Integer32"""
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


_EnvRelay2State_Type.__name__ = "Integer32"
_EnvRelay2State_Object = MibScalar
envRelay2State = _EnvRelay2State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 3, 2, 1),
    _EnvRelay2State_Type()
)
envRelay2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envRelay2State.setStatus("mandatory")
_EnvRelay2Label_Type = DisplayString
_EnvRelay2Label_Object = MibScalar
envRelay2Label = _EnvRelay2Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 3, 2, 2),
    _EnvRelay2Label_Type()
)
envRelay2Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envRelay2Label.setStatus("mandatory")


class _EnvRelay2Control_Type(Integer32):
    """Custom type envRelay2Control based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvRelay2Control_Type.__name__ = "Integer32"
_EnvRelay2Control_Object = MibScalar
envRelay2Control = _EnvRelay2Control_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 3, 2, 3),
    _EnvRelay2Control_Type()
)
envRelay2Control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envRelay2Control.setStatus("mandatory")
_EnvOutputs_ObjectIdentity = ObjectIdentity
envOutputs = _EnvOutputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4)
)
_EnvAudible_ObjectIdentity = ObjectIdentity
envAudible = _EnvAudible_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 1)
)


class _EnvAudibleState_Type(Integer32):
    """Custom type envAudibleState based on Integer32"""
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


_EnvAudibleState_Type.__name__ = "Integer32"
_EnvAudibleState_Object = MibScalar
envAudibleState = _EnvAudibleState_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 1, 1),
    _EnvAudibleState_Type()
)
envAudibleState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envAudibleState.setStatus("mandatory")


class _EnvAudibleControl_Type(Integer32):
    """Custom type envAudibleControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvAudibleControl_Type.__name__ = "Integer32"
_EnvAudibleControl_Object = MibScalar
envAudibleControl = _EnvAudibleControl_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 1, 2),
    _EnvAudibleControl_Type()
)
envAudibleControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envAudibleControl.setStatus("mandatory")
_EnvLED1_ObjectIdentity = ObjectIdentity
envLED1 = _EnvLED1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 2)
)


class _EnvLED1State_Type(Integer32):
    """Custom type envLED1State based on Integer32"""
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


_EnvLED1State_Type.__name__ = "Integer32"
_EnvLED1State_Object = MibScalar
envLED1State = _EnvLED1State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 2, 1),
    _EnvLED1State_Type()
)
envLED1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envLED1State.setStatus("mandatory")
_EnvLED1Label_Type = DisplayString
_EnvLED1Label_Object = MibScalar
envLED1Label = _EnvLED1Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 2, 2),
    _EnvLED1Label_Type()
)
envLED1Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envLED1Label.setStatus("mandatory")


class _EnvLED1Control_Type(Integer32):
    """Custom type envLED1Control based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvLED1Control_Type.__name__ = "Integer32"
_EnvLED1Control_Object = MibScalar
envLED1Control = _EnvLED1Control_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 2, 3),
    _EnvLED1Control_Type()
)
envLED1Control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envLED1Control.setStatus("mandatory")
_EnvLED2_ObjectIdentity = ObjectIdentity
envLED2 = _EnvLED2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 3)
)


class _EnvLED2State_Type(Integer32):
    """Custom type envLED2State based on Integer32"""
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


_EnvLED2State_Type.__name__ = "Integer32"
_EnvLED2State_Object = MibScalar
envLED2State = _EnvLED2State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 3, 1),
    _EnvLED2State_Type()
)
envLED2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envLED2State.setStatus("mandatory")
_EnvLED2Label_Type = DisplayString
_EnvLED2Label_Object = MibScalar
envLED2Label = _EnvLED2Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 3, 2),
    _EnvLED2Label_Type()
)
envLED2Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envLED2Label.setStatus("mandatory")


class _EnvLED2Control_Type(Integer32):
    """Custom type envLED2Control based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvLED2Control_Type.__name__ = "Integer32"
_EnvLED2Control_Object = MibScalar
envLED2Control = _EnvLED2Control_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 3, 3),
    _EnvLED2Control_Type()
)
envLED2Control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envLED2Control.setStatus("mandatory")
_EnvLED3_ObjectIdentity = ObjectIdentity
envLED3 = _EnvLED3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 4)
)


class _EnvLED3State_Type(Integer32):
    """Custom type envLED3State based on Integer32"""
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


_EnvLED3State_Type.__name__ = "Integer32"
_EnvLED3State_Object = MibScalar
envLED3State = _EnvLED3State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 4, 1),
    _EnvLED3State_Type()
)
envLED3State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envLED3State.setStatus("mandatory")
_EnvLED3Label_Type = DisplayString
_EnvLED3Label_Object = MibScalar
envLED3Label = _EnvLED3Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 4, 2),
    _EnvLED3Label_Type()
)
envLED3Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envLED3Label.setStatus("mandatory")


class _EnvLED3Control_Type(Integer32):
    """Custom type envLED3Control based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvLED3Control_Type.__name__ = "Integer32"
_EnvLED3Control_Object = MibScalar
envLED3Control = _EnvLED3Control_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 4, 4, 3),
    _EnvLED3Control_Type()
)
envLED3Control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envLED3Control.setStatus("mandatory")
_EnvReceptacles_ObjectIdentity = ObjectIdentity
envReceptacles = _EnvReceptacles_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5)
)
_EnvReceptacle1_ObjectIdentity = ObjectIdentity
envReceptacle1 = _EnvReceptacle1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 1)
)


class _EnvReceptacle1State_Type(Integer32):
    """Custom type envReceptacle1State based on Integer32"""
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
        *(("on", 1),
          ("off", 2),
          ("reboot", 3),
          ("eventOn", 4),
          ("eventOff", 5),
          ("eventReboot", 6))
    )


_EnvReceptacle1State_Type.__name__ = "Integer32"
_EnvReceptacle1State_Object = MibScalar
envReceptacle1State = _EnvReceptacle1State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 1, 1),
    _EnvReceptacle1State_Type()
)
envReceptacle1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle1State.setStatus("mandatory")
_EnvReceptacle1Label_Type = DisplayString
_EnvReceptacle1Label_Object = MibScalar
envReceptacle1Label = _EnvReceptacle1Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 1, 2),
    _EnvReceptacle1Label_Type()
)
envReceptacle1Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle1Label.setStatus("mandatory")


class _EnvReceptacle1Control_Type(Integer32):
    """Custom type envReceptacle1Control based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvReceptacle1Control_Type.__name__ = "Integer32"
_EnvReceptacle1Control_Object = MibScalar
envReceptacle1Control = _EnvReceptacle1Control_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 1, 3),
    _EnvReceptacle1Control_Type()
)
envReceptacle1Control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle1Control.setStatus("mandatory")


class _EnvReceptacle1Status_Type(Integer32):
    """Custom type envReceptacle1Status based on Integer32"""
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
        *(("on", 1),
          ("off", 2),
          ("reboot", 3),
          ("eventOn", 4),
          ("eventOff", 5),
          ("eventReboot", 6))
    )


_EnvReceptacle1Status_Type.__name__ = "Integer32"
_EnvReceptacle1Status_Object = MibScalar
envReceptacle1Status = _EnvReceptacle1Status_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 1, 4),
    _EnvReceptacle1Status_Type()
)
envReceptacle1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envReceptacle1Status.setStatus("mandatory")


class _EnvReceptacle1ReceptDelay_Type(Integer32):
    """Custom type envReceptacle1ReceptDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EnvReceptacle1ReceptDelay_Type.__name__ = "Integer32"
_EnvReceptacle1ReceptDelay_Object = MibScalar
envReceptacle1ReceptDelay = _EnvReceptacle1ReceptDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 1, 5),
    _EnvReceptacle1ReceptDelay_Type()
)
envReceptacle1ReceptDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle1ReceptDelay.setStatus("optional")
_EnvReceptacle2_ObjectIdentity = ObjectIdentity
envReceptacle2 = _EnvReceptacle2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 2)
)


class _EnvReceptacle2State_Type(Integer32):
    """Custom type envReceptacle2State based on Integer32"""
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
        *(("on", 1),
          ("off", 2),
          ("reboot", 3),
          ("eventOn", 4),
          ("eventOff", 5),
          ("eventReboot", 6))
    )


_EnvReceptacle2State_Type.__name__ = "Integer32"
_EnvReceptacle2State_Object = MibScalar
envReceptacle2State = _EnvReceptacle2State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 2, 1),
    _EnvReceptacle2State_Type()
)
envReceptacle2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle2State.setStatus("mandatory")
_EnvReceptacle2Label_Type = DisplayString
_EnvReceptacle2Label_Object = MibScalar
envReceptacle2Label = _EnvReceptacle2Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 2, 2),
    _EnvReceptacle2Label_Type()
)
envReceptacle2Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle2Label.setStatus("mandatory")


class _EnvReceptacle2Control_Type(Integer32):
    """Custom type envReceptacle2Control based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvReceptacle2Control_Type.__name__ = "Integer32"
_EnvReceptacle2Control_Object = MibScalar
envReceptacle2Control = _EnvReceptacle2Control_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 2, 3),
    _EnvReceptacle2Control_Type()
)
envReceptacle2Control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle2Control.setStatus("mandatory")


class _EnvReceptacle2Status_Type(Integer32):
    """Custom type envReceptacle2Status based on Integer32"""
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
        *(("on", 1),
          ("off", 2),
          ("reboot", 3),
          ("eventOn", 4),
          ("eventOff", 5),
          ("eventReboot", 6))
    )


_EnvReceptacle2Status_Type.__name__ = "Integer32"
_EnvReceptacle2Status_Object = MibScalar
envReceptacle2Status = _EnvReceptacle2Status_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 2, 4),
    _EnvReceptacle2Status_Type()
)
envReceptacle2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envReceptacle2Status.setStatus("mandatory")


class _EnvReceptacle2ReceptDelay_Type(Integer32):
    """Custom type envReceptacle2ReceptDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EnvReceptacle2ReceptDelay_Type.__name__ = "Integer32"
_EnvReceptacle2ReceptDelay_Object = MibScalar
envReceptacle2ReceptDelay = _EnvReceptacle2ReceptDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 2, 5),
    _EnvReceptacle2ReceptDelay_Type()
)
envReceptacle2ReceptDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle2ReceptDelay.setStatus("optional")
_EnvReceptacle3_ObjectIdentity = ObjectIdentity
envReceptacle3 = _EnvReceptacle3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 3)
)


class _EnvReceptacle3State_Type(Integer32):
    """Custom type envReceptacle3State based on Integer32"""
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
        *(("on", 1),
          ("off", 2),
          ("reboot", 3),
          ("eventOn", 4),
          ("eventOff", 5),
          ("eventReboot", 6))
    )


_EnvReceptacle3State_Type.__name__ = "Integer32"
_EnvReceptacle3State_Object = MibScalar
envReceptacle3State = _EnvReceptacle3State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 3, 1),
    _EnvReceptacle3State_Type()
)
envReceptacle3State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle3State.setStatus("mandatory")
_EnvReceptacle3Label_Type = DisplayString
_EnvReceptacle3Label_Object = MibScalar
envReceptacle3Label = _EnvReceptacle3Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 3, 2),
    _EnvReceptacle3Label_Type()
)
envReceptacle3Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle3Label.setStatus("mandatory")


class _EnvReceptacle3Control_Type(Integer32):
    """Custom type envReceptacle3Control based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvReceptacle3Control_Type.__name__ = "Integer32"
_EnvReceptacle3Control_Object = MibScalar
envReceptacle3Control = _EnvReceptacle3Control_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 3, 3),
    _EnvReceptacle3Control_Type()
)
envReceptacle3Control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle3Control.setStatus("mandatory")


class _EnvReceptacle3Status_Type(Integer32):
    """Custom type envReceptacle3Status based on Integer32"""
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
        *(("on", 1),
          ("off", 2),
          ("reboot", 3),
          ("eventOn", 4),
          ("eventOff", 5),
          ("eventReboot", 6))
    )


_EnvReceptacle3Status_Type.__name__ = "Integer32"
_EnvReceptacle3Status_Object = MibScalar
envReceptacle3Status = _EnvReceptacle3Status_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 3, 4),
    _EnvReceptacle3Status_Type()
)
envReceptacle3Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envReceptacle3Status.setStatus("mandatory")


class _EnvReceptacle3ReceptDelay_Type(Integer32):
    """Custom type envReceptacle3ReceptDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EnvReceptacle3ReceptDelay_Type.__name__ = "Integer32"
_EnvReceptacle3ReceptDelay_Object = MibScalar
envReceptacle3ReceptDelay = _EnvReceptacle3ReceptDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 3, 5),
    _EnvReceptacle3ReceptDelay_Type()
)
envReceptacle3ReceptDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle3ReceptDelay.setStatus("optional")
_EnvReceptacle4_ObjectIdentity = ObjectIdentity
envReceptacle4 = _EnvReceptacle4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 4)
)


class _EnvReceptacle4State_Type(Integer32):
    """Custom type envReceptacle4State based on Integer32"""
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
        *(("on", 1),
          ("off", 2),
          ("reboot", 3),
          ("eventOn", 4),
          ("eventOff", 5),
          ("eventReboot", 6))
    )


_EnvReceptacle4State_Type.__name__ = "Integer32"
_EnvReceptacle4State_Object = MibScalar
envReceptacle4State = _EnvReceptacle4State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 4, 1),
    _EnvReceptacle4State_Type()
)
envReceptacle4State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle4State.setStatus("mandatory")
_EnvReceptacle4Label_Type = DisplayString
_EnvReceptacle4Label_Object = MibScalar
envReceptacle4Label = _EnvReceptacle4Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 4, 2),
    _EnvReceptacle4Label_Type()
)
envReceptacle4Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle4Label.setStatus("mandatory")


class _EnvReceptacle4Control_Type(Integer32):
    """Custom type envReceptacle4Control based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvReceptacle4Control_Type.__name__ = "Integer32"
_EnvReceptacle4Control_Object = MibScalar
envReceptacle4Control = _EnvReceptacle4Control_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 4, 3),
    _EnvReceptacle4Control_Type()
)
envReceptacle4Control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle4Control.setStatus("mandatory")


class _EnvReceptacle4Status_Type(Integer32):
    """Custom type envReceptacle4Status based on Integer32"""
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
        *(("on", 1),
          ("off", 2),
          ("reboot", 3),
          ("eventOn", 4),
          ("eventOff", 5),
          ("eventReboot", 6))
    )


_EnvReceptacle4Status_Type.__name__ = "Integer32"
_EnvReceptacle4Status_Object = MibScalar
envReceptacle4Status = _EnvReceptacle4Status_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 4, 4),
    _EnvReceptacle4Status_Type()
)
envReceptacle4Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envReceptacle4Status.setStatus("mandatory")


class _EnvReceptacle4ReceptDelay_Type(Integer32):
    """Custom type envReceptacle4ReceptDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EnvReceptacle4ReceptDelay_Type.__name__ = "Integer32"
_EnvReceptacle4ReceptDelay_Object = MibScalar
envReceptacle4ReceptDelay = _EnvReceptacle4ReceptDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 4, 5),
    _EnvReceptacle4ReceptDelay_Type()
)
envReceptacle4ReceptDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle4ReceptDelay.setStatus("optional")
_EnvReceptacle5_ObjectIdentity = ObjectIdentity
envReceptacle5 = _EnvReceptacle5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 5)
)


class _EnvReceptacle5State_Type(Integer32):
    """Custom type envReceptacle5State based on Integer32"""
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
        *(("on", 1),
          ("off", 2),
          ("reboot", 3),
          ("eventOn", 4),
          ("eventOff", 5),
          ("eventReboot", 6))
    )


_EnvReceptacle5State_Type.__name__ = "Integer32"
_EnvReceptacle5State_Object = MibScalar
envReceptacle5State = _EnvReceptacle5State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 5, 1),
    _EnvReceptacle5State_Type()
)
envReceptacle5State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle5State.setStatus("mandatory")
_EnvReceptacle5Label_Type = DisplayString
_EnvReceptacle5Label_Object = MibScalar
envReceptacle5Label = _EnvReceptacle5Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 5, 2),
    _EnvReceptacle5Label_Type()
)
envReceptacle5Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle5Label.setStatus("mandatory")


class _EnvReceptacle5Control_Type(Integer32):
    """Custom type envReceptacle5Control based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvReceptacle5Control_Type.__name__ = "Integer32"
_EnvReceptacle5Control_Object = MibScalar
envReceptacle5Control = _EnvReceptacle5Control_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 5, 3),
    _EnvReceptacle5Control_Type()
)
envReceptacle5Control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle5Control.setStatus("mandatory")


class _EnvReceptacle5Status_Type(Integer32):
    """Custom type envReceptacle5Status based on Integer32"""
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
        *(("on", 1),
          ("off", 2),
          ("reboot", 3),
          ("eventOn", 4),
          ("eventOff", 5),
          ("eventReboot", 6))
    )


_EnvReceptacle5Status_Type.__name__ = "Integer32"
_EnvReceptacle5Status_Object = MibScalar
envReceptacle5Status = _EnvReceptacle5Status_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 5, 4),
    _EnvReceptacle5Status_Type()
)
envReceptacle5Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envReceptacle5Status.setStatus("mandatory")


class _EnvReceptacle5ReceptDelay_Type(Integer32):
    """Custom type envReceptacle5ReceptDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EnvReceptacle5ReceptDelay_Type.__name__ = "Integer32"
_EnvReceptacle5ReceptDelay_Object = MibScalar
envReceptacle5ReceptDelay = _EnvReceptacle5ReceptDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 5, 5),
    _EnvReceptacle5ReceptDelay_Type()
)
envReceptacle5ReceptDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle5ReceptDelay.setStatus("optional")
_EnvReceptacle6_ObjectIdentity = ObjectIdentity
envReceptacle6 = _EnvReceptacle6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 6)
)


class _EnvReceptacle6State_Type(Integer32):
    """Custom type envReceptacle6State based on Integer32"""
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
        *(("on", 1),
          ("off", 2),
          ("reboot", 3),
          ("eventOn", 4),
          ("eventOff", 5),
          ("eventReboot", 6))
    )


_EnvReceptacle6State_Type.__name__ = "Integer32"
_EnvReceptacle6State_Object = MibScalar
envReceptacle6State = _EnvReceptacle6State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 6, 1),
    _EnvReceptacle6State_Type()
)
envReceptacle6State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle6State.setStatus("mandatory")
_EnvReceptacle6Label_Type = DisplayString
_EnvReceptacle6Label_Object = MibScalar
envReceptacle6Label = _EnvReceptacle6Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 6, 2),
    _EnvReceptacle6Label_Type()
)
envReceptacle6Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle6Label.setStatus("mandatory")


class _EnvReceptacle6Control_Type(Integer32):
    """Custom type envReceptacle6Control based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvReceptacle6Control_Type.__name__ = "Integer32"
_EnvReceptacle6Control_Object = MibScalar
envReceptacle6Control = _EnvReceptacle6Control_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 6, 3),
    _EnvReceptacle6Control_Type()
)
envReceptacle6Control.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle6Control.setStatus("mandatory")


class _EnvReceptacle6Status_Type(Integer32):
    """Custom type envReceptacle6Status based on Integer32"""
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
        *(("on", 1),
          ("off", 2),
          ("reboot", 3),
          ("eventOn", 4),
          ("eventOff", 5),
          ("eventReboot", 6))
    )


_EnvReceptacle6Status_Type.__name__ = "Integer32"
_EnvReceptacle6Status_Object = MibScalar
envReceptacle6Status = _EnvReceptacle6Status_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 6, 4),
    _EnvReceptacle6Status_Type()
)
envReceptacle6Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envReceptacle6Status.setStatus("mandatory")


class _EnvReceptacle6ReceptDelay_Type(Integer32):
    """Custom type envReceptacle6ReceptDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_EnvReceptacle6ReceptDelay_Type.__name__ = "Integer32"
_EnvReceptacle6ReceptDelay_Object = MibScalar
envReceptacle6ReceptDelay = _EnvReceptacle6ReceptDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 6, 5),
    _EnvReceptacle6ReceptDelay_Type()
)
envReceptacle6ReceptDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacle6ReceptDelay.setStatus("optional")
_EnvReceptacleMaster_ObjectIdentity = ObjectIdentity
envReceptacleMaster = _EnvReceptacleMaster_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 7)
)


class _EnvReceptacleMasterOnOff_Type(Integer32):
    """Custom type envReceptacleMasterOnOff based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("reboot", 3))
    )


_EnvReceptacleMasterOnOff_Type.__name__ = "Integer32"
_EnvReceptacleMasterOnOff_Object = MibScalar
envReceptacleMasterOnOff = _EnvReceptacleMasterOnOff_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 7, 1),
    _EnvReceptacleMasterOnOff_Type()
)
envReceptacleMasterOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacleMasterOnOff.setStatus("mandatory")


class _EnvReceptacleMasterDelay_Type(Integer32):
    """Custom type envReceptacleMasterDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EnvReceptacleMasterDelay_Type.__name__ = "Integer32"
_EnvReceptacleMasterDelay_Object = MibScalar
envReceptacleMasterDelay = _EnvReceptacleMasterDelay_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 5, 7, 2),
    _EnvReceptacleMasterDelay_Type()
)
envReceptacleMasterDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envReceptacleMasterDelay.setStatus("optional")
_EnvAlarms_ObjectIdentity = ObjectIdentity
envAlarms = _EnvAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 6)
)


class _EnvSummaryAlarm_Type(Integer32):
    """Custom type envSummaryAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvSummaryAlarm_Type.__name__ = "Integer32"
_EnvSummaryAlarm_Object = MibScalar
envSummaryAlarm = _EnvSummaryAlarm_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 6, 1),
    _EnvSummaryAlarm_Type()
)
envSummaryAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envSummaryAlarm.setStatus("mandatory")
_EnvTemperatureSensors_ObjectIdentity = ObjectIdentity
envTemperatureSensors = _EnvTemperatureSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7)
)
_EnvTemperature1_ObjectIdentity = ObjectIdentity
envTemperature1 = _EnvTemperature1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 1)
)


class _EnvTemperature1State_Type(Integer32):
    """Custom type envTemperature1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 1),
          ("installed", 2))
    )


_EnvTemperature1State_Type.__name__ = "Integer32"
_EnvTemperature1State_Object = MibScalar
envTemperature1State = _EnvTemperature1State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 1, 1),
    _EnvTemperature1State_Type()
)
envTemperature1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemperature1State.setStatus("mandatory")


class _EnvTemperature1F_Type(Integer32):
    """Custom type envTemperature1F based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemperature1F_Type.__name__ = "Integer32"
_EnvTemperature1F_Object = MibScalar
envTemperature1F = _EnvTemperature1F_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 1, 2),
    _EnvTemperature1F_Type()
)
envTemperature1F.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTemperature1F.setStatus("mandatory")


class _EnvTemperature1C_Type(Integer32):
    """Custom type envTemperature1C based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemperature1C_Type.__name__ = "Integer32"
_EnvTemperature1C_Object = MibScalar
envTemperature1C = _EnvTemperature1C_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 1, 3),
    _EnvTemperature1C_Type()
)
envTemperature1C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTemperature1C.setStatus("mandatory")
_EnvTemperature1Label_Type = DisplayString
_EnvTemperature1Label_Object = MibScalar
envTemperature1Label = _EnvTemperature1Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 1, 4),
    _EnvTemperature1Label_Type()
)
envTemperature1Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemperature1Label.setStatus("mandatory")


class _EnvTemperature1OffsetF_Type(Integer32):
    """Custom type envTemperature1OffsetF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemperature1OffsetF_Type.__name__ = "Integer32"
_EnvTemperature1OffsetF_Object = MibScalar
envTemperature1OffsetF = _EnvTemperature1OffsetF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 1, 5),
    _EnvTemperature1OffsetF_Type()
)
envTemperature1OffsetF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemperature1OffsetF.setStatus("mandatory")


class _EnvTemperature1OffsetC_Type(Integer32):
    """Custom type envTemperature1OffsetC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemperature1OffsetC_Type.__name__ = "Integer32"
_EnvTemperature1OffsetC_Object = MibScalar
envTemperature1OffsetC = _EnvTemperature1OffsetC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 1, 6),
    _EnvTemperature1OffsetC_Type()
)
envTemperature1OffsetC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemperature1OffsetC.setStatus("mandatory")


class _EnvTemp1HighLimitF_Type(Integer32):
    """Custom type envTemp1HighLimitF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemp1HighLimitF_Type.__name__ = "Integer32"
_EnvTemp1HighLimitF_Object = MibScalar
envTemp1HighLimitF = _EnvTemp1HighLimitF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 1, 7),
    _EnvTemp1HighLimitF_Type()
)
envTemp1HighLimitF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemp1HighLimitF.setStatus("mandatory")


class _EnvTemp1HighLimitC_Type(Integer32):
    """Custom type envTemp1HighLimitC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemp1HighLimitC_Type.__name__ = "Integer32"
_EnvTemp1HighLimitC_Object = MibScalar
envTemp1HighLimitC = _EnvTemp1HighLimitC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 1, 8),
    _EnvTemp1HighLimitC_Type()
)
envTemp1HighLimitC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemp1HighLimitC.setStatus("mandatory")


class _EnvTemp1LowLimitF_Type(Integer32):
    """Custom type envTemp1LowLimitF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemp1LowLimitF_Type.__name__ = "Integer32"
_EnvTemp1LowLimitF_Object = MibScalar
envTemp1LowLimitF = _EnvTemp1LowLimitF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 1, 9),
    _EnvTemp1LowLimitF_Type()
)
envTemp1LowLimitF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemp1LowLimitF.setStatus("mandatory")


class _EnvTemp1LowLimitC_Type(Integer32):
    """Custom type envTemp1LowLimitC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemp1LowLimitC_Type.__name__ = "Integer32"
_EnvTemp1LowLimitC_Object = MibScalar
envTemp1LowLimitC = _EnvTemp1LowLimitC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 1, 10),
    _EnvTemp1LowLimitC_Type()
)
envTemp1LowLimitC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemp1LowLimitC.setStatus("mandatory")
_EnvTemperature2_ObjectIdentity = ObjectIdentity
envTemperature2 = _EnvTemperature2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 2)
)


class _EnvTemperature2State_Type(Integer32):
    """Custom type envTemperature2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 1),
          ("installed", 2))
    )


_EnvTemperature2State_Type.__name__ = "Integer32"
_EnvTemperature2State_Object = MibScalar
envTemperature2State = _EnvTemperature2State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 2, 1),
    _EnvTemperature2State_Type()
)
envTemperature2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemperature2State.setStatus("mandatory")


class _EnvTemperature2F_Type(Integer32):
    """Custom type envTemperature2F based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemperature2F_Type.__name__ = "Integer32"
_EnvTemperature2F_Object = MibScalar
envTemperature2F = _EnvTemperature2F_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 2, 2),
    _EnvTemperature2F_Type()
)
envTemperature2F.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTemperature2F.setStatus("mandatory")


class _EnvTemperature2C_Type(Integer32):
    """Custom type envTemperature2C based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemperature2C_Type.__name__ = "Integer32"
_EnvTemperature2C_Object = MibScalar
envTemperature2C = _EnvTemperature2C_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 2, 3),
    _EnvTemperature2C_Type()
)
envTemperature2C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTemperature2C.setStatus("mandatory")
_EnvTemperature2Label_Type = DisplayString
_EnvTemperature2Label_Object = MibScalar
envTemperature2Label = _EnvTemperature2Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 2, 4),
    _EnvTemperature2Label_Type()
)
envTemperature2Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemperature2Label.setStatus("mandatory")


class _EnvTemperature2OffsetF_Type(Integer32):
    """Custom type envTemperature2OffsetF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemperature2OffsetF_Type.__name__ = "Integer32"
_EnvTemperature2OffsetF_Object = MibScalar
envTemperature2OffsetF = _EnvTemperature2OffsetF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 2, 5),
    _EnvTemperature2OffsetF_Type()
)
envTemperature2OffsetF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemperature2OffsetF.setStatus("mandatory")


class _EnvTemperature2OffsetC_Type(Integer32):
    """Custom type envTemperature2OffsetC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemperature2OffsetC_Type.__name__ = "Integer32"
_EnvTemperature2OffsetC_Object = MibScalar
envTemperature2OffsetC = _EnvTemperature2OffsetC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 2, 6),
    _EnvTemperature2OffsetC_Type()
)
envTemperature2OffsetC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemperature2OffsetC.setStatus("mandatory")


class _EnvTemp2HighLimitF_Type(Integer32):
    """Custom type envTemp2HighLimitF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemp2HighLimitF_Type.__name__ = "Integer32"
_EnvTemp2HighLimitF_Object = MibScalar
envTemp2HighLimitF = _EnvTemp2HighLimitF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 2, 7),
    _EnvTemp2HighLimitF_Type()
)
envTemp2HighLimitF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemp2HighLimitF.setStatus("mandatory")


class _EnvTemp2HighLimitC_Type(Integer32):
    """Custom type envTemp2HighLimitC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemp2HighLimitC_Type.__name__ = "Integer32"
_EnvTemp2HighLimitC_Object = MibScalar
envTemp2HighLimitC = _EnvTemp2HighLimitC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 2, 8),
    _EnvTemp2HighLimitC_Type()
)
envTemp2HighLimitC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemp2HighLimitC.setStatus("mandatory")


class _EnvTemp2LowLimitF_Type(Integer32):
    """Custom type envTemp2LowLimitF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemp2LowLimitF_Type.__name__ = "Integer32"
_EnvTemp2LowLimitF_Object = MibScalar
envTemp2LowLimitF = _EnvTemp2LowLimitF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 2, 9),
    _EnvTemp2LowLimitF_Type()
)
envTemp2LowLimitF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemp2LowLimitF.setStatus("mandatory")


class _EnvTemp2LowLimitC_Type(Integer32):
    """Custom type envTemp2LowLimitC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemp2LowLimitC_Type.__name__ = "Integer32"
_EnvTemp2LowLimitC_Object = MibScalar
envTemp2LowLimitC = _EnvTemp2LowLimitC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 2, 10),
    _EnvTemp2LowLimitC_Type()
)
envTemp2LowLimitC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemp2LowLimitC.setStatus("mandatory")
_EnvTemperature3_ObjectIdentity = ObjectIdentity
envTemperature3 = _EnvTemperature3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 3)
)


class _EnvTemperature3State_Type(Integer32):
    """Custom type envTemperature3State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 1),
          ("airSensorInstalled", 2),
          ("waterSensorInstalled", 3))
    )


_EnvTemperature3State_Type.__name__ = "Integer32"
_EnvTemperature3State_Object = MibScalar
envTemperature3State = _EnvTemperature3State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 3, 1),
    _EnvTemperature3State_Type()
)
envTemperature3State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemperature3State.setStatus("mandatory")


class _EnvTemperature3F_Type(Integer32):
    """Custom type envTemperature3F based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemperature3F_Type.__name__ = "Integer32"
_EnvTemperature3F_Object = MibScalar
envTemperature3F = _EnvTemperature3F_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 3, 2),
    _EnvTemperature3F_Type()
)
envTemperature3F.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTemperature3F.setStatus("mandatory")


class _EnvTemperature3C_Type(Integer32):
    """Custom type envTemperature3C based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemperature3C_Type.__name__ = "Integer32"
_EnvTemperature3C_Object = MibScalar
envTemperature3C = _EnvTemperature3C_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 3, 3),
    _EnvTemperature3C_Type()
)
envTemperature3C.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envTemperature3C.setStatus("mandatory")
_EnvTemperature3Label_Type = DisplayString
_EnvTemperature3Label_Object = MibScalar
envTemperature3Label = _EnvTemperature3Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 3, 4),
    _EnvTemperature3Label_Type()
)
envTemperature3Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemperature3Label.setStatus("mandatory")


class _EnvTemperature3OffsetF_Type(Integer32):
    """Custom type envTemperature3OffsetF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemperature3OffsetF_Type.__name__ = "Integer32"
_EnvTemperature3OffsetF_Object = MibScalar
envTemperature3OffsetF = _EnvTemperature3OffsetF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 3, 5),
    _EnvTemperature3OffsetF_Type()
)
envTemperature3OffsetF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemperature3OffsetF.setStatus("mandatory")


class _EnvTemperature3OffsetC_Type(Integer32):
    """Custom type envTemperature3OffsetC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemperature3OffsetC_Type.__name__ = "Integer32"
_EnvTemperature3OffsetC_Object = MibScalar
envTemperature3OffsetC = _EnvTemperature3OffsetC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 3, 6),
    _EnvTemperature3OffsetC_Type()
)
envTemperature3OffsetC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemperature3OffsetC.setStatus("mandatory")


class _EnvTemp3HighLimitF_Type(Integer32):
    """Custom type envTemp3HighLimitF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemp3HighLimitF_Type.__name__ = "Integer32"
_EnvTemp3HighLimitF_Object = MibScalar
envTemp3HighLimitF = _EnvTemp3HighLimitF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 3, 7),
    _EnvTemp3HighLimitF_Type()
)
envTemp3HighLimitF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemp3HighLimitF.setStatus("mandatory")


class _EnvTemp3HighLimitC_Type(Integer32):
    """Custom type envTemp3HighLimitC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemp3HighLimitC_Type.__name__ = "Integer32"
_EnvTemp3HighLimitC_Object = MibScalar
envTemp3HighLimitC = _EnvTemp3HighLimitC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 3, 8),
    _EnvTemp3HighLimitC_Type()
)
envTemp3HighLimitC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemp3HighLimitC.setStatus("mandatory")


class _EnvTemp3LowLimitF_Type(Integer32):
    """Custom type envTemp3LowLimitF based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemp3LowLimitF_Type.__name__ = "Integer32"
_EnvTemp3LowLimitF_Object = MibScalar
envTemp3LowLimitF = _EnvTemp3LowLimitF_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 3, 9),
    _EnvTemp3LowLimitF_Type()
)
envTemp3LowLimitF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemp3LowLimitF.setStatus("mandatory")


class _EnvTemp3LowLimitC_Type(Integer32):
    """Custom type envTemp3LowLimitC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvTemp3LowLimitC_Type.__name__ = "Integer32"
_EnvTemp3LowLimitC_Object = MibScalar
envTemp3LowLimitC = _EnvTemp3LowLimitC_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 3, 10),
    _EnvTemp3LowLimitC_Type()
)
envTemp3LowLimitC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemp3LowLimitC.setStatus("mandatory")


class _EnvTemp3Calibrate_Type(Integer32):
    """Custom type envTemp3Calibrate based on Integer32"""
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


_EnvTemp3Calibrate_Type.__name__ = "Integer32"
_EnvTemp3Calibrate_Object = MibScalar
envTemp3Calibrate = _EnvTemp3Calibrate_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 7, 3, 11),
    _EnvTemp3Calibrate_Type()
)
envTemp3Calibrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envTemp3Calibrate.setStatus("mandatory")
_EnvHumiditySensors_ObjectIdentity = ObjectIdentity
envHumiditySensors = _EnvHumiditySensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8)
)
_EnvHumidity1_ObjectIdentity = ObjectIdentity
envHumidity1 = _EnvHumidity1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 1)
)


class _EnvHumidity1State_Type(Integer32):
    """Custom type envHumidity1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 1),
          ("installed", 2))
    )


_EnvHumidity1State_Type.__name__ = "Integer32"
_EnvHumidity1State_Object = MibScalar
envHumidity1State = _EnvHumidity1State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 1, 1),
    _EnvHumidity1State_Type()
)
envHumidity1State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envHumidity1State.setStatus("mandatory")


class _EnvHumidity1RH_Type(Integer32):
    """Custom type envHumidity1RH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvHumidity1RH_Type.__name__ = "Integer32"
_EnvHumidity1RH_Object = MibScalar
envHumidity1RH = _EnvHumidity1RH_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 1, 2),
    _EnvHumidity1RH_Type()
)
envHumidity1RH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envHumidity1RH.setStatus("mandatory")
_EnvHumidity1Label_Type = DisplayString
_EnvHumidity1Label_Object = MibScalar
envHumidity1Label = _EnvHumidity1Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 1, 3),
    _EnvHumidity1Label_Type()
)
envHumidity1Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envHumidity1Label.setStatus("mandatory")


class _EnvHumidity1Offset_Type(Integer32):
    """Custom type envHumidity1Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvHumidity1Offset_Type.__name__ = "Integer32"
_EnvHumidity1Offset_Object = MibScalar
envHumidity1Offset = _EnvHumidity1Offset_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 1, 4),
    _EnvHumidity1Offset_Type()
)
envHumidity1Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envHumidity1Offset.setStatus("mandatory")


class _EnvHumidity1HighLimit_Type(Integer32):
    """Custom type envHumidity1HighLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvHumidity1HighLimit_Type.__name__ = "Integer32"
_EnvHumidity1HighLimit_Object = MibScalar
envHumidity1HighLimit = _EnvHumidity1HighLimit_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 1, 5),
    _EnvHumidity1HighLimit_Type()
)
envHumidity1HighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envHumidity1HighLimit.setStatus("mandatory")


class _EnvHumidity1LowLimit_Type(Integer32):
    """Custom type envHumidity1LowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvHumidity1LowLimit_Type.__name__ = "Integer32"
_EnvHumidity1LowLimit_Object = MibScalar
envHumidity1LowLimit = _EnvHumidity1LowLimit_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 1, 6),
    _EnvHumidity1LowLimit_Type()
)
envHumidity1LowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envHumidity1LowLimit.setStatus("mandatory")
_EnvHumidity2_ObjectIdentity = ObjectIdentity
envHumidity2 = _EnvHumidity2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 2)
)


class _EnvHumidity2State_Type(Integer32):
    """Custom type envHumidity2State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notInstalled", 1),
          ("installed", 2))
    )


_EnvHumidity2State_Type.__name__ = "Integer32"
_EnvHumidity2State_Object = MibScalar
envHumidity2State = _EnvHumidity2State_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 2, 1),
    _EnvHumidity2State_Type()
)
envHumidity2State.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envHumidity2State.setStatus("mandatory")


class _EnvHumidity2RH_Type(Integer32):
    """Custom type envHumidity2RH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvHumidity2RH_Type.__name__ = "Integer32"
_EnvHumidity2RH_Object = MibScalar
envHumidity2RH = _EnvHumidity2RH_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 2, 2),
    _EnvHumidity2RH_Type()
)
envHumidity2RH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    envHumidity2RH.setStatus("mandatory")
_EnvHumidity2Label_Type = DisplayString
_EnvHumidity2Label_Object = MibScalar
envHumidity2Label = _EnvHumidity2Label_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 2, 3),
    _EnvHumidity2Label_Type()
)
envHumidity2Label.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envHumidity2Label.setStatus("mandatory")


class _EnvHumidity2Offset_Type(Integer32):
    """Custom type envHumidity2Offset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvHumidity2Offset_Type.__name__ = "Integer32"
_EnvHumidity2Offset_Object = MibScalar
envHumidity2Offset = _EnvHumidity2Offset_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 2, 4),
    _EnvHumidity2Offset_Type()
)
envHumidity2Offset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envHumidity2Offset.setStatus("mandatory")


class _EnvHumidity2HighLimit_Type(Integer32):
    """Custom type envHumidity2HighLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvHumidity2HighLimit_Type.__name__ = "Integer32"
_EnvHumidity2HighLimit_Object = MibScalar
envHumidity2HighLimit = _EnvHumidity2HighLimit_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 2, 5),
    _EnvHumidity2HighLimit_Type()
)
envHumidity2HighLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envHumidity2HighLimit.setStatus("mandatory")


class _EnvHumidity2LowLimit_Type(Integer32):
    """Custom type envHumidity2LowLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EnvHumidity2LowLimit_Type.__name__ = "Integer32"
_EnvHumidity2LowLimit_Object = MibScalar
envHumidity2LowLimit = _EnvHumidity2LowLimit_Object(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 8, 2, 6),
    _EnvHumidity2LowLimit_Type()
)
envHumidity2LowLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    envHumidity2LowLimit.setStatus("mandatory")
_EnvTraps_ObjectIdentity = ObjectIdentity
envTraps = _EnvTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11)
)
_LeExperimental_ObjectIdentity = ObjectIdentity
leExperimental = _LeExperimental_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 2)
)
_LePrivate_ObjectIdentity = ObjectIdentity
lePrivate = _LePrivate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 3)
)

# Managed Objects groups


# Notification objects

lcUpsOverloadWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 1)
)
lcUpsOverloadWarningTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOverloadWarningTrap.setStatus(
        ""
    )

lcUpsOverloadShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 2)
)
lcUpsOverloadShutdownTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOverloadShutdownTrap.setStatus(
        ""
    )

lcUpsOnBatteryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 3)
)
lcUpsOnBatteryTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOnBatteryTrap.setStatus(
        ""
    )

lcUpsLowBatteryWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 4)
)
lcUpsLowBatteryWarningTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsLowBatteryWarningTrap.setStatus(
        ""
    )

lcUpsLowBatteryShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 5)
)
lcUpsLowBatteryShutdownTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsLowBatteryShutdownTrap.setStatus(
        ""
    )

lcUpsUtilPowerFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 6)
)
lcUpsUtilPowerFailedTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsUtilPowerFailedTrap.setStatus(
        ""
    )

lcUpsUtilPowerRestoredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 7)
)
lcUpsUtilPowerRestoredTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsUtilPowerRestoredTrap.setStatus(
        ""
    )

lcUpsInputOverVoltageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 8)
)
lcUpsInputOverVoltageTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsInputOverVoltageTrap.setStatus(
        ""
    )

lcUpsOverTempWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 9)
)
lcUpsOverTempWarningTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOverTempWarningTrap.setStatus(
        ""
    )

lcUpsOverTempShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 10)
)
lcUpsOverTempShutdownTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOverTempShutdownTrap.setStatus(
        ""
    )

lcUpsAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 11)
)
lcUpsAlarmTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsAlarmTrap.setStatus(
        ""
    )

lcUpsOutputOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 12)
)
lcUpsOutputOffTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOutputOffTrap.setStatus(
        ""
    )

lcUpsOutputOffWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 13)
)
lcUpsOutputOffWarningTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOutputOffWarningTrap.setStatus(
        ""
    )

lcUpsOutputOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 14)
)
lcUpsOutputOnTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOutputOnTrap.setStatus(
        ""
    )

lcUpsOutputOnWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 15)
)
lcUpsOutputOnWarningTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOutputOnWarningTrap.setStatus(
        ""
    )

lcUpsUnixShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 16)
)
lcUpsUnixShutdownTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsUnixShutdownTrap.setStatus(
        ""
    )

lcUpsUnixShutdownWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 17)
)
lcUpsUnixShutdownWarningTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsUnixShutdownWarningTrap.setStatus(
        ""
    )

lcUpsReceptOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 18)
)
lcUpsReceptOffTrap.setObjects(
      *(("LIEBERT-MIB", "sysUpTime"),
        ("LIEBERT-MIB", "lcUpsSwitchedReceptIndex"))
)
if mibBuilder.loadTexts:
    lcUpsReceptOffTrap.setStatus(
        ""
    )

lcUpsReceptOffWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 19)
)
lcUpsReceptOffWarningTrap.setObjects(
      *(("LIEBERT-MIB", "sysUpTime"),
        ("LIEBERT-MIB", "lcUpsSwitchedReceptIndex"))
)
if mibBuilder.loadTexts:
    lcUpsReceptOffWarningTrap.setStatus(
        ""
    )

lcUpsReceptOnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 20)
)
lcUpsReceptOnTrap.setObjects(
      *(("LIEBERT-MIB", "sysUpTime"),
        ("LIEBERT-MIB", "lcUpsSwitchedReceptIndex"))
)
if mibBuilder.loadTexts:
    lcUpsReceptOnTrap.setStatus(
        ""
    )

lcUpsReceptOnWarningTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 21)
)
lcUpsReceptOnWarningTrap.setObjects(
      *(("LIEBERT-MIB", "sysUpTime"),
        ("LIEBERT-MIB", "lcUpsSwitchedReceptIndex"))
)
if mibBuilder.loadTexts:
    lcUpsReceptOnWarningTrap.setStatus(
        ""
    )

lcUpsInputFreqErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 22)
)
lcUpsInputFreqErrorTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsInputFreqErrorTrap.setStatus(
        ""
    )

lcUpsDCOverVoltageShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 23)
)
lcUpsDCOverVoltageShutdownTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsDCOverVoltageShutdownTrap.setStatus(
        ""
    )

lcUpsOutputOverVoltageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 24)
)
lcUpsOutputOverVoltageTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsOutputOverVoltageTrap.setStatus(
        ""
    )

lcUpsFuseBlownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 25)
)
lcUpsFuseBlownTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsFuseBlownTrap.setStatus(
        ""
    )

lcUpsEmergencyPowerOffTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 26)
)
lcUpsEmergencyPowerOffTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsEmergencyPowerOffTrap.setStatus(
        ""
    )

lcUpsControlPowerFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 27)
)
lcUpsControlPowerFailureTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsControlPowerFailureTrap.setStatus(
        ""
    )

lcUpsReversePowerTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 28)
)
lcUpsReversePowerTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsReversePowerTrap.setStatus(
        ""
    )

lcUpsPhaseRotationErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 29)
)
lcUpsPhaseRotationErrorTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsPhaseRotationErrorTrap.setStatus(
        ""
    )

lcUpsLoadOnBypassTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 30)
)
lcUpsLoadOnBypassTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsLoadOnBypassTrap.setStatus(
        ""
    )

lcUpsEmergencyXferToBypassTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 31)
)
lcUpsEmergencyXferToBypassTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsEmergencyXferToBypassTrap.setStatus(
        ""
    )

lcUpsInverterFaultTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 1, 11, 0, 34)
)
lcUpsInverterFaultTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lcUpsInverterFaultTrap.setStatus(
        ""
    )

lsUpsCheckAirFilterTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 2, 11, 0, 1)
)
lsUpsCheckAirFilterTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lsUpsCheckAirFilterTrap.setStatus(
        ""
    )

ldUpsDCOverVoltageShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 11, 0, 1)
)
ldUpsDCOverVoltageShutdownTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    ldUpsDCOverVoltageShutdownTrap.setStatus(
        ""
    )

ldUpsOutputShortShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 11, 0, 2)
)
ldUpsOutputShortShutdownTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    ldUpsOutputShortShutdownTrap.setStatus(
        ""
    )

ldUpsLNReversedShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 11, 0, 3)
)
ldUpsLNReversedShutdownTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    ldUpsLNReversedShutdownTrap.setStatus(
        ""
    )

ldUpsImminentShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 11, 0, 4)
)
ldUpsImminentShutdownTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    ldUpsImminentShutdownTrap.setStatus(
        ""
    )

ldUpsInputFreqErrorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 11, 0, 5)
)
ldUpsInputFreqErrorTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    ldUpsInputFreqErrorTrap.setStatus(
        ""
    )

ldUpsOutputOverVoltageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 11, 0, 6)
)
ldUpsOutputOverVoltageTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    ldUpsOutputOverVoltageTrap.setStatus(
        ""
    )

ldUpsOutputUnderVoltageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 11, 0, 7)
)
ldUpsOutputUnderVoltageTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    ldUpsOutputUnderVoltageTrap.setStatus(
        ""
    )

ldUpsChargerFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 3, 11, 0, 8)
)
ldUpsChargerFailedTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    ldUpsChargerFailedTrap.setStatus(
        ""
    )

lgUpsDCOverVoltageShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 11, 0, 1)
)
lgUpsDCOverVoltageShutdownTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgUpsDCOverVoltageShutdownTrap.setStatus(
        ""
    )

lgUpsOutputShortShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 11, 0, 2)
)
lgUpsOutputShortShutdownTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgUpsOutputShortShutdownTrap.setStatus(
        ""
    )

lgUpsLNReversedShutdownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 11, 0, 3)
)
lgUpsLNReversedShutdownTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgUpsLNReversedShutdownTrap.setStatus(
        ""
    )

lgUpsInputUVOnStartupTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 1, 1, 4, 11, 0, 4)
)
lgUpsInputUVOnStartupTrap.setObjects(
    ("LIEBERT-MIB", "sysUpTime")
)
if mibBuilder.loadTexts:
    lgUpsInputUVOnStartupTrap.setStatus(
        ""
    )

envSummaryAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 1)
)
if mibBuilder.loadTexts:
    envSummaryAlarmTrap.setStatus(
        ""
    )

envDigInput1TrueTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 2)
)
if mibBuilder.loadTexts:
    envDigInput1TrueTrap.setStatus(
        ""
    )

envDigInput1FalseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 3)
)
if mibBuilder.loadTexts:
    envDigInput1FalseTrap.setStatus(
        ""
    )

envDigInput2TrueTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 4)
)
if mibBuilder.loadTexts:
    envDigInput2TrueTrap.setStatus(
        ""
    )

envDigInput2FalseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 5)
)
if mibBuilder.loadTexts:
    envDigInput2FalseTrap.setStatus(
        ""
    )

envDigInput3TrueTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 6)
)
if mibBuilder.loadTexts:
    envDigInput3TrueTrap.setStatus(
        ""
    )

envDigInput3FalseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 7)
)
if mibBuilder.loadTexts:
    envDigInput3FalseTrap.setStatus(
        ""
    )

envDigInput4TrueTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 8)
)
if mibBuilder.loadTexts:
    envDigInput4TrueTrap.setStatus(
        ""
    )

envDigInput4FalseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 9)
)
if mibBuilder.loadTexts:
    envDigInput4FalseTrap.setStatus(
        ""
    )

envDigInput5TrueTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 10)
)
if mibBuilder.loadTexts:
    envDigInput5TrueTrap.setStatus(
        ""
    )

envDigInput5FalseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 11)
)
if mibBuilder.loadTexts:
    envDigInput5FalseTrap.setStatus(
        ""
    )

envDigInput6TrueTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 12)
)
if mibBuilder.loadTexts:
    envDigInput6TrueTrap.setStatus(
        ""
    )

envDigInput6FalseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 13)
)
if mibBuilder.loadTexts:
    envDigInput6FalseTrap.setStatus(
        ""
    )

envDigInput7TrueTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 14)
)
if mibBuilder.loadTexts:
    envDigInput7TrueTrap.setStatus(
        ""
    )

envDigInput7FalseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 15)
)
if mibBuilder.loadTexts:
    envDigInput7FalseTrap.setStatus(
        ""
    )

envDigInput8TrueTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 16)
)
if mibBuilder.loadTexts:
    envDigInput8TrueTrap.setStatus(
        ""
    )

envDigInput8FalseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 17)
)
if mibBuilder.loadTexts:
    envDigInput8FalseTrap.setStatus(
        ""
    )

envDigInput9TrueTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 18)
)
if mibBuilder.loadTexts:
    envDigInput9TrueTrap.setStatus(
        ""
    )

envDigInput9FalseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 19)
)
if mibBuilder.loadTexts:
    envDigInput9FalseTrap.setStatus(
        ""
    )

envDigInput10TrueTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 20)
)
if mibBuilder.loadTexts:
    envDigInput10TrueTrap.setStatus(
        ""
    )

envDigInput10FalseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 21)
)
if mibBuilder.loadTexts:
    envDigInput10FalseTrap.setStatus(
        ""
    )

envTemperature1HighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 22)
)
if mibBuilder.loadTexts:
    envTemperature1HighTrap.setStatus(
        ""
    )

envTemperature1LowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 23)
)
if mibBuilder.loadTexts:
    envTemperature1LowTrap.setStatus(
        ""
    )

envTemperature1NormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 24)
)
if mibBuilder.loadTexts:
    envTemperature1NormalTrap.setStatus(
        ""
    )

envTemperature2HighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 25)
)
if mibBuilder.loadTexts:
    envTemperature2HighTrap.setStatus(
        ""
    )

envTemperature2LowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 26)
)
if mibBuilder.loadTexts:
    envTemperature2LowTrap.setStatus(
        ""
    )

envTemperature2NormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 27)
)
if mibBuilder.loadTexts:
    envTemperature2NormalTrap.setStatus(
        ""
    )

envTemperature3HighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 28)
)
if mibBuilder.loadTexts:
    envTemperature3HighTrap.setStatus(
        ""
    )

envTemperature3LowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 29)
)
if mibBuilder.loadTexts:
    envTemperature3LowTrap.setStatus(
        ""
    )

envTemperature3NormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 30)
)
if mibBuilder.loadTexts:
    envTemperature3NormalTrap.setStatus(
        ""
    )

envHumidity1HighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 31)
)
if mibBuilder.loadTexts:
    envHumidity1HighTrap.setStatus(
        ""
    )

envHumidity1LowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 32)
)
if mibBuilder.loadTexts:
    envHumidity1LowTrap.setStatus(
        ""
    )

envHumidity1NormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 33)
)
if mibBuilder.loadTexts:
    envHumidity1NormalTrap.setStatus(
        ""
    )

envHumidity2HighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 34)
)
if mibBuilder.loadTexts:
    envHumidity2HighTrap.setStatus(
        ""
    )

envHumidity2LowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 35)
)
if mibBuilder.loadTexts:
    envHumidity2LowTrap.setStatus(
        ""
    )

envHumidity2NormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 476, 1, 2, 1, 1, 1, 11, 0, 36)
)
if mibBuilder.loadTexts:
    envHumidity2NormalTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LIEBERT-MIB",
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
       "lcUpsIdentManufactureDate": lcUpsIdentManufactureDate,
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
       "lcUpsInputFrequency": lcUpsInputFrequency,
       "lcUpsInputBrownOuts": lcUpsInputBrownOuts,
       "lcUpsInputBlackOuts": lcUpsInputBlackOuts,
       "lcUpsInputTransients": lcUpsInputTransients,
       "lcUpsInputNumLines": lcUpsInputNumLines,
       "lcUpsInputTable": lcUpsInputTable,
       "lcUpsInputEntry": lcUpsInputEntry,
       "lcUpsInputLine": lcUpsInputLine,
       "lcUpsInputVoltage": lcUpsInputVoltage,
       "lcUpsInputCurrent": lcUpsInputCurrent,
       "lcUpsInputVA": lcUpsInputVA,
       "lcUpsOutput": lcUpsOutput,
       "lcUpsOutputFrequency": lcUpsOutputFrequency,
       "lcUpsOutputLoad": lcUpsOutputLoad,
       "lcUpsOutputNumLines": lcUpsOutputNumLines,
       "lcUpsOutputTable": lcUpsOutputTable,
       "lcUpsOutputEntry": lcUpsOutputEntry,
       "lcUpsOutputLine": lcUpsOutputLine,
       "lcUpsOutputVoltage": lcUpsOutputVoltage,
       "lcUpsOutputCurrent": lcUpsOutputCurrent,
       "lcUpsOutputVA": lcUpsOutputVA,
       "lcUpsOutputWatts": lcUpsOutputWatts,
       "lcUpsInverter": lcUpsInverter,
       "lcUpsInverterStatus": lcUpsInverterStatus,
       "lcUpsInverterTemp": lcUpsInverterTemp,
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
       "lcUpsAlarmOutputOverloadShutdown": lcUpsAlarmOutputOverloadShutdown,
       "lcUpsAlarmInputOverVoltage": lcUpsAlarmInputOverVoltage,
       "lcUpsAlarmBatteryBad": lcUpsAlarmBatteryBad,
       "lcUpsAlarmOnBattery": lcUpsAlarmOnBattery,
       "lcUpsAlarmStopNoticeIssued": lcUpsAlarmStopNoticeIssued,
       "lcUpsAlarmUpsOff": lcUpsAlarmUpsOff,
       "lcUpsAlarmInputFreqError": lcUpsAlarmInputFreqError,
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
       "lcUpsAlarmModuleSummary": lcUpsAlarmModuleSummary,
       "lcUpsLineCorrectionActive": lcUpsLineCorrectionActive,
       "lcUpsTest": lcUpsTest,
       "lcUpsTestBattery": lcUpsTestBattery,
       "lcUpsTestBatteryStatus": lcUpsTestBatteryStatus,
       "lcUpsTestDiag": lcUpsTestDiag,
       "lcUpsTestDiagStatus": lcUpsTestDiagStatus,
       "lcUpsControl": lcUpsControl,
       "lcUpsControlOutputOffDelay": lcUpsControlOutputOffDelay,
       "lcUpsControlOutputOnDelay": lcUpsControlOutputOnDelay,
       "lcUpsControlOutputOffTrapDelay": lcUpsControlOutputOffTrapDelay,
       "lcUpsControlOutputOnTrapDelay": lcUpsControlOutputOnTrapDelay,
       "lcUpsControlUnixShutdownDelay": lcUpsControlUnixShutdownDelay,
       "lcUpsControlUnixShutdownTrapDelay": lcUpsControlUnixShutdownTrapDelay,
       "lcUpsControlCancelCommands": lcUpsControlCancelCommands,
       "lcUpsControlRebootAgentDelay": lcUpsControlRebootAgentDelay,
       "lcUpsNominal": lcUpsNominal,
       "lcUpsNominalOutputVoltage": lcUpsNominalOutputVoltage,
       "lcUpsNominalInputVoltage": lcUpsNominalInputVoltage,
       "lcUpsNominalOutputVA": lcUpsNominalOutputVA,
       "lcUpsNominalOutputWatts": lcUpsNominalOutputWatts,
       "lcUpsNominalOutputFreq": lcUpsNominalOutputFreq,
       "lcUpsNominalInputFreq": lcUpsNominalInputFreq,
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
       "lcUpsOutputOffWarningTrap": lcUpsOutputOffWarningTrap,
       "lcUpsOutputOnTrap": lcUpsOutputOnTrap,
       "lcUpsOutputOnWarningTrap": lcUpsOutputOnWarningTrap,
       "lcUpsUnixShutdownTrap": lcUpsUnixShutdownTrap,
       "lcUpsUnixShutdownWarningTrap": lcUpsUnixShutdownWarningTrap,
       "lcUpsReceptOffTrap": lcUpsReceptOffTrap,
       "lcUpsReceptOffWarningTrap": lcUpsReceptOffWarningTrap,
       "lcUpsReceptOnTrap": lcUpsReceptOnTrap,
       "lcUpsReceptOnWarningTrap": lcUpsReceptOnWarningTrap,
       "lcUpsInputFreqErrorTrap": lcUpsInputFreqErrorTrap,
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
       "lcUpsSwitchedReceptacles": lcUpsSwitchedReceptacles,
       "lcUpsSwitchedReceptMaxNum": lcUpsSwitchedReceptMaxNum,
       "lcUpsSwitchedReceptTable": lcUpsSwitchedReceptTable,
       "lcUpsSwitchedReceptEntry": lcUpsSwitchedReceptEntry,
       "lcUpsSwitchedReceptIndex": lcUpsSwitchedReceptIndex,
       "lcUpsSwitchedReceptOnDelay": lcUpsSwitchedReceptOnDelay,
       "lcUpsSwitchedReceptOnTrapDelay": lcUpsSwitchedReceptOnTrapDelay,
       "lcUpsSwitchedReceptOffDelay": lcUpsSwitchedReceptOffDelay,
       "lcUpsSwitchedReceptOffTrapDelay": lcUpsSwitchedReceptOffTrapDelay,
       "lcUpsSwitchedReceptStatus": lcUpsSwitchedReceptStatus,
       "lcUpsSwitchedReceptLabel": lcUpsSwitchedReceptLabel,
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
       "lcUpsConfigModuleCount": lcUpsConfigModuleCount,
       "lcUpsConfigCurrentModule": lcUpsConfigCurrentModule,
       "lcUpsConfigAudibleStatus": lcUpsConfigAudibleStatus,
       "lcUpsConfigLowBattTime": lcUpsConfigLowBattTime,
       "lcUpsConfigAutoRestart": lcUpsConfigAutoRestart,
       "luUPStationS": luUPStationS,
       "lsUpsIdent": lsUpsIdent,
       "lsUpsIdentFirmwareVersion": lsUpsIdentFirmwareVersion,
       "lsUpsAlarm": lsUpsAlarm,
       "lsUpsAlarmConditions": lsUpsAlarmConditions,
       "lsUpsAlarmCheckAirFilter": lsUpsAlarmCheckAirFilter,
       "lsUpsTraps": lsUpsTraps,
       "lsUpsCheckAirFilterTrap": lsUpsCheckAirFilterTrap,
       "lsUpsConfig": lsUpsConfig,
       "lsUpsConfigBypassInstalled": lsUpsConfigBypassInstalled,
       "lsUpsBypass": lsUpsBypass,
       "lsUpsOnBypass": lsUpsOnBypass,
       "lsUpsBypassFrequency": lsUpsBypassFrequency,
       "lsUpsBypassNumLines": lsUpsBypassNumLines,
       "lsUpsBypassTable": lsUpsBypassTable,
       "lsUpsBypassEntry": lsUpsBypassEntry,
       "lsUpsBypassLine": lsUpsBypassLine,
       "lsUpsBypassVoltage": lsUpsBypassVoltage,
       "lsUpsBypassCurrent": lsUpsBypassCurrent,
       "luUPStationD": luUPStationD,
       "ldUpsInput": ldUpsInput,
       "ldUpsInputMaxVoltsSinceLastPoll": ldUpsInputMaxVoltsSinceLastPoll,
       "ldUpsInputMinVoltsSinceLastPoll": ldUpsInputMinVoltsSinceLastPoll,
       "ldUpsOutput": ldUpsOutput,
       "ldUpsOutputMaxVoltsSinceLastPoll": ldUpsOutputMaxVoltsSinceLastPoll,
       "ldUpsOutputMinVoltsSinceLastPoll": ldUpsOutputMinVoltsSinceLastPoll,
       "ldUpsAlarm": ldUpsAlarm,
       "ldUpsAlarmConditions": ldUpsAlarmConditions,
       "ldUpsAlarmDCOverVoltageShutdown": ldUpsAlarmDCOverVoltageShutdown,
       "ldUpsAlarmOutputShortShutdown": ldUpsAlarmOutputShortShutdown,
       "ldUpsAlarmLNReversedShutdown": ldUpsAlarmLNReversedShutdown,
       "ldUpsAlarmImminentShutdown": ldUpsAlarmImminentShutdown,
       "ldUpsAlarmInputFreqError": ldUpsAlarmInputFreqError,
       "ldUpsAlarmBoostOn": ldUpsAlarmBoostOn,
       "ldUpsAlarmReplaceBattery": ldUpsAlarmReplaceBattery,
       "ldUpsAlarmOutputOverVoltage": ldUpsAlarmOutputOverVoltage,
       "ldUpsAlarmOutputUnderVoltage": ldUpsAlarmOutputUnderVoltage,
       "ldUpsAlarmChargerFailed": ldUpsAlarmChargerFailed,
       "ldUpsTraps": ldUpsTraps,
       "ldUpsDCOverVoltageShutdownTrap": ldUpsDCOverVoltageShutdownTrap,
       "ldUpsOutputShortShutdownTrap": ldUpsOutputShortShutdownTrap,
       "ldUpsLNReversedShutdownTrap": ldUpsLNReversedShutdownTrap,
       "ldUpsImminentShutdownTrap": ldUpsImminentShutdownTrap,
       "ldUpsInputFreqErrorTrap": ldUpsInputFreqErrorTrap,
       "ldUpsOutputOverVoltageTrap": ldUpsOutputOverVoltageTrap,
       "ldUpsOutputUnderVoltageTrap": ldUpsOutputUnderVoltageTrap,
       "ldUpsChargerFailedTrap": ldUpsChargerFailedTrap,
       "luUPStationG": luUPStationG,
       "lgUpsAlarm": lgUpsAlarm,
       "lgUpsAlarmConditions": lgUpsAlarmConditions,
       "lgUpsAlarmDCOverVoltageShutdown": lgUpsAlarmDCOverVoltageShutdown,
       "lgUpsAlarmOutputShortShutdown": lgUpsAlarmOutputShortShutdown,
       "lgUpsAlarmLNReversedShutdown": lgUpsAlarmLNReversedShutdown,
       "lgUpsAlarmRemoteShutdown": lgUpsAlarmRemoteShutdown,
       "lgUpsAlarmInputUVOnStartup": lgUpsAlarmInputUVOnStartup,
       "lgUpsAlarmPFCFailedOnStartup": lgUpsAlarmPFCFailedOnStartup,
       "lgUpsTraps": lgUpsTraps,
       "lgUpsDCOverVoltageShutdownTrap": lgUpsDCOverVoltageShutdownTrap,
       "lgUpsOutputShortShutdownTrap": lgUpsOutputShortShutdownTrap,
       "lgUpsLNReversedShutdownTrap": lgUpsLNReversedShutdownTrap,
       "lgUpsInputUVOnStartupTrap": lgUpsInputUVOnStartupTrap,
       "luSeries300": luSeries300,
       "luExternal": luExternal,
       "luUPStationS3": luUPStationS3,
       "luSeries200": luSeries200,
       "luSeries200Input": luSeries200Input,
       "luSeries200InputMaxVoltsSinceLastPoll": luSeries200InputMaxVoltsSinceLastPoll,
       "luSeries200InputMinVoltsSinceLastPoll": luSeries200InputMinVoltsSinceLastPoll,
       "luSeries200Alarm": luSeries200Alarm,
       "luSeries200AlarmConditions": luSeries200AlarmConditions,
       "luSeries200AlarmInputFreqError": luSeries200AlarmInputFreqError,
       "luSeries200Config": luSeries200Config,
       "luSeries200ConfigBypassInstalled": luSeries200ConfigBypassInstalled,
       "luSeries200ConfigFrequencyChangerModel": luSeries200ConfigFrequencyChangerModel,
       "luSeries200Bypass": luSeries200Bypass,
       "luSeries200OnBypass": luSeries200OnBypass,
       "luSeries4300": luSeries4300,
       "ls43cUpsIdent": ls43cUpsIdent,
       "ls43cUpsIdentFirmwareVersion": ls43cUpsIdentFirmwareVersion,
       "ls43cUpsConfig": ls43cUpsConfig,
       "ls43cUpsConfigBypassInstalled": ls43cUpsConfigBypassInstalled,
       "ls43cUpsBypass": ls43cUpsBypass,
       "ls43cUpsOnBypass": ls43cUpsOnBypass,
       "ls43cUpsBypassFrequency": ls43cUpsBypassFrequency,
       "ls43cUpsBypassNumLines": ls43cUpsBypassNumLines,
       "ls43cUpsBypassTable": ls43cUpsBypassTable,
       "ls43cUpsBypassEntry": ls43cUpsBypassEntry,
       "ls43cUpsBypassLine": ls43cUpsBypassLine,
       "ls43cUpsBypassVoltage": ls43cUpsBypassVoltage,
       "ls43cUpsBypassCurrent": ls43cUpsBypassCurrent,
       "luUpsModule": luUpsModule,
       "luSystemCabinet": luSystemCabinet,
       "luUPStationGxt": luUPStationGxt,
       "luPowerSure": luPowerSure,
       "luExperimental": luExperimental,
       "luPrivate": luPrivate,
       "liebertEnvironment": liebertEnvironment,
       "leExtensions": leExtensions,
       "leSiteNet01": leSiteNet01,
       "envMIB": envMIB,
       "envIdent": envIdent,
       "envIdentManufacturer": envIdentManufacturer,
       "envIdentModel": envIdentModel,
       "envIdentSoftwareVersion": envIdentSoftwareVersion,
       "envIdentSpecific": envIdentSpecific,
       "envDigitalInputs": envDigitalInputs,
       "envDigInput1": envDigInput1,
       "envDigInput1State": envDigInput1State,
       "envDigInput1Label": envDigInput1Label,
       "envDigInput1Polarity": envDigInput1Polarity,
       "envDigInput1TrapEnabled": envDigInput1TrapEnabled,
       "envDigInput2": envDigInput2,
       "envDigInput2State": envDigInput2State,
       "envDigInput2Label": envDigInput2Label,
       "envDigInput2Polarity": envDigInput2Polarity,
       "envDigInput2TrapEnabled": envDigInput2TrapEnabled,
       "envDigInput3": envDigInput3,
       "envDigInput3State": envDigInput3State,
       "envDigInput3Label": envDigInput3Label,
       "envDigInput3Polarity": envDigInput3Polarity,
       "envDigInput3TrapEnabled": envDigInput3TrapEnabled,
       "envDigInput4": envDigInput4,
       "envDigInput4State": envDigInput4State,
       "envDigInput4Label": envDigInput4Label,
       "envDigInput4Polarity": envDigInput4Polarity,
       "envDigInput4TrapEnabled": envDigInput4TrapEnabled,
       "envDigInput5": envDigInput5,
       "envDigInput5State": envDigInput5State,
       "envDigInput5Label": envDigInput5Label,
       "envDigInput5Polarity": envDigInput5Polarity,
       "envDigInput5TrapEnabled": envDigInput5TrapEnabled,
       "envDigInput6": envDigInput6,
       "envDigInput6State": envDigInput6State,
       "envDigInput6Label": envDigInput6Label,
       "envDigInput6Polarity": envDigInput6Polarity,
       "envDigInput6TrapEnabled": envDigInput6TrapEnabled,
       "envDigInput7": envDigInput7,
       "envDigInput7State": envDigInput7State,
       "envDigInput7Label": envDigInput7Label,
       "envDigInput7Polarity": envDigInput7Polarity,
       "envDigInput7TrapEnabled": envDigInput7TrapEnabled,
       "envDigInput8": envDigInput8,
       "envDigInput8State": envDigInput8State,
       "envDigInput8Label": envDigInput8Label,
       "envDigInput8Polarity": envDigInput8Polarity,
       "envDigInput8TrapEnabled": envDigInput8TrapEnabled,
       "envDigInput9": envDigInput9,
       "envDigInput9State": envDigInput9State,
       "envDigInput9Label": envDigInput9Label,
       "envDigInput9Polarity": envDigInput9Polarity,
       "envDigInput9TrapEnabled": envDigInput9TrapEnabled,
       "envDigInput10": envDigInput10,
       "envDigInput10State": envDigInput10State,
       "envDigInput10Label": envDigInput10Label,
       "envDigInput10Polarity": envDigInput10Polarity,
       "envDigInput10TrapEnabled": envDigInput10TrapEnabled,
       "envRelays": envRelays,
       "envRelay1": envRelay1,
       "envRelay1State": envRelay1State,
       "envRelay1Label": envRelay1Label,
       "envRelay1Control": envRelay1Control,
       "envRelay2": envRelay2,
       "envRelay2State": envRelay2State,
       "envRelay2Label": envRelay2Label,
       "envRelay2Control": envRelay2Control,
       "envOutputs": envOutputs,
       "envAudible": envAudible,
       "envAudibleState": envAudibleState,
       "envAudibleControl": envAudibleControl,
       "envLED1": envLED1,
       "envLED1State": envLED1State,
       "envLED1Label": envLED1Label,
       "envLED1Control": envLED1Control,
       "envLED2": envLED2,
       "envLED2State": envLED2State,
       "envLED2Label": envLED2Label,
       "envLED2Control": envLED2Control,
       "envLED3": envLED3,
       "envLED3State": envLED3State,
       "envLED3Label": envLED3Label,
       "envLED3Control": envLED3Control,
       "envReceptacles": envReceptacles,
       "envReceptacle1": envReceptacle1,
       "envReceptacle1State": envReceptacle1State,
       "envReceptacle1Label": envReceptacle1Label,
       "envReceptacle1Control": envReceptacle1Control,
       "envReceptacle1Status": envReceptacle1Status,
       "envReceptacle1ReceptDelay": envReceptacle1ReceptDelay,
       "envReceptacle2": envReceptacle2,
       "envReceptacle2State": envReceptacle2State,
       "envReceptacle2Label": envReceptacle2Label,
       "envReceptacle2Control": envReceptacle2Control,
       "envReceptacle2Status": envReceptacle2Status,
       "envReceptacle2ReceptDelay": envReceptacle2ReceptDelay,
       "envReceptacle3": envReceptacle3,
       "envReceptacle3State": envReceptacle3State,
       "envReceptacle3Label": envReceptacle3Label,
       "envReceptacle3Control": envReceptacle3Control,
       "envReceptacle3Status": envReceptacle3Status,
       "envReceptacle3ReceptDelay": envReceptacle3ReceptDelay,
       "envReceptacle4": envReceptacle4,
       "envReceptacle4State": envReceptacle4State,
       "envReceptacle4Label": envReceptacle4Label,
       "envReceptacle4Control": envReceptacle4Control,
       "envReceptacle4Status": envReceptacle4Status,
       "envReceptacle4ReceptDelay": envReceptacle4ReceptDelay,
       "envReceptacle5": envReceptacle5,
       "envReceptacle5State": envReceptacle5State,
       "envReceptacle5Label": envReceptacle5Label,
       "envReceptacle5Control": envReceptacle5Control,
       "envReceptacle5Status": envReceptacle5Status,
       "envReceptacle5ReceptDelay": envReceptacle5ReceptDelay,
       "envReceptacle6": envReceptacle6,
       "envReceptacle6State": envReceptacle6State,
       "envReceptacle6Label": envReceptacle6Label,
       "envReceptacle6Control": envReceptacle6Control,
       "envReceptacle6Status": envReceptacle6Status,
       "envReceptacle6ReceptDelay": envReceptacle6ReceptDelay,
       "envReceptacleMaster": envReceptacleMaster,
       "envReceptacleMasterOnOff": envReceptacleMasterOnOff,
       "envReceptacleMasterDelay": envReceptacleMasterDelay,
       "envAlarms": envAlarms,
       "envSummaryAlarm": envSummaryAlarm,
       "envTemperatureSensors": envTemperatureSensors,
       "envTemperature1": envTemperature1,
       "envTemperature1State": envTemperature1State,
       "envTemperature1F": envTemperature1F,
       "envTemperature1C": envTemperature1C,
       "envTemperature1Label": envTemperature1Label,
       "envTemperature1OffsetF": envTemperature1OffsetF,
       "envTemperature1OffsetC": envTemperature1OffsetC,
       "envTemp1HighLimitF": envTemp1HighLimitF,
       "envTemp1HighLimitC": envTemp1HighLimitC,
       "envTemp1LowLimitF": envTemp1LowLimitF,
       "envTemp1LowLimitC": envTemp1LowLimitC,
       "envTemperature2": envTemperature2,
       "envTemperature2State": envTemperature2State,
       "envTemperature2F": envTemperature2F,
       "envTemperature2C": envTemperature2C,
       "envTemperature2Label": envTemperature2Label,
       "envTemperature2OffsetF": envTemperature2OffsetF,
       "envTemperature2OffsetC": envTemperature2OffsetC,
       "envTemp2HighLimitF": envTemp2HighLimitF,
       "envTemp2HighLimitC": envTemp2HighLimitC,
       "envTemp2LowLimitF": envTemp2LowLimitF,
       "envTemp2LowLimitC": envTemp2LowLimitC,
       "envTemperature3": envTemperature3,
       "envTemperature3State": envTemperature3State,
       "envTemperature3F": envTemperature3F,
       "envTemperature3C": envTemperature3C,
       "envTemperature3Label": envTemperature3Label,
       "envTemperature3OffsetF": envTemperature3OffsetF,
       "envTemperature3OffsetC": envTemperature3OffsetC,
       "envTemp3HighLimitF": envTemp3HighLimitF,
       "envTemp3HighLimitC": envTemp3HighLimitC,
       "envTemp3LowLimitF": envTemp3LowLimitF,
       "envTemp3LowLimitC": envTemp3LowLimitC,
       "envTemp3Calibrate": envTemp3Calibrate,
       "envHumiditySensors": envHumiditySensors,
       "envHumidity1": envHumidity1,
       "envHumidity1State": envHumidity1State,
       "envHumidity1RH": envHumidity1RH,
       "envHumidity1Label": envHumidity1Label,
       "envHumidity1Offset": envHumidity1Offset,
       "envHumidity1HighLimit": envHumidity1HighLimit,
       "envHumidity1LowLimit": envHumidity1LowLimit,
       "envHumidity2": envHumidity2,
       "envHumidity2State": envHumidity2State,
       "envHumidity2RH": envHumidity2RH,
       "envHumidity2Label": envHumidity2Label,
       "envHumidity2Offset": envHumidity2Offset,
       "envHumidity2HighLimit": envHumidity2HighLimit,
       "envHumidity2LowLimit": envHumidity2LowLimit,
       "envTraps": envTraps,
       "envSummaryAlarmTrap": envSummaryAlarmTrap,
       "envDigInput1TrueTrap": envDigInput1TrueTrap,
       "envDigInput1FalseTrap": envDigInput1FalseTrap,
       "envDigInput2TrueTrap": envDigInput2TrueTrap,
       "envDigInput2FalseTrap": envDigInput2FalseTrap,
       "envDigInput3TrueTrap": envDigInput3TrueTrap,
       "envDigInput3FalseTrap": envDigInput3FalseTrap,
       "envDigInput4TrueTrap": envDigInput4TrueTrap,
       "envDigInput4FalseTrap": envDigInput4FalseTrap,
       "envDigInput5TrueTrap": envDigInput5TrueTrap,
       "envDigInput5FalseTrap": envDigInput5FalseTrap,
       "envDigInput6TrueTrap": envDigInput6TrueTrap,
       "envDigInput6FalseTrap": envDigInput6FalseTrap,
       "envDigInput7TrueTrap": envDigInput7TrueTrap,
       "envDigInput7FalseTrap": envDigInput7FalseTrap,
       "envDigInput8TrueTrap": envDigInput8TrueTrap,
       "envDigInput8FalseTrap": envDigInput8FalseTrap,
       "envDigInput9TrueTrap": envDigInput9TrueTrap,
       "envDigInput9FalseTrap": envDigInput9FalseTrap,
       "envDigInput10TrueTrap": envDigInput10TrueTrap,
       "envDigInput10FalseTrap": envDigInput10FalseTrap,
       "envTemperature1HighTrap": envTemperature1HighTrap,
       "envTemperature1LowTrap": envTemperature1LowTrap,
       "envTemperature1NormalTrap": envTemperature1NormalTrap,
       "envTemperature2HighTrap": envTemperature2HighTrap,
       "envTemperature2LowTrap": envTemperature2LowTrap,
       "envTemperature2NormalTrap": envTemperature2NormalTrap,
       "envTemperature3HighTrap": envTemperature3HighTrap,
       "envTemperature3LowTrap": envTemperature3LowTrap,
       "envTemperature3NormalTrap": envTemperature3NormalTrap,
       "envHumidity1HighTrap": envHumidity1HighTrap,
       "envHumidity1LowTrap": envHumidity1LowTrap,
       "envHumidity1NormalTrap": envHumidity1NormalTrap,
       "envHumidity2HighTrap": envHumidity2HighTrap,
       "envHumidity2LowTrap": envHumidity2LowTrap,
       "envHumidity2NormalTrap": envHumidity2NormalTrap,
       "leExperimental": leExperimental,
       "lePrivate": lePrivate}
)
