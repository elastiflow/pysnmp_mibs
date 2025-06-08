# SNMP MIB module (NDS-DTH3-SDIRD) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/news_digital_1855/NDS-DTH3-SDIRD.mib
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

_SdirdEnc_ObjectIdentity = ObjectIdentity
sdirdEnc = _SdirdEnc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17)
)


class _SdirdPartNumber_Type(DisplayString):
    """Custom type sdirdPartNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdPartNumber_Type.__name__ = "DisplayString"
_SdirdPartNumber_Object = MibScalar
sdirdPartNumber = _SdirdPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 1),
    _SdirdPartNumber_Type()
)
sdirdPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdPartNumber.setStatus("current")


class _SdirdVersion_Type(DisplayString):
    """Custom type sdirdVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVersion_Type.__name__ = "DisplayString"
_SdirdVersion_Object = MibScalar
sdirdVersion = _SdirdVersion_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 2),
    _SdirdVersion_Type()
)
sdirdVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVersion.setStatus("current")
_SdirdnextTimeDate_Type = DateAndTime
_SdirdnextTimeDate_Object = MibScalar
sdirdnextTimeDate = _SdirdnextTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 3),
    _SdirdnextTimeDate_Type()
)
sdirdnextTimeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdnextTimeDate.setStatus("current")
_SdirdServiceTable_Object = MibTable
sdirdServiceTable = _SdirdServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 4)
)
if mibBuilder.loadTexts:
    sdirdServiceTable.setStatus("current")
_SdirdServiceTableEntry_Object = MibTableRow
sdirdServiceTableEntry = _SdirdServiceTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 4, 1)
)
sdirdServiceTableEntry.setIndexNames(
    (0, "NDS-DTH3-SDIRD", "sdirdServiceTableIndex"),
)
if mibBuilder.loadTexts:
    sdirdServiceTableEntry.setStatus("current")


class _SdirdServiceTableIndex_Type(Integer32):
    """Custom type sdirdServiceTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SdirdServiceTableIndex_Type.__name__ = "Integer32"
_SdirdServiceTableIndex_Object = MibTableColumn
sdirdServiceTableIndex = _SdirdServiceTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 4, 1, 1),
    _SdirdServiceTableIndex_Type()
)
sdirdServiceTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdServiceTableIndex.setStatus("current")


class _SdirdServiceTableEntryName_Type(DisplayString):
    """Custom type sdirdServiceTableEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdServiceTableEntryName_Type.__name__ = "DisplayString"
_SdirdServiceTableEntryName_Object = MibTableColumn
sdirdServiceTableEntryName = _SdirdServiceTableEntryName_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 4, 1, 2),
    _SdirdServiceTableEntryName_Type()
)
sdirdServiceTableEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdServiceTableEntryName.setStatus("current")


class _SdirdServiceIndex_Type(Integer32):
    """Custom type sdirdServiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SdirdServiceIndex_Type.__name__ = "Integer32"
_SdirdServiceIndex_Object = MibScalar
sdirdServiceIndex = _SdirdServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 5),
    _SdirdServiceIndex_Type()
)
sdirdServiceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdServiceIndex.setStatus("current")


class _SdirdServiceStatus_Type(DisplayString):
    """Custom type sdirdServiceStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdServiceStatus_Type.__name__ = "DisplayString"
_SdirdServiceStatus_Object = MibScalar
sdirdServiceStatus = _SdirdServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 6),
    _SdirdServiceStatus_Type()
)
sdirdServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdServiceStatus.setStatus("current")
_SdirdAudioStreamTable_Object = MibTable
sdirdAudioStreamTable = _SdirdAudioStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 7)
)
if mibBuilder.loadTexts:
    sdirdAudioStreamTable.setStatus("current")
_SdirdAudioStreamTableEntry_Object = MibTableRow
sdirdAudioStreamTableEntry = _SdirdAudioStreamTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 7, 1)
)
sdirdAudioStreamTableEntry.setIndexNames(
    (0, "NDS-DTH3-SDIRD", "sdirdAudioStreamTableIndex"),
)
if mibBuilder.loadTexts:
    sdirdAudioStreamTableEntry.setStatus("current")


class _SdirdAudioStreamTableIndex_Type(Integer32):
    """Custom type sdirdAudioStreamTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SdirdAudioStreamTableIndex_Type.__name__ = "Integer32"
_SdirdAudioStreamTableIndex_Object = MibTableColumn
sdirdAudioStreamTableIndex = _SdirdAudioStreamTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 7, 1, 1),
    _SdirdAudioStreamTableIndex_Type()
)
sdirdAudioStreamTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdAudioStreamTableIndex.setStatus("current")


class _SdirdAudioStreamTableEntryName_Type(DisplayString):
    """Custom type sdirdAudioStreamTableEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdAudioStreamTableEntryName_Type.__name__ = "DisplayString"
_SdirdAudioStreamTableEntryName_Object = MibTableColumn
sdirdAudioStreamTableEntryName = _SdirdAudioStreamTableEntryName_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 7, 1, 2),
    _SdirdAudioStreamTableEntryName_Type()
)
sdirdAudioStreamTableEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdAudioStreamTableEntryName.setStatus("current")


class _SdirdAudio1Index_Type(Integer32):
    """Custom type sdirdAudio1Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SdirdAudio1Index_Type.__name__ = "Integer32"
_SdirdAudio1Index_Object = MibScalar
sdirdAudio1Index = _SdirdAudio1Index_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 8),
    _SdirdAudio1Index_Type()
)
sdirdAudio1Index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdAudio1Index.setStatus("current")


class _SdirdAudio1Status_Type(DisplayString):
    """Custom type sdirdAudio1Status based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdAudio1Status_Type.__name__ = "DisplayString"
_SdirdAudio1Status_Object = MibScalar
sdirdAudio1Status = _SdirdAudio1Status_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 9),
    _SdirdAudio1Status_Type()
)
sdirdAudio1Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdAudio1Status.setStatus("current")


class _SdirdAudio2Index_Type(Integer32):
    """Custom type sdirdAudio2Index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SdirdAudio2Index_Type.__name__ = "Integer32"
_SdirdAudio2Index_Object = MibScalar
sdirdAudio2Index = _SdirdAudio2Index_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 10),
    _SdirdAudio2Index_Type()
)
sdirdAudio2Index.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdAudio2Index.setStatus("current")


class _SdirdAudio2Status_Type(DisplayString):
    """Custom type sdirdAudio2Status based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdAudio2Status_Type.__name__ = "DisplayString"
_SdirdAudio2Status_Object = MibScalar
sdirdAudio2Status = _SdirdAudio2Status_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 11),
    _SdirdAudio2Status_Type()
)
sdirdAudio2Status.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdAudio2Status.setStatus("current")
_SdirdSubtitlesStreamTable_Object = MibTable
sdirdSubtitlesStreamTable = _SdirdSubtitlesStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 12)
)
if mibBuilder.loadTexts:
    sdirdSubtitlesStreamTable.setStatus("current")
_SdirdSubtitlesStreamTableEntry_Object = MibTableRow
sdirdSubtitlesStreamTableEntry = _SdirdSubtitlesStreamTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 12, 1)
)
sdirdSubtitlesStreamTableEntry.setIndexNames(
    (0, "NDS-DTH3-SDIRD", "sdirdSubtitlesStreamTableIndex"),
)
if mibBuilder.loadTexts:
    sdirdSubtitlesStreamTableEntry.setStatus("current")


class _SdirdSubtitlesStreamTableIndex_Type(Integer32):
    """Custom type sdirdSubtitlesStreamTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SdirdSubtitlesStreamTableIndex_Type.__name__ = "Integer32"
_SdirdSubtitlesStreamTableIndex_Object = MibTableColumn
sdirdSubtitlesStreamTableIndex = _SdirdSubtitlesStreamTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 12, 1, 1),
    _SdirdSubtitlesStreamTableIndex_Type()
)
sdirdSubtitlesStreamTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdSubtitlesStreamTableIndex.setStatus("current")


class _SdirdSubtitlesStreamTableEntryName_Type(DisplayString):
    """Custom type sdirdSubtitlesStreamTableEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdSubtitlesStreamTableEntryName_Type.__name__ = "DisplayString"
_SdirdSubtitlesStreamTableEntryName_Object = MibTableColumn
sdirdSubtitlesStreamTableEntryName = _SdirdSubtitlesStreamTableEntryName_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 12, 1, 2),
    _SdirdSubtitlesStreamTableEntryName_Type()
)
sdirdSubtitlesStreamTableEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdSubtitlesStreamTableEntryName.setStatus("current")


class _SdirdSubtitlesIndex_Type(Integer32):
    """Custom type sdirdSubtitlesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SdirdSubtitlesIndex_Type.__name__ = "Integer32"
_SdirdSubtitlesIndex_Object = MibScalar
sdirdSubtitlesIndex = _SdirdSubtitlesIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 13),
    _SdirdSubtitlesIndex_Type()
)
sdirdSubtitlesIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdSubtitlesIndex.setStatus("current")


class _SdirdSubtitlesStatus_Type(DisplayString):
    """Custom type sdirdSubtitlesStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdSubtitlesStatus_Type.__name__ = "DisplayString"
_SdirdSubtitlesStatus_Object = MibScalar
sdirdSubtitlesStatus = _SdirdSubtitlesStatus_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 14),
    _SdirdSubtitlesStatus_Type()
)
sdirdSubtitlesStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdSubtitlesStatus.setStatus("current")
_SdirdTeletextStreamTable_Object = MibTable
sdirdTeletextStreamTable = _SdirdTeletextStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 15)
)
if mibBuilder.loadTexts:
    sdirdTeletextStreamTable.setStatus("current")
_SdirdTeletextStreamTableEntry_Object = MibTableRow
sdirdTeletextStreamTableEntry = _SdirdTeletextStreamTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 15, 1)
)
sdirdTeletextStreamTableEntry.setIndexNames(
    (0, "NDS-DTH3-SDIRD", "sdirdTeletextStreamTableIndex"),
)
if mibBuilder.loadTexts:
    sdirdTeletextStreamTableEntry.setStatus("current")


class _SdirdTeletextStreamTableIndex_Type(Integer32):
    """Custom type sdirdTeletextStreamTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SdirdTeletextStreamTableIndex_Type.__name__ = "Integer32"
_SdirdTeletextStreamTableIndex_Object = MibTableColumn
sdirdTeletextStreamTableIndex = _SdirdTeletextStreamTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 15, 1, 1),
    _SdirdTeletextStreamTableIndex_Type()
)
sdirdTeletextStreamTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdTeletextStreamTableIndex.setStatus("current")


class _SdirdTeletextStreamTableEntryName_Type(DisplayString):
    """Custom type sdirdTeletextStreamTableEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdTeletextStreamTableEntryName_Type.__name__ = "DisplayString"
_SdirdTeletextStreamTableEntryName_Object = MibTableColumn
sdirdTeletextStreamTableEntryName = _SdirdTeletextStreamTableEntryName_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 15, 1, 2),
    _SdirdTeletextStreamTableEntryName_Type()
)
sdirdTeletextStreamTableEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdTeletextStreamTableEntryName.setStatus("current")


class _SdirdTeletextIndex_Type(Integer32):
    """Custom type sdirdTeletextIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SdirdTeletextIndex_Type.__name__ = "Integer32"
_SdirdTeletextIndex_Object = MibScalar
sdirdTeletextIndex = _SdirdTeletextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 16),
    _SdirdTeletextIndex_Type()
)
sdirdTeletextIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdTeletextIndex.setStatus("current")


class _SdirdTeletextStatus_Type(DisplayString):
    """Custom type sdirdTeletextStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdTeletextStatus_Type.__name__ = "DisplayString"
_SdirdTeletextStatus_Object = MibScalar
sdirdTeletextStatus = _SdirdTeletextStatus_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 17),
    _SdirdTeletextStatus_Type()
)
sdirdTeletextStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdTeletextStatus.setStatus("current")
_SdirdAsyncStreamTable_Object = MibTable
sdirdAsyncStreamTable = _SdirdAsyncStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 18)
)
if mibBuilder.loadTexts:
    sdirdAsyncStreamTable.setStatus("current")
_SdirdAsyncStreamTableEntry_Object = MibTableRow
sdirdAsyncStreamTableEntry = _SdirdAsyncStreamTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 18, 1)
)
sdirdAsyncStreamTableEntry.setIndexNames(
    (0, "NDS-DTH3-SDIRD", "sdirdAsyncStreamTableIndex"),
)
if mibBuilder.loadTexts:
    sdirdAsyncStreamTableEntry.setStatus("current")


class _SdirdAsyncStreamTableIndex_Type(Integer32):
    """Custom type sdirdAsyncStreamTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SdirdAsyncStreamTableIndex_Type.__name__ = "Integer32"
_SdirdAsyncStreamTableIndex_Object = MibTableColumn
sdirdAsyncStreamTableIndex = _SdirdAsyncStreamTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 18, 1, 1),
    _SdirdAsyncStreamTableIndex_Type()
)
sdirdAsyncStreamTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdAsyncStreamTableIndex.setStatus("current")


class _SdirdAsyncStreamTableEntryName_Type(DisplayString):
    """Custom type sdirdAsyncStreamTableEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdAsyncStreamTableEntryName_Type.__name__ = "DisplayString"
_SdirdAsyncStreamTableEntryName_Object = MibTableColumn
sdirdAsyncStreamTableEntryName = _SdirdAsyncStreamTableEntryName_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 18, 1, 2),
    _SdirdAsyncStreamTableEntryName_Type()
)
sdirdAsyncStreamTableEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdAsyncStreamTableEntryName.setStatus("current")


class _SdirdAsyncIndex_Type(Integer32):
    """Custom type sdirdAsyncIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SdirdAsyncIndex_Type.__name__ = "Integer32"
_SdirdAsyncIndex_Object = MibScalar
sdirdAsyncIndex = _SdirdAsyncIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 19),
    _SdirdAsyncIndex_Type()
)
sdirdAsyncIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdAsyncIndex.setStatus("current")


class _SdirdAsyncStatus_Type(DisplayString):
    """Custom type sdirdAsyncStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdAsyncStatus_Type.__name__ = "DisplayString"
_SdirdAsyncStatus_Object = MibScalar
sdirdAsyncStatus = _SdirdAsyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 20),
    _SdirdAsyncStatus_Type()
)
sdirdAsyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdAsyncStatus.setStatus("current")
_SdirdSyncStreamTable_Object = MibTable
sdirdSyncStreamTable = _SdirdSyncStreamTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 21)
)
if mibBuilder.loadTexts:
    sdirdSyncStreamTable.setStatus("current")
_SdirdSyncStreamTableEntry_Object = MibTableRow
sdirdSyncStreamTableEntry = _SdirdSyncStreamTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 21, 1)
)
sdirdSyncStreamTableEntry.setIndexNames(
    (0, "NDS-DTH3-SDIRD", "sdirdSyncStreamTableIndex"),
)
if mibBuilder.loadTexts:
    sdirdSyncStreamTableEntry.setStatus("current")


class _SdirdSyncStreamTableIndex_Type(Integer32):
    """Custom type sdirdSyncStreamTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SdirdSyncStreamTableIndex_Type.__name__ = "Integer32"
_SdirdSyncStreamTableIndex_Object = MibTableColumn
sdirdSyncStreamTableIndex = _SdirdSyncStreamTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 21, 1, 1),
    _SdirdSyncStreamTableIndex_Type()
)
sdirdSyncStreamTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdSyncStreamTableIndex.setStatus("current")


class _SdirdSyncStreamTableEntryName_Type(DisplayString):
    """Custom type sdirdSyncStreamTableEntryName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdSyncStreamTableEntryName_Type.__name__ = "DisplayString"
