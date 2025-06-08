# SNMP MIB module (NDS-DTH3-MODULATOR) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/news_digital_1855/NDS-DTH3-MODULATOR.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:44:39 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

ndsDTH3Encoder = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ModEnc_ObjectIdentity = ObjectIdentity
modEnc = _ModEnc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 9)
)


class _ModHardwareRelease_Type(DisplayString):
    """Custom type modHardwareRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ModHardwareRelease_Type.__name__ = "DisplayString"
_ModHardwareRelease_Object = MibScalar
modHardwareRelease = _ModHardwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 9, 1),
    _ModHardwareRelease_Type()
)
modHardwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modHardwareRelease.setStatus("current")


class _ModSoftwareRelease_Type(DisplayString):
    """Custom type modSoftwareRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ModSoftwareRelease_Type.__name__ = "DisplayString"
_ModSoftwareRelease_Object = MibScalar
modSoftwareRelease = _ModSoftwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 9, 2),
    _ModSoftwareRelease_Type()
)
modSoftwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modSoftwareRelease.setStatus("current")


class _ModFirmwareRelease_Type(DisplayString):
    """Custom type modFirmwareRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_ModFirmwareRelease_Type.__name__ = "DisplayString"
_ModFirmwareRelease_Object = MibScalar
modFirmwareRelease = _ModFirmwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 9, 3),
    _ModFirmwareRelease_Type()
)
modFirmwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modFirmwareRelease.setStatus("current")


class _ModType_Type(Integer32):
    """Custom type modType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 0),
          ("sat-Mod-3", 2))
    )


_ModType_Type.__name__ = "Integer32"
_ModType_Object = MibScalar
modType = _ModType_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 9, 4),
    _ModType_Type()
)
modType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modType.setStatus("current")
_ModnextTimeDate_Type = DateAndTime
_ModnextTimeDate_Object = MibScalar
modnextTimeDate = _ModnextTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 9, 5),
    _ModnextTimeDate_Type()
)
modnextTimeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modnextTimeDate.setStatus("current")
_ModTable_Object = MibTable
modTable = _ModTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 9, 6)
)
if mibBuilder.loadTexts:
    modTable.setStatus("current")
_ModEntry_Object = MibTableRow
modEntry = _ModEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 9, 6, 1)
)
modEntry.setIndexNames(
    (0, "NDS-DTH3-MODULATOR", "modCurrentNextIndex"),
)
if mibBuilder.loadTexts:
    modEntry.setStatus("current")


class _ModCurrentNextIndex_Type(Integer32):
    """Custom type modCurrentNextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("index-current", 1),
          ("index-next", 2))
    )


_ModCurrentNextIndex_Type.__name__ = "Integer32"
_ModCurrentNextIndex_Object = MibTableColumn
modCurrentNextIndex = _ModCurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 9, 6, 1, 1),
    _ModCurrentNextIndex_Type()
)
modCurrentNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modCurrentNextIndex.setStatus("current")


class _ModFormat_Type(Integer32):
    """Custom type modFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("baseband", 0),
          ("iFOutput", 1))
    )


_ModFormat_Type.__name__ = "Integer32"
_ModFormat_Object = MibTableColumn
modFormat = _ModFormat_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 9, 6, 1, 2),
    _ModFormat_Type()
)
modFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modFormat.setStatus("current")


class _ModOutput_Type(Integer32):
    """Custom type modOutput based on Integer32"""
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


_ModOutput_Type.__name__ = "Integer32"
_ModOutput_Object = MibTableColumn
modOutput = _ModOutput_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 9, 6, 1, 3),
    _ModOutput_Type()
)
modOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modOutput.setStatus("current")


class _ModPower_Type(Integer32):
    """Custom type modPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-200, 50),
    )


_ModPower_Type.__name__ = "Integer32"
_ModPower_Object = MibTableColumn
modPower = _ModPower_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 9, 6, 1, 4),
    _ModPower_Type()
)
modPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modPower.setStatus("current")


class _ModModulation_Type(Integer32):
    """Custom type modModulation based on Integer32"""
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


_ModModulation_Type.__name__ = "Integer32"
_ModModulation_Object = MibTableColumn
modModulation = _ModModulation_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 9, 6, 1, 5),
    _ModModulation_Type()
)
modModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modModulation.setStatus("current")


class _ModModulationType_Type(Integer32):
    """Custom type modModulationType based on Integer32"""
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
        *(("modBPSK", 0),
          ("modQPSK", 1),
          ("mod8PSK", 2),
          ("mod16QAM", 3))
    )


_ModModulationType_Type.__name__ = "Integer32"
_ModModulationType_Object = MibTableColumn
modModulationType = _ModModulationType_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 9, 6, 1, 6),
    _ModModulationType_Type()
)
modModulationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modModulationType.setStatus("current")


class _ModSymbolRate_Type(Integer32):
    """Custom type modSymbolRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000000, 37500000),
    )


_ModSymbolRate_Type.__name__ = "Integer32"
_ModSymbolRate_Object = MibTableColumn
modSymbolRate = _ModSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 9, 6, 1, 7),
    _ModSymbolRate_Type()
)
modSymbolRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modSymbolRate.setStatus("current")


class _ModPacketLength_Type(Integer32):
    """Custom type modPacketLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("packet188", 0),
          ("packet204", 1))
    )


_ModPacketLength_Type.__name__ = "Integer32"
_ModPacketLength_Object = MibTableColumn
modPacketLength = _ModPacketLength_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 9, 6, 1, 8),
    _ModPacketLength_Type()
)
modPacketLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modPacketLength.setStatus("current")


class _ModFECRate_Type(Integer32):
    """Custom type modFECRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("fec1-1", 1),
          ("fec1-2", 2),
          ("fec2-3", 3),
          ("fec3-4", 4),
          ("fec5-6", 6),
          ("fec7-8", 8),
          ("fec8-9", 9))
    )


