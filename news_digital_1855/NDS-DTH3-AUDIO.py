# SNMP MIB module (NDS-DTH3-AUDIO) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/news_digital_1855/NDS-DTH3-AUDIO.mib
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

_AudioEnc_ObjectIdentity = ObjectIdentity
audioEnc = _AudioEnc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7)
)


class _AudioModuleNumber_Type(Integer32):
    """Custom type audioModuleNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AudioModuleNumber_Type.__name__ = "Integer32"
_AudioModuleNumber_Object = MibScalar
audioModuleNumber = _AudioModuleNumber_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 1),
    _AudioModuleNumber_Type()
)
audioModuleNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioModuleNumber.setStatus("current")
_AudioModuleTable_Object = MibTable
audioModuleTable = _AudioModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 2)
)
if mibBuilder.loadTexts:
    audioModuleTable.setStatus("current")
_AudioModuleEntry_Object = MibTableRow
audioModuleEntry = _AudioModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 2, 1)
)
audioModuleEntry.setIndexNames(
    (0, "NDS-DTH3-AUDIO", "audioModuleIndex"),
    (0, "NDS-DTH3-AUDIO", "audioChannelIndex"),
)
if mibBuilder.loadTexts:
    audioModuleEntry.setStatus("current")


class _AudioModuleIndex_Type(Integer32):
    """Custom type audioModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AudioModuleIndex_Type.__name__ = "Integer32"
_AudioModuleIndex_Object = MibTableColumn
audioModuleIndex = _AudioModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 2, 1, 1),
    _AudioModuleIndex_Type()
)
audioModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioModuleIndex.setStatus("current")


class _AudioChannelIndex_Type(Integer32):
    """Custom type audioChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("b", 2))
    )


_AudioChannelIndex_Type.__name__ = "Integer32"
_AudioChannelIndex_Object = MibTableColumn
audioChannelIndex = _AudioChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 2, 1, 2),
    _AudioChannelIndex_Type()
)
audioChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioChannelIndex.setStatus("current")


class _AudioHardwareRelease_Type(DisplayString):
    """Custom type audioHardwareRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AudioHardwareRelease_Type.__name__ = "DisplayString"
_AudioHardwareRelease_Object = MibTableColumn
audioHardwareRelease = _AudioHardwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 2, 1, 3),
    _AudioHardwareRelease_Type()
)
audioHardwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioHardwareRelease.setStatus("current")


class _AudioSoftwareRelease_Type(DisplayString):
    """Custom type audioSoftwareRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AudioSoftwareRelease_Type.__name__ = "DisplayString"
_AudioSoftwareRelease_Object = MibTableColumn
audioSoftwareRelease = _AudioSoftwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 2, 1, 4),
    _AudioSoftwareRelease_Type()
)
audioSoftwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioSoftwareRelease.setStatus("current")


class _AudioFirmwareRelease_Type(DisplayString):
    """Custom type audioFirmwareRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_AudioFirmwareRelease_Type.__name__ = "DisplayString"
_AudioFirmwareRelease_Object = MibTableColumn
audioFirmwareRelease = _AudioFirmwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 2, 1, 5),
    _AudioFirmwareRelease_Type()
)
audioFirmwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioFirmwareRelease.setStatus("current")


class _AudioModuleId_Type(Integer32):
    """Custom type audioModuleId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
              7,
              16,
              17,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("ice-SD-WMA-AAC", 5),
          ("ice-HD-WMA-AAC", 7),
          ("mPEG2-Musicam", 16),
          ("dolbyDigital-AC-3", 17),
          ("dolbyDigital-AC-3-Pass-Thru", 19),
          ("linearPCM", 20))
    )


_AudioModuleId_Type.__name__ = "Integer32"
_AudioModuleId_Object = MibTableColumn
audioModuleId = _AudioModuleId_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 2, 1, 6),
    _AudioModuleId_Type()
)
audioModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioModuleId.setStatus("current")
_AudionextTimeDate_Type = DateAndTime
_AudionextTimeDate_Object = MibTableColumn
audionextTimeDate = _AudionextTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 2, 1, 7),
    _AudionextTimeDate_Type()
)
audionextTimeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audionextTimeDate.setStatus("current")


class _AudioLevelLeft_Type(Integer32):
    """Custom type audioLevelLeft based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AudioLevelLeft_Type.__name__ = "Integer32"
_AudioLevelLeft_Object = MibTableColumn
audioLevelLeft = _AudioLevelLeft_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 2, 1, 8),
    _AudioLevelLeft_Type()
)
audioLevelLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioLevelLeft.setStatus("current")


class _AudioLevelRight_Type(Integer32):
    """Custom type audioLevelRight based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AudioLevelRight_Type.__name__ = "Integer32"
_AudioLevelRight_Object = MibTableColumn
audioLevelRight = _AudioLevelRight_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 2, 1, 9),
    _AudioLevelRight_Type()
)
audioLevelRight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioLevelRight.setStatus("current")
_AudioTable_Object = MibTable
audioTable = _AudioTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3)
)
if mibBuilder.loadTexts:
    audioTable.setStatus("current")
_AudioEntry_Object = MibTableRow
audioEntry = _AudioEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1)
)
audioEntry.setIndexNames(
    (0, "NDS-DTH3-AUDIO", "audioCurrentNextIndex"),
    (0, "NDS-DTH3-AUDIO", "audioModIndex"),
    (0, "NDS-DTH3-AUDIO", "audioChanIndex"),
)
if mibBuilder.loadTexts:
    audioEntry.setStatus("current")


class _AudioCurrentNextIndex_Type(Integer32):
    """Custom type audioCurrentNextIndex based on Integer32"""
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


_AudioCurrentNextIndex_Type.__name__ = "Integer32"
_AudioCurrentNextIndex_Object = MibTableColumn
audioCurrentNextIndex = _AudioCurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 1),
    _AudioCurrentNextIndex_Type()
)
audioCurrentNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioCurrentNextIndex.setStatus("current")


class _AudioModIndex_Type(Integer32):
    """Custom type audioModIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AudioModIndex_Type.__name__ = "Integer32"
_AudioModIndex_Object = MibTableColumn
audioModIndex = _AudioModIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 2),
    _AudioModIndex_Type()
)
audioModIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioModIndex.setStatus("current")