_SdirdSyncStreamTableEntryName_Object = MibTableColumn
sdirdSyncStreamTableEntryName = _SdirdSyncStreamTableEntryName_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 21, 1, 2),
    _SdirdSyncStreamTableEntryName_Type()
)
sdirdSyncStreamTableEntryName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdSyncStreamTableEntryName.setStatus("current")


class _SdirdSyncIndex_Type(Integer32):
    """Custom type sdirdSyncIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_SdirdSyncIndex_Type.__name__ = "Integer32"
_SdirdSyncIndex_Object = MibScalar
sdirdSyncIndex = _SdirdSyncIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 22),
    _SdirdSyncIndex_Type()
)
sdirdSyncIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdSyncIndex.setStatus("current")


class _SdirdSyncStatus_Type(DisplayString):
    """Custom type sdirdSyncStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdSyncStatus_Type.__name__ = "DisplayString"
_SdirdSyncStatus_Object = MibScalar
sdirdSyncStatus = _SdirdSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 23),
    _SdirdSyncStatus_Type()
)
sdirdSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdSyncStatus.setStatus("current")
_SdirdVideoTable_Object = MibTable
sdirdVideoTable = _SdirdVideoTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 24)
)
if mibBuilder.loadTexts:
    sdirdVideoTable.setStatus("current")
_SdirdVideoTableEntry_Object = MibTableRow
sdirdVideoTableEntry = _SdirdVideoTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 24, 1)
)
sdirdVideoTableEntry.setIndexNames(
    (0, "NDS-DTH3-SDIRD", "sdirdVideoTableCurrentNextIndex"),
)
if mibBuilder.loadTexts:
    sdirdVideoTableEntry.setStatus("current")


class _SdirdVideoTableCurrentNextIndex_Type(Integer32):
    """Custom type sdirdVideoTableCurrentNextIndex based on Integer32"""
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


_SdirdVideoTableCurrentNextIndex_Type.__name__ = "Integer32"
_SdirdVideoTableCurrentNextIndex_Object = MibTableColumn
sdirdVideoTableCurrentNextIndex = _SdirdVideoTableCurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 24, 1, 1),
    _SdirdVideoTableCurrentNextIndex_Type()
)
sdirdVideoTableCurrentNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVideoTableCurrentNextIndex.setStatus("current")


class _SdirdVideoTableVideoStatus_Type(DisplayString):
    """Custom type sdirdVideoTableVideoStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVideoTableVideoStatus_Type.__name__ = "DisplayString"
_SdirdVideoTableVideoStatus_Object = MibTableColumn
sdirdVideoTableVideoStatus = _SdirdVideoTableVideoStatus_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 24, 1, 2),
    _SdirdVideoTableVideoStatus_Type()
)
sdirdVideoTableVideoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVideoTableVideoStatus.setStatus("current")


class _SdirdVideoTableVStopMode_Type(Integer32):
    """Custom type sdirdVideoTableVStopMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("blank", 0),
          ("freeze", 1))
    )


_SdirdVideoTableVStopMode_Type.__name__ = "Integer32"
_SdirdVideoTableVStopMode_Object = MibTableColumn
sdirdVideoTableVStopMode = _SdirdVideoTableVStopMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 24, 1, 3),
    _SdirdVideoTableVStopMode_Type()
)
sdirdVideoTableVStopMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdVideoTableVStopMode.setStatus("current")


class _SdirdVideoTableAspectRatio_Type(Integer32):
    """Custom type sdirdVideoTableAspectRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("aspect-4-3", 0),
          ("aspect-16-9", 1))
    )


_SdirdVideoTableAspectRatio_Type.__name__ = "Integer32"
_SdirdVideoTableAspectRatio_Object = MibTableColumn
sdirdVideoTableAspectRatio = _SdirdVideoTableAspectRatio_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 24, 1, 4),
    _SdirdVideoTableAspectRatio_Type()
)
sdirdVideoTableAspectRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdVideoTableAspectRatio.setStatus("current")


class _SdirdVideoTableVideoOutputSource_Type(Integer32):
    """Custom type sdirdVideoTableVideoOutputSource based on Integer32"""
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
              10,
              11,
              12,
              13,
              14,
              15,
              16)
        )
    )
    namedValues = NamedValues(
        *(("vNORMAL-VIDEO", 0),
          ("v625-PULSE-BAR", 1),
          ("v625-MULTIBURST", 2),
          ("v625-MAGENTA-STEP-PULSE-BAR", 3),
          ("v625-MAGENTA-STEP-FLAT-FIELD", 4),
          ("v625-FLAT-FIELD-RED", 5),
          ("v625-LUMINANCE-RAMP", 6),
          ("v625-BOWTIE", 7),
          ("v625-COLOURBARS", 8),
          ("v525-PULSE-BAR", 9),
          ("v525-MULTIBURST", 10),
          ("v525-MAGENTA-STEP-PULSE-BAR", 11),
          ("v525-MAGENTA-STEP-FLAT-FIELD", 12),
          ("v525-FLAT-FIELD-RED", 13),
          ("v525-LUMINANCE-RAMP", 14),
          ("v525-BOWTIE", 15),
          ("v525-COLOURBARS", 16))
    )


_SdirdVideoTableVideoOutputSource_Type.__name__ = "Integer32"
_SdirdVideoTableVideoOutputSource_Object = MibTableColumn
sdirdVideoTableVideoOutputSource = _SdirdVideoTableVideoOutputSource_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 24, 1, 5),
    _SdirdVideoTableVideoOutputSource_Type()
)
sdirdVideoTableVideoOutputSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdVideoTableVideoOutputSource.setStatus("current")


class _SdirdVideoTableStartLine525_Type(Integer32):
    """Custom type sdirdVideoTableStartLine525 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("line-22", 0),
          ("line-23", 1))
    )


_SdirdVideoTableStartLine525_Type.__name__ = "Integer32"
_SdirdVideoTableStartLine525_Object = MibTableColumn
sdirdVideoTableStartLine525 = _SdirdVideoTableStartLine525_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 24, 1, 6),
    _SdirdVideoTableStartLine525_Type()
)
sdirdVideoTableStartLine525.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdVideoTableStartLine525.setStatus("current")


class _SdirdVideoTableComposite525_Type(Integer32):
    """Custom type sdirdVideoTableComposite525 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ntsc-m", 0),
          ("ntsc-m-np", 1),
          ("pal-m", 2))
    )


_SdirdVideoTableComposite525_Type.__name__ = "Integer32"
_SdirdVideoTableComposite525_Object = MibTableColumn
sdirdVideoTableComposite525 = _SdirdVideoTableComposite525_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 24, 1, 7),
    _SdirdVideoTableComposite525_Type()
)
sdirdVideoTableComposite525.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdVideoTableComposite525.setStatus("current")


class _SdirdVideoTableComposite625_Type(Integer32):
    """Custom type sdirdVideoTableComposite625 based on Integer32"""
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
        *(("pal-i", 0),
          ("pal-bg", 1),
          ("secam", 2),
          ("pal-n", 3))
    )


_SdirdVideoTableComposite625_Type.__name__ = "Integer32"
_SdirdVideoTableComposite625_Object = MibTableColumn
sdirdVideoTableComposite625 = _SdirdVideoTableComposite625_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 24, 1, 8),
    _SdirdVideoTableComposite625_Type()
)
sdirdVideoTableComposite625.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdVideoTableComposite625.setStatus("current")


class _SdirdVideoTableRateBufferMode_Type(Integer32):
    """Custom type sdirdVideoTableRateBufferMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("small", 1))
    )


_SdirdVideoTableRateBufferMode_Type.__name__ = "Integer32"
_SdirdVideoTableRateBufferMode_Object = MibTableColumn
sdirdVideoTableRateBufferMode = _SdirdVideoTableRateBufferMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 24, 1, 9),
    _SdirdVideoTableRateBufferMode_Type()
)
sdirdVideoTableRateBufferMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdVideoTableRateBufferMode.setStatus("current")


class _SdirdVideoTableVideoDefOutput_Type(Integer32):
    """Custom type sdirdVideoTableVideoDefOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("video-525", 0),
          ("video-625", 1))
    )


_SdirdVideoTableVideoDefOutput_Type.__name__ = "Integer32"
_SdirdVideoTableVideoDefOutput_Object = MibTableColumn
sdirdVideoTableVideoDefOutput = _SdirdVideoTableVideoDefOutput_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 24, 1, 10),
    _SdirdVideoTableVideoDefOutput_Type()
)
sdirdVideoTableVideoDefOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdVideoTableVideoDefOutput.setStatus("current")


class _SdirdVideoTableVideoLevel_Type(Integer32):
    """Custom type sdirdVideoTableVideoLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(70, 130),
    )


_SdirdVideoTableVideoLevel_Type.__name__ = "Integer32"
_SdirdVideoTableVideoLevel_Object = MibTableColumn
sdirdVideoTableVideoLevel = _SdirdVideoTableVideoLevel_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 24, 1, 11),
    _SdirdVideoTableVideoLevel_Type()
)
sdirdVideoTableVideoLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdVideoTableVideoLevel.setStatus("current")


class _SdirdVideoTableEDHEnable_Type(Integer32):
    """Custom type sdirdVideoTableEDHEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SdirdVideoTableEDHEnable_Type.__name__ = "Integer32"
_SdirdVideoTableEDHEnable_Object = MibTableColumn
sdirdVideoTableEDHEnable = _SdirdVideoTableEDHEnable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 24, 1, 12),
    _SdirdVideoTableEDHEnable_Type()
)
sdirdVideoTableEDHEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdVideoTableEDHEnable.setStatus("current")


class _SdirdVideoTableEmbedAudioMode_Type(Integer32):
    """Custom type sdirdVideoTableEmbedAudioMode based on Integer32"""
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
        *(("no-audio", 0),
          ("audio-1-only", 1),
          ("audio-2-only", 2),
          ("audio-1-2", 3))
    )


_SdirdVideoTableEmbedAudioMode_Type.__name__ = "Integer32"
_SdirdVideoTableEmbedAudioMode_Object = MibTableColumn
sdirdVideoTableEmbedAudioMode = _SdirdVideoTableEmbedAudioMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 24, 1, 13),
    _SdirdVideoTableEmbedAudioMode_Type()
)
sdirdVideoTableEmbedAudioMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdVideoTableEmbedAudioMode.setStatus("current")


class _SdirdVideoTableEmbedDataID_Type(Integer32):
    """Custom type sdirdVideoTableEmbedDataID based on Integer32"""
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
        *(("did-2FF", 0),
          ("did-1FD", 1),
          ("did-1FB", 2),
          ("did-2F9", 3))
    )


_SdirdVideoTableEmbedDataID_Type.__name__ = "Integer32"
_SdirdVideoTableEmbedDataID_Object = MibTableColumn
sdirdVideoTableEmbedDataID = _SdirdVideoTableEmbedDataID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 24, 1, 14),
    _SdirdVideoTableEmbedDataID_Type()
)
sdirdVideoTableEmbedDataID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdVideoTableEmbedDataID.setStatus("current")


class _SdirdVideoTableVideoPID_Type(Integer32):
    """Custom type sdirdVideoTableVideoPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_SdirdVideoTableVideoPID_Type.__name__ = "Integer32"
_SdirdVideoTableVideoPID_Object = MibTableColumn
sdirdVideoTableVideoPID = _SdirdVideoTableVideoPID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 24, 1, 15),
    _SdirdVideoTableVideoPID_Type()
)
sdirdVideoTableVideoPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVideoTableVideoPID.setStatus("current")


class _SdirdVideoTableVideoHres_Type(Integer32):
    """Custom type sdirdVideoTableVideoHres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_SdirdVideoTableVideoHres_Type.__name__ = "Integer32"
_SdirdVideoTableVideoHres_Object = MibTableColumn
sdirdVideoTableVideoHres = _SdirdVideoTableVideoHres_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 24, 1, 16),
    _SdirdVideoTableVideoHres_Type()
)
sdirdVideoTableVideoHres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVideoTableVideoHres.setStatus("current")


class _SdirdVideoTableVideoVres_Type(Integer32):
    """Custom type sdirdVideoTableVideoVres based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_SdirdVideoTableVideoVres_Type.__name__ = "Integer32"
_SdirdVideoTableVideoVres_Object = MibTableColumn
sdirdVideoTableVideoVres = _SdirdVideoTableVideoVres_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 24, 1, 17),
    _SdirdVideoTableVideoVres_Type()
)
sdirdVideoTableVideoVres.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVideoTableVideoVres.setStatus("current")


class _SdirdVideoTableVideoMode_Type(DisplayString):
    """Custom type sdirdVideoTableVideoMode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVideoTableVideoMode_Type.__name__ = "DisplayString"
_SdirdVideoTableVideoMode_Object = MibTableColumn
sdirdVideoTableVideoMode = _SdirdVideoTableVideoMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 24, 1, 18),
    _SdirdVideoTableVideoMode_Type()
)
sdirdVideoTableVideoMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVideoTableVideoMode.setStatus("current")


class _SdirdVideoTableVideoLStd_Type(DisplayString):
    """Custom type sdirdVideoTableVideoLStd based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVideoTableVideoLStd_Type.__name__ = "DisplayString"
_SdirdVideoTableVideoLStd_Object = MibTableColumn
sdirdVideoTableVideoLStd = _SdirdVideoTableVideoLStd_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 24, 1, 19),
    _SdirdVideoTableVideoLStd_Type()
)
sdirdVideoTableVideoLStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVideoTableVideoLStd.setStatus("current")


class _SdirdVideoTableVideoPEL_Type(DisplayString):
    """Custom type sdirdVideoTableVideoPEL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVideoTableVideoPEL_Type.__name__ = "DisplayString"
_SdirdVideoTableVideoPEL_Object = MibTableColumn
sdirdVideoTableVideoPEL = _SdirdVideoTableVideoPEL_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 24, 1, 20),
    _SdirdVideoTableVideoPEL_Type()
)
sdirdVideoTableVideoPEL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVideoTableVideoPEL.setStatus("current")


class _SdirdVideoTableVideoFRate_Type(DisplayString):
    """Custom type sdirdVideoTableVideoFRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVideoTableVideoFRate_Type.__name__ = "DisplayString"
_SdirdVideoTableVideoFRate_Object = MibTableColumn
sdirdVideoTableVideoFRate = _SdirdVideoTableVideoFRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 24, 1, 21),
    _SdirdVideoTableVideoFRate_Type()
)
sdirdVideoTableVideoFRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVideoTableVideoFRate.setStatus("current")
_SdirdAudio1Table_Object = MibTable
sdirdAudio1Table = _SdirdAudio1Table_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 25)
)
if mibBuilder.loadTexts:
    sdirdAudio1Table.setStatus("current")
_SdirdAudio1TableEntry_Object = MibTableRow
sdirdAudio1TableEntry = _SdirdAudio1TableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 25, 1)
)
sdirdAudio1TableEntry.setIndexNames(
    (0, "NDS-DTH3-SDIRD", "sdirdAudio1TableCurrentNextIndex"),
)
if mibBuilder.loadTexts:
    sdirdAudio1TableEntry.setStatus("current")


class _SdirdAudio1TableCurrentNextIndex_Type(Integer32):
    """Custom type sdirdAudio1TableCurrentNextIndex based on Integer32"""
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


_SdirdAudio1TableCurrentNextIndex_Type.__name__ = "Integer32"
_SdirdAudio1TableCurrentNextIndex_Object = MibTableColumn
sdirdAudio1TableCurrentNextIndex = _SdirdAudio1TableCurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 25, 1, 1),
    _SdirdAudio1TableCurrentNextIndex_Type()
)
sdirdAudio1TableCurrentNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdAudio1TableCurrentNextIndex.setStatus("current")