_ModFECRate_Type.__name__ = "Integer32"
_ModFECRate_Object = MibTableColumn
modFECRate = _ModFECRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 9, 6, 1, 9),
    _ModFECRate_Type()
)
modFECRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modFECRate.setStatus("current")


class _ModOutputFrequency_Type(Integer32):
    """Custom type modOutputFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50000000, 1750000000),
    )


_ModOutputFrequency_Type.__name__ = "Integer32"
_ModOutputFrequency_Object = MibTableColumn
modOutputFrequency = _ModOutputFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 9, 6, 1, 10),
    _ModOutputFrequency_Type()
)
modOutputFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modOutputFrequency.setStatus("current")


class _ModSpectrumInversion_Type(Integer32):
    """Custom type modSpectrumInversion based on Integer32"""
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


_ModSpectrumInversion_Type.__name__ = "Integer32"
_ModSpectrumInversion_Object = MibTableColumn
modSpectrumInversion = _ModSpectrumInversion_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 9, 6, 1, 11),
    _ModSpectrumInversion_Type()
)
modSpectrumInversion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modSpectrumInversion.setStatus("current")


class _ModPolarisation_Type(Integer32):
    """Custom type modPolarisation based on Integer32"""
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
        *(("linear-horizontal", 0),
          ("linear-vertical", 1),
          ("circular-left", 2),
          ("circular-right", 3))
    )


_ModPolarisation_Type.__name__ = "Integer32"
_ModPolarisation_Object = MibTableColumn
modPolarisation = _ModPolarisation_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 9, 6, 1, 12),
    _ModPolarisation_Type()
)
modPolarisation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modPolarisation.setStatus("current")


class _ModSatFrequency_Type(Integer32):
    """Custom type modSatFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999999),
    )


_ModSatFrequency_Type.__name__ = "Integer32"
_ModSatFrequency_Object = MibTableColumn
modSatFrequency = _ModSatFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 9, 6, 1, 13),
    _ModSatFrequency_Type()
)
modSatFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modSatFrequency.setStatus("current")


class _ModWestEast_Type(Integer32):
    """Custom type modWestEast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("west", 0),
          ("east", 1))
    )


_ModWestEast_Type.__name__ = "Integer32"
_ModWestEast_Object = MibTableColumn
modWestEast = _ModWestEast_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 9, 6, 1, 14),
    _ModWestEast_Type()
)
modWestEast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modWestEast.setStatus("current")


class _ModOrbitalPosition_Type(Integer32):
    """Custom type modOrbitalPosition based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_ModOrbitalPosition_Type.__name__ = "Integer32"
_ModOrbitalPosition_Object = MibTableColumn
modOrbitalPosition = _ModOrbitalPosition_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 9, 6, 1, 15),
    _ModOrbitalPosition_Type()
)
modOrbitalPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modOrbitalPosition.setStatus("current")


class _ModRollOffFactor_Type(Integer32):
    """Custom type modRollOffFactor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("rolloff-25-per-cent", 0),
          ("rolloff-35-per-cent", 1))
    )


_ModRollOffFactor_Type.__name__ = "Integer32"
_ModRollOffFactor_Object = MibTableColumn
modRollOffFactor = _ModRollOffFactor_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 9, 6, 1, 16),
    _ModRollOffFactor_Type()
)
modRollOffFactor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modRollOffFactor.setStatus("current")


class _ModRefFrequencyOffset_Type(Integer32):
    """Custom type modRefFrequencyOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-40000, 25520),
    )


_ModRefFrequencyOffset_Type.__name__ = "Integer32"
_ModRefFrequencyOffset_Object = MibTableColumn
modRefFrequencyOffset = _ModRefFrequencyOffset_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 9, 6, 1, 17),
    _ModRefFrequencyOffset_Type()
)
modRefFrequencyOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    modRefFrequencyOffset.setStatus("current")


class _ModOutputType_Type(Integer32):
    """Custom type modOutputType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("output-BaseBand", 0),
          ("output-IF", 1),
          ("output-L-Band", 2))
    )


_ModOutputType_Type.__name__ = "Integer32"
_ModOutputType_Object = MibScalar
modOutputType = _ModOutputType_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 9, 7),
    _ModOutputType_Type()
)
modOutputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modOutputType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NDS-DTH3-MODULATOR",
    **{"ndsDTH3Encoder": ndsDTH3Encoder,
       "modEnc": modEnc,
       "modHardwareRelease": modHardwareRelease,
       "modSoftwareRelease": modSoftwareRelease,
       "modFirmwareRelease": modFirmwareRelease,
       "modType": modType,
       "modnextTimeDate": modnextTimeDate,
       "modTable": modTable,
       "modEntry": modEntry,
       "modCurrentNextIndex": modCurrentNextIndex,
       "modFormat": modFormat,
       "modOutput": modOutput,
       "modPower": modPower,
       "modModulation": modModulation,
       "modModulationType": modModulationType,
       "modSymbolRate": modSymbolRate,
       "modPacketLength": modPacketLength,
       "modFECRate": modFECRate,
       "modOutputFrequency": modOutputFrequency,
       "modSpectrumInversion": modSpectrumInversion,
       "modPolarisation": modPolarisation,
       "modSatFrequency": modSatFrequency,
       "modWestEast": modWestEast,
       "modOrbitalPosition": modOrbitalPosition,
       "modRollOffFactor": modRollOffFactor,
       "modRefFrequencyOffset": modRefFrequencyOffset,
       "modOutputType": modOutputType}
)