class _AudioChanIndex_Type(Integer32):
    """Custom type audioChanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("b", 2))
    )


_AudioChanIndex_Type.__name__ = "Integer32"
_AudioChanIndex_Object = MibTableColumn
audioChanIndex = _AudioChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 3),
    _AudioChanIndex_Type()
)
audioChanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioChanIndex.setStatus("current")


class _AudioSource_Type(Integer32):
    """Custom type audioSource based on Integer32"""
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
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("mute", 1),
          ("testTone", 2),
          ("analogue", 3),
          ("digital", 4),
          ("digital-2-old", 5),
          ("embedded-1", 6),
          ("embedded-2", 7),
          ("embedded-3", 8),
          ("embedded-4", 9),
          ("digital-viaSRC-old", 10),
          ("digital-2-viaSRC-old", 11),
          ("embedded-1-viaSRC-old", 12),
          ("embedded-2-viaSRC-old", 13),
          ("embedded-3-viaSRC-old", 14),
          ("embedded-4-viaSRC-old", 15),
          ("xlr-module", 16),
          ("hd-avc-embedded-Group-1-2", 20),
          ("hd-avc-embedded-Group-3-4", 21),
          ("hd-avc-embedded-1", 22),
          ("hd-avc-embedded-2", 23),
          ("hd-avc-embedded-3", 24),
          ("hd-avc-embedded-4", 25),
          ("hd-avc-embedded-5", 26),
          ("hd-avc-embedded-6", 27),
          ("hd-avc-embedded-7", 28),
          ("hd-avc-embedded-8", 29))
    )


_AudioSource_Type.__name__ = "Integer32"
_AudioSource_Object = MibTableColumn
audioSource = _AudioSource_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 4),
    _AudioSource_Type()
)
audioSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioSource.setStatus("current")


class _AudioClipLevel_Type(Integer32):
    """Custom type audioClipLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("gain12dB", 0),
          ("gain18dB", 1),
          ("gain15dB", 2),
          ("gain16dB", 3),
          ("gain21dB", 4),
          ("gain22dB", 5),
          ("gain24dB", 6))
    )


_AudioClipLevel_Type.__name__ = "Integer32"
_AudioClipLevel_Object = MibTableColumn
audioClipLevel = _AudioClipLevel_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 5),
    _AudioClipLevel_Type()
)
audioClipLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioClipLevel.setStatus("current")


class _AudioTermination_Type(Integer32):
    """Custom type audioTermination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("term20kOhms", 0),
          ("term600Ohms", 1))
    )


_AudioTermination_Type.__name__ = "Integer32"
_AudioTermination_Object = MibTableColumn
audioTermination = _AudioTermination_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 6),
    _AudioTermination_Type()
)
audioTermination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioTermination.setStatus("current")


class _AudioSilenceTimeout_Type(Integer32):
    """Custom type audioSilenceTimeout based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AudioSilenceTimeout_Type.__name__ = "Integer32"
_AudioSilenceTimeout_Object = MibTableColumn
audioSilenceTimeout = _AudioSilenceTimeout_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 7),
    _AudioSilenceTimeout_Type()
)
audioSilenceTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioSilenceTimeout.setStatus("current")


class _AudioSampleFrequency_Type(Integer32):
    """Custom type audioSampleFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("freq48kHz", 0),
          ("freq44-1kHz", 1),
          ("freq32kHz", 2))
    )


_AudioSampleFrequency_Type.__name__ = "Integer32"
_AudioSampleFrequency_Object = MibTableColumn
audioSampleFrequency = _AudioSampleFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 8),
    _AudioSampleFrequency_Type()
)
audioSampleFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioSampleFrequency.setStatus("current")


class _AudioCodingStd_Type(Integer32):
    """Custom type audioCodingStd based on Integer32"""
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
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("dolbyDigital-AC-3", 0),
          ("linearPCMdirect", 1),
          ("mPEGLayer2", 2),
          ("dolbyDigital-AC-3-Pass-Thru", 3),
          ("dolbyE-Pass-Thru", 4),
          ("dts-Pass-Thru", 5),
          ("linearPCMviaSRC", 6),
          ("wma-standard", 10),
          ("wma-low-delay", 11),
          ("wma-AAC-standard", 12),
          ("wma-AAC-plus", 13))
    )


_AudioCodingStd_Type.__name__ = "Integer32"
_AudioCodingStd_Object = MibTableColumn
audioCodingStd = _AudioCodingStd_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 9),
    _AudioCodingStd_Type()
)
audioCodingStd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioCodingStd.setStatus("current")


class _AudioCopyright_Type(Integer32):
    """Custom type audioCopyright based on Integer32"""
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


_AudioCopyright_Type.__name__ = "Integer32"
_AudioCopyright_Object = MibTableColumn
audioCopyright = _AudioCopyright_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 10),
    _AudioCopyright_Type()
)
audioCopyright.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioCopyright.setStatus("current")


class _AudioOriginal_Type(Integer32):
    """Custom type audioOriginal based on Integer32"""
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


_AudioOriginal_Type.__name__ = "Integer32"
_AudioOriginal_Object = MibTableColumn
audioOriginal = _AudioOriginal_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 11),
    _AudioOriginal_Type()
)
audioOriginal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioOriginal.setStatus("current")


class _AudioDeEmphasis_Type(Integer32):
    """Custom type audioDeEmphasis based on Integer32"""
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
        *(("deEmphasisNone", 0),
          ("deEmphasisAuto", 1),
          ("deEmphasis50-15usec", 2),
          ("deEmphasisCCITT-J17", 3))
    )


_AudioDeEmphasis_Type.__name__ = "Integer32"
_AudioDeEmphasis_Object = MibTableColumn
audioDeEmphasis = _AudioDeEmphasis_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 12),
    _AudioDeEmphasis_Type()
)
audioDeEmphasis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioDeEmphasis.setStatus("current")


class _AudioBitRate_Type(Integer32):
    """Custom type audioBitRate based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("bitRate32kBits-s", 0),
          ("bitRate40kBits-s", 1),
          ("bitRate48kBits-s", 2),
          ("bitRate56kBits-s", 3),
          ("bitRate64kBits-s", 4),
          ("bitRate80kBits-s", 5),
          ("bitRate96kBits-s", 6),
          ("bitRate112kBits-s", 7),
          ("bitRate128kBits-s", 8),
          ("bitRate160kBits-s", 9),
          ("bitRate192kBits-s", 10),
          ("bitRate224kBits-s", 11),
          ("bitRate256kBits-s", 12),
          ("bitRate320kBits-s", 13),
          ("bitRate384kBits-s", 14),
          ("bitRate448kBits-s", 15),
          ("bitRate512kBits-s", 16),
          ("bitRate576kBits-s", 17),
          ("bitRate640kBits-s", 18))
    )


_AudioBitRate_Type.__name__ = "Integer32"
_AudioBitRate_Object = MibTableColumn
audioBitRate = _AudioBitRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 13),
    _AudioBitRate_Type()
)
audioBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioBitRate.setStatus("current")