class _SdirdAudio1TableDeflang_Type(Integer32):
    """Custom type sdirdAudio1TableDeflang based on Integer32"""
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
              58)
        )
    )
    namedValues = NamedValues(
        *(("arabic", 0),
          ("basa", 1),
          ("bengali", 2),
          ("bulgarian", 3),
          ("chinese", 4),
          ("czech", 5),
          ("dansih", 6),
          ("dutch", 7),
          ("english", 8),
          ("finnish", 9),
          ("french", 10),
          ("german", 11),
          ("greek", 12),
          ("gujurati", 13),
          ("hebrew", 14),
          ("hindi", 15),
          ("hungarian", 16),
          ("icelandic", 17),
          ("indonesian", 18),
          ("irish-gaelic", 19),
          ("irish-std", 20),
          ("italian", 21),
          ("japanese", 22),
          ("javanese", 23),
          ("korean", 24),
          ("malay", 25),
          ("norwegian", 26),
          ("polish", 27),
          ("portuguese", 28),
          ("romanian", 29),
          ("russian", 30),
          ("spanish", 31),
          ("swahili", 32),
          ("swedish", 33),
          ("thai", 34),
          ("turkish", 35),
          ("ukranianN", 36),
          ("urdu", 37),
          ("vietnamese", 38),
          ("back-sound-feed", 39),
          ("main", 40),
          ("aux", 41),
          ("int-sound", 42),
          ("audio-1", 43),
          ("audio-2", 44),
          ("audio-3", 45),
          ("audio-4", 46),
          ("audio-5", 47),
          ("audio-6", 48),
          ("audio-7", 49),
          ("audio-8", 50),
          ("audio-9", 51),
          ("audio-10", 52),
          ("audio-11", 53),
          ("audio-12", 54),
          ("audio-13", 55),
          ("audio-14", 56),
          ("audio-15", 57),
          ("audio-16", 58))
    )


_SdirdAudio1TableDeflang_Type.__name__ = "Integer32"
_SdirdAudio1TableDeflang_Object = MibTableColumn
sdirdAudio1TableDeflang = _SdirdAudio1TableDeflang_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 25, 1, 2),
    _SdirdAudio1TableDeflang_Type()
)
sdirdAudio1TableDeflang.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdAudio1TableDeflang.setStatus("current")


class _SdirdAudio1TableDownmixing_Type(Integer32):
    """Custom type sdirdAudio1TableDownmixing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("conventional", 0),
          ("surround", 1))
    )


_SdirdAudio1TableDownmixing_Type.__name__ = "Integer32"
_SdirdAudio1TableDownmixing_Object = MibTableColumn
sdirdAudio1TableDownmixing = _SdirdAudio1TableDownmixing_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 25, 1, 3),
    _SdirdAudio1TableDownmixing_Type()
)
sdirdAudio1TableDownmixing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdAudio1TableDownmixing.setStatus("current")


class _SdirdAudio1TableMuteState_Type(Integer32):
    """Custom type sdirdAudio1TableMuteState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mute-off", 0),
          ("mute-on", 1))
    )


_SdirdAudio1TableMuteState_Type.__name__ = "Integer32"
_SdirdAudio1TableMuteState_Object = MibTableColumn
sdirdAudio1TableMuteState = _SdirdAudio1TableMuteState_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 25, 1, 4),
    _SdirdAudio1TableMuteState_Type()
)
sdirdAudio1TableMuteState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdAudio1TableMuteState.setStatus("current")


class _SdirdAudio1TableRouting_Type(Integer32):
    """Custom type sdirdAudio1TableRouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal-stereo", 0),
          ("left-both", 1),
          ("right-both", 2))
    )


_SdirdAudio1TableRouting_Type.__name__ = "Integer32"
_SdirdAudio1TableRouting_Object = MibTableColumn
sdirdAudio1TableRouting = _SdirdAudio1TableRouting_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 25, 1, 5),
    _SdirdAudio1TableRouting_Type()
)
sdirdAudio1TableRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdAudio1TableRouting.setStatus("current")


class _SdirdAudio1TableOutput_Type(Integer32):
    """Custom type sdirdAudio1TableOutput based on Integer32"""
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
        *(("analogue", 0),
          ("iec958-cons", 1),
          ("iec958-ptr", 2),
          ("iec958-AC3-cons", 3))
    )


_SdirdAudio1TableOutput_Type.__name__ = "Integer32"
_SdirdAudio1TableOutput_Object = MibTableColumn
sdirdAudio1TableOutput = _SdirdAudio1TableOutput_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 25, 1, 6),
    _SdirdAudio1TableOutput_Type()
)
sdirdAudio1TableOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdAudio1TableOutput.setStatus("current")


class _SdirdAudio1TableAudioLeftSysClip_Type(Integer32):
    """Custom type sdirdAudio1TableAudioLeftSysClip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SdirdAudio1TableAudioLeftSysClip_Type.__name__ = "Integer32"
_SdirdAudio1TableAudioLeftSysClip_Object = MibTableColumn
sdirdAudio1TableAudioLeftSysClip = _SdirdAudio1TableAudioLeftSysClip_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 25, 1, 7),
    _SdirdAudio1TableAudioLeftSysClip_Type()
)
sdirdAudio1TableAudioLeftSysClip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdAudio1TableAudioLeftSysClip.setStatus("current")


class _SdirdAudio1TableAudioLeftOffset_Type(Integer32):
    """Custom type sdirdAudio1TableAudioLeftOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-30, 30),
    )


_SdirdAudio1TableAudioLeftOffset_Type.__name__ = "Integer32"
_SdirdAudio1TableAudioLeftOffset_Object = MibTableColumn
sdirdAudio1TableAudioLeftOffset = _SdirdAudio1TableAudioLeftOffset_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 25, 1, 8),
    _SdirdAudio1TableAudioLeftOffset_Type()
)
sdirdAudio1TableAudioLeftOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdAudio1TableAudioLeftOffset.setStatus("current")


class _SdirdAudio1TableAudioRightSysClip_Type(Integer32):
    """Custom type sdirdAudio1TableAudioRightSysClip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SdirdAudio1TableAudioRightSysClip_Type.__name__ = "Integer32"
_SdirdAudio1TableAudioRightSysClip_Object = MibTableColumn
sdirdAudio1TableAudioRightSysClip = _SdirdAudio1TableAudioRightSysClip_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 25, 1, 9),
    _SdirdAudio1TableAudioRightSysClip_Type()
)
sdirdAudio1TableAudioRightSysClip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdAudio1TableAudioRightSysClip.setStatus("current")


class _SdirdAudio1TableAudioRightOffset_Type(Integer32):
    """Custom type sdirdAudio1TableAudioRightOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-30, 30),
    )


_SdirdAudio1TableAudioRightOffset_Type.__name__ = "Integer32"
_SdirdAudio1TableAudioRightOffset_Object = MibTableColumn
sdirdAudio1TableAudioRightOffset = _SdirdAudio1TableAudioRightOffset_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 25, 1, 10),
    _SdirdAudio1TableAudioRightOffset_Type()
)
sdirdAudio1TableAudioRightOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdAudio1TableAudioRightOffset.setStatus("current")


class _SdirdAudio1TableAudioStatus_Type(DisplayString):
    """Custom type sdirdAudio1TableAudioStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdAudio1TableAudioStatus_Type.__name__ = "DisplayString"
_SdirdAudio1TableAudioStatus_Object = MibTableColumn
sdirdAudio1TableAudioStatus = _SdirdAudio1TableAudioStatus_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 25, 1, 11),
    _SdirdAudio1TableAudioStatus_Type()
)
sdirdAudio1TableAudioStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdAudio1TableAudioStatus.setStatus("current")


class _SdirdAudio1TableAudioPID_Type(Integer32):
    """Custom type sdirdAudio1TableAudioPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_SdirdAudio1TableAudioPID_Type.__name__ = "Integer32"
_SdirdAudio1TableAudioPID_Object = MibTableColumn
sdirdAudio1TableAudioPID = _SdirdAudio1TableAudioPID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 25, 1, 12),
    _SdirdAudio1TableAudioPID_Type()
)
sdirdAudio1TableAudioPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdAudio1TableAudioPID.setStatus("current")


class _SdirdAudio1TableSampleRate_Type(DisplayString):
    """Custom type sdirdAudio1TableSampleRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdAudio1TableSampleRate_Type.__name__ = "DisplayString"
_SdirdAudio1TableSampleRate_Object = MibTableColumn
sdirdAudio1TableSampleRate = _SdirdAudio1TableSampleRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 25, 1, 13),
    _SdirdAudio1TableSampleRate_Type()
)
sdirdAudio1TableSampleRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdAudio1TableSampleRate.setStatus("current")


class _SdirdAudio1TableAudioType_Type(DisplayString):
    """Custom type sdirdAudio1TableAudioType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdAudio1TableAudioType_Type.__name__ = "DisplayString"
_SdirdAudio1TableAudioType_Object = MibTableColumn
sdirdAudio1TableAudioType = _SdirdAudio1TableAudioType_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 25, 1, 14),
    _SdirdAudio1TableAudioType_Type()
)
sdirdAudio1TableAudioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdAudio1TableAudioType.setStatus("current")
_SdirdAudio2Table_Object = MibTable
sdirdAudio2Table = _SdirdAudio2Table_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 26)
)
if mibBuilder.loadTexts:
    sdirdAudio2Table.setStatus("current")
_SdirdAudio2TableEntry_Object = MibTableRow
sdirdAudio2TableEntry = _SdirdAudio2TableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 26, 1)
)
sdirdAudio2TableEntry.setIndexNames(
    (0, "NDS-DTH3-SDIRD", "sdirdAudio2TableCurrentNextIndex"),
)
if mibBuilder.loadTexts:
    sdirdAudio2TableEntry.setStatus("current")


class _SdirdAudio2TableCurrentNextIndex_Type(Integer32):
    """Custom type sdirdAudio2TableCurrentNextIndex based on Integer32"""
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


_SdirdAudio2TableCurrentNextIndex_Type.__name__ = "Integer32"
_SdirdAudio2TableCurrentNextIndex_Object = MibTableColumn
sdirdAudio2TableCurrentNextIndex = _SdirdAudio2TableCurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 26, 1, 1),
    _SdirdAudio2TableCurrentNextIndex_Type()
)
sdirdAudio2TableCurrentNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdAudio2TableCurrentNextIndex.setStatus("current")


class _SdirdAudio2TableDeflang_Type(Integer32):
    """Custom type sdirdAudio2TableDeflang based on Integer32"""
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
              58)
        )
    )
    namedValues = NamedValues(
        *(("arabic", 0),
          ("basa", 1),
          ("bengali", 2),
          ("bulgarian", 3),
          ("chinese", 4),
          ("czech", 5),
          ("dansih", 6),
          ("dutch", 7),
          ("english", 8),
          ("finnish", 9),
          ("french", 10),
          ("german", 11),
          ("greek", 12),
          ("gujurati", 13),
          ("hebrew", 14),
          ("hindi", 15),
          ("hungarian", 16),
          ("icelandic", 17),
          ("indonesian", 18),
          ("irish-gaelic", 19),
          ("irish-std", 20),
          ("italian", 21),
          ("japanese", 22),
          ("javanese", 23),
          ("korean", 24),
          ("malay", 25),
          ("norwegian", 26),
          ("polish", 27),
          ("portuguese", 28),
          ("romanian", 29),
          ("russian", 30),
          ("spanish", 31),
          ("swahili", 32),
          ("swedish", 33),
          ("thai", 34),
          ("turkish", 35),
          ("ukranianN", 36),
          ("urdu", 37),
          ("vietnamese", 38),
          ("back-sound-feed", 39),
          ("main", 40),
          ("aux", 41),
          ("int-sound", 42),
          ("audio-1", 43),
          ("audio-2", 44),
          ("audio-3", 45),
          ("audio-4", 46),
          ("audio-5", 47),
          ("audio-6", 48),
          ("audio-7", 49),
          ("audio-8", 50),
          ("audio-9", 51),
          ("audio-10", 52),
          ("audio-11", 53),
          ("audio-12", 54),
          ("audio-13", 55),
          ("audio-14", 56),
          ("audio-15", 57),
          ("audio-16", 58))
    )


_SdirdAudio2TableDeflang_Type.__name__ = "Integer32"
_SdirdAudio2TableDeflang_Object = MibTableColumn
sdirdAudio2TableDeflang = _SdirdAudio2TableDeflang_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 26, 1, 2),
    _SdirdAudio2TableDeflang_Type()
)
sdirdAudio2TableDeflang.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdAudio2TableDeflang.setStatus("current")


class _SdirdAudio2TableDownmixing_Type(Integer32):
    """Custom type sdirdAudio2TableDownmixing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("conventional", 0),
          ("surround", 1))
    )


_SdirdAudio2TableDownmixing_Type.__name__ = "Integer32"
_SdirdAudio2TableDownmixing_Object = MibTableColumn
sdirdAudio2TableDownmixing = _SdirdAudio2TableDownmixing_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 26, 1, 3),
    _SdirdAudio2TableDownmixing_Type()
)
sdirdAudio2TableDownmixing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdAudio2TableDownmixing.setStatus("current")


class _SdirdAudio2TableMuteState_Type(Integer32):
    """Custom type sdirdAudio2TableMuteState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("mute-off", 0),
          ("mute-on", 1))
    )


_SdirdAudio2TableMuteState_Type.__name__ = "Integer32"
_SdirdAudio2TableMuteState_Object = MibTableColumn
sdirdAudio2TableMuteState = _SdirdAudio2TableMuteState_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 26, 1, 4),
    _SdirdAudio2TableMuteState_Type()
)
sdirdAudio2TableMuteState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdAudio2TableMuteState.setStatus("current")


class _SdirdAudio2TableRouting_Type(Integer32):
    """Custom type sdirdAudio2TableRouting based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal-stereo", 0),
          ("left-both", 1),
          ("right-both", 2))
    )


_SdirdAudio2TableRouting_Type.__name__ = "Integer32"
_SdirdAudio2TableRouting_Object = MibTableColumn
sdirdAudio2TableRouting = _SdirdAudio2TableRouting_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 26, 1, 5),
    _SdirdAudio2TableRouting_Type()
)
sdirdAudio2TableRouting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdAudio2TableRouting.setStatus("current")


class _SdirdAudio2TableOutput_Type(Integer32):
    """Custom type sdirdAudio2TableOutput based on Integer32"""
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
        *(("analogue", 0),
          ("iec958-cons", 1),
          ("iec958-ptr", 2),
          ("iec958-AC3-cons", 3))
    )


_SdirdAudio2TableOutput_Type.__name__ = "Integer32"
_SdirdAudio2TableOutput_Object = MibTableColumn
sdirdAudio2TableOutput = _SdirdAudio2TableOutput_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 26, 1, 6),
    _SdirdAudio2TableOutput_Type()
)
sdirdAudio2TableOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdAudio2TableOutput.setStatus("current")


class _SdirdAudio2TableAudioLeftSysClip_Type(Integer32):
    """Custom type sdirdAudio2TableAudioLeftSysClip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SdirdAudio2TableAudioLeftSysClip_Type.__name__ = "Integer32"
_SdirdAudio2TableAudioLeftSysClip_Object = MibTableColumn
sdirdAudio2TableAudioLeftSysClip = _SdirdAudio2TableAudioLeftSysClip_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 26, 1, 7),
    _SdirdAudio2TableAudioLeftSysClip_Type()
)
sdirdAudio2TableAudioLeftSysClip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdAudio2TableAudioLeftSysClip.setStatus("current")


class _SdirdAudio2TableAudioLeftOffset_Type(Integer32):
    """Custom type sdirdAudio2TableAudioLeftOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-30, 30),
    )