class _AudioCoding_Type(Integer32):
    """Custom type audioCoding based on Integer32"""
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
        *(("stereo", 0),
          ("jointStereo", 1),
          ("dualMono", 2),
          ("mono-left", 3),
          ("oneplusone", 4),
          ("c-left", 5),
          ("l-R", 6),
          ("l-C-R", 7),
          ("l-R-s", 8),
          ("l-C-R-s", 9),
          ("l-R-Ls-Rs", 10),
          ("l-C-R-Ls-Rs", 11),
          ("audioDescriptiveService", 12),
          ("mono-right", 13),
          ("c-right", 14),
          ("avc-surround-5-1", 15),
          ("avc-surround-7-1", 16))
    )


_AudioCoding_Type.__name__ = "Integer32"
_AudioCoding_Object = MibTableColumn
audioCoding = _AudioCoding_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 14),
    _AudioCoding_Type()
)
audioCoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioCoding.setStatus("current")


class _AudioDelay_Type(Integer32):
    """Custom type audioDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(111, 10000),
    )


_AudioDelay_Type.__name__ = "Integer32"
_AudioDelay_Object = MibTableColumn
audioDelay = _AudioDelay_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 15),
    _AudioDelay_Type()
)
audioDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioDelay.setStatus("current")


class _AudioPID_Type(Integer32):
    """Custom type audioPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_AudioPID_Type.__name__ = "Integer32"
_AudioPID_Object = MibTableColumn
audioPID = _AudioPID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 16),
    _AudioPID_Type()
)
audioPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioPID.setStatus("current")


class _AudioSMPTEstandard_Type(Integer32):
    """Custom type audioSMPTEstandard based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("standard-1998", 0),
          ("standard-2000", 1))
    )


_AudioSMPTEstandard_Type.__name__ = "Integer32"
_AudioSMPTEstandard_Object = MibTableColumn
audioSMPTEstandard = _AudioSMPTEstandard_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 17),
    _AudioSMPTEstandard_Type()
)
audioSMPTEstandard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioSMPTEstandard.setStatus("current")


class _AudioLipSync_Type(Integer32):
    """Custom type audioLipSync based on Integer32"""
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
          ("off-min-delay", 2))
    )


_AudioLipSync_Type.__name__ = "Integer32"
_AudioLipSync_Object = MibTableColumn
audioLipSync = _AudioLipSync_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 18),
    _AudioLipSync_Type()
)
audioLipSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioLipSync.setStatus("current")


class _AudioLinearPCMChannelNo_Type(Integer32):
    """Custom type audioLinearPCMChannelNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_AudioLinearPCMChannelNo_Type.__name__ = "Integer32"
_AudioLinearPCMChannelNo_Object = MibTableColumn
audioLinearPCMChannelNo = _AudioLinearPCMChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 19),
    _AudioLinearPCMChannelNo_Type()
)
audioLinearPCMChannelNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioLinearPCMChannelNo.setStatus("current")


class _AudioLipSyncOffset_Type(Integer32):
    """Custom type audioLipSyncOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 50),
    )


_AudioLipSyncOffset_Type.__name__ = "Integer32"
_AudioLipSyncOffset_Object = MibTableColumn
audioLipSyncOffset = _AudioLipSyncOffset_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 20),
    _AudioLipSyncOffset_Type()
)
audioLipSyncOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioLipSyncOffset.setStatus("current")


class _AudioInsertPCROnPID_Type(Integer32):
    """Custom type audioInsertPCROnPID based on Integer32"""
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


_AudioInsertPCROnPID_Type.__name__ = "Integer32"
_AudioInsertPCROnPID_Object = MibTableColumn
audioInsertPCROnPID = _AudioInsertPCROnPID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 21),
    _AudioInsertPCROnPID_Type()
)
audioInsertPCROnPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioInsertPCROnPID.setStatus("current")


class _AudioShortList_Type(OctetString):
    """Custom type audioShortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(23, 26),
    )


_AudioShortList_Type.__name__ = "OctetString"
_AudioShortList_Object = MibTableColumn
audioShortList = _AudioShortList_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 22),
    _AudioShortList_Type()
)
audioShortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioShortList.setStatus("current")


class _AudioComponentTag_Type(Integer32):
    """Custom type audioComponentTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AudioComponentTag_Type.__name__ = "Integer32"
_AudioComponentTag_Object = MibTableColumn
audioComponentTag = _AudioComponentTag_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 23),
    _AudioComponentTag_Type()
)
audioComponentTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioComponentTag.setStatus("current")


class _AudioDTSFrameSize_Type(Integer32):
    """Custom type audioDTSFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("size-512", 0),
          ("size-1024", 1),
          ("size-2048", 2))
    )


_AudioDTSFrameSize_Type.__name__ = "Integer32"
_AudioDTSFrameSize_Object = MibTableColumn
audioDTSFrameSize = _AudioDTSFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 24),
    _AudioDTSFrameSize_Type()
)
audioDTSFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioDTSFrameSize.setStatus("current")


class _AudioDTSLinRegDescriptor_Type(Integer32):
    """Custom type audioDTSLinRegDescriptor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dts-descriptor-only", 0),
          ("dts-and-bssd", 1))
    )


_AudioDTSLinRegDescriptor_Type.__name__ = "Integer32"
_AudioDTSLinRegDescriptor_Object = MibTableColumn
audioDTSLinRegDescriptor = _AudioDTSLinRegDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 25),
    _AudioDTSLinRegDescriptor_Type()
)
audioDTSLinRegDescriptor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioDTSLinRegDescriptor.setStatus("current")


class _AudioOPDigitalInputLoss_Type(Integer32):
    """Custom type audioOPDigitalInputLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("silence", 0),
          ("no-pid", 1),
          ("no-ASI", 2))
    )


_AudioOPDigitalInputLoss_Type.__name__ = "Integer32"
_AudioOPDigitalInputLoss_Object = MibTableColumn
audioOPDigitalInputLoss = _AudioOPDigitalInputLoss_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 26),
    _AudioOPDigitalInputLoss_Type()
)
audioOPDigitalInputLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioOPDigitalInputLoss.setStatus("current")


class _AudioHDSource_Type(Integer32):
    """Custom type audioHDSource based on Integer32"""
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
        *(("off", 0),
          ("embedded-Group-1-2", 1),
          ("embedded-Group-3-4", 2),
          ("embedded-1", 3),
          ("embedded-2", 4),
          ("embedded-3", 5),
          ("embedded-4", 6),
          ("embedded-5", 7),
          ("embedded-6", 8),
          ("embedded-7", 9),
          ("embedded-8", 10))
    )


_AudioHDSource_Type.__name__ = "Integer32"
_AudioHDSource_Object = MibTableColumn
audioHDSource = _AudioHDSource_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 27),
    _AudioHDSource_Type()
)
audioHDSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioHDSource.setStatus("current")


class _AudioVPSControlsCodingMode_Type(Integer32):
    """Custom type audioVPSControlsCodingMode based on Integer32"""
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


_AudioVPSControlsCodingMode_Type.__name__ = "Integer32"
_AudioVPSControlsCodingMode_Object = MibTableColumn
audioVPSControlsCodingMode = _AudioVPSControlsCodingMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 28),
    _AudioVPSControlsCodingMode_Type()
)
audioVPSControlsCodingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioVPSControlsCodingMode.setStatus("current")


class _AudioVPSCodingMode_Type(Integer32):
    """Custom type audioVPSCodingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("not-detected", 0),
          ("undefined", 1),
          ("single-chan-mono", 2),
          ("stereo", 3),
          ("dual-chan", 4))
    )


_AudioVPSCodingMode_Type.__name__ = "Integer32"
_AudioVPSCodingMode_Object = MibTableColumn
audioVPSCodingMode = _AudioVPSCodingMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 29),
    _AudioVPSCodingMode_Type()
)
audioVPSCodingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioVPSCodingMode.setStatus("current")


class _AudioVPSWord5_Type(Integer32):
    """Custom type audioVPSWord5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AudioVPSWord5_Type.__name__ = "Integer32"
_AudioVPSWord5_Object = MibTableColumn
audioVPSWord5 = _AudioVPSWord5_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 30),
    _AudioVPSWord5_Type()
)
audioVPSWord5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioVPSWord5.setStatus("current")


class _AudioVPSStereoMode_Type(Integer32):
    """Custom type audioVPSStereoMode based on Integer32"""
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
        *(("auto-bit-5", 0),
          ("auto-bit-6", 1),
          ("auto-bit-7", 2),
          ("auto-bit-8", 3),
          ("stereo", 4),
          ("joint", 5))
    )


_AudioVPSStereoMode_Type.__name__ = "Integer32"
_AudioVPSStereoMode_Object = MibTableColumn
audioVPSStereoMode = _AudioVPSStereoMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 31),
    _AudioVPSStereoMode_Type()
)
audioVPSStereoMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioVPSStereoMode.setStatus("current")


class _AudioVPSDualChanMode_Type(Integer32):
    """Custom type audioVPSDualChanMode based on Integer32"""
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
        *(("auto-bit-5", 0),
          ("auto-bit-6", 1),
          ("auto-bit-7", 2),
          ("auto-bit-8", 3),
          ("dual", 4),
          ("single", 5))
    )


_AudioVPSDualChanMode_Type.__name__ = "Integer32"
_AudioVPSDualChanMode_Object = MibTableColumn
audioVPSDualChanMode = _AudioVPSDualChanMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 32),
    _AudioVPSDualChanMode_Type()
)
audioVPSDualChanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioVPSDualChanMode.setStatus("current")


class _AudioLowDelay_Type(Integer32):
    """Custom type audioLowDelay based on Integer32"""
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


_AudioLowDelay_Type.__name__ = "Integer32"
_AudioLowDelay_Object = MibTableColumn
audioLowDelay = _AudioLowDelay_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 3, 1, 33),
    _AudioLowDelay_Type()
)
audioLowDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioLowDelay.setStatus("current")
_AudioAC3Table_Object = MibTable
audioAC3Table = _AudioAC3Table_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 4)
)
if mibBuilder.loadTexts:
    audioAC3Table.setStatus("current")
_AudioAC3Entry_Object = MibTableRow
audioAC3Entry = _AudioAC3Entry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 4, 1)
)
audioAC3Entry.setIndexNames(
    (0, "NDS-DTH3-AUDIO", "audioAC3CurrentNextIndex"),
    (0, "NDS-DTH3-AUDIO", "audioAC3ModIndex"),
    (0, "NDS-DTH3-AUDIO", "audioAC3ChanIndex"),
)
if mibBuilder.loadTexts:
    audioAC3Entry.setStatus("current")


class _AudioAC3CurrentNextIndex_Type(Integer32):
    """Custom type audioAC3CurrentNextIndex based on Integer32"""
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


_AudioAC3CurrentNextIndex_Type.__name__ = "Integer32"
_AudioAC3CurrentNextIndex_Object = MibTableColumn
audioAC3CurrentNextIndex = _AudioAC3CurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 4, 1, 1),
    _AudioAC3CurrentNextIndex_Type()
)
audioAC3CurrentNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioAC3CurrentNextIndex.setStatus("current")


class _AudioAC3ModIndex_Type(Integer32):
    """Custom type audioAC3ModIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AudioAC3ModIndex_Type.__name__ = "Integer32"
_AudioAC3ModIndex_Object = MibTableColumn
audioAC3ModIndex = _AudioAC3ModIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 4, 1, 2),
    _AudioAC3ModIndex_Type()
)
audioAC3ModIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioAC3ModIndex.setStatus("current")


class _AudioAC3ChanIndex_Type(Integer32):
    """Custom type audioAC3ChanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("b", 2))
    )


_AudioAC3ChanIndex_Type.__name__ = "Integer32"
_AudioAC3ChanIndex_Object = MibTableColumn
audioAC3ChanIndex = _AudioAC3ChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 4, 1, 3),
    _AudioAC3ChanIndex_Type()
)
audioAC3ChanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioAC3ChanIndex.setStatus("current")


class _AudioBitStream_Type(Integer32):
    """Custom type audioBitStream based on Integer32"""
    defaultValue = 0

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
              9)
        )
    )
    namedValues = NamedValues(
        *(("completeMain", 0),
          ("musicandEffects", 1),
          ("visuallyImpaired", 2),
          ("hearingImpaired", 3),
          ("dialogue", 4),
          ("commentary", 5),
          ("emergency", 6),
          ("reserved", 7),
          ("voiceover", 8),
          ("karaoke", 9))
    )


_AudioBitStream_Type.__name__ = "Integer32"
_AudioBitStream_Object = MibTableColumn
audioBitStream = _AudioBitStream_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 4, 1, 4),
    _AudioBitStream_Type()
)
audioBitStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioBitStream.setStatus("current")


class _AudioLowFreq_Type(Integer32):
    """Custom type audioLowFreq based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("off", 0)
    )


_AudioLowFreq_Type.__name__ = "Integer32"
_AudioLowFreq_Object = MibTableColumn
audioLowFreq = _AudioLowFreq_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 4, 1, 5),
    _AudioLowFreq_Type()
)
audioLowFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioLowFreq.setStatus("current")


class _AudioSurroundDownmix_Type(Integer32):
    """Custom type audioSurroundDownmix based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("minus3pt0dB", 0),
          ("minus6pt0dB", 1),
          ("minusinfinitydB", 2))
    )