_SdirdAudio2TableAudioLeftOffset_Type.__name__ = "Integer32"
_SdirdAudio2TableAudioLeftOffset_Object = MibTableColumn
sdirdAudio2TableAudioLeftOffset = _SdirdAudio2TableAudioLeftOffset_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 26, 1, 8),
    _SdirdAudio2TableAudioLeftOffset_Type()
)
sdirdAudio2TableAudioLeftOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdAudio2TableAudioLeftOffset.setStatus("current")


class _SdirdAudio2TableAudioRightSysClip_Type(Integer32):
    """Custom type sdirdAudio2TableAudioRightSysClip based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SdirdAudio2TableAudioRightSysClip_Type.__name__ = "Integer32"
_SdirdAudio2TableAudioRightSysClip_Object = MibTableColumn
sdirdAudio2TableAudioRightSysClip = _SdirdAudio2TableAudioRightSysClip_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 26, 1, 9),
    _SdirdAudio2TableAudioRightSysClip_Type()
)
sdirdAudio2TableAudioRightSysClip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdAudio2TableAudioRightSysClip.setStatus("current")


class _SdirdAudio2TableAudioRightOffset_Type(Integer32):
    """Custom type sdirdAudio2TableAudioRightOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-30, 30),
    )


_SdirdAudio2TableAudioRightOffset_Type.__name__ = "Integer32"
_SdirdAudio2TableAudioRightOffset_Object = MibTableColumn
sdirdAudio2TableAudioRightOffset = _SdirdAudio2TableAudioRightOffset_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 26, 1, 10),
    _SdirdAudio2TableAudioRightOffset_Type()
)
sdirdAudio2TableAudioRightOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdAudio2TableAudioRightOffset.setStatus("current")


class _SdirdAudio2TableAudioStatus_Type(DisplayString):
    """Custom type sdirdAudio2TableAudioStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdAudio2TableAudioStatus_Type.__name__ = "DisplayString"
_SdirdAudio2TableAudioStatus_Object = MibTableColumn
sdirdAudio2TableAudioStatus = _SdirdAudio2TableAudioStatus_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 26, 1, 11),
    _SdirdAudio2TableAudioStatus_Type()
)
sdirdAudio2TableAudioStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdAudio2TableAudioStatus.setStatus("current")


class _SdirdAudio2TableAudioPID_Type(Integer32):
    """Custom type sdirdAudio2TableAudioPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_SdirdAudio2TableAudioPID_Type.__name__ = "Integer32"
_SdirdAudio2TableAudioPID_Object = MibTableColumn
sdirdAudio2TableAudioPID = _SdirdAudio2TableAudioPID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 26, 1, 12),
    _SdirdAudio2TableAudioPID_Type()
)
sdirdAudio2TableAudioPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdAudio2TableAudioPID.setStatus("current")


class _SdirdAudio2TableSampleRate_Type(DisplayString):
    """Custom type sdirdAudio2TableSampleRate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdAudio2TableSampleRate_Type.__name__ = "DisplayString"
_SdirdAudio2TableSampleRate_Object = MibTableColumn
sdirdAudio2TableSampleRate = _SdirdAudio2TableSampleRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 26, 1, 13),
    _SdirdAudio2TableSampleRate_Type()
)
sdirdAudio2TableSampleRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdAudio2TableSampleRate.setStatus("current")


class _SdirdAudio2TableAudioType_Type(DisplayString):
    """Custom type sdirdAudio2TableAudioType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdAudio2TableAudioType_Type.__name__ = "DisplayString"
_SdirdAudio2TableAudioType_Object = MibTableColumn
sdirdAudio2TableAudioType = _SdirdAudio2TableAudioType_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 26, 1, 14),
    _SdirdAudio2TableAudioType_Type()
)
sdirdAudio2TableAudioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdAudio2TableAudioType.setStatus("current")
_SdirdVBITable_Object = MibTable
sdirdVBITable = _SdirdVBITable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27)
)
if mibBuilder.loadTexts:
    sdirdVBITable.setStatus("current")
_SdirdVBITableEntry_Object = MibTableRow
sdirdVBITableEntry = _SdirdVBITableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1)
)
sdirdVBITableEntry.setIndexNames(
    (0, "NDS-DTH3-SDIRD", "sdirdVBITableCurrentNextIndex"),
)
if mibBuilder.loadTexts:
    sdirdVBITableEntry.setStatus("current")


class _SdirdVBITableCurrentNextIndex_Type(Integer32):
    """Custom type sdirdVBITableCurrentNextIndex based on Integer32"""
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


_SdirdVBITableCurrentNextIndex_Type.__name__ = "Integer32"
_SdirdVBITableCurrentNextIndex_Object = MibTableColumn
sdirdVBITableCurrentNextIndex = _SdirdVBITableCurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 1),
    _SdirdVBITableCurrentNextIndex_Type()
)
sdirdVBITableCurrentNextIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdVBITableCurrentNextIndex.setStatus("current")


class _SdirdVBITableVITSEnable_Type(Integer32):
    """Custom type sdirdVBITableVITSEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vits-disabled", 0),
          ("vits-CCIR", 1),
          ("vits-FCC-UK", 2))
    )


_SdirdVBITableVITSEnable_Type.__name__ = "Integer32"
_SdirdVBITableVITSEnable_Object = MibTableColumn
sdirdVBITableVITSEnable = _SdirdVBITableVITSEnable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 2),
    _SdirdVBITableVITSEnable_Type()
)
sdirdVBITableVITSEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdVBITableVITSEnable.setStatus("current")


class _SdirdVBITableCCVCEnable_Type(Integer32):
    """Custom type sdirdVBITableCCVCEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SdirdVBITableCCVCEnable_Type.__name__ = "Integer32"
_SdirdVBITableCCVCEnable_Object = MibTableColumn
sdirdVBITableCCVCEnable = _SdirdVBITableCCVCEnable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 3),
    _SdirdVBITableCCVCEnable_Type()
)
sdirdVBITableCCVCEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdVBITableCCVCEnable.setStatus("current")


class _SdirdVBITableVITCEnable_Type(Integer32):
    """Custom type sdirdVBITableVITCEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SdirdVBITableVITCEnable_Type.__name__ = "Integer32"
_SdirdVBITableVITCEnable_Object = MibTableColumn
sdirdVBITableVITCEnable = _SdirdVBITableVITCEnable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 4),
    _SdirdVBITableVITCEnable_Type()
)
sdirdVBITableVITCEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdVBITableVITCEnable.setStatus("current")


class _SdirdVBITableGCREnable_Type(Integer32):
    """Custom type sdirdVBITableGCREnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_SdirdVBITableGCREnable_Type.__name__ = "Integer32"
_SdirdVBITableGCREnable_Object = MibTableColumn
sdirdVBITableGCREnable = _SdirdVBITableGCREnable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 5),
    _SdirdVBITableGCREnable_Type()
)
sdirdVBITableGCREnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdVBITableGCREnable.setStatus("current")


class _SdirdVBITableEnables525_Type(Integer32):
    """Custom type sdirdVBITableEnables525 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 511),
    )


_SdirdVBITableEnables525_Type.__name__ = "Integer32"
_SdirdVBITableEnables525_Object = MibTableColumn
sdirdVBITableEnables525 = _SdirdVBITableEnables525_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 6),
    _SdirdVBITableEnables525_Type()
)
sdirdVBITableEnables525.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdVBITableEnables525.setStatus("current")


class _SdirdVBITableEnables625_Type(Integer32):
    """Custom type sdirdVBITableEnables625 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_SdirdVBITableEnables625_Type.__name__ = "Integer32"
_SdirdVBITableEnables625_Object = MibTableColumn
sdirdVBITableEnables625 = _SdirdVBITableEnables625_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 7),
    _SdirdVBITableEnables625_Type()
)
sdirdVBITableEnables625.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdVBITableEnables625.setStatus("current")


class _SdirdVBITableCCVCStatus_Type(DisplayString):
    """Custom type sdirdVBITableCCVCStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableCCVCStatus_Type.__name__ = "DisplayString"
_SdirdVBITableCCVCStatus_Object = MibTableColumn
sdirdVBITableCCVCStatus = _SdirdVBITableCCVCStatus_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 8),
    _SdirdVBITableCCVCStatus_Type()
)
sdirdVBITableCCVCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableCCVCStatus.setStatus("current")


class _SdirdVBITableVBIStatus_Type(DisplayString):
    """Custom type sdirdVBITableVBIStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableVBIStatus_Type.__name__ = "DisplayString"
_SdirdVBITableVBIStatus_Object = MibTableColumn
sdirdVBITableVBIStatus = _SdirdVBITableVBIStatus_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 9),
    _SdirdVBITableVBIStatus_Type()
)
sdirdVBITableVBIStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableVBIStatus.setStatus("current")


class _SdirdVBITableVBI_InTypeLine11_Type(DisplayString):
    """Custom type sdirdVBITableVBI_InTypeLine11 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableVBI_InTypeLine11_Type.__name__ = "DisplayString"
_SdirdVBITableVBI_InTypeLine11_Object = MibTableColumn
sdirdVBITableVBI_InTypeLine11 = _SdirdVBITableVBI_InTypeLine11_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 10),
    _SdirdVBITableVBI_InTypeLine11_Type()
)
sdirdVBITableVBI_InTypeLine11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableVBI_InTypeLine11.setStatus("current")


class _SdirdVBITableVBI_InTypeLine12_Type(DisplayString):
    """Custom type sdirdVBITableVBI_InTypeLine12 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableVBI_InTypeLine12_Type.__name__ = "DisplayString"
_SdirdVBITableVBI_InTypeLine12_Object = MibTableColumn
sdirdVBITableVBI_InTypeLine12 = _SdirdVBITableVBI_InTypeLine12_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 11),
    _SdirdVBITableVBI_InTypeLine12_Type()
)
sdirdVBITableVBI_InTypeLine12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableVBI_InTypeLine12.setStatus("current")


class _SdirdVBITableVBI_InTypeLine13_Type(DisplayString):
    """Custom type sdirdVBITableVBI_InTypeLine13 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableVBI_InTypeLine13_Type.__name__ = "DisplayString"
_SdirdVBITableVBI_InTypeLine13_Object = MibTableColumn
sdirdVBITableVBI_InTypeLine13 = _SdirdVBITableVBI_InTypeLine13_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 12),
    _SdirdVBITableVBI_InTypeLine13_Type()
)
sdirdVBITableVBI_InTypeLine13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableVBI_InTypeLine13.setStatus("current")


class _SdirdVBITableVBI_InTypeLine14_Type(DisplayString):
    """Custom type sdirdVBITableVBI_InTypeLine14 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableVBI_InTypeLine14_Type.__name__ = "DisplayString"
_SdirdVBITableVBI_InTypeLine14_Object = MibTableColumn
sdirdVBITableVBI_InTypeLine14 = _SdirdVBITableVBI_InTypeLine14_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 13),
    _SdirdVBITableVBI_InTypeLine14_Type()
)
sdirdVBITableVBI_InTypeLine14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableVBI_InTypeLine14.setStatus("current")


class _SdirdVBITableVBI_InTypeLine15_Type(DisplayString):
    """Custom type sdirdVBITableVBI_InTypeLine15 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableVBI_InTypeLine15_Type.__name__ = "DisplayString"
_SdirdVBITableVBI_InTypeLine15_Object = MibTableColumn
sdirdVBITableVBI_InTypeLine15 = _SdirdVBITableVBI_InTypeLine15_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 14),
    _SdirdVBITableVBI_InTypeLine15_Type()
)
sdirdVBITableVBI_InTypeLine15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableVBI_InTypeLine15.setStatus("current")


class _SdirdVBITableVBI_InTypeLine16_Type(DisplayString):
    """Custom type sdirdVBITableVBI_InTypeLine16 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableVBI_InTypeLine16_Type.__name__ = "DisplayString"
_SdirdVBITableVBI_InTypeLine16_Object = MibTableColumn
sdirdVBITableVBI_InTypeLine16 = _SdirdVBITableVBI_InTypeLine16_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 15),
    _SdirdVBITableVBI_InTypeLine16_Type()
)
sdirdVBITableVBI_InTypeLine16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableVBI_InTypeLine16.setStatus("current")


class _SdirdVBITableVBI_InTypeLine17_Type(DisplayString):
    """Custom type sdirdVBITableVBI_InTypeLine17 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableVBI_InTypeLine17_Type.__name__ = "DisplayString"
_SdirdVBITableVBI_InTypeLine17_Object = MibTableColumn
sdirdVBITableVBI_InTypeLine17 = _SdirdVBITableVBI_InTypeLine17_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 16),
    _SdirdVBITableVBI_InTypeLine17_Type()
)
sdirdVBITableVBI_InTypeLine17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableVBI_InTypeLine17.setStatus("current")


class _SdirdVBITableVBI_InTypeLine18_Type(DisplayString):
    """Custom type sdirdVBITableVBI_InTypeLine18 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableVBI_InTypeLine18_Type.__name__ = "DisplayString"
_SdirdVBITableVBI_InTypeLine18_Object = MibTableColumn
sdirdVBITableVBI_InTypeLine18 = _SdirdVBITableVBI_InTypeLine18_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 17),
    _SdirdVBITableVBI_InTypeLine18_Type()
)
sdirdVBITableVBI_InTypeLine18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableVBI_InTypeLine18.setStatus("current")


class _SdirdVBITableVBI_InTypeLine19_Type(DisplayString):
    """Custom type sdirdVBITableVBI_InTypeLine19 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableVBI_InTypeLine19_Type.__name__ = "DisplayString"
_SdirdVBITableVBI_InTypeLine19_Object = MibTableColumn
sdirdVBITableVBI_InTypeLine19 = _SdirdVBITableVBI_InTypeLine19_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 18),
    _SdirdVBITableVBI_InTypeLine19_Type()
)
sdirdVBITableVBI_InTypeLine19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableVBI_InTypeLine19.setStatus("current")


class _SdirdVBITableVBI_InTypeLine20_Type(DisplayString):
    """Custom type sdirdVBITableVBI_InTypeLine20 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableVBI_InTypeLine20_Type.__name__ = "DisplayString"
_SdirdVBITableVBI_InTypeLine20_Object = MibTableColumn
sdirdVBITableVBI_InTypeLine20 = _SdirdVBITableVBI_InTypeLine20_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 19),
    _SdirdVBITableVBI_InTypeLine20_Type()
)
sdirdVBITableVBI_InTypeLine20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableVBI_InTypeLine20.setStatus("current")


class _SdirdVBITableVBI_InTypeLine21_Type(DisplayString):
    """Custom type sdirdVBITableVBI_InTypeLine21 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableVBI_InTypeLine21_Type.__name__ = "DisplayString"
_SdirdVBITableVBI_InTypeLine21_Object = MibTableColumn
sdirdVBITableVBI_InTypeLine21 = _SdirdVBITableVBI_InTypeLine21_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 20),
    _SdirdVBITableVBI_InTypeLine21_Type()
)
sdirdVBITableVBI_InTypeLine21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableVBI_InTypeLine21.setStatus("current")


class _SdirdVBITableVBI_InTypeLine22_Type(DisplayString):
    """Custom type sdirdVBITableVBI_InTypeLine22 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableVBI_InTypeLine22_Type.__name__ = "DisplayString"
_SdirdVBITableVBI_InTypeLine22_Object = MibTableColumn
sdirdVBITableVBI_InTypeLine22 = _SdirdVBITableVBI_InTypeLine22_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 21),
    _SdirdVBITableVBI_InTypeLine22_Type()
)
sdirdVBITableVBI_InTypeLine22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableVBI_InTypeLine22.setStatus("current")


class _SdirdVBITableVBI_InTypeLine23_Type(DisplayString):
    """Custom type sdirdVBITableVBI_InTypeLine23 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableVBI_InTypeLine23_Type.__name__ = "DisplayString"
_SdirdVBITableVBI_InTypeLine23_Object = MibTableColumn
sdirdVBITableVBI_InTypeLine23 = _SdirdVBITableVBI_InTypeLine23_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 22),
    _SdirdVBITableVBI_InTypeLine23_Type()
)
sdirdVBITableVBI_InTypeLine23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableVBI_InTypeLine23.setStatus("current")


class _SdirdVBITableVBI_OutTypeLine11_Type(DisplayString):
    """Custom type sdirdVBITableVBI_OutTypeLine11 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableVBI_OutTypeLine11_Type.__name__ = "DisplayString"
_SdirdVBITableVBI_OutTypeLine11_Object = MibTableColumn
sdirdVBITableVBI_OutTypeLine11 = _SdirdVBITableVBI_OutTypeLine11_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 23),
    _SdirdVBITableVBI_OutTypeLine11_Type()
)
sdirdVBITableVBI_OutTypeLine11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableVBI_OutTypeLine11.setStatus("current")


class _SdirdVBITableVBI_OutTypeLine12_Type(DisplayString):
    """Custom type sdirdVBITableVBI_OutTypeLine12 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableVBI_OutTypeLine12_Type.__name__ = "DisplayString"
_SdirdVBITableVBI_OutTypeLine12_Object = MibTableColumn
sdirdVBITableVBI_OutTypeLine12 = _SdirdVBITableVBI_OutTypeLine12_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 24),
    _SdirdVBITableVBI_OutTypeLine12_Type()
)
sdirdVBITableVBI_OutTypeLine12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableVBI_OutTypeLine12.setStatus("current")


class _SdirdVBITableVBI_OutTypeLine13_Type(DisplayString):
    """Custom type sdirdVBITableVBI_OutTypeLine13 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableVBI_OutTypeLine13_Type.__name__ = "DisplayString"
_SdirdVBITableVBI_OutTypeLine13_Object = MibTableColumn
sdirdVBITableVBI_OutTypeLine13 = _SdirdVBITableVBI_OutTypeLine13_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 25),
    _SdirdVBITableVBI_OutTypeLine13_Type()
)
sdirdVBITableVBI_OutTypeLine13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableVBI_OutTypeLine13.setStatus("current")


class _SdirdVBITableVBI_OutTypeLine14_Type(DisplayString):
    """Custom type sdirdVBITableVBI_OutTypeLine14 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableVBI_OutTypeLine14_Type.__name__ = "DisplayString"
_SdirdVBITableVBI_OutTypeLine14_Object = MibTableColumn
sdirdVBITableVBI_OutTypeLine14 = _SdirdVBITableVBI_OutTypeLine14_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 26),
    _SdirdVBITableVBI_OutTypeLine14_Type()
)
sdirdVBITableVBI_OutTypeLine14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableVBI_OutTypeLine14.setStatus("current")


class _SdirdVBITableVBI_OutTypeLine15_Type(DisplayString):
    """Custom type sdirdVBITableVBI_OutTypeLine15 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableVBI_OutTypeLine15_Type.__name__ = "DisplayString"
_SdirdVBITableVBI_OutTypeLine15_Object = MibTableColumn
sdirdVBITableVBI_OutTypeLine15 = _SdirdVBITableVBI_OutTypeLine15_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 27),
    _SdirdVBITableVBI_OutTypeLine15_Type()
)
sdirdVBITableVBI_OutTypeLine15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableVBI_OutTypeLine15.setStatus("current")


class _SdirdVBITableVBI_OutTypeLine16_Type(DisplayString):
    """Custom type sdirdVBITableVBI_OutTypeLine16 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableVBI_OutTypeLine16_Type.__name__ = "DisplayString"
_SdirdVBITableVBI_OutTypeLine16_Object = MibTableColumn
sdirdVBITableVBI_OutTypeLine16 = _SdirdVBITableVBI_OutTypeLine16_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 28),
    _SdirdVBITableVBI_OutTypeLine16_Type()
)
sdirdVBITableVBI_OutTypeLine16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableVBI_OutTypeLine16.setStatus("current")


class _SdirdVBITableVBI_OutTypeLine17_Type(DisplayString):
    """Custom type sdirdVBITableVBI_OutTypeLine17 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableVBI_OutTypeLine17_Type.__name__ = "DisplayString"
_SdirdVBITableVBI_OutTypeLine17_Object = MibTableColumn
sdirdVBITableVBI_OutTypeLine17 = _SdirdVBITableVBI_OutTypeLine17_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 29),
    _SdirdVBITableVBI_OutTypeLine17_Type()
)
sdirdVBITableVBI_OutTypeLine17.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableVBI_OutTypeLine17.setStatus("current")


class _SdirdVBITableVBI_OutTypeLine18_Type(DisplayString):
    """Custom type sdirdVBITableVBI_OutTypeLine18 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableVBI_OutTypeLine18_Type.__name__ = "DisplayString"
_SdirdVBITableVBI_OutTypeLine18_Object = MibTableColumn
sdirdVBITableVBI_OutTypeLine18 = _SdirdVBITableVBI_OutTypeLine18_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 30),
    _SdirdVBITableVBI_OutTypeLine18_Type()
)
sdirdVBITableVBI_OutTypeLine18.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableVBI_OutTypeLine18.setStatus("current")


class _SdirdVBITableVBI_OutTypeLine19_Type(DisplayString):
    """Custom type sdirdVBITableVBI_OutTypeLine19 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableVBI_OutTypeLine19_Type.__name__ = "DisplayString"
_SdirdVBITableVBI_OutTypeLine19_Object = MibTableColumn
sdirdVBITableVBI_OutTypeLine19 = _SdirdVBITableVBI_OutTypeLine19_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 31),
    _SdirdVBITableVBI_OutTypeLine19_Type()
)
sdirdVBITableVBI_OutTypeLine19.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableVBI_OutTypeLine19.setStatus("current")


class _SdirdVBITableVBI_OutTypeLine20_Type(DisplayString):
    """Custom type sdirdVBITableVBI_OutTypeLine20 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableVBI_OutTypeLine20_Type.__name__ = "DisplayString"
_SdirdVBITableVBI_OutTypeLine20_Object = MibTableColumn
sdirdVBITableVBI_OutTypeLine20 = _SdirdVBITableVBI_OutTypeLine20_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 32),
    _SdirdVBITableVBI_OutTypeLine20_Type()
)
sdirdVBITableVBI_OutTypeLine20.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableVBI_OutTypeLine20.setStatus("current")


class _SdirdVBITableVBI_OutTypeLine21_Type(DisplayString):
    """Custom type sdirdVBITableVBI_OutTypeLine21 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableVBI_OutTypeLine21_Type.__name__ = "DisplayString"
_SdirdVBITableVBI_OutTypeLine21_Object = MibTableColumn
sdirdVBITableVBI_OutTypeLine21 = _SdirdVBITableVBI_OutTypeLine21_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 33),
    _SdirdVBITableVBI_OutTypeLine21_Type()
)
sdirdVBITableVBI_OutTypeLine21.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableVBI_OutTypeLine21.setStatus("current")


class _SdirdVBITableVBI_OutTypeLine22_Type(DisplayString):
    """Custom type sdirdVBITableVBI_OutTypeLine22 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableVBI_OutTypeLine22_Type.__name__ = "DisplayString"
_SdirdVBITableVBI_OutTypeLine22_Object = MibTableColumn
sdirdVBITableVBI_OutTypeLine22 = _SdirdVBITableVBI_OutTypeLine22_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 34),
    _SdirdVBITableVBI_OutTypeLine22_Type()
)
sdirdVBITableVBI_OutTypeLine22.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableVBI_OutTypeLine22.setStatus("current")


class _SdirdVBITableVBI_OutTypeLine23_Type(DisplayString):
    """Custom type sdirdVBITableVBI_OutTypeLine23 based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdVBITableVBI_OutTypeLine23_Type.__name__ = "DisplayString"
_SdirdVBITableVBI_OutTypeLine23_Object = MibTableColumn
sdirdVBITableVBI_OutTypeLine23 = _SdirdVBITableVBI_OutTypeLine23_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 27, 1, 35),
    _SdirdVBITableVBI_OutTypeLine23_Type()
)
sdirdVBITableVBI_OutTypeLine23.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdVBITableVBI_OutTypeLine23.setStatus("current")
_SdirdDataTable_Object = MibTable
sdirdDataTable = _SdirdDataTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 28)
)
if mibBuilder.loadTexts:
    sdirdDataTable.setStatus("current")
_SdirdDataTableEntry_Object = MibTableRow
sdirdDataTableEntry = _SdirdDataTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 28, 1)
)
sdirdDataTableEntry.setIndexNames(
    (0, "NDS-DTH3-SDIRD", "sdirdDataTableCurrentNextIndex"),
)
if mibBuilder.loadTexts:
    sdirdDataTableEntry.setStatus("current")


class _SdirdDataTableCurrentNextIndex_Type(Integer32):
    """Custom type sdirdDataTableCurrentNextIndex based on Integer32"""
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


_SdirdDataTableCurrentNextIndex_Type.__name__ = "Integer32"
_SdirdDataTableCurrentNextIndex_Object = MibTableColumn
sdirdDataTableCurrentNextIndex = _SdirdDataTableCurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 28, 1, 1),
    _SdirdDataTableCurrentNextIndex_Type()
)
sdirdDataTableCurrentNextIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdDataTableCurrentNextIndex.setStatus("current")


class _SdirdDataTableSubtitlesLang_Type(Integer32):
    """Custom type sdirdDataTableSubtitlesLang based on Integer32"""
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
              58)
        )
    )
    namedValues = NamedValues(
        *(("arabic", 0),
          ("basa", 1),
          ("bengali", 2),
          ("bulgarian", 3),
          ("chinese", 4),
          ("czech", 5),
          ("dansih", 6),
          ("dutch", 7),
          ("english", 8),
          ("finnish", 9),
          ("french", 10),
          ("german", 11),
          ("greek", 12),
          ("gujurati", 13),
          ("hebrew", 14),
          ("hindi", 15),
          ("hungarian", 16),
          ("icelandic", 17),
          ("indonesian", 18),
          ("irish-gaelic", 19),
          ("irish-std", 20),
          ("italian", 21),
          ("japanese", 22),
          ("javanese", 23),
          ("korean", 24),
          ("malay", 25),
          ("norwegian", 26),
          ("polish", 27),
          ("portuguese", 28),
          ("romanian", 29),
          ("russian", 30),
          ("spanish", 31),
          ("swahili", 32),
          ("swedish", 33),
          ("thai", 34),
          ("turkish", 35),
          ("ukranianN", 36),
          ("urdu", 37),
          ("vietnamese", 38),
          ("back-sound-feed", 39),
          ("main", 40),
          ("aux", 41),
          ("int-sound", 42),
          ("audio-1", 43),
          ("audio-2", 44),
          ("audio-3", 45),
          ("audio-4", 46),
          ("audio-5", 47),
          ("audio-6", 48),
          ("audio-7", 49),
          ("audio-8", 50),
          ("audio-9", 51),
          ("audio-10", 52),
          ("audio-11", 53),
          ("audio-12", 54),
          ("audio-13", 55),
          ("audio-14", 56),
          ("audio-15", 57),
          ("audio-16", 58))
    )


_SdirdDataTableSubtitlesLang_Type.__name__ = "Integer32"
_SdirdDataTableSubtitlesLang_Object = MibTableColumn
sdirdDataTableSubtitlesLang = _SdirdDataTableSubtitlesLang_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 28, 1, 2),
    _SdirdDataTableSubtitlesLang_Type()
)
sdirdDataTableSubtitlesLang.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdDataTableSubtitlesLang.setStatus("current")


class _SdirdDataTableSubtitlesType_Type(Integer32):
    """Custom type sdirdDataTableSubtitlesType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("normal-sub", 0),
          ("normal-sub-4-3", 1),
          ("normal-sub-16-9", 2),
          ("normal-sub-2-1", 3),
          ("h-o-h-sub", 4),
          ("h-o-h-sub-4-3", 5),
          ("h-o-h-sub-16-9", 6),
          ("h-o-h-sub-2-1", 7))
    )


_SdirdDataTableSubtitlesType_Type.__name__ = "Integer32"
_SdirdDataTableSubtitlesType_Object = MibTableColumn
sdirdDataTableSubtitlesType = _SdirdDataTableSubtitlesType_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 28, 1, 3),
    _SdirdDataTableSubtitlesType_Type()
)
sdirdDataTableSubtitlesType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdDataTableSubtitlesType.setStatus("current")


class _SdirdDataTableSubtitlesStatus_Type(DisplayString):
    """Custom type sdirdDataTableSubtitlesStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdDataTableSubtitlesStatus_Type.__name__ = "DisplayString"
_SdirdDataTableSubtitlesStatus_Object = MibTableColumn
sdirdDataTableSubtitlesStatus = _SdirdDataTableSubtitlesStatus_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 28, 1, 4),
    _SdirdDataTableSubtitlesStatus_Type()
)
sdirdDataTableSubtitlesStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdDataTableSubtitlesStatus.setStatus("current")


class _SdirdDataTableTeletextStatus_Type(DisplayString):
    """Custom type sdirdDataTableTeletextStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdDataTableTeletextStatus_Type.__name__ = "DisplayString"
_SdirdDataTableTeletextStatus_Object = MibTableColumn
sdirdDataTableTeletextStatus = _SdirdDataTableTeletextStatus_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 28, 1, 5),
    _SdirdDataTableTeletextStatus_Type()
)
sdirdDataTableTeletextStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdDataTableTeletextStatus.setStatus("current")


class _SdirdDataTableAsyncStatus_Type(DisplayString):
    """Custom type sdirdDataTableAsyncStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdDataTableAsyncStatus_Type.__name__ = "DisplayString"
_SdirdDataTableAsyncStatus_Object = MibTableColumn
sdirdDataTableAsyncStatus = _SdirdDataTableAsyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 28, 1, 6),
    _SdirdDataTableAsyncStatus_Type()
)
sdirdDataTableAsyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdDataTableAsyncStatus.setStatus("current")


class _SdirdDataTableAsyncBaudrate_Type(DisplayString):
    """Custom type sdirdDataTableAsyncBaudrate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdDataTableAsyncBaudrate_Type.__name__ = "DisplayString"
_SdirdDataTableAsyncBaudrate_Object = MibTableColumn
sdirdDataTableAsyncBaudrate = _SdirdDataTableAsyncBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 28, 1, 7),
    _SdirdDataTableAsyncBaudrate_Type()
)
sdirdDataTableAsyncBaudrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdDataTableAsyncBaudrate.setStatus("current")


class _SdirdDataTableSyncStatus_Type(DisplayString):
    """Custom type sdirdDataTableSyncStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdDataTableSyncStatus_Type.__name__ = "DisplayString"
_SdirdDataTableSyncStatus_Object = MibTableColumn
sdirdDataTableSyncStatus = _SdirdDataTableSyncStatus_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 28, 1, 8),
    _SdirdDataTableSyncStatus_Type()
)
sdirdDataTableSyncStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdDataTableSyncStatus.setStatus("current")