_AudioSurroundDownmix_Type.__name__ = "Integer32"
_AudioSurroundDownmix_Object = MibTableColumn
audioSurroundDownmix = _AudioSurroundDownmix_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 4, 1, 6),
    _AudioSurroundDownmix_Type()
)
audioSurroundDownmix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioSurroundDownmix.setStatus("current")


class _AudioDolbySurround_Type(Integer32):
    """Custom type audioDolbySurround based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notIndicated", 0),
          ("nOTDolbySurround", 1),
          ("dolbySurround", 2))
    )


_AudioDolbySurround_Type.__name__ = "Integer32"
_AudioDolbySurround_Object = MibTableColumn
audioDolbySurround = _AudioDolbySurround_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 4, 1, 7),
    _AudioDolbySurround_Type()
)
audioDolbySurround.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioDolbySurround.setStatus("current")


class _AudioDialogueNorm_Type(Integer32):
    """Custom type audioDialogueNorm based on Integer32"""
    defaultValue = 1

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
              31)
        )
    )
    namedValues = NamedValues(
        *(("minus1dB", 1),
          ("minus2dB", 2),
          ("minus3dB", 3),
          ("minus4dB", 4),
          ("minus5dB", 5),
          ("minus6dB", 6),
          ("minus7dB", 7),
          ("minus8dB", 8),
          ("minus9dB", 9),
          ("minus10dB", 10),
          ("minus11dB", 11),
          ("minus12dB", 12),
          ("minus13dB", 13),
          ("minus14dB", 14),
          ("minus15dB", 15),
          ("minus16dB", 16),
          ("minus17dB", 17),
          ("minus18dB", 18),
          ("minus19dB", 19),
          ("minus20dB", 20),
          ("minus21dB", 21),
          ("minus22dB", 22),
          ("minus23dB", 23),
          ("minus24dB", 24),
          ("minus25dB", 25),
          ("minus26dB", 26),
          ("minus27dB", 27),
          ("minus28dB", 28),
          ("minus29dB", 29),
          ("minus30dB", 30),
          ("minus31dB", 31))
    )


_AudioDialogueNorm_Type.__name__ = "Integer32"
_AudioDialogueNorm_Object = MibTableColumn
audioDialogueNorm = _AudioDialogueNorm_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 4, 1, 8),
    _AudioDialogueNorm_Type()
)
audioDialogueNorm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioDialogueNorm.setStatus("current")


class _AudioProdInfo_Type(Integer32):
    """Custom type audioProdInfo based on Integer32"""
    defaultValue = 0

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


_AudioProdInfo_Type.__name__ = "Integer32"
_AudioProdInfo_Object = MibTableColumn
audioProdInfo = _AudioProdInfo_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 4, 1, 9),
    _AudioProdInfo_Type()
)
audioProdInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioProdInfo.setStatus("current")


class _AudioMixLevel_Type(Integer32):
    """Custom type audioMixLevel based on Integer32"""
    defaultValue = 0

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
              31)
        )
    )
    namedValues = NamedValues(
        *(("zerodB", 0),
          ("plus1dB", 1),
          ("plus2dB", 2),
          ("plus3dB", 3),
          ("plus4dB", 4),
          ("plus5dB", 5),
          ("plus6dB", 6),
          ("plus7dB", 7),
          ("plus8dB", 8),
          ("plus9dB", 9),
          ("plus10dB", 10),
          ("plus11dB", 11),
          ("plus12dB", 12),
          ("plus13dB", 13),
          ("plus14dB", 14),
          ("plus15dB", 15),
          ("plus16dB", 16),
          ("plus17dB", 17),
          ("plus18dB", 18),
          ("plus19dB", 19),
          ("plus20dB", 20),
          ("plus21dB", 21),
          ("plus22dB", 22),
          ("plus23dB", 23),
          ("plus24dB", 24),
          ("plus25dB", 25),
          ("plus26dB", 26),
          ("plus27dB", 27),
          ("plus28dB", 28),
          ("plus29dB", 29),
          ("plus30dB", 30),
          ("plus31dB", 31))
    )


_AudioMixLevel_Type.__name__ = "Integer32"
_AudioMixLevel_Object = MibTableColumn
audioMixLevel = _AudioMixLevel_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 4, 1, 10),
    _AudioMixLevel_Type()
)
audioMixLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioMixLevel.setStatus("current")


class _AudioRoomType_Type(Integer32):
    """Custom type audioRoomType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notIndicated", 0),
          ("largeRoom", 1),
          ("smallRoom", 2))
    )


_AudioRoomType_Type.__name__ = "Integer32"
_AudioRoomType_Object = MibTableColumn
audioRoomType = _AudioRoomType_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 4, 1, 11),
    _AudioRoomType_Type()
)
audioRoomType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioRoomType.setStatus("current")


class _AudioCompression_Type(Integer32):
    """Custom type audioCompression based on Integer32"""
    defaultValue = 0

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
        *(("none", 0),
          ("filmStandardCompression", 1),
          ("filmLightCompression", 2),
          ("musicStandardCompression", 3),
          ("musicLightCompression", 4),
          ("speechCompression", 5),
          ("reserved-6", 6),
          ("reserved-7", 7))
    )


_AudioCompression_Type.__name__ = "Integer32"
_AudioCompression_Object = MibTableColumn
audioCompression = _AudioCompression_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 4, 1, 12),
    _AudioCompression_Type()
)
audioCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioCompression.setStatus("current")


class _AudioCBLowFilter_Type(Integer32):
    """Custom type audioCBLowFilter based on Integer32"""
    defaultValue = 0

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


_AudioCBLowFilter_Type.__name__ = "Integer32"
_AudioCBLowFilter_Object = MibTableColumn
audioCBLowFilter = _AudioCBLowFilter_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 4, 1, 13),
    _AudioCBLowFilter_Type()
)
audioCBLowFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioCBLowFilter.setStatus("current")


class _AudioLFELowFilter_Type(Integer32):
    """Custom type audioLFELowFilter based on Integer32"""
    defaultValue = 0

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


_AudioLFELowFilter_Type.__name__ = "Integer32"
_AudioLFELowFilter_Object = MibTableColumn
audioLFELowFilter = _AudioLFELowFilter_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 4, 1, 14),
    _AudioLFELowFilter_Type()
)
audioLFELowFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioLFELowFilter.setStatus("current")


class _AudioDCHighFilter_Type(Integer32):
    """Custom type audioDCHighFilter based on Integer32"""
    defaultValue = 0

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


_AudioDCHighFilter_Type.__name__ = "Integer32"
_AudioDCHighFilter_Object = MibTableColumn
audioDCHighFilter = _AudioDCHighFilter_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 4, 1, 15),
    _AudioDCHighFilter_Type()
)
audioDCHighFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioDCHighFilter.setStatus("current")