class _SdirdDataTableSyncBitrate_Type(DisplayString):
    """Custom type sdirdDataTableSyncBitrate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdDataTableSyncBitrate_Type.__name__ = "DisplayString"
_SdirdDataTableSyncBitrate_Object = MibTableColumn
sdirdDataTableSyncBitrate = _SdirdDataTableSyncBitrate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 28, 1, 9),
    _SdirdDataTableSyncBitrate_Type()
)
sdirdDataTableSyncBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdDataTableSyncBitrate.setStatus("current")
_SdirdDemodTable_Object = MibTable
sdirdDemodTable = _SdirdDemodTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 29)
)
if mibBuilder.loadTexts:
    sdirdDemodTable.setStatus("current")
_SdirdDemodTableEntry_Object = MibTableRow
sdirdDemodTableEntry = _SdirdDemodTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 29, 1)
)
sdirdDemodTableEntry.setIndexNames(
    (0, "NDS-DTH3-SDIRD", "sdirdDemodTableCurrentNextIndex"),
)
if mibBuilder.loadTexts:
    sdirdDemodTableEntry.setStatus("current")


class _SdirdDemodTableCurrentNextIndex_Type(Integer32):
    """Custom type sdirdDemodTableCurrentNextIndex based on Integer32"""
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


_SdirdDemodTableCurrentNextIndex_Type.__name__ = "Integer32"
_SdirdDemodTableCurrentNextIndex_Object = MibTableColumn
sdirdDemodTableCurrentNextIndex = _SdirdDemodTableCurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 29, 1, 1),
    _SdirdDemodTableCurrentNextIndex_Type()
)
sdirdDemodTableCurrentNextIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdDemodTableCurrentNextIndex.setStatus("current")


class _SdirdDemodTableDemodStatus_Type(DisplayString):
    """Custom type sdirdDemodTableDemodStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdDemodTableDemodStatus_Type.__name__ = "DisplayString"
_SdirdDemodTableDemodStatus_Object = MibTableColumn
sdirdDemodTableDemodStatus = _SdirdDemodTableDemodStatus_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 29, 1, 2),
    _SdirdDemodTableDemodStatus_Type()
)
sdirdDemodTableDemodStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdDemodTableDemodStatus.setStatus("current")


class _SdirdDemodTableFrequency_Type(Integer32):
    """Custom type sdirdDemodTableFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(950000, 15150000),
    )


_SdirdDemodTableFrequency_Type.__name__ = "Integer32"
_SdirdDemodTableFrequency_Object = MibTableColumn
sdirdDemodTableFrequency = _SdirdDemodTableFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 29, 1, 3),
    _SdirdDemodTableFrequency_Type()
)
sdirdDemodTableFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdDemodTableFrequency.setStatus("current")


class _SdirdDemodTableIFFrequency_Type(Integer32):
    """Custom type sdirdDemodTableIFFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(70000000, 180000000),
    )


_SdirdDemodTableIFFrequency_Type.__name__ = "Integer32"
_SdirdDemodTableIFFrequency_Object = MibTableColumn
sdirdDemodTableIFFrequency = _SdirdDemodTableIFFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 29, 1, 4),
    _SdirdDemodTableIFFrequency_Type()
)
sdirdDemodTableIFFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdDemodTableIFFrequency.setStatus("current")


class _SdirdDemodTableSymbolRate_Type(Integer32):
    """Custom type sdirdDemodTableSymbolRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000000, 45000000),
    )


_SdirdDemodTableSymbolRate_Type.__name__ = "Integer32"
_SdirdDemodTableSymbolRate_Object = MibTableColumn
sdirdDemodTableSymbolRate = _SdirdDemodTableSymbolRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 29, 1, 5),
    _SdirdDemodTableSymbolRate_Type()
)
sdirdDemodTableSymbolRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdDemodTableSymbolRate.setStatus("current")


class _SdirdDemodTableFECRate_Type(Integer32):
    """Custom type sdirdDemodTableFECRate based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("fec1-2", 0),
          ("fec2-3", 1),
          ("fec3-4", 2),
          ("fec4-5", 3),
          ("fec5-6", 4),
          ("fec6-7", 5),
          ("fec7-8", 6),
          ("fec8-9", 7))
    )


_SdirdDemodTableFECRate_Type.__name__ = "Integer32"
_SdirdDemodTableFECRate_Object = MibTableColumn
sdirdDemodTableFECRate = _SdirdDemodTableFECRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 29, 1, 6),
    _SdirdDemodTableFECRate_Type()
)
sdirdDemodTableFECRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdDemodTableFECRate.setStatus("current")


class _SdirdDemodTablePolarization_Type(Integer32):
    """Custom type sdirdDemodTablePolarization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("horizontal", 0),
          ("vertical", 1))
    )


_SdirdDemodTablePolarization_Type.__name__ = "Integer32"
_SdirdDemodTablePolarization_Object = MibTableColumn
sdirdDemodTablePolarization = _SdirdDemodTablePolarization_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 29, 1, 7),
    _SdirdDemodTablePolarization_Type()
)
sdirdDemodTablePolarization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdDemodTablePolarization.setStatus("current")


class _SdirdDemodTableSatAerial_Type(Integer32):
    """Custom type sdirdDemodTableSatAerial based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aerial-0", 0),
          ("aerial-1", 1),
          ("aerial-2", 2))
    )


_SdirdDemodTableSatAerial_Type.__name__ = "Integer32"
_SdirdDemodTableSatAerial_Object = MibTableColumn
sdirdDemodTableSatAerial = _SdirdDemodTableSatAerial_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 29, 1, 8),
    _SdirdDemodTableSatAerial_Type()
)
sdirdDemodTableSatAerial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdDemodTableSatAerial.setStatus("current")


class _SdirdDemodTableBERLimit_Type(Integer32):
    """Custom type sdirdDemodTableBERLimit based on Integer32"""
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
              62)
        )
    )
    namedValues = NamedValues(
        *(("ber-limit-1E-7", 0),
          ("ber-limit-2E-7", 1),
          ("ber-limit-3E-7", 2),
          ("ber-limit-4E-7", 3),
          ("ber-limit-5E-7", 4),
          ("ber-limit-6E-7", 5),
          ("ber-limit-7E-7", 6),
          ("ber-limit-8E-7", 7),
          ("ber-limit-9E-7", 8),
          ("ber-limit-1E-6", 9),
          ("ber-limit-2E-6", 10),
          ("ber-limit-3E-6", 11),
          ("ber-limit-4E-6", 12),
          ("ber-limit-5E-6", 13),
          ("ber-limit-6E-6", 14),
          ("ber-limit-7E-6", 15),
          ("ber-limit-8E-6", 16),
          ("ber-limit-9E-6", 17),
          ("ber-limit-1E-5", 18),
          ("ber-limit-2E-5", 19),
          ("ber-limit-3E-5", 20),
          ("ber-limit-4E-5", 21),
          ("ber-limit-5E-5", 22),
          ("ber-limit-6E-5", 23),
          ("ber-limit-7E-5", 24),
          ("ber-limit-8E-5", 25),
          ("ber-limit-9E-5", 26),
          ("ber-limit-1E-4", 27),
          ("ber-limit-2E-4", 28),
          ("ber-limit-3E-4", 29),
          ("ber-limit-4E-4", 30),
          ("ber-limit-5E-4", 31),
          ("ber-limit-6E-4", 32),
          ("ber-limit-7E-4", 33),
          ("ber-limit-8E-4", 34),
          ("ber-limit-9E-4", 35),
          ("ber-limit-1E-3", 36),
          ("ber-limit-2E-3", 37),
          ("ber-limit-3E-3", 38),
          ("ber-limit-4E-3", 39),
          ("ber-limit-5E-3", 40),
          ("ber-limit-6E-3", 41),
          ("ber-limit-7E-3", 42),
          ("ber-limit-8E-3", 43),
          ("ber-limit-9E-3", 44),
          ("ber-limit-1E-2", 45),
          ("ber-limit-2E-2", 46),
          ("ber-limit-3E-2", 47),
          ("ber-limit-4E-2", 48),
          ("ber-limit-5E-2", 49),
          ("ber-limit-6E-2", 50),
          ("ber-limit-7E-2", 51),
          ("ber-limit-8E-2", 52),
          ("ber-limit-9E-2", 53),
          ("ber-limit-1E-1", 54),
          ("ber-limit-2E-1", 55),
          ("ber-limit-3E-1", 56),
          ("ber-limit-4E-1", 57),
          ("ber-limit-5E-1", 58),
          ("ber-limit-6E-1", 59),
          ("ber-limit-7E-1", 60),
          ("ber-limit-8E-1", 61),
          ("ber-limit-9E-1", 62))
    )


_SdirdDemodTableBERLimit_Type.__name__ = "Integer32"
_SdirdDemodTableBERLimit_Object = MibTableColumn
sdirdDemodTableBERLimit = _SdirdDemodTableBERLimit_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 29, 1, 9),
    _SdirdDemodTableBERLimit_Type()
)
sdirdDemodTableBERLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdDemodTableBERLimit.setStatus("current")


class _SdirdDemodTableLNBActive_Type(Integer32):
    """Custom type sdirdDemodTableLNBActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lnb-active", 0),
          ("direct-RF", 1))
    )


_SdirdDemodTableLNBActive_Type.__name__ = "Integer32"
_SdirdDemodTableLNBActive_Object = MibTableColumn
sdirdDemodTableLNBActive = _SdirdDemodTableLNBActive_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 29, 1, 10),
    _SdirdDemodTableLNBActive_Type()
)
sdirdDemodTableLNBActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdDemodTableLNBActive.setStatus("current")


class _SdirdDemodTableLNBLoFreq_Type(Integer32):
    """Custom type sdirdDemodTableLNBLoFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 13000000),
    )


_SdirdDemodTableLNBLoFreq_Type.__name__ = "Integer32"
_SdirdDemodTableLNBLoFreq_Object = MibTableColumn
sdirdDemodTableLNBLoFreq = _SdirdDemodTableLNBLoFreq_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 29, 1, 11),
    _SdirdDemodTableLNBLoFreq_Type()
)
sdirdDemodTableLNBLoFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdDemodTableLNBLoFreq.setStatus("current")


class _SdirdDemodTableLNBHiFreq_Type(Integer32):
    """Custom type sdirdDemodTableLNBHiFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 13000000),
    )


_SdirdDemodTableLNBHiFreq_Type.__name__ = "Integer32"
_SdirdDemodTableLNBHiFreq_Object = MibTableColumn
sdirdDemodTableLNBHiFreq = _SdirdDemodTableLNBHiFreq_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 29, 1, 12),
    _SdirdDemodTableLNBHiFreq_Type()
)
sdirdDemodTableLNBHiFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdDemodTableLNBHiFreq.setStatus("current")


class _SdirdDemodTableLNBSwitchFreq_Type(Integer32):
    """Custom type sdirdDemodTableLNBSwitchFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 14000000),
    )


_SdirdDemodTableLNBSwitchFreq_Type.__name__ = "Integer32"
_SdirdDemodTableLNBSwitchFreq_Object = MibTableColumn
sdirdDemodTableLNBSwitchFreq = _SdirdDemodTableLNBSwitchFreq_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 29, 1, 13),
    _SdirdDemodTableLNBSwitchFreq_Type()
)
sdirdDemodTableLNBSwitchFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdDemodTableLNBSwitchFreq.setStatus("current")


class _SdirdDemodTableLNBSupplyState_Type(Integer32):
    """Custom type sdirdDemodTableLNBSupplyState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("boost", 2))
    )


_SdirdDemodTableLNBSupplyState_Type.__name__ = "Integer32"
_SdirdDemodTableLNBSupplyState_Object = MibTableColumn
sdirdDemodTableLNBSupplyState = _SdirdDemodTableLNBSupplyState_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 29, 1, 14),
    _SdirdDemodTableLNBSupplyState_Type()
)
sdirdDemodTableLNBSupplyState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdDemodTableLNBSupplyState.setStatus("current")


class _SdirdDemodTableSearchRange_Type(Integer32):
    """Custom type sdirdDemodTableSearchRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5000),
    )


_SdirdDemodTableSearchRange_Type.__name__ = "Integer32"
_SdirdDemodTableSearchRange_Object = MibTableColumn
sdirdDemodTableSearchRange = _SdirdDemodTableSearchRange_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 29, 1, 15),
    _SdirdDemodTableSearchRange_Type()
)
sdirdDemodTableSearchRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdDemodTableSearchRange.setStatus("current")


class _SdirdDemodTableModulation_Type(Integer32):
    """Custom type sdirdDemodTableModulation based on Integer32"""
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
        *(("dmQPSK", 0),
          ("dmBPSK", 1),
          ("dm8PSK", 2),
          ("dm16QAM", 3))
    )


_SdirdDemodTableModulation_Type.__name__ = "Integer32"
_SdirdDemodTableModulation_Object = MibTableColumn
sdirdDemodTableModulation = _SdirdDemodTableModulation_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 29, 1, 16),
    _SdirdDemodTableModulation_Type()
)
sdirdDemodTableModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdDemodTableModulation.setStatus("current")


class _SdirdDemodTableLNBFaultStatus_Type(DisplayString):
    """Custom type sdirdDemodTableLNBFaultStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdDemodTableLNBFaultStatus_Type.__name__ = "DisplayString"
_SdirdDemodTableLNBFaultStatus_Object = MibTableColumn
sdirdDemodTableLNBFaultStatus = _SdirdDemodTableLNBFaultStatus_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 29, 1, 17),
    _SdirdDemodTableLNBFaultStatus_Type()
)
sdirdDemodTableLNBFaultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdDemodTableLNBFaultStatus.setStatus("current")


class _SdirdDemodTableSATStatus_Type(DisplayString):
    """Custom type sdirdDemodTableSATStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdDemodTableSATStatus_Type.__name__ = "DisplayString"
_SdirdDemodTableSATStatus_Object = MibTableColumn
sdirdDemodTableSATStatus = _SdirdDemodTableSATStatus_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 29, 1, 18),
    _SdirdDemodTableSATStatus_Type()
)
sdirdDemodTableSATStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdDemodTableSATStatus.setStatus("current")


class _SdirdDemodTableSatPartNo_Type(DisplayString):
    """Custom type sdirdDemodTableSatPartNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdDemodTableSatPartNo_Type.__name__ = "DisplayString"
_SdirdDemodTableSatPartNo_Object = MibTableColumn
sdirdDemodTableSatPartNo = _SdirdDemodTableSatPartNo_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 29, 1, 19),
    _SdirdDemodTableSatPartNo_Type()
)
sdirdDemodTableSatPartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdDemodTableSatPartNo.setStatus("current")


class _SdirdDemodTableSatCodeVersion_Type(DisplayString):
    """Custom type sdirdDemodTableSatCodeVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdDemodTableSatCodeVersion_Type.__name__ = "DisplayString"
_SdirdDemodTableSatCodeVersion_Object = MibTableColumn
sdirdDemodTableSatCodeVersion = _SdirdDemodTableSatCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 29, 1, 20),
    _SdirdDemodTableSatCodeVersion_Type()
)
sdirdDemodTableSatCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdDemodTableSatCodeVersion.setStatus("current")
_SdirdCATable_Object = MibTable
sdirdCATable = _SdirdCATable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 30)
)
if mibBuilder.loadTexts:
    sdirdCATable.setStatus("current")
_SdirdCATableEntry_Object = MibTableRow
sdirdCATableEntry = _SdirdCATableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 30, 1)
)
sdirdCATableEntry.setIndexNames(
    (0, "NDS-DTH3-SDIRD", "sdirdCATableCurrentNextIndex"),
)
if mibBuilder.loadTexts:
    sdirdCATableEntry.setStatus("current")


class _SdirdCATableCurrentNextIndex_Type(Integer32):
    """Custom type sdirdCATableCurrentNextIndex based on Integer32"""
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


_SdirdCATableCurrentNextIndex_Type.__name__ = "Integer32"
_SdirdCATableCurrentNextIndex_Object = MibTableColumn
sdirdCATableCurrentNextIndex = _SdirdCATableCurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 30, 1, 1),
    _SdirdCATableCurrentNextIndex_Type()
)
sdirdCATableCurrentNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdCATableCurrentNextIndex.setStatus("current")


class _SdirdCATableCAStatus_Type(DisplayString):
    """Custom type sdirdCATableCAStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdCATableCAStatus_Type.__name__ = "DisplayString"
_SdirdCATableCAStatus_Object = MibTableColumn
sdirdCATableCAStatus = _SdirdCATableCAStatus_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 30, 1, 2),
    _SdirdCATableCAStatus_Type()
)
sdirdCATableCAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdCATableCAStatus.setStatus("current")


class _SdirdCATableRASMode_Type(Integer32):
    """Custom type sdirdCATableRASMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("fixed-mode", 0),
          ("dsng-mode", 1))
    )


_SdirdCATableRASMode_Type.__name__ = "Integer32"
_SdirdCATableRASMode_Object = MibTableColumn
sdirdCATableRASMode = _SdirdCATableRASMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 30, 1, 3),
    _SdirdCATableRASMode_Type()
)
sdirdCATableRASMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdCATableRASMode.setStatus("current")


class _SdirdCATableDSNGKey_Type(Integer32):
    """Custom type sdirdCATableDSNGKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9999999),
    )


_SdirdCATableDSNGKey_Type.__name__ = "Integer32"
_SdirdCATableDSNGKey_Object = MibTableColumn
sdirdCATableDSNGKey = _SdirdCATableDSNGKey_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 30, 1, 4),
    _SdirdCATableDSNGKey_Type()
)
sdirdCATableDSNGKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdCATableDSNGKey.setStatus("current")


class _SdirdCATableBISSMode_Type(Integer32):
    """Custom type sdirdCATableBISSMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("biss-disabled", 0),
          ("biss-mode-1", 1),
          ("biss-mode-e", 2))
    )


_SdirdCATableBISSMode_Type.__name__ = "Integer32"
_SdirdCATableBISSMode_Object = MibTableColumn
sdirdCATableBISSMode = _SdirdCATableBISSMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 30, 1, 5),
    _SdirdCATableBISSMode_Type()
)
sdirdCATableBISSMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdCATableBISSMode.setStatus("current")


class _SdirdCATableBISSKeyString_Type(DisplayString):
    """Custom type sdirdCATableBISSKeyString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SdirdCATableBISSKeyString_Type.__name__ = "DisplayString"
_SdirdCATableBISSKeyString_Object = MibTableColumn
sdirdCATableBISSKeyString = _SdirdCATableBISSKeyString_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 30, 1, 6),
    _SdirdCATableBISSKeyString_Type()
)
sdirdCATableBISSKeyString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdCATableBISSKeyString.setStatus("current")


class _SdirdCATableBISSESWString_Type(DisplayString):
    """Custom type sdirdCATableBISSESWString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_SdirdCATableBISSESWString_Type.__name__ = "DisplayString"
_SdirdCATableBISSESWString_Object = MibTableColumn
sdirdCATableBISSESWString = _SdirdCATableBISSESWString_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 30, 1, 7),
    _SdirdCATableBISSESWString_Type()
)
sdirdCATableBISSESWString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdCATableBISSESWString.setStatus("current")
_SdirdSystemTable_Object = MibTable
sdirdSystemTable = _SdirdSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 31)
)
if mibBuilder.loadTexts:
    sdirdSystemTable.setStatus("current")
_SdirdSystemTableEntry_Object = MibTableRow
sdirdSystemTableEntry = _SdirdSystemTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 31, 1)
)
sdirdSystemTableEntry.setIndexNames(
    (0, "NDS-DTH3-SDIRD", "sdirdSystemTableTS-Lock"),
)
if mibBuilder.loadTexts:
    sdirdSystemTableEntry.setStatus("current")


class _SdirdSystemTableTS_Lock_Type(DisplayString):
    """Custom type sdirdSystemTableTS_Lock based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdSystemTableTS_Lock_Type.__name__ = "DisplayString"
_SdirdSystemTableTS_Lock_Object = MibTableColumn
sdirdSystemTableTS_Lock = _SdirdSystemTableTS_Lock_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 31, 1, 1),
    _SdirdSystemTableTS_Lock_Type()
)
sdirdSystemTableTS_Lock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdSystemTableTS_Lock.setStatus("current")


class _SdirdSystemTableNetworkName_Type(DisplayString):
    """Custom type sdirdSystemTableNetworkName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdSystemTableNetworkName_Type.__name__ = "DisplayString"
_SdirdSystemTableNetworkName_Object = MibTableColumn
sdirdSystemTableNetworkName = _SdirdSystemTableNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 31, 1, 2),
    _SdirdSystemTableNetworkName_Type()
)
sdirdSystemTableNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdSystemTableNetworkName.setStatus("current")


class _SdirdSystemTableNetworkID_Type(Integer32):
    """Custom type sdirdSystemTableNetworkID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_SdirdSystemTableNetworkID_Type.__name__ = "Integer32"
_SdirdSystemTableNetworkID_Object = MibTableColumn
sdirdSystemTableNetworkID = _SdirdSystemTableNetworkID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 31, 1, 3),
    _SdirdSystemTableNetworkID_Type()
)
sdirdSystemTableNetworkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdSystemTableNetworkID.setStatus("current")


class _SdirdSystemTableNumServices_Type(Integer32):
    """Custom type sdirdSystemTableNumServices based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SdirdSystemTableNumServices_Type.__name__ = "Integer32"
_SdirdSystemTableNumServices_Object = MibTableColumn
sdirdSystemTableNumServices = _SdirdSystemTableNumServices_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 31, 1, 4),
    _SdirdSystemTableNumServices_Type()
)
sdirdSystemTableNumServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdSystemTableNumServices.setStatus("current")


class _SdirdSystemTableCurrent_Service_ID_Type(Integer32):
    """Custom type sdirdSystemTableCurrent_Service_ID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_SdirdSystemTableCurrent_Service_ID_Type.__name__ = "Integer32"
_SdirdSystemTableCurrent_Service_ID_Object = MibTableColumn
sdirdSystemTableCurrent_Service_ID = _SdirdSystemTableCurrent_Service_ID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 31, 1, 5),
    _SdirdSystemTableCurrent_Service_ID_Type()
)
sdirdSystemTableCurrent_Service_ID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdSystemTableCurrent_Service_ID.setStatus("current")


class _SdirdSystemTableCurrent_TSID_Type(Integer32):
    """Custom type sdirdSystemTableCurrent_TSID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_SdirdSystemTableCurrent_TSID_Type.__name__ = "Integer32"
_SdirdSystemTableCurrent_TSID_Object = MibTableColumn
sdirdSystemTableCurrent_TSID = _SdirdSystemTableCurrent_TSID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 31, 1, 6),
    _SdirdSystemTableCurrent_TSID_Type()
)
sdirdSystemTableCurrent_TSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdSystemTableCurrent_TSID.setStatus("current")


class _SdirdSystemTableCurrent_ONID_Type(Integer32):
    """Custom type sdirdSystemTableCurrent_ONID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_SdirdSystemTableCurrent_ONID_Type.__name__ = "Integer32"
_SdirdSystemTableCurrent_ONID_Object = MibTableColumn
sdirdSystemTableCurrent_ONID = _SdirdSystemTableCurrent_ONID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 31, 1, 7),
    _SdirdSystemTableCurrent_ONID_Type()
)
sdirdSystemTableCurrent_ONID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdSystemTableCurrent_ONID.setStatus("current")


class _SdirdSystemTableModelNumber_Type(DisplayString):
    """Custom type sdirdSystemTableModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdSystemTableModelNumber_Type.__name__ = "DisplayString"
_SdirdSystemTableModelNumber_Object = MibTableColumn
sdirdSystemTableModelNumber = _SdirdSystemTableModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 31, 1, 8),
    _SdirdSystemTableModelNumber_Type()
)
sdirdSystemTableModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdSystemTableModelNumber.setStatus("current")


class _SdirdSystemTableModelOptions_Type(DisplayString):
    """Custom type sdirdSystemTableModelOptions based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdSystemTableModelOptions_Type.__name__ = "DisplayString"
_SdirdSystemTableModelOptions_Object = MibTableColumn
sdirdSystemTableModelOptions = _SdirdSystemTableModelOptions_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 31, 1, 9),
    _SdirdSystemTableModelOptions_Type()
)
sdirdSystemTableModelOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdSystemTableModelOptions.setStatus("current")


class _SdirdSystemTableComp_PartNo_Type(DisplayString):
    """Custom type sdirdSystemTableComp_PartNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdSystemTableComp_PartNo_Type.__name__ = "DisplayString"
_SdirdSystemTableComp_PartNo_Object = MibTableColumn
sdirdSystemTableComp_PartNo = _SdirdSystemTableComp_PartNo_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 31, 1, 10),
    _SdirdSystemTableComp_PartNo_Type()
)
sdirdSystemTableComp_PartNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdSystemTableComp_PartNo.setStatus("current")


class _SdirdSystemTableComp_SerialNo_Type(DisplayString):
    """Custom type sdirdSystemTableComp_SerialNo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdSystemTableComp_SerialNo_Type.__name__ = "DisplayString"
_SdirdSystemTableComp_SerialNo_Object = MibTableColumn
sdirdSystemTableComp_SerialNo = _SdirdSystemTableComp_SerialNo_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 31, 1, 11),
    _SdirdSystemTableComp_SerialNo_Type()
)
sdirdSystemTableComp_SerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdSystemTableComp_SerialNo.setStatus("current")


class _SdirdSystemTableComp_AppVer_Type(DisplayString):
    """Custom type sdirdSystemTableComp_AppVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdSystemTableComp_AppVer_Type.__name__ = "DisplayString"
_SdirdSystemTableComp_AppVer_Object = MibTableColumn
sdirdSystemTableComp_AppVer = _SdirdSystemTableComp_AppVer_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 31, 1, 12),
    _SdirdSystemTableComp_AppVer_Type()
)
sdirdSystemTableComp_AppVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdSystemTableComp_AppVer.setStatus("current")


class _SdirdSystemTableComp_CoreVer_Type(DisplayString):
    """Custom type sdirdSystemTableComp_CoreVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdSystemTableComp_CoreVer_Type.__name__ = "DisplayString"
_SdirdSystemTableComp_CoreVer_Object = MibTableColumn
sdirdSystemTableComp_CoreVer = _SdirdSystemTableComp_CoreVer_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 31, 1, 13),
    _SdirdSystemTableComp_CoreVer_Type()
)
sdirdSystemTableComp_CoreVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdSystemTableComp_CoreVer.setStatus("current")


class _SdirdSystemTableComp_DriverVer_Type(DisplayString):
    """Custom type sdirdSystemTableComp_DriverVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdSystemTableComp_DriverVer_Type.__name__ = "DisplayString"
_SdirdSystemTableComp_DriverVer_Object = MibTableColumn
sdirdSystemTableComp_DriverVer = _SdirdSystemTableComp_DriverVer_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 31, 1, 14),
    _SdirdSystemTableComp_DriverVer_Type()
)
sdirdSystemTableComp_DriverVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdSystemTableComp_DriverVer.setStatus("current")


class _SdirdSystemTableComp_DiagVer_Type(DisplayString):
    """Custom type sdirdSystemTableComp_DiagVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_SdirdSystemTableComp_DiagVer_Type.__name__ = "DisplayString"
_SdirdSystemTableComp_DiagVer_Object = MibTableColumn
sdirdSystemTableComp_DiagVer = _SdirdSystemTableComp_DiagVer_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 31, 1, 15),
    _SdirdSystemTableComp_DiagVer_Type()
)
sdirdSystemTableComp_DiagVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdSystemTableComp_DiagVer.setStatus("current")


class _SdirdSystemTableSystemStatus_Type(Integer32):
    """Custom type sdirdSystemTableSystemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SdirdSystemTableSystemStatus_Type.__name__ = "Integer32"
_SdirdSystemTableSystemStatus_Object = MibTableColumn
sdirdSystemTableSystemStatus = _SdirdSystemTableSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 31, 1, 16),
    _SdirdSystemTableSystemStatus_Type()
)
sdirdSystemTableSystemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdirdSystemTableSystemStatus.setStatus("current")


class _SdirdTSSource_Type(Integer32):
    """Custom type sdirdTSSource based on Integer32"""
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
        *(("sdirdTSSourceInternalClear", 0),
          ("sdirdTSSourceInternalEncrypted", 1),
          ("sdirdTSSourceDemod", 2),
          ("sdirdTSSourceSlot5", 3),
          ("sdirdTSSourceRemux", 4),
          ("sdirdTSSourceDemodASI", 5))
    )


_SdirdTSSource_Type.__name__ = "Integer32"
_SdirdTSSource_Object = MibScalar
sdirdTSSource = _SdirdTSSource_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 32),
    _SdirdTSSource_Type()
)
sdirdTSSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdTSSource.setStatus("current")


class _SdirdTrackingMode_Type(Integer32):
    """Custom type sdirdTrackingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("trackingModeOff", 0),
          ("trackingModeOn", 1))
    )


_SdirdTrackingMode_Type.__name__ = "Integer32"
_SdirdTrackingMode_Object = MibScalar
sdirdTrackingMode = _SdirdTrackingMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 33),
    _SdirdTrackingMode_Type()
)
sdirdTrackingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdTrackingMode.setStatus("current")


class _SdirdTSOMode_Type(Integer32):
    """Custom type sdirdTSOMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tso-Encrypted", 0),
          ("tso-Decrypted", 1))
    )


_SdirdTSOMode_Type.__name__ = "Integer32"
_SdirdTSOMode_Object = MibScalar
sdirdTSOMode = _SdirdTSOMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 34),
    _SdirdTSOMode_Type()
)
sdirdTSOMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdTSOMode.setStatus("current")