class _AudioExternalDelay_Type(Integer32):
    """Custom type audioExternalDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 450),
    )


_AudioExternalDelay_Type.__name__ = "Integer32"
_AudioExternalDelay_Object = MibTableColumn
audioExternalDelay = _AudioExternalDelay_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 4, 1, 16),
    _AudioExternalDelay_Type()
)
audioExternalDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioExternalDelay.setStatus("current")


class _AudioRFProtection_Type(Integer32):
    """Custom type audioRFProtection based on Integer32"""
    defaultValue = 0

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


_AudioRFProtection_Type.__name__ = "Integer32"
_AudioRFProtection_Object = MibTableColumn
audioRFProtection = _AudioRFProtection_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 4, 1, 17),
    _AudioRFProtection_Type()
)
audioRFProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioRFProtection.setStatus("current")
_AudioLangTable_Object = MibTable
audioLangTable = _AudioLangTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 5)
)
if mibBuilder.loadTexts:
    audioLangTable.setStatus("current")
_AudioLangEntry_Object = MibTableRow
audioLangEntry = _AudioLangEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 5, 1)
)
audioLangEntry.setIndexNames(
    (0, "NDS-DTH3-AUDIO", "audioCurrentNextLangIndex"),
    (0, "NDS-DTH3-AUDIO", "audioLangModIndex"),
    (0, "NDS-DTH3-AUDIO", "audioLangChanIndex"),
    (0, "NDS-DTH3-AUDIO", "audioLangIndex"),
)
if mibBuilder.loadTexts:
    audioLangEntry.setStatus("current")


class _AudioCurrentNextLangIndex_Type(Integer32):
    """Custom type audioCurrentNextLangIndex based on Integer32"""
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


_AudioCurrentNextLangIndex_Type.__name__ = "Integer32"
_AudioCurrentNextLangIndex_Object = MibTableColumn
audioCurrentNextLangIndex = _AudioCurrentNextLangIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 5, 1, 1),
    _AudioCurrentNextLangIndex_Type()
)
audioCurrentNextLangIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioCurrentNextLangIndex.setStatus("current")


class _AudioLangModIndex_Type(Integer32):
    """Custom type audioLangModIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AudioLangModIndex_Type.__name__ = "Integer32"
_AudioLangModIndex_Object = MibTableColumn
audioLangModIndex = _AudioLangModIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 5, 1, 2),
    _AudioLangModIndex_Type()
)
audioLangModIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioLangModIndex.setStatus("current")


class _AudioLangChanIndex_Type(Integer32):
    """Custom type audioLangChanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("b", 2))
    )


_AudioLangChanIndex_Type.__name__ = "Integer32"
_AudioLangChanIndex_Object = MibTableColumn
audioLangChanIndex = _AudioLangChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 5, 1, 3),
    _AudioLangChanIndex_Type()
)
audioLangChanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioLangChanIndex.setStatus("current")


class _AudioLangIndex_Type(Integer32):
    """Custom type audioLangIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("language", 1),
          ("left", 2),
          ("right", 3))
    )


_AudioLangIndex_Type.__name__ = "Integer32"
_AudioLangIndex_Object = MibTableColumn
audioLangIndex = _AudioLangIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 5, 1, 4),
    _AudioLangIndex_Type()
)
audioLangIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioLangIndex.setStatus("current")


class _AudioLanguage_Type(DisplayString):
    """Custom type audioLanguage based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_AudioLanguage_Type.__name__ = "DisplayString"
_AudioLanguage_Object = MibTableColumn
audioLanguage = _AudioLanguage_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 5, 1, 5),
    _AudioLanguage_Type()
)
audioLanguage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioLanguage.setStatus("current")
_AudioCalibrationTable_Object = MibTable
audioCalibrationTable = _AudioCalibrationTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 6)
)
if mibBuilder.loadTexts:
    audioCalibrationTable.setStatus("current")
_AudioCalibrationEntry_Object = MibTableRow
audioCalibrationEntry = _AudioCalibrationEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 6, 1)
)
audioCalibrationEntry.setIndexNames(
    (0, "NDS-DTH3-AUDIO", "audioCalibrationModuleIndex"),
    (0, "NDS-DTH3-AUDIO", "audioCalibrationChannelIndex"),
)
if mibBuilder.loadTexts:
    audioCalibrationEntry.setStatus("current")


class _AudioCalibrationModuleIndex_Type(Integer32):
    """Custom type audioCalibrationModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AudioCalibrationModuleIndex_Type.__name__ = "Integer32"
_AudioCalibrationModuleIndex_Object = MibTableColumn
audioCalibrationModuleIndex = _AudioCalibrationModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 6, 1, 1),
    _AudioCalibrationModuleIndex_Type()
)
audioCalibrationModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioCalibrationModuleIndex.setStatus("current")


class _AudioCalibrationChannelIndex_Type(Integer32):
    """Custom type audioCalibrationChannelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("b", 2))
    )


_AudioCalibrationChannelIndex_Type.__name__ = "Integer32"
_AudioCalibrationChannelIndex_Object = MibTableColumn
audioCalibrationChannelIndex = _AudioCalibrationChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 6, 1, 2),
    _AudioCalibrationChannelIndex_Type()
)
audioCalibrationChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioCalibrationChannelIndex.setStatus("current")


class _AudioBeginCalibration_Type(Integer32):
    """Custom type audioBeginCalibration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stop", 1),
          ("start", 2))
    )


_AudioBeginCalibration_Type.__name__ = "Integer32"
_AudioBeginCalibration_Object = MibTableColumn
audioBeginCalibration = _AudioBeginCalibration_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 6, 1, 3),
    _AudioBeginCalibration_Type()
)
audioBeginCalibration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    audioBeginCalibration.setStatus("current")


class _AudioCalibrationStatus_Type(Integer32):
    """Custom type audioCalibrationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-calibrating", 1),
          ("busy-calibrating", 2),
          ("calibration-done", 3))
    )


_AudioCalibrationStatus_Type.__name__ = "Integer32"
_AudioCalibrationStatus_Object = MibTableColumn
audioCalibrationStatus = _AudioCalibrationStatus_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 6, 1, 4),
    _AudioCalibrationStatus_Type()
)
audioCalibrationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioCalibrationStatus.setStatus("current")
_AudioDTSStatusTable_Object = MibTable
audioDTSStatusTable = _AudioDTSStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 7)
)
if mibBuilder.loadTexts:
    audioDTSStatusTable.setStatus("current")
_AudioDTSStatusEntry_Object = MibTableRow
audioDTSStatusEntry = _AudioDTSStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 7, 1)
)
audioDTSStatusEntry.setIndexNames(
    (0, "NDS-DTH3-AUDIO", "audioDTSStatusModIndex"),
    (0, "NDS-DTH3-AUDIO", "audioDTSStatusChanIndex"),
)
if mibBuilder.loadTexts:
    audioDTSStatusEntry.setStatus("current")


class _AudioDTSStatusModIndex_Type(Integer32):
    """Custom type audioDTSStatusModIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_AudioDTSStatusModIndex_Type.__name__ = "Integer32"