class _SdirdBISTRequired_Type(Integer32):
    """Custom type sdirdBISTRequired based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SdirdBISTRequired_Type.__name__ = "Integer32"
_SdirdBISTRequired_Object = MibScalar
sdirdBISTRequired = _SdirdBISTRequired_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 17, 35),
    _SdirdBISTRequired_Type()
)
sdirdBISTRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sdirdBISTRequired.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NDS-DTH3-SDIRD",
    **{"ndsDTH3Encoder": ndsDTH3Encoder,
       "sdirdEnc": sdirdEnc,
       "sdirdPartNumber": sdirdPartNumber,
       "sdirdVersion": sdirdVersion,
       "sdirdnextTimeDate": sdirdnextTimeDate,
       "sdirdServiceTable": sdirdServiceTable,
       "sdirdServiceTableEntry": sdirdServiceTableEntry,
       "sdirdServiceTableIndex": sdirdServiceTableIndex,
       "sdirdServiceTableEntryName": sdirdServiceTableEntryName,
       "sdirdServiceIndex": sdirdServiceIndex,
       "sdirdServiceStatus": sdirdServiceStatus,
       "sdirdAudioStreamTable": sdirdAudioStreamTable,
       "sdirdAudioStreamTableEntry": sdirdAudioStreamTableEntry,
       "sdirdAudioStreamTableIndex": sdirdAudioStreamTableIndex,
       "sdirdAudioStreamTableEntryName": sdirdAudioStreamTableEntryName,
       "sdirdAudio1Index": sdirdAudio1Index,
       "sdirdAudio1Status": sdirdAudio1Status,
       "sdirdAudio2Index": sdirdAudio2Index,
       "sdirdAudio2Status": sdirdAudio2Status,
       "sdirdSubtitlesStreamTable": sdirdSubtitlesStreamTable,
       "sdirdSubtitlesStreamTableEntry": sdirdSubtitlesStreamTableEntry,
       "sdirdSubtitlesStreamTableIndex": sdirdSubtitlesStreamTableIndex,
       "sdirdSubtitlesStreamTableEntryName": sdirdSubtitlesStreamTableEntryName,
       "sdirdSubtitlesIndex": sdirdSubtitlesIndex,
       "sdirdSubtitlesStatus": sdirdSubtitlesStatus,
       "sdirdTeletextStreamTable": sdirdTeletextStreamTable,
       "sdirdTeletextStreamTableEntry": sdirdTeletextStreamTableEntry,
       "sdirdTeletextStreamTableIndex": sdirdTeletextStreamTableIndex,
       "sdirdTeletextStreamTableEntryName": sdirdTeletextStreamTableEntryName,
       "sdirdTeletextIndex": sdirdTeletextIndex,
       "sdirdTeletextStatus": sdirdTeletextStatus,
       "sdirdAsyncStreamTable": sdirdAsyncStreamTable,
       "sdirdAsyncStreamTableEntry": sdirdAsyncStreamTableEntry,
       "sdirdAsyncStreamTableIndex": sdirdAsyncStreamTableIndex,
       "sdirdAsyncStreamTableEntryName": sdirdAsyncStreamTableEntryName,
       "sdirdAsyncIndex": sdirdAsyncIndex,
       "sdirdAsyncStatus": sdirdAsyncStatus,
       "sdirdSyncStreamTable": sdirdSyncStreamTable,
       "sdirdSyncStreamTableEntry": sdirdSyncStreamTableEntry,
       "sdirdSyncStreamTableIndex": sdirdSyncStreamTableIndex,
       "sdirdSyncStreamTableEntryName": sdirdSyncStreamTableEntryName,
       "sdirdSyncIndex": sdirdSyncIndex,
       "sdirdSyncStatus": sdirdSyncStatus,
       "sdirdVideoTable": sdirdVideoTable,
       "sdirdVideoTableEntry": sdirdVideoTableEntry,
       "sdirdVideoTableCurrentNextIndex": sdirdVideoTableCurrentNextIndex,
       "sdirdVideoTableVideoStatus": sdirdVideoTableVideoStatus,
       "sdirdVideoTableVStopMode": sdirdVideoTableVStopMode,
       "sdirdVideoTableAspectRatio": sdirdVideoTableAspectRatio,
       "sdirdVideoTableVideoOutputSource": sdirdVideoTableVideoOutputSource,
       "sdirdVideoTableStartLine525": sdirdVideoTableStartLine525,
       "sdirdVideoTableComposite525": sdirdVideoTableComposite525,
       "sdirdVideoTableComposite625": sdirdVideoTableComposite625,
       "sdirdVideoTableRateBufferMode": sdirdVideoTableRateBufferMode,
       "sdirdVideoTableVideoDefOutput": sdirdVideoTableVideoDefOutput,
       "sdirdVideoTableVideoLevel": sdirdVideoTableVideoLevel,
       "sdirdVideoTableEDHEnable": sdirdVideoTableEDHEnable,
       "sdirdVideoTableEmbedAudioMode": sdirdVideoTableEmbedAudioMode,
       "sdirdVideoTableEmbedDataID": sdirdVideoTableEmbedDataID,
       "sdirdVideoTableVideoPID": sdirdVideoTableVideoPID,
       "sdirdVideoTableVideoHres": sdirdVideoTableVideoHres,
       "sdirdVideoTableVideoVres": sdirdVideoTableVideoVres,
       "sdirdVideoTableVideoMode": sdirdVideoTableVideoMode,
       "sdirdVideoTableVideoLStd": sdirdVideoTableVideoLStd,
       "sdirdVideoTableVideoPEL": sdirdVideoTableVideoPEL,
       "sdirdVideoTableVideoFRate": sdirdVideoTableVideoFRate,
       "sdirdAudio1Table": sdirdAudio1Table,
       "sdirdAudio1TableEntry": sdirdAudio1TableEntry,
       "sdirdAudio1TableCurrentNextIndex": sdirdAudio1TableCurrentNextIndex,
       "sdirdAudio1TableDeflang": sdirdAudio1TableDeflang,
       "sdirdAudio1TableDownmixing": sdirdAudio1TableDownmixing,
       "sdirdAudio1TableMuteState": sdirdAudio1TableMuteState,
       "sdirdAudio1TableRouting": sdirdAudio1TableRouting,
       "sdirdAudio1TableOutput": sdirdAudio1TableOutput,
       "sdirdAudio1TableAudioLeftSysClip": sdirdAudio1TableAudioLeftSysClip,
       "sdirdAudio1TableAudioLeftOffset": sdirdAudio1TableAudioLeftOffset,
       "sdirdAudio1TableAudioRightSysClip": sdirdAudio1TableAudioRightSysClip,
       "sdirdAudio1TableAudioRightOffset": sdirdAudio1TableAudioRightOffset,
       "sdirdAudio1TableAudioStatus": sdirdAudio1TableAudioStatus,
       "sdirdAudio1TableAudioPID": sdirdAudio1TableAudioPID,
       "sdirdAudio1TableSampleRate": sdirdAudio1TableSampleRate,
       "sdirdAudio1TableAudioType": sdirdAudio1TableAudioType,
       "sdirdAudio2Table": sdirdAudio2Table,
       "sdirdAudio2TableEntry": sdirdAudio2TableEntry,
       "sdirdAudio2TableCurrentNextIndex": sdirdAudio2TableCurrentNextIndex,
       "sdirdAudio2TableDeflang": sdirdAudio2TableDeflang,
       "sdirdAudio2TableDownmixing": sdirdAudio2TableDownmixing,
       "sdirdAudio2TableMuteState": sdirdAudio2TableMuteState,
       "sdirdAudio2TableRouting": sdirdAudio2TableRouting,
       "sdirdAudio2TableOutput": sdirdAudio2TableOutput,
       "sdirdAudio2TableAudioLeftSysClip": sdirdAudio2TableAudioLeftSysClip,
       "sdirdAudio2TableAudioLeftOffset": sdirdAudio2TableAudioLeftOffset,
       "sdirdAudio2TableAudioRightSysClip": sdirdAudio2TableAudioRightSysClip,
       "sdirdAudio2TableAudioRightOffset": sdirdAudio2TableAudioRightOffset,
       "sdirdAudio2TableAudioStatus": sdirdAudio2TableAudioStatus,
       "sdirdAudio2TableAudioPID": sdirdAudio2TableAudioPID,
       "sdirdAudio2TableSampleRate": sdirdAudio2TableSampleRate,
       "sdirdAudio2TableAudioType": sdirdAudio2TableAudioType,
       "sdirdVBITable": sdirdVBITable,
       "sdirdVBITableEntry": sdirdVBITableEntry,
       "sdirdVBITableCurrentNextIndex": sdirdVBITableCurrentNextIndex,
       "sdirdVBITableVITSEnable": sdirdVBITableVITSEnable,
       "sdirdVBITableCCVCEnable": sdirdVBITableCCVCEnable,
       "sdirdVBITableVITCEnable": sdirdVBITableVITCEnable,
       "sdirdVBITableGCREnable": sdirdVBITableGCREnable,
       "sdirdVBITableEnables525": sdirdVBITableEnables525,
       "sdirdVBITableEnables625": sdirdVBITableEnables625,
       "sdirdVBITableCCVCStatus": sdirdVBITableCCVCStatus,
       "sdirdVBITableVBIStatus": sdirdVBITableVBIStatus,
       "sdirdVBITableVBI-InTypeLine11": sdirdVBITableVBI_InTypeLine11,
       "sdirdVBITableVBI-InTypeLine12": sdirdVBITableVBI_InTypeLine12,
       "sdirdVBITableVBI-InTypeLine13": sdirdVBITableVBI_InTypeLine13,
       "sdirdVBITableVBI-InTypeLine14": sdirdVBITableVBI_InTypeLine14,
       "sdirdVBITableVBI-InTypeLine15": sdirdVBITableVBI_InTypeLine15,
       "sdirdVBITableVBI-InTypeLine16": sdirdVBITableVBI_InTypeLine16,
       "sdirdVBITableVBI-InTypeLine17": sdirdVBITableVBI_InTypeLine17,
       "sdirdVBITableVBI-InTypeLine18": sdirdVBITableVBI_InTypeLine18,
       "sdirdVBITableVBI-InTypeLine19": sdirdVBITableVBI_InTypeLine19,
       "sdirdVBITableVBI-InTypeLine20": sdirdVBITableVBI_InTypeLine20,
       "sdirdVBITableVBI-InTypeLine21": sdirdVBITableVBI_InTypeLine21,
       "sdirdVBITableVBI-InTypeLine22": sdirdVBITableVBI_InTypeLine22,
       "sdirdVBITableVBI-InTypeLine23": sdirdVBITableVBI_InTypeLine23,
       "sdirdVBITableVBI-OutTypeLine11": sdirdVBITableVBI_OutTypeLine11,
       "sdirdVBITableVBI-OutTypeLine12": sdirdVBITableVBI_OutTypeLine12,
       "sdirdVBITableVBI-OutTypeLine13": sdirdVBITableVBI_OutTypeLine13,
       "sdirdVBITableVBI-OutTypeLine14": sdirdVBITableVBI_OutTypeLine14,
       "sdirdVBITableVBI-OutTypeLine15": sdirdVBITableVBI_OutTypeLine15,
       "sdirdVBITableVBI-OutTypeLine16": sdirdVBITableVBI_OutTypeLine16,
       "sdirdVBITableVBI-OutTypeLine17": sdirdVBITableVBI_OutTypeLine17,
       "sdirdVBITableVBI-OutTypeLine18": sdirdVBITableVBI_OutTypeLine18,
       "sdirdVBITableVBI-OutTypeLine19": sdirdVBITableVBI_OutTypeLine19,
       "sdirdVBITableVBI-OutTypeLine20": sdirdVBITableVBI_OutTypeLine20,
       "sdirdVBITableVBI-OutTypeLine21": sdirdVBITableVBI_OutTypeLine21,
       "sdirdVBITableVBI-OutTypeLine22": sdirdVBITableVBI_OutTypeLine22,
       "sdirdVBITableVBI-OutTypeLine23": sdirdVBITableVBI_OutTypeLine23,
       "sdirdDataTable": sdirdDataTable,
       "sdirdDataTableEntry": sdirdDataTableEntry,
       "sdirdDataTableCurrentNextIndex": sdirdDataTableCurrentNextIndex,
       "sdirdDataTableSubtitlesLang": sdirdDataTableSubtitlesLang,
       "sdirdDataTableSubtitlesType": sdirdDataTableSubtitlesType,
       "sdirdDataTableSubtitlesStatus": sdirdDataTableSubtitlesStatus,
       "sdirdDataTableTeletextStatus": sdirdDataTableTeletextStatus,
       "sdirdDataTableAsyncStatus": sdirdDataTableAsyncStatus,
       "sdirdDataTableAsyncBaudrate": sdirdDataTableAsyncBaudrate,
       "sdirdDataTableSyncStatus": sdirdDataTableSyncStatus,
       "sdirdDataTableSyncBitrate": sdirdDataTableSyncBitrate,
       "sdirdDemodTable": sdirdDemodTable,
       "sdirdDemodTableEntry": sdirdDemodTableEntry,
       "sdirdDemodTableCurrentNextIndex": sdirdDemodTableCurrentNextIndex,
       "sdirdDemodTableDemodStatus": sdirdDemodTableDemodStatus,
       "sdirdDemodTableFrequency": sdirdDemodTableFrequency,
       "sdirdDemodTableIFFrequency": sdirdDemodTableIFFrequency,
       "sdirdDemodTableSymbolRate": sdirdDemodTableSymbolRate,
       "sdirdDemodTableFECRate": sdirdDemodTableFECRate,
       "sdirdDemodTablePolarization": sdirdDemodTablePolarization,
       "sdirdDemodTableSatAerial": sdirdDemodTableSatAerial,
       "sdirdDemodTableBERLimit": sdirdDemodTableBERLimit,
       "sdirdDemodTableLNBActive": sdirdDemodTableLNBActive,
       "sdirdDemodTableLNBLoFreq": sdirdDemodTableLNBLoFreq,
       "sdirdDemodTableLNBHiFreq": sdirdDemodTableLNBHiFreq,
       "sdirdDemodTableLNBSwitchFreq": sdirdDemodTableLNBSwitchFreq,
       "sdirdDemodTableLNBSupplyState": sdirdDemodTableLNBSupplyState,
       "sdirdDemodTableSearchRange": sdirdDemodTableSearchRange,
       "sdirdDemodTableModulation": sdirdDemodTableModulation,
       "sdirdDemodTableLNBFaultStatus": sdirdDemodTableLNBFaultStatus,
       "sdirdDemodTableSATStatus": sdirdDemodTableSATStatus,
       "sdirdDemodTableSatPartNo": sdirdDemodTableSatPartNo,
       "sdirdDemodTableSatCodeVersion": sdirdDemodTableSatCodeVersion,
       "sdirdCATable": sdirdCATable,
       "sdirdCATableEntry": sdirdCATableEntry,
       "sdirdCATableCurrentNextIndex": sdirdCATableCurrentNextIndex,
       "sdirdCATableCAStatus": sdirdCATableCAStatus,
       "sdirdCATableRASMode": sdirdCATableRASMode,
       "sdirdCATableDSNGKey": sdirdCATableDSNGKey,
       "sdirdCATableBISSMode": sdirdCATableBISSMode,
       "sdirdCATableBISSKeyString": sdirdCATableBISSKeyString,
       "sdirdCATableBISSESWString": sdirdCATableBISSESWString,
       "sdirdSystemTable": sdirdSystemTable,
       "sdirdSystemTableEntry": sdirdSystemTableEntry,
       "sdirdSystemTableTS-Lock": sdirdSystemTableTS_Lock,
       "sdirdSystemTableNetworkName": sdirdSystemTableNetworkName,
       "sdirdSystemTableNetworkID": sdirdSystemTableNetworkID,
       "sdirdSystemTableNumServices": sdirdSystemTableNumServices,
       "sdirdSystemTableCurrent-Service-ID": sdirdSystemTableCurrent_Service_ID,
       "sdirdSystemTableCurrent-TSID": sdirdSystemTableCurrent_TSID,
       "sdirdSystemTableCurrent-ONID": sdirdSystemTableCurrent_ONID,
       "sdirdSystemTableModelNumber": sdirdSystemTableModelNumber,
       "sdirdSystemTableModelOptions": sdirdSystemTableModelOptions,
       "sdirdSystemTableComp-PartNo": sdirdSystemTableComp_PartNo,
       "sdirdSystemTableComp-SerialNo": sdirdSystemTableComp_SerialNo,
       "sdirdSystemTableComp-AppVer": sdirdSystemTableComp_AppVer,
       "sdirdSystemTableComp-CoreVer": sdirdSystemTableComp_CoreVer,
       "sdirdSystemTableComp-DriverVer": sdirdSystemTableComp_DriverVer,
       "sdirdSystemTableComp-DiagVer": sdirdSystemTableComp_DiagVer,
       "sdirdSystemTableSystemStatus": sdirdSystemTableSystemStatus,
       "sdirdTSSource": sdirdTSSource,
       "sdirdTrackingMode": sdirdTrackingMode,
       "sdirdTSOMode": sdirdTSOMode,
       "sdirdBISTRequired": sdirdBISTRequired}
)