_AudioDTSStatusModIndex_Object = MibTableColumn
audioDTSStatusModIndex = _AudioDTSStatusModIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 7, 1, 1),
    _AudioDTSStatusModIndex_Type()
)
audioDTSStatusModIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioDTSStatusModIndex.setStatus("current")


class _AudioDTSStatusChanIndex_Type(Integer32):
    """Custom type audioDTSStatusChanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("a", 1),
          ("b", 2))
    )


_AudioDTSStatusChanIndex_Type.__name__ = "Integer32"
_AudioDTSStatusChanIndex_Object = MibTableColumn
audioDTSStatusChanIndex = _AudioDTSStatusChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 7, 1, 2),
    _AudioDTSStatusChanIndex_Type()
)
audioDTSStatusChanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioDTSStatusChanIndex.setStatus("current")


class _AudioDTSStatusValid_Type(Integer32):
    """Custom type audioDTSStatusValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("error", 0),
          ("valid", 1))
    )


_AudioDTSStatusValid_Type.__name__ = "Integer32"
_AudioDTSStatusValid_Object = MibTableColumn
audioDTSStatusValid = _AudioDTSStatusValid_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 7, 1, 3),
    _AudioDTSStatusValid_Type()
)
audioDTSStatusValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioDTSStatusValid.setStatus("current")


class _AudioDTSStatusFrameSize_Type(Integer32):
    """Custom type audioDTSStatusFrameSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("size-512", 0),
          ("size-1024", 1),
          ("size-2048", 2))
    )


_AudioDTSStatusFrameSize_Type.__name__ = "Integer32"
_AudioDTSStatusFrameSize_Object = MibTableColumn
audioDTSStatusFrameSize = _AudioDTSStatusFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 7, 1, 4),
    _AudioDTSStatusFrameSize_Type()
)
audioDTSStatusFrameSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioDTSStatusFrameSize.setStatus("current")


class _AudioDTSStatusSampleRate_Type(Integer32):
    """Custom type audioDTSStatusSampleRate based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("rate-8-kHz", 1),
          ("rate-16-kHz", 2),
          ("rate-32-kHz", 3),
          ("rate-64-kHz", 4),
          ("rate-128-kHz", 5),
          ("rate-11pt025-kHz", 6),
          ("rate-22pt05-kHz", 7),
          ("rate-44pt1-kHz", 8),
          ("rate-88pt02-kHz", 9),
          ("rate-176pt4-kHz", 10),
          ("rate-12-kHz", 11),
          ("rate-24-kHz", 12),
          ("rate-48-kHz", 13),
          ("rate-96-kHz", 14),
          ("rate-192-kHz", 15))
    )


_AudioDTSStatusSampleRate_Type.__name__ = "Integer32"
_AudioDTSStatusSampleRate_Object = MibTableColumn
audioDTSStatusSampleRate = _AudioDTSStatusSampleRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 7, 1, 5),
    _AudioDTSStatusSampleRate_Type()
)
audioDTSStatusSampleRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioDTSStatusSampleRate.setStatus("current")


class _AudioDTSStatusBitRate_Type(Integer32):
    """Custom type audioDTSStatusBitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(5,
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
              31)
        )
    )
    namedValues = NamedValues(
        *(("rate-128-kbps", 5),
          ("rate-192-kbps", 6),
          ("rate-224-kbps", 7),
          ("rate-256-kbps", 8),
          ("rate-320-kbps", 9),
          ("rate-384-kbps", 10),
          ("rate-448-kbps", 11),
          ("rate-512-kbps", 12),
          ("rate-576-kbps", 13),
          ("rate-640-kbps", 14),
          ("rate-768-kbps", 15),
          ("rate-960-kbps", 16),
          ("rate-1024-kbps", 17),
          ("rate-1152-kbps", 18),
          ("rate-1280-kbps", 19),
          ("rate-1344-kbps", 20),
          ("rate-1408-kbps", 21),
          ("rate-1411pt2-kbps", 22),
          ("rate-1472-kbps", 23),
          ("rate-1536-kHz", 24),
          ("rate-1920-kHz", 25),
          ("rate-2048-kHz", 26),
          ("rate-3072-kHz", 27),
          ("rate-3840-kHz", 28),
          ("open", 29),
          ("variable", 30),
          ("lossless", 31))
    )


_AudioDTSStatusBitRate_Type.__name__ = "Integer32"
_AudioDTSStatusBitRate_Object = MibTableColumn
audioDTSStatusBitRate = _AudioDTSStatusBitRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 7, 1, 6),
    _AudioDTSStatusBitRate_Type()
)
audioDTSStatusBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioDTSStatusBitRate.setStatus("current")


class _AudioDTSStatusnblks_Type(Integer32):
    """Custom type audioDTSStatusnblks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_AudioDTSStatusnblks_Type.__name__ = "Integer32"
_AudioDTSStatusnblks_Object = MibTableColumn
audioDTSStatusnblks = _AudioDTSStatusnblks_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 7, 1, 7),
    _AudioDTSStatusnblks_Type()
)
audioDTSStatusnblks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioDTSStatusnblks.setStatus("current")


class _AudioDTSStatusFSize_Type(Integer32):
    """Custom type audioDTSStatusFSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16383),
    )


_AudioDTSStatusFSize_Type.__name__ = "Integer32"
_AudioDTSStatusFSize_Object = MibTableColumn
audioDTSStatusFSize = _AudioDTSStatusFSize_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 7, 1, 8),
    _AudioDTSStatusFSize_Type()
)
audioDTSStatusFSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioDTSStatusFSize.setStatus("current")


class _AudioDTSStatusSurroundMode_Type(Integer32):
    """Custom type audioDTSStatusSurroundMode based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("mode-1-mono", 0),
          ("mode-user-defined", 1),
          ("mode-2-L-R-stereo", 2),
          ("mode-2-LplusR-LminusR", 3),
          ("mode-2-LT-RT", 4),
          ("mode-3-C-L-R", 5),
          ("mode-3-L-R-S", 6),
          ("mode-4-C-L-R-S", 7),
          ("mode-4-L-R-SL-SR", 8),
          ("mode-35-C-L-R-SL-SR", 9))
    )


_AudioDTSStatusSurroundMode_Type.__name__ = "Integer32"
_AudioDTSStatusSurroundMode_Object = MibTableColumn
audioDTSStatusSurroundMode = _AudioDTSStatusSurroundMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 7, 1, 9),
    _AudioDTSStatusSurroundMode_Type()
)
audioDTSStatusSurroundMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioDTSStatusSurroundMode.setStatus("current")


class _AudioDTSStatusLFEFlag_Type(Integer32):
    """Custom type audioDTSStatusLFEFlag based on Integer32"""
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


_AudioDTSStatusLFEFlag_Type.__name__ = "Integer32"
_AudioDTSStatusLFEFlag_Object = MibTableColumn
audioDTSStatusLFEFlag = _AudioDTSStatusLFEFlag_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 7, 1, 10),
    _AudioDTSStatusLFEFlag_Type()
)
audioDTSStatusLFEFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioDTSStatusLFEFlag.setStatus("current")


class _AudioDTSStatusSurroundFlag_Type(Integer32):
    """Custom type audioDTSStatusSurroundFlag based on Integer32"""
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
          ("matrixed", 1),
          ("discrete", 2))
    )


_AudioDTSStatusSurroundFlag_Type.__name__ = "Integer32"
_AudioDTSStatusSurroundFlag_Object = MibTableColumn
audioDTSStatusSurroundFlag = _AudioDTSStatusSurroundFlag_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 7, 7, 1, 11),
    _AudioDTSStatusSurroundFlag_Type()
)
audioDTSStatusSurroundFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    audioDTSStatusSurroundFlag.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NDS-DTH3-AUDIO",
    **{"ndsDTH3Encoder": ndsDTH3Encoder,
       "audioEnc": audioEnc,
       "audioModuleNumber": audioModuleNumber,
       "audioModuleTable": audioModuleTable,
       "audioModuleEntry": audioModuleEntry,
       "audioModuleIndex": audioModuleIndex,
       "audioChannelIndex": audioChannelIndex,
       "audioHardwareRelease": audioHardwareRelease,
       "audioSoftwareRelease": audioSoftwareRelease,
       "audioFirmwareRelease": audioFirmwareRelease,
       "audioModuleId": audioModuleId,
       "audionextTimeDate": audionextTimeDate,
       "audioLevelLeft": audioLevelLeft,
       "audioLevelRight": audioLevelRight,
       "audioTable": audioTable,
       "audioEntry": audioEntry,
       "audioCurrentNextIndex": audioCurrentNextIndex,
       "audioModIndex": audioModIndex,
       "audioChanIndex": audioChanIndex,
       "audioSource": audioSource,
       "audioClipLevel": audioClipLevel,
       "audioTermination": audioTermination,
       "audioSilenceTimeout": audioSilenceTimeout,
       "audioSampleFrequency": audioSampleFrequency,
       "audioCodingStd": audioCodingStd,
       "audioCopyright": audioCopyright,
       "audioOriginal": audioOriginal,
       "audioDeEmphasis": audioDeEmphasis,
       "audioBitRate": audioBitRate,
       "audioCoding": audioCoding,
       "audioDelay": audioDelay,
       "audioPID": audioPID,
       "audioSMPTEstandard": audioSMPTEstandard,
       "audioLipSync": audioLipSync,
       "audioLinearPCMChannelNo": audioLinearPCMChannelNo,
       "audioLipSyncOffset": audioLipSyncOffset,
       "audioInsertPCROnPID": audioInsertPCROnPID,
       "audioShortList": audioShortList,
       "audioComponentTag": audioComponentTag,
       "audioDTSFrameSize": audioDTSFrameSize,
       "audioDTSLinRegDescriptor": audioDTSLinRegDescriptor,
       "audioOPDigitalInputLoss": audioOPDigitalInputLoss,
       "audioHDSource": audioHDSource,
       "audioVPSControlsCodingMode": audioVPSControlsCodingMode,
       "audioVPSCodingMode": audioVPSCodingMode,
       "audioVPSWord5": audioVPSWord5,
       "audioVPSStereoMode": audioVPSStereoMode,
       "audioVPSDualChanMode": audioVPSDualChanMode,
       "audioLowDelay": audioLowDelay,
       "audioAC3Table": audioAC3Table,
       "audioAC3Entry": audioAC3Entry,
       "audioAC3CurrentNextIndex": audioAC3CurrentNextIndex,
       "audioAC3ModIndex": audioAC3ModIndex,
       "audioAC3ChanIndex": audioAC3ChanIndex,
       "audioBitStream": audioBitStream,
       "audioLowFreq": audioLowFreq,
       "audioSurroundDownmix": audioSurroundDownmix,
       "audioDolbySurround": audioDolbySurround,
       "audioDialogueNorm": audioDialogueNorm,
       "audioProdInfo": audioProdInfo,
       "audioMixLevel": audioMixLevel,
       "audioRoomType": audioRoomType,
       "audioCompression": audioCompression,
       "audioCBLowFilter": audioCBLowFilter,
       "audioLFELowFilter": audioLFELowFilter,
       "audioDCHighFilter": audioDCHighFilter,
       "audioExternalDelay": audioExternalDelay,
       "audioRFProtection": audioRFProtection,
       "audioLangTable": audioLangTable,
       "audioLangEntry": audioLangEntry,
       "audioCurrentNextLangIndex": audioCurrentNextLangIndex,
       "audioLangModIndex": audioLangModIndex,
       "audioLangChanIndex": audioLangChanIndex,
       "audioLangIndex": audioLangIndex,
       "audioLanguage": audioLanguage,
       "audioCalibrationTable": audioCalibrationTable,
       "audioCalibrationEntry": audioCalibrationEntry,
       "audioCalibrationModuleIndex": audioCalibrationModuleIndex,
       "audioCalibrationChannelIndex": audioCalibrationChannelIndex,
       "audioBeginCalibration": audioBeginCalibration,
       "audioCalibrationStatus": audioCalibrationStatus,
       "audioDTSStatusTable": audioDTSStatusTable,
       "audioDTSStatusEntry": audioDTSStatusEntry,
       "audioDTSStatusModIndex": audioDTSStatusModIndex,
       "audioDTSStatusChanIndex": audioDTSStatusChanIndex,
       "audioDTSStatusValid": audioDTSStatusValid,
       "audioDTSStatusFrameSize": audioDTSStatusFrameSize,
       "audioDTSStatusSampleRate": audioDTSStatusSampleRate,
       "audioDTSStatusBitRate": audioDTSStatusBitRate,
       "audioDTSStatusnblks": audioDTSStatusnblks,
       "audioDTSStatusFSize": audioDTSStatusFSize,
       "audioDTSStatusSurroundMode": audioDTSStatusSurroundMode,
       "audioDTSStatusLFEFlag": audioDTSStatusLFEFlag,
       "audioDTSStatusSurroundFlag": audioDTSStatusSurroundFlag}
)
