# SNMP MIB module (SCTE-HMS-MPEG-ENCODER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/scte_5591/SCTE-HMS-MPEG-ENCODER-MIB.mib
# Produced by pysmi-1.5.11 at Fri May 23 22:32:18 2025
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

(PhysicalIndex,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex",
    "entPhysicalIndex")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType",
    "InetPortNumber")

(DeviceEnableDisableValues,
 HePIDValue,
 MpegErrorStatus,
 VideoInputFrameRateType) = mibBuilder.importSymbols(
    "SCTE-HMS-HEADENDIDENT-TC-MIB",
    "DeviceEnableDisableValues",
    "HePIDValue",
    "MpegErrorStatus",
    "VideoInputFrameRateType")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

mpegEncoderMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MpegEncoderMIBObjects_ObjectIdentity = ObjectIdentity
mpegEncoderMIBObjects = _MpegEncoderMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1)
)
_ConfigurationReport_ObjectIdentity = ObjectIdentity
configurationReport = _ConfigurationReport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1)
)
_EncoderCfgVideoTable_Object = MibTable
encoderCfgVideoTable = _EncoderCfgVideoTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    encoderCfgVideoTable.setStatus("current")
_EncoderCfgVideoEntry_Object = MibTableRow
encoderCfgVideoEntry = _EncoderCfgVideoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 1, 1)
)
encoderCfgVideoEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVideoIndex"),
)
if mibBuilder.loadTexts:
    encoderCfgVideoEntry.setStatus("current")
_EncoderCfgVideoIndex_Type = Unsigned32
_EncoderCfgVideoIndex_Object = MibTableColumn
encoderCfgVideoIndex = _EncoderCfgVideoIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 1, 1, 1),
    _EncoderCfgVideoIndex_Type()
)
encoderCfgVideoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    encoderCfgVideoIndex.setStatus("current")


class _EncoderCfgVideoType_Type(Integer32):
    """Custom type encoderCfgVideoType based on Integer32"""
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
        *(("other", 1),
          ("primary", 2),
          ("pip", 3),
          ("dvbH", 4))
    )


_EncoderCfgVideoType_Type.__name__ = "Integer32"
_EncoderCfgVideoType_Object = MibTableColumn
encoderCfgVideoType = _EncoderCfgVideoType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 1, 1, 2),
    _EncoderCfgVideoType_Type()
)
encoderCfgVideoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVideoType.setStatus("current")


class _EncoderCfgVideoCompression_Type(Integer32):
    """Custom type encoderCfgVideoCompression based on Integer32"""
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
        *(("other", 1),
          ("mpeg2", 2),
          ("mpeg4", 3),
          ("avc", 4))
    )


_EncoderCfgVideoCompression_Type.__name__ = "Integer32"
_EncoderCfgVideoCompression_Object = MibTableColumn
encoderCfgVideoCompression = _EncoderCfgVideoCompression_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 1, 1, 3),
    _EncoderCfgVideoCompression_Type()
)
encoderCfgVideoCompression.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVideoCompression.setStatus("current")
_EncoderCfgVideoPid_Type = HePIDValue
_EncoderCfgVideoPid_Object = MibTableColumn
encoderCfgVideoPid = _EncoderCfgVideoPid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 1, 1, 4),
    _EncoderCfgVideoPid_Type()
)
encoderCfgVideoPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVideoPid.setStatus("current")
_EncoderCfgVideoPcrPid_Type = HePIDValue
_EncoderCfgVideoPcrPid_Object = MibTableColumn
encoderCfgVideoPcrPid = _EncoderCfgVideoPcrPid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 1, 1, 5),
    _EncoderCfgVideoPcrPid_Type()
)
encoderCfgVideoPcrPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVideoPcrPid.setStatus("current")
_EncoderCfgVideoServiceIndex_Type = Unsigned32
_EncoderCfgVideoServiceIndex_Object = MibTableColumn
encoderCfgVideoServiceIndex = _EncoderCfgVideoServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 1, 1, 6),
    _EncoderCfgVideoServiceIndex_Type()
)
encoderCfgVideoServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVideoServiceIndex.setStatus("current")
_EncoderCfgVideoVertResolution_Type = Integer32
_EncoderCfgVideoVertResolution_Object = MibTableColumn
encoderCfgVideoVertResolution = _EncoderCfgVideoVertResolution_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 1, 1, 7),
    _EncoderCfgVideoVertResolution_Type()
)
encoderCfgVideoVertResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVideoVertResolution.setStatus("current")
_EncoderCfgVideoHorzResolution_Type = Integer32
_EncoderCfgVideoHorzResolution_Object = MibTableColumn
encoderCfgVideoHorzResolution = _EncoderCfgVideoHorzResolution_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 1, 1, 8),
    _EncoderCfgVideoHorzResolution_Type()
)
encoderCfgVideoHorzResolution.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVideoHorzResolution.setStatus("current")
_EncoderCfgVideoBitrateAvg_Type = Integer32
_EncoderCfgVideoBitrateAvg_Object = MibTableColumn
encoderCfgVideoBitrateAvg = _EncoderCfgVideoBitrateAvg_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 1, 1, 9),
    _EncoderCfgVideoBitrateAvg_Type()
)
encoderCfgVideoBitrateAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVideoBitrateAvg.setStatus("current")
if mibBuilder.loadTexts:
    encoderCfgVideoBitrateAvg.setUnits("bps")
_EncoderCfgVideoBitrateMax_Type = Integer32
_EncoderCfgVideoBitrateMax_Object = MibTableColumn
encoderCfgVideoBitrateMax = _EncoderCfgVideoBitrateMax_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 1, 1, 10),
    _EncoderCfgVideoBitrateMax_Type()
)
encoderCfgVideoBitrateMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVideoBitrateMax.setStatus("current")
if mibBuilder.loadTexts:
    encoderCfgVideoBitrateMax.setUnits("bps")
_EncoderCfgVideoBitrateMin_Type = Integer32
_EncoderCfgVideoBitrateMin_Object = MibTableColumn
encoderCfgVideoBitrateMin = _EncoderCfgVideoBitrateMin_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 1, 1, 11),
    _EncoderCfgVideoBitrateMin_Type()
)
encoderCfgVideoBitrateMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVideoBitrateMin.setStatus("current")
if mibBuilder.loadTexts:
    encoderCfgVideoBitrateMin.setUnits("bps")
_EncoderCfgVideoFilmMode_Type = DeviceEnableDisableValues
_EncoderCfgVideoFilmMode_Object = MibTableColumn
encoderCfgVideoFilmMode = _EncoderCfgVideoFilmMode_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 1, 1, 12),
    _EncoderCfgVideoFilmMode_Type()
)
encoderCfgVideoFilmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVideoFilmMode.setStatus("current")


class _EncoderCfgVideoRateMode_Type(Integer32):
    """Custom type encoderCfgVideoRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 1),
          ("vbr", 2))
    )


_EncoderCfgVideoRateMode_Type.__name__ = "Integer32"
_EncoderCfgVideoRateMode_Object = MibTableColumn
encoderCfgVideoRateMode = _EncoderCfgVideoRateMode_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 1, 1, 14),
    _EncoderCfgVideoRateMode_Type()
)
encoderCfgVideoRateMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVideoRateMode.setStatus("current")


class _EncoderCfgVideoBorderProcessing_Type(Integer32):
    """Custom type encoderCfgVideoBorderProcessing based on Integer32"""
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
          ("cropped", 2),
          ("other", 3))
    )


_EncoderCfgVideoBorderProcessing_Type.__name__ = "Integer32"
_EncoderCfgVideoBorderProcessing_Object = MibTableColumn
encoderCfgVideoBorderProcessing = _EncoderCfgVideoBorderProcessing_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 1, 1, 15),
    _EncoderCfgVideoBorderProcessing_Type()
)
encoderCfgVideoBorderProcessing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVideoBorderProcessing.setStatus("current")


class _EncoderCfgVideoPesAlignment_Type(Integer32):
    """Custom type encoderCfgVideoPesAlignment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("aligned", 2),
          ("nonAligned", 3))
    )


_EncoderCfgVideoPesAlignment_Type.__name__ = "Integer32"
_EncoderCfgVideoPesAlignment_Object = MibTableColumn
encoderCfgVideoPesAlignment = _EncoderCfgVideoPesAlignment_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 1, 1, 16),
    _EncoderCfgVideoPesAlignment_Type()
)
encoderCfgVideoPesAlignment.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVideoPesAlignment.setStatus("current")
_EncoderCfgVideoCodingDelay_Type = Integer32
_EncoderCfgVideoCodingDelay_Object = MibTableColumn
encoderCfgVideoCodingDelay = _EncoderCfgVideoCodingDelay_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 1, 1, 17),
    _EncoderCfgVideoCodingDelay_Type()
)
encoderCfgVideoCodingDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVideoCodingDelay.setStatus("current")
if mibBuilder.loadTexts:
    encoderCfgVideoCodingDelay.setUnits("milliseconds")
_EncoderCfgVideoDeblockEnable_Type = DeviceEnableDisableValues
_EncoderCfgVideoDeblockEnable_Object = MibTableColumn
encoderCfgVideoDeblockEnable = _EncoderCfgVideoDeblockEnable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 1, 1, 18),
    _EncoderCfgVideoDeblockEnable_Type()
)
encoderCfgVideoDeblockEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVideoDeblockEnable.setStatus("current")


class _EncoderCfgVideoDeblockAlpha_Type(Integer32):
    """Custom type encoderCfgVideoDeblockAlpha based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-6, 6),
    )


_EncoderCfgVideoDeblockAlpha_Type.__name__ = "Integer32"
_EncoderCfgVideoDeblockAlpha_Object = MibTableColumn
encoderCfgVideoDeblockAlpha = _EncoderCfgVideoDeblockAlpha_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 1, 1, 19),
    _EncoderCfgVideoDeblockAlpha_Type()
)
encoderCfgVideoDeblockAlpha.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVideoDeblockAlpha.setStatus("current")


class _EncoderCfgVideoDeblockBeta_Type(Integer32):
    """Custom type encoderCfgVideoDeblockBeta based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-6, 6),
    )


_EncoderCfgVideoDeblockBeta_Type.__name__ = "Integer32"
_EncoderCfgVideoDeblockBeta_Object = MibTableColumn
encoderCfgVideoDeblockBeta = _EncoderCfgVideoDeblockBeta_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 1, 1, 20),
    _EncoderCfgVideoDeblockBeta_Type()
)
encoderCfgVideoDeblockBeta.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVideoDeblockBeta.setStatus("current")
_EncoderCfgVideoIdrRate_Type = Integer32
_EncoderCfgVideoIdrRate_Object = MibTableColumn
encoderCfgVideoIdrRate = _EncoderCfgVideoIdrRate_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 1, 1, 21),
    _EncoderCfgVideoIdrRate_Type()
)
encoderCfgVideoIdrRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVideoIdrRate.setStatus("current")


class _EncoderCfgVideoInputIf_Type(Integer32):
    """Custom type encoderCfgVideoInputIf based on Integer32"""
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
        *(("other", 1),
          ("analog", 2),
          ("sdi", 3),
          ("hdsdi", 4))
    )


_EncoderCfgVideoInputIf_Type.__name__ = "Integer32"
_EncoderCfgVideoInputIf_Object = MibTableColumn
encoderCfgVideoInputIf = _EncoderCfgVideoInputIf_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 1, 1, 22),
    _EncoderCfgVideoInputIf_Type()
)
encoderCfgVideoInputIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVideoInputIf.setStatus("current")
_EncoderCfgVideoInputFrameRate_Type = VideoInputFrameRateType
_EncoderCfgVideoInputFrameRate_Object = MibTableColumn
encoderCfgVideoInputFrameRate = _EncoderCfgVideoInputFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 1, 1, 23),
    _EncoderCfgVideoInputFrameRate_Type()
)
encoderCfgVideoInputFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVideoInputFrameRate.setStatus("current")


class _EncoderCfgVideoInputScan_Type(Integer32):
    """Custom type encoderCfgVideoInputScan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interlaced", 1),
          ("progressive", 2))
    )


_EncoderCfgVideoInputScan_Type.__name__ = "Integer32"
_EncoderCfgVideoInputScan_Object = MibTableColumn
encoderCfgVideoInputScan = _EncoderCfgVideoInputScan_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 1, 1, 24),
    _EncoderCfgVideoInputScan_Type()
)
encoderCfgVideoInputScan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVideoInputScan.setStatus("current")


class _EncoderCfgVideoInputFormat_Type(Integer32):
    """Custom type encoderCfgVideoInputFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("component", 1),
          ("composite", 2))
    )


_EncoderCfgVideoInputFormat_Type.__name__ = "Integer32"
_EncoderCfgVideoInputFormat_Object = MibTableColumn
encoderCfgVideoInputFormat = _EncoderCfgVideoInputFormat_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 1, 1, 25),
    _EncoderCfgVideoInputFormat_Type()
)
encoderCfgVideoInputFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVideoInputFormat.setStatus("current")


class _EncoderCfgVideoAspectRatio_Type(Integer32):
    """Custom type encoderCfgVideoAspectRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("aspect4x3", 2),
          ("aspect16x9", 3))
    )


_EncoderCfgVideoAspectRatio_Type.__name__ = "Integer32"
_EncoderCfgVideoAspectRatio_Object = MibTableColumn
encoderCfgVideoAspectRatio = _EncoderCfgVideoAspectRatio_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 1, 1, 26),
    _EncoderCfgVideoAspectRatio_Type()
)
encoderCfgVideoAspectRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVideoAspectRatio.setStatus("current")
_EncoderCfgAudioTable_Object = MibTable
encoderCfgAudioTable = _EncoderCfgAudioTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 2)
)
if mibBuilder.loadTexts:
    encoderCfgAudioTable.setStatus("current")
_EncoderCfgAudioEntry_Object = MibTableRow
encoderCfgAudioEntry = _EncoderCfgAudioEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 2, 1)
)
encoderCfgAudioEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgAudioChannelIndex"),
)
if mibBuilder.loadTexts:
    encoderCfgAudioEntry.setStatus("current")
_EncoderCfgAudioChannelIndex_Type = Unsigned32
_EncoderCfgAudioChannelIndex_Object = MibTableColumn
encoderCfgAudioChannelIndex = _EncoderCfgAudioChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 2, 1, 1),
    _EncoderCfgAudioChannelIndex_Type()
)
encoderCfgAudioChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    encoderCfgAudioChannelIndex.setStatus("current")
_EncoderCfgAudioEnabled_Type = DeviceEnableDisableValues
_EncoderCfgAudioEnabled_Object = MibTableColumn
encoderCfgAudioEnabled = _EncoderCfgAudioEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 2, 1, 2),
    _EncoderCfgAudioEnabled_Type()
)
encoderCfgAudioEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgAudioEnabled.setStatus("current")


class _EncoderCfgAudioStandard_Type(Integer32):
    """Custom type encoderCfgAudioStandard based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("ac3", 2),
          ("eac3", 3),
          ("mpeg1", 4),
          ("mpeg2", 5),
          ("aacMpeg2", 6),
          ("heAacMpeg2", 7),
          ("aacMpeg4", 8),
          ("heAacMpeg4", 9))
    )


_EncoderCfgAudioStandard_Type.__name__ = "Integer32"
_EncoderCfgAudioStandard_Object = MibTableColumn
encoderCfgAudioStandard = _EncoderCfgAudioStandard_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 2, 1, 3),
    _EncoderCfgAudioStandard_Type()
)
encoderCfgAudioStandard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgAudioStandard.setStatus("current")
_EncoderCfgAudioPid_Type = HePIDValue
_EncoderCfgAudioPid_Object = MibTableColumn
encoderCfgAudioPid = _EncoderCfgAudioPid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 2, 1, 4),
    _EncoderCfgAudioPid_Type()
)
encoderCfgAudioPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgAudioPid.setStatus("current")
_EncoderCfgAudioPcrPid_Type = HePIDValue
_EncoderCfgAudioPcrPid_Object = MibTableColumn
encoderCfgAudioPcrPid = _EncoderCfgAudioPcrPid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 2, 1, 5),
    _EncoderCfgAudioPcrPid_Type()
)
encoderCfgAudioPcrPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgAudioPcrPid.setStatus("current")
_EncoderCfgAudioServiceIndex_Type = Unsigned32
_EncoderCfgAudioServiceIndex_Object = MibTableColumn
encoderCfgAudioServiceIndex = _EncoderCfgAudioServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 2, 1, 6),
    _EncoderCfgAudioServiceIndex_Type()
)
encoderCfgAudioServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgAudioServiceIndex.setStatus("current")


class _EncoderCfgAudioMode_Type(Integer32):
    """Custom type encoderCfgAudioMode based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("stereo", 2),
          ("joint", 3),
          ("mono", 4),
          ("monoL", 5),
          ("monoR", 6),
          ("dualMono", 7),
          ("fivePlusOne", 8),
          ("unknown", 9))
    )


_EncoderCfgAudioMode_Type.__name__ = "Integer32"
_EncoderCfgAudioMode_Object = MibTableColumn
encoderCfgAudioMode = _EncoderCfgAudioMode_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 2, 1, 7),
    _EncoderCfgAudioMode_Type()
)
encoderCfgAudioMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgAudioMode.setStatus("current")


class _EncoderCfgAudioPassThru_Type(Integer32):
    """Custom type encoderCfgAudioPassThru based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("encoded", 1),
          ("passThrough", 2))
    )


_EncoderCfgAudioPassThru_Type.__name__ = "Integer32"
_EncoderCfgAudioPassThru_Object = MibTableColumn
encoderCfgAudioPassThru = _EncoderCfgAudioPassThru_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 2, 1, 8),
    _EncoderCfgAudioPassThru_Type()
)
encoderCfgAudioPassThru.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgAudioPassThru.setStatus("current")
_EncoderCfgAudioRate_Type = Integer32
_EncoderCfgAudioRate_Object = MibTableColumn
encoderCfgAudioRate = _EncoderCfgAudioRate_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 2, 1, 9),
    _EncoderCfgAudioRate_Type()
)
encoderCfgAudioRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgAudioRate.setStatus("current")
if mibBuilder.loadTexts:
    encoderCfgAudioRate.setUnits("kbps")
_EncoderCfgAudioLanguageA_Type = DisplayString
_EncoderCfgAudioLanguageA_Object = MibTableColumn
encoderCfgAudioLanguageA = _EncoderCfgAudioLanguageA_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 2, 1, 10),
    _EncoderCfgAudioLanguageA_Type()
)
encoderCfgAudioLanguageA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgAudioLanguageA.setStatus("current")
_EncoderCfgAudioLanguageB_Type = DisplayString
_EncoderCfgAudioLanguageB_Object = MibTableColumn
encoderCfgAudioLanguageB = _EncoderCfgAudioLanguageB_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 2, 1, 11),
    _EncoderCfgAudioLanguageB_Type()
)
encoderCfgAudioLanguageB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgAudioLanguageB.setStatus("current")


class _EncoderCfgAudioLipSync_Type(Integer32):
    """Custom type encoderCfgAudioLipSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixed", 1),
          ("manual", 2))
    )


_EncoderCfgAudioLipSync_Type.__name__ = "Integer32"
_EncoderCfgAudioLipSync_Object = MibTableColumn
encoderCfgAudioLipSync = _EncoderCfgAudioLipSync_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 2, 1, 12),
    _EncoderCfgAudioLipSync_Type()
)
encoderCfgAudioLipSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgAudioLipSync.setStatus("current")


class _EncoderCfgAudioDialogNorm_Type(Integer32):
    """Custom type encoderCfgAudioDialogNorm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-31, 0),
    )


_EncoderCfgAudioDialogNorm_Type.__name__ = "Integer32"
_EncoderCfgAudioDialogNorm_Object = MibTableColumn
encoderCfgAudioDialogNorm = _EncoderCfgAudioDialogNorm_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 2, 1, 13),
    _EncoderCfgAudioDialogNorm_Type()
)
encoderCfgAudioDialogNorm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgAudioDialogNorm.setStatus("current")
if mibBuilder.loadTexts:
    encoderCfgAudioDialogNorm.setUnits("dBFS")


class _EncoderCfgAudioInputType_Type(Integer32):
    """Custom type encoderCfgAudioInputType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("embedded", 1),
          ("aes", 2),
          ("analog", 3))
    )


_EncoderCfgAudioInputType_Type.__name__ = "Integer32"
_EncoderCfgAudioInputType_Object = MibTableColumn
encoderCfgAudioInputType = _EncoderCfgAudioInputType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 2, 1, 14),
    _EncoderCfgAudioInputType_Type()
)
encoderCfgAudioInputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgAudioInputType.setStatus("current")
_EncoderCfgAudioInputLabel_Type = DisplayString
_EncoderCfgAudioInputLabel_Object = MibTableColumn
encoderCfgAudioInputLabel = _EncoderCfgAudioInputLabel_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 2, 1, 15),
    _EncoderCfgAudioInputLabel_Type()
)
encoderCfgAudioInputLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgAudioInputLabel.setStatus("current")
_EncoderCfgVbiTable_Object = MibTable
encoderCfgVbiTable = _EncoderCfgVbiTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 3)
)
if mibBuilder.loadTexts:
    encoderCfgVbiTable.setStatus("current")
_EncoderCfgVbiEntry_Object = MibTableRow
encoderCfgVbiEntry = _EncoderCfgVbiEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 3, 1)
)
encoderCfgVbiEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVbiIndex"),
)
if mibBuilder.loadTexts:
    encoderCfgVbiEntry.setStatus("current")
_EncoderCfgVbiIndex_Type = Unsigned32
_EncoderCfgVbiIndex_Object = MibTableColumn
encoderCfgVbiIndex = _EncoderCfgVbiIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 3, 1, 1),
    _EncoderCfgVbiIndex_Type()
)
encoderCfgVbiIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    encoderCfgVbiIndex.setStatus("current")


class _EncoderCfgVbiField_Type(Integer32):
    """Custom type encoderCfgVbiField based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("field1", 1),
          ("field2", 2),
          ("both", 3))
    )


_EncoderCfgVbiField_Type.__name__ = "Integer32"
_EncoderCfgVbiField_Object = MibTableColumn
encoderCfgVbiField = _EncoderCfgVbiField_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 3, 1, 2),
    _EncoderCfgVbiField_Type()
)
encoderCfgVbiField.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVbiField.setStatus("current")
_EncoderCfgVbiLine_Type = Integer32
_EncoderCfgVbiLine_Object = MibTableColumn
encoderCfgVbiLine = _EncoderCfgVbiLine_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 3, 1, 3),
    _EncoderCfgVbiLine_Type()
)
encoderCfgVbiLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVbiLine.setStatus("current")


class _EncoderCfgVbiType_Type(Integer32):
    """Custom type encoderCfgVbiType based on Integer32"""
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
              16)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("eia608Caption", 2),
          ("amol", 3),
          ("amol2", 4),
          ("nabts", 5),
          ("vitc", 6),
          ("vits", 7),
          ("tvGuide", 8),
          ("cgmsA", 9),
          ("dataBcast", 10),
          ("wst", 11),
          ("vps", 12),
          ("wss", 13),
          ("epg", 14),
          ("barData", 15),
          ("scte104", 16))
    )


_EncoderCfgVbiType_Type.__name__ = "Integer32"
_EncoderCfgVbiType_Object = MibTableColumn
encoderCfgVbiType = _EncoderCfgVbiType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 3, 1, 4),
    _EncoderCfgVbiType_Type()
)
encoderCfgVbiType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVbiType.setStatus("current")


class _EncoderCfgVbiCarriage_Type(Integer32):
    """Custom type encoderCfgVbiCarriage based on Integer32"""
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
        *(("otherInVideo", 1),
          ("otherInPid", 2),
          ("scte20", 3),
          ("scte21", 4),
          ("scte127", 5),
          ("etsiEn300472", 6),
          ("etsiEn301775", 7))
    )


_EncoderCfgVbiCarriage_Type.__name__ = "Integer32"
_EncoderCfgVbiCarriage_Object = MibTableColumn
encoderCfgVbiCarriage = _EncoderCfgVbiCarriage_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 3, 1, 5),
    _EncoderCfgVbiCarriage_Type()
)
encoderCfgVbiCarriage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVbiCarriage.setStatus("current")
_EncoderCfgVbiCompIndex_Type = Unsigned32
_EncoderCfgVbiCompIndex_Object = MibTableColumn
encoderCfgVbiCompIndex = _EncoderCfgVbiCompIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 3, 1, 6),
    _EncoderCfgVbiCompIndex_Type()
)
encoderCfgVbiCompIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVbiCompIndex.setStatus("current")
_EncoderCfgVancTable_Object = MibTable
encoderCfgVancTable = _EncoderCfgVancTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 4)
)
if mibBuilder.loadTexts:
    encoderCfgVancTable.setStatus("current")
_EncoderCfgVancEntry_Object = MibTableRow
encoderCfgVancEntry = _EncoderCfgVancEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 4, 1)
)
encoderCfgVancEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVancServiceIndex"),
)
if mibBuilder.loadTexts:
    encoderCfgVancEntry.setStatus("current")
_EncoderCfgVancServiceIndex_Type = Unsigned32
_EncoderCfgVancServiceIndex_Object = MibTableColumn
encoderCfgVancServiceIndex = _EncoderCfgVancServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 4, 1, 1),
    _EncoderCfgVancServiceIndex_Type()
)
encoderCfgVancServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    encoderCfgVancServiceIndex.setStatus("current")


class _EncoderCfgVancDid_Type(Integer32):
    """Custom type encoderCfgVancDid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_EncoderCfgVancDid_Type.__name__ = "Integer32"
_EncoderCfgVancDid_Object = MibTableColumn
encoderCfgVancDid = _EncoderCfgVancDid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 4, 1, 2),
    _EncoderCfgVancDid_Type()
)
encoderCfgVancDid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVancDid.setStatus("current")


class _EncoderCfgVancSdid_Type(Integer32):
    """Custom type encoderCfgVancSdid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_EncoderCfgVancSdid_Type.__name__ = "Integer32"
_EncoderCfgVancSdid_Object = MibTableColumn
encoderCfgVancSdid = _EncoderCfgVancSdid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 4, 1, 3),
    _EncoderCfgVancSdid_Type()
)
encoderCfgVancSdid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVancSdid.setStatus("current")


class _EncoderCfgVancType_Type(Integer32):
    """Custom type encoderCfgVancType based on Integer32"""
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
              23)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("smpte334p1Cea608", 2),
          ("smpte334p1Cea708", 3),
          ("reserved1", 4),
          ("smpteRp207", 5),
          ("smpte334p1DataBcst", 6),
          ("smpte2031Nabts", 7),
          ("smpte2031Tvg2x", 8),
          ("smpte2031Amol48", 9),
          ("smpte2031Amol96", 10),
          ("smpte2031EbuTxt", 11),
          ("smpte2031EbuTxtSub", 12),
          ("smpte2031InvTxt", 13),
          ("smpte2031Vps", 14),
          ("smpte2031Wss", 15),
          ("smpte2031Cea608", 16),
          ("smpte2031CpyProt", 17),
          ("smpte2031Vitc", 18),
          ("smpteRp2010scte104", 19),
          ("smpteRp2016p3afdBar", 20),
          ("smpteRp2016p4panScan", 21),
          ("smpte12p2timecode", 22),
          ("smpte353", 23))
    )


_EncoderCfgVancType_Type.__name__ = "Integer32"
_EncoderCfgVancType_Object = MibTableColumn
encoderCfgVancType = _EncoderCfgVancType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 4, 1, 4),
    _EncoderCfgVancType_Type()
)
encoderCfgVancType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVancType.setStatus("current")


class _EncoderCfgVancCarriage_Type(Integer32):
    """Custom type encoderCfgVancCarriage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inVideo", 1),
          ("inOwnPid", 2))
    )


_EncoderCfgVancCarriage_Type.__name__ = "Integer32"
_EncoderCfgVancCarriage_Object = MibTableColumn
encoderCfgVancCarriage = _EncoderCfgVancCarriage_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 4, 1, 5),
    _EncoderCfgVancCarriage_Type()
)
encoderCfgVancCarriage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVancCarriage.setStatus("current")
_EncoderCfgVancCompIndex_Type = Unsigned32
_EncoderCfgVancCompIndex_Object = MibTableColumn
encoderCfgVancCompIndex = _EncoderCfgVancCompIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 4, 1, 6),
    _EncoderCfgVancCompIndex_Type()
)
encoderCfgVancCompIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgVancCompIndex.setStatus("current")
_EncoderCfgAncilTable_Object = MibTable
encoderCfgAncilTable = _EncoderCfgAncilTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    encoderCfgAncilTable.setStatus("current")
_EncoderCfgAncilEntry_Object = MibTableRow
encoderCfgAncilEntry = _EncoderCfgAncilEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 5, 1)
)
encoderCfgAncilEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgAncilComponentIndex"),
)
if mibBuilder.loadTexts:
    encoderCfgAncilEntry.setStatus("current")
_EncoderCfgAncilComponentIndex_Type = Unsigned32
_EncoderCfgAncilComponentIndex_Object = MibTableColumn
encoderCfgAncilComponentIndex = _EncoderCfgAncilComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 5, 1, 1),
    _EncoderCfgAncilComponentIndex_Type()
)
encoderCfgAncilComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    encoderCfgAncilComponentIndex.setStatus("current")
_EncoderCfgAncilEnabled_Type = DeviceEnableDisableValues
_EncoderCfgAncilEnabled_Object = MibTableColumn
encoderCfgAncilEnabled = _EncoderCfgAncilEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 5, 1, 2),
    _EncoderCfgAncilEnabled_Type()
)
encoderCfgAncilEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgAncilEnabled.setStatus("current")


class _EncoderCfgAncilType_Type(Integer32):
    """Custom type encoderCfgAncilType based on Integer32"""
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
        *(("other", 1),
          ("scte35", 2),
          ("subtitles", 3),
          ("codeDownload", 4),
          ("dsmcc", 5),
          ("epg", 6),
          ("eia708", 7))
    )


_EncoderCfgAncilType_Type.__name__ = "Integer32"
_EncoderCfgAncilType_Object = MibTableColumn
encoderCfgAncilType = _EncoderCfgAncilType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 5, 1, 3),
    _EncoderCfgAncilType_Type()
)
encoderCfgAncilType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgAncilType.setStatus("current")


class _EncoderCfgAncilSourceType_Type(Integer32):
    """Custom type encoderCfgAncilSourceType based on Integer32"""
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
        *(("other", 1),
          ("physical", 2),
          ("ip", 3),
          ("vbi", 4),
          ("vanc", 5))
    )


_EncoderCfgAncilSourceType_Type.__name__ = "Integer32"
_EncoderCfgAncilSourceType_Object = MibTableColumn
encoderCfgAncilSourceType = _EncoderCfgAncilSourceType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 5, 1, 4),
    _EncoderCfgAncilSourceType_Type()
)
encoderCfgAncilSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgAncilSourceType.setStatus("current")
_EncoderCfgAncilPid_Type = HePIDValue
_EncoderCfgAncilPid_Object = MibTableColumn
encoderCfgAncilPid = _EncoderCfgAncilPid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 5, 1, 5),
    _EncoderCfgAncilPid_Type()
)
encoderCfgAncilPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgAncilPid.setStatus("current")
_EncoderCfgAncilPcrPid_Type = HePIDValue
_EncoderCfgAncilPcrPid_Object = MibTableColumn
encoderCfgAncilPcrPid = _EncoderCfgAncilPcrPid_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 5, 1, 6),
    _EncoderCfgAncilPcrPid_Type()
)
encoderCfgAncilPcrPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgAncilPcrPid.setStatus("current")
_EncoderCfgAncilRate_Type = Integer32
_EncoderCfgAncilRate_Object = MibTableColumn
encoderCfgAncilRate = _EncoderCfgAncilRate_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 5, 1, 7),
    _EncoderCfgAncilRate_Type()
)
encoderCfgAncilRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgAncilRate.setStatus("current")
if mibBuilder.loadTexts:
    encoderCfgAncilRate.setUnits("bps")
_EncoderCfgAncilLanguage_Type = DisplayString
_EncoderCfgAncilLanguage_Object = MibTableColumn
encoderCfgAncilLanguage = _EncoderCfgAncilLanguage_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 5, 1, 8),
    _EncoderCfgAncilLanguage_Type()
)
encoderCfgAncilLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgAncilLanguage.setStatus("current")
_EncoderCfgAncilServiceIndex_Type = Unsigned32
_EncoderCfgAncilServiceIndex_Object = MibTableColumn
encoderCfgAncilServiceIndex = _EncoderCfgAncilServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 5, 1, 9),
    _EncoderCfgAncilServiceIndex_Type()
)
encoderCfgAncilServiceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgAncilServiceIndex.setStatus("current")
_EncoderCfgServiceTable_Object = MibTable
encoderCfgServiceTable = _EncoderCfgServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 6)
)
if mibBuilder.loadTexts:
    encoderCfgServiceTable.setStatus("current")
_EncoderCfgServiceEntry_Object = MibTableRow
encoderCfgServiceEntry = _EncoderCfgServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 6, 1)
)
encoderCfgServiceEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgServiceInstIndex"),
)
if mibBuilder.loadTexts:
    encoderCfgServiceEntry.setStatus("current")
_EncoderCfgServiceInstIndex_Type = Unsigned32
_EncoderCfgServiceInstIndex_Object = MibTableColumn
encoderCfgServiceInstIndex = _EncoderCfgServiceInstIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 6, 1, 1),
    _EncoderCfgServiceInstIndex_Type()
)
encoderCfgServiceInstIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    encoderCfgServiceInstIndex.setStatus("current")


class _EncoderCfgServiceType_Type(Integer32):
    """Custom type encoderCfgServiceType based on Integer32"""
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
        *(("other", 1),
          ("noService", 2),
          ("primary", 3),
          ("audio", 4),
          ("data", 5),
          ("codeDownload", 6),
          ("pip", 7),
          ("epg", 8))
    )


_EncoderCfgServiceType_Type.__name__ = "Integer32"
_EncoderCfgServiceType_Object = MibTableColumn
encoderCfgServiceType = _EncoderCfgServiceType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 6, 1, 2),
    _EncoderCfgServiceType_Type()
)
encoderCfgServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgServiceType.setStatus("current")


class _EncoderCfgServiceId_Type(Integer32):
    """Custom type encoderCfgServiceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_EncoderCfgServiceId_Type.__name__ = "Integer32"
_EncoderCfgServiceId_Object = MibTableColumn
encoderCfgServiceId = _EncoderCfgServiceId_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 6, 1, 3),
    _EncoderCfgServiceId_Type()
)
encoderCfgServiceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgServiceId.setStatus("current")
_EncoderCfgServiceName_Type = DisplayString
_EncoderCfgServiceName_Object = MibTableColumn
encoderCfgServiceName = _EncoderCfgServiceName_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 6, 1, 6),
    _EncoderCfgServiceName_Type()
)
encoderCfgServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgServiceName.setStatus("current")
_EncoderCfgServiceTransportIndex_Type = Integer32
_EncoderCfgServiceTransportIndex_Object = MibTableColumn
encoderCfgServiceTransportIndex = _EncoderCfgServiceTransportIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 6, 1, 7),
    _EncoderCfgServiceTransportIndex_Type()
)
encoderCfgServiceTransportIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgServiceTransportIndex.setStatus("current")
_EncoderCfgTransportTable_Object = MibTable
encoderCfgTransportTable = _EncoderCfgTransportTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 7)
)
if mibBuilder.loadTexts:
    encoderCfgTransportTable.setStatus("current")
_EncoderCfgTransportEntry_Object = MibTableRow
encoderCfgTransportEntry = _EncoderCfgTransportEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 7, 1)
)
encoderCfgTransportEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgTransportChannelIndex"),
)
if mibBuilder.loadTexts:
    encoderCfgTransportEntry.setStatus("current")
_EncoderCfgTransportChannelIndex_Type = Unsigned32
_EncoderCfgTransportChannelIndex_Object = MibTableColumn
encoderCfgTransportChannelIndex = _EncoderCfgTransportChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 7, 1, 1),
    _EncoderCfgTransportChannelIndex_Type()
)
encoderCfgTransportChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    encoderCfgTransportChannelIndex.setStatus("current")
_EncoderCfgTransportIfIndex_Type = InterfaceIndex
_EncoderCfgTransportIfIndex_Object = MibTableColumn
encoderCfgTransportIfIndex = _EncoderCfgTransportIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 7, 1, 2),
    _EncoderCfgTransportIfIndex_Type()
)
encoderCfgTransportIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgTransportIfIndex.setStatus("current")
_EncoderCfgTransportEnabled_Type = DeviceEnableDisableValues
_EncoderCfgTransportEnabled_Object = MibTableColumn
encoderCfgTransportEnabled = _EncoderCfgTransportEnabled_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 7, 1, 3),
    _EncoderCfgTransportEnabled_Type()
)
encoderCfgTransportEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgTransportEnabled.setStatus("current")


class _EncoderCfgTransportType_Type(Integer32):
    """Custom type encoderCfgTransportType based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("asi", 2),
          ("dhei", 3),
          ("spmte310", 4),
          ("ds3", 5),
          ("ip", 6),
          ("idp", 7),
          ("ipRtp", 8),
          ("ipUdp", 9),
          ("modulated", 10))
    )


_EncoderCfgTransportType_Type.__name__ = "Integer32"
_EncoderCfgTransportType_Object = MibTableColumn
encoderCfgTransportType = _EncoderCfgTransportType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 7, 1, 4),
    _EncoderCfgTransportType_Type()
)
encoderCfgTransportType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgTransportType.setStatus("current")
_EncoderCfgTransportId_Type = Integer32
_EncoderCfgTransportId_Object = MibTableColumn
encoderCfgTransportId = _EncoderCfgTransportId_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 7, 1, 5),
    _EncoderCfgTransportId_Type()
)
encoderCfgTransportId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgTransportId.setStatus("current")


class _EncoderCfgTransportSiStd_Type(Integer32):
    """Custom type encoderCfgTransportSiStd based on Integer32"""
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
        *(("other", 1),
          ("mpeg2", 2),
          ("atsc", 3),
          ("dvb", 4),
          ("dcii", 5),
          ("atscDvb", 6),
          ("noTables", 7))
    )


_EncoderCfgTransportSiStd_Type.__name__ = "Integer32"
_EncoderCfgTransportSiStd_Object = MibTableColumn
encoderCfgTransportSiStd = _EncoderCfgTransportSiStd_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 7, 1, 6),
    _EncoderCfgTransportSiStd_Type()
)
encoderCfgTransportSiStd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgTransportSiStd.setStatus("current")
_EncoderCfgTransportRate_Type = Integer32
_EncoderCfgTransportRate_Object = MibTableColumn
encoderCfgTransportRate = _EncoderCfgTransportRate_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 7, 1, 7),
    _EncoderCfgTransportRate_Type()
)
encoderCfgTransportRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgTransportRate.setStatus("current")
if mibBuilder.loadTexts:
    encoderCfgTransportRate.setUnits("bps")


class _EncoderCfgTransportRateMode_Type(Integer32):
    """Custom type encoderCfgTransportRateMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cbr", 1),
          ("vbr", 2))
    )


_EncoderCfgTransportRateMode_Type.__name__ = "Integer32"
_EncoderCfgTransportRateMode_Object = MibTableColumn
encoderCfgTransportRateMode = _EncoderCfgTransportRateMode_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 7, 1, 8),
    _EncoderCfgTransportRateMode_Type()
)
encoderCfgTransportRateMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgTransportRateMode.setStatus("current")
_EncoderCfgTransportInetAddrType_Type = InetAddressType
_EncoderCfgTransportInetAddrType_Object = MibTableColumn
encoderCfgTransportInetAddrType = _EncoderCfgTransportInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 7, 1, 9),
    _EncoderCfgTransportInetAddrType_Type()
)
encoderCfgTransportInetAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgTransportInetAddrType.setStatus("current")
_EncoderCfgTransportDestIpAddr_Type = InetAddress
_EncoderCfgTransportDestIpAddr_Object = MibTableColumn
encoderCfgTransportDestIpAddr = _EncoderCfgTransportDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 7, 1, 10),
    _EncoderCfgTransportDestIpAddr_Type()
)
encoderCfgTransportDestIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgTransportDestIpAddr.setStatus("current")
_EncoderCfgTransportDestUdpPort_Type = InetPortNumber
_EncoderCfgTransportDestUdpPort_Object = MibTableColumn
encoderCfgTransportDestUdpPort = _EncoderCfgTransportDestUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 7, 1, 11),
    _EncoderCfgTransportDestUdpPort_Type()
)
encoderCfgTransportDestUdpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgTransportDestUdpPort.setStatus("current")
_EncoderCfgTransportGatewayAddr_Type = InetAddress
_EncoderCfgTransportGatewayAddr_Object = MibTableColumn
encoderCfgTransportGatewayAddr = _EncoderCfgTransportGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 7, 1, 12),
    _EncoderCfgTransportGatewayAddr_Type()
)
encoderCfgTransportGatewayAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgTransportGatewayAddr.setStatus("current")
_EncoderCfgTransportSubnetMask_Type = InetAddressPrefixLength
_EncoderCfgTransportSubnetMask_Object = MibTableColumn
encoderCfgTransportSubnetMask = _EncoderCfgTransportSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 7, 1, 13),
    _EncoderCfgTransportSubnetMask_Type()
)
encoderCfgTransportSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgTransportSubnetMask.setStatus("current")


class _EncoderCfgTransportIpFec_Type(Integer32):
    """Custom type encoderCfgTransportIpFec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_EncoderCfgTransportIpFec_Type.__name__ = "Integer32"
_EncoderCfgTransportIpFec_Object = MibTableColumn
encoderCfgTransportIpFec = _EncoderCfgTransportIpFec_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 7, 1, 14),
    _EncoderCfgTransportIpFec_Type()
)
encoderCfgTransportIpFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgTransportIpFec.setStatus("current")


class _EncoderCfgTransportIpInterleave_Type(Integer32):
    """Custom type encoderCfgTransportIpInterleave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_EncoderCfgTransportIpInterleave_Type.__name__ = "Integer32"
_EncoderCfgTransportIpInterleave_Object = MibTableColumn
encoderCfgTransportIpInterleave = _EncoderCfgTransportIpInterleave_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 7, 1, 15),
    _EncoderCfgTransportIpInterleave_Type()
)
encoderCfgTransportIpInterleave.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgTransportIpInterleave.setStatus("current")


class _EncoderCfgTransportIpAddrgMode_Type(Integer32):
    """Custom type encoderCfgTransportIpAddrgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("multicast", 2),
          ("broadcast", 3))
    )


_EncoderCfgTransportIpAddrgMode_Type.__name__ = "Integer32"
_EncoderCfgTransportIpAddrgMode_Object = MibTableColumn
encoderCfgTransportIpAddrgMode = _EncoderCfgTransportIpAddrgMode_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 1, 7, 1, 16),
    _EncoderCfgTransportIpAddrgMode_Type()
)
encoderCfgTransportIpAddrgMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderCfgTransportIpAddrgMode.setStatus("current")
_InputMonitor_ObjectIdentity = ObjectIdentity
inputMonitor = _InputMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2)
)
_EncoderInputMonVideoTable_Object = MibTable
encoderInputMonVideoTable = _EncoderInputMonVideoTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    encoderInputMonVideoTable.setStatus("current")
_EncoderInputMonVideoEntry_Object = MibTableRow
encoderInputMonVideoEntry = _EncoderInputMonVideoEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 1, 1)
)
encoderInputMonVideoEntry.setIndexNames(
    (0, "SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonVideoIfIndex"),
)
if mibBuilder.loadTexts:
    encoderInputMonVideoEntry.setStatus("current")
_EncoderInputMonVideoIfIndex_Type = InterfaceIndex
_EncoderInputMonVideoIfIndex_Object = MibTableColumn
encoderInputMonVideoIfIndex = _EncoderInputMonVideoIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 1, 1, 1),
    _EncoderInputMonVideoIfIndex_Type()
)
encoderInputMonVideoIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    encoderInputMonVideoIfIndex.setStatus("current")
_EncoderInputMonVideoChannelIndex_Type = Unsigned32
_EncoderInputMonVideoChannelIndex_Object = MibTableColumn
encoderInputMonVideoChannelIndex = _EncoderInputMonVideoChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 1, 1, 2),
    _EncoderInputMonVideoChannelIndex_Type()
)
encoderInputMonVideoChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonVideoChannelIndex.setStatus("current")
_EncoderInputMonVideoPhysIndex_Type = PhysicalIndex
_EncoderInputMonVideoPhysIndex_Object = MibTableColumn
encoderInputMonVideoPhysIndex = _EncoderInputMonVideoPhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 1, 1, 3),
    _EncoderInputMonVideoPhysIndex_Type()
)
encoderInputMonVideoPhysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonVideoPhysIndex.setStatus("current")


class _EncoderInputMonVideoType_Type(Integer32):
    """Custom type encoderInputMonVideoType based on Integer32"""
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
        *(("other", 1),
          ("analogComposite", 2),
          ("analogComponent", 3),
          ("sdi", 4),
          ("hdSdi", 5),
          ("ip", 6))
    )


_EncoderInputMonVideoType_Type.__name__ = "Integer32"
_EncoderInputMonVideoType_Object = MibTableColumn
encoderInputMonVideoType = _EncoderInputMonVideoType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 1, 1, 4),
    _EncoderInputMonVideoType_Type()
)
encoderInputMonVideoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonVideoType.setStatus("current")


class _EncoderInputMonVideoSyncLock_Type(Integer32):
    """Custom type encoderInputMonVideoSyncLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("notLocked", 2),
          ("intermittent", 3))
    )


_EncoderInputMonVideoSyncLock_Type.__name__ = "Integer32"
_EncoderInputMonVideoSyncLock_Object = MibTableColumn
encoderInputMonVideoSyncLock = _EncoderInputMonVideoSyncLock_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 1, 1, 5),
    _EncoderInputMonVideoSyncLock_Type()
)
encoderInputMonVideoSyncLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonVideoSyncLock.setStatus("current")
_EncoderMonVideoInputFrameRate_Type = VideoInputFrameRateType
_EncoderMonVideoInputFrameRate_Object = MibTableColumn
encoderMonVideoInputFrameRate = _EncoderMonVideoInputFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 1, 1, 6),
    _EncoderMonVideoInputFrameRate_Type()
)
encoderMonVideoInputFrameRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderMonVideoInputFrameRate.setStatus("current")


class _EncoderInputMonVideoFrameLock_Type(Integer32):
    """Custom type encoderInputMonVideoFrameLock based on Integer32"""
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
        *(("notSupported", 1),
          ("locked", 2),
          ("notLocked", 3),
          ("intermittent", 4))
    )


_EncoderInputMonVideoFrameLock_Type.__name__ = "Integer32"
_EncoderInputMonVideoFrameLock_Object = MibTableColumn
encoderInputMonVideoFrameLock = _EncoderInputMonVideoFrameLock_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 1, 1, 7),
    _EncoderInputMonVideoFrameLock_Type()
)
encoderInputMonVideoFrameLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonVideoFrameLock.setStatus("current")
_EncoderInputMonVideoChromaStable_Type = MpegErrorStatus
_EncoderInputMonVideoChromaStable_Object = MibTableColumn
encoderInputMonVideoChromaStable = _EncoderInputMonVideoChromaStable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 1, 1, 8),
    _EncoderInputMonVideoChromaStable_Type()
)
encoderInputMonVideoChromaStable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonVideoChromaStable.setStatus("current")


class _EncoderInputMonVideoBlack_Type(Integer32):
    """Custom type encoderInputMonVideoBlack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("good", 2),
          ("black", 3))
    )


_EncoderInputMonVideoBlack_Type.__name__ = "Integer32"
_EncoderInputMonVideoBlack_Object = MibTableColumn
encoderInputMonVideoBlack = _EncoderInputMonVideoBlack_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 1, 1, 9),
    _EncoderInputMonVideoBlack_Type()
)
encoderInputMonVideoBlack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonVideoBlack.setStatus("current")


class _EncoderInputMonVideoLines_Type(Integer32):
    """Custom type encoderInputMonVideoLines based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSupported", 1),
          ("good", 2),
          ("mismatch", 3))
    )


_EncoderInputMonVideoLines_Type.__name__ = "Integer32"
_EncoderInputMonVideoLines_Object = MibTableColumn
encoderInputMonVideoLines = _EncoderInputMonVideoLines_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 1, 1, 10),
    _EncoderInputMonVideoLines_Type()
)
encoderInputMonVideoLines.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonVideoLines.setStatus("current")


class _EncoderInputMonVideoSdiCk_Type(Integer32):
    """Custom type encoderInputMonVideoSdiCk based on Integer32"""
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
        *(("locked", 1),
          ("notLocked", 2),
          ("intermittent", 3),
          ("notSdi", 4))
    )


_EncoderInputMonVideoSdiCk_Type.__name__ = "Integer32"
_EncoderInputMonVideoSdiCk_Object = MibTableColumn
encoderInputMonVideoSdiCk = _EncoderInputMonVideoSdiCk_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 1, 1, 11),
    _EncoderInputMonVideoSdiCk_Type()
)
encoderInputMonVideoSdiCk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonVideoSdiCk.setStatus("current")
_EncoderInputMonAudioTable_Object = MibTable
encoderInputMonAudioTable = _EncoderInputMonAudioTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 2)
)
if mibBuilder.loadTexts:
    encoderInputMonAudioTable.setStatus("current")
_EncoderInputMonAudioEntry_Object = MibTableRow
encoderInputMonAudioEntry = _EncoderInputMonAudioEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 2, 1)
)
encoderInputMonAudioEntry.setIndexNames(
    (0, "SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonAudioIfIndex"),
    (0, "SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonAudioInputChanIndex"),
)
if mibBuilder.loadTexts:
    encoderInputMonAudioEntry.setStatus("current")
_EncoderInputMonAudioIfIndex_Type = InterfaceIndex
_EncoderInputMonAudioIfIndex_Object = MibTableColumn
encoderInputMonAudioIfIndex = _EncoderInputMonAudioIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 2, 1, 1),
    _EncoderInputMonAudioIfIndex_Type()
)
encoderInputMonAudioIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    encoderInputMonAudioIfIndex.setStatus("current")
_EncoderInputMonAudioInputChanIndex_Type = Unsigned32
_EncoderInputMonAudioInputChanIndex_Object = MibTableColumn
encoderInputMonAudioInputChanIndex = _EncoderInputMonAudioInputChanIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 2, 1, 2),
    _EncoderInputMonAudioInputChanIndex_Type()
)
encoderInputMonAudioInputChanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    encoderInputMonAudioInputChanIndex.setStatus("current")
_EncoderInputMonAudioPhysIndex_Type = PhysicalIndex
_EncoderInputMonAudioPhysIndex_Object = MibTableColumn
encoderInputMonAudioPhysIndex = _EncoderInputMonAudioPhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 2, 1, 3),
    _EncoderInputMonAudioPhysIndex_Type()
)
encoderInputMonAudioPhysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonAudioPhysIndex.setStatus("current")
_EncoderInputMonAudioCfgChannel_Type = Unsigned32
_EncoderInputMonAudioCfgChannel_Object = MibTableColumn
encoderInputMonAudioCfgChannel = _EncoderInputMonAudioCfgChannel_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 2, 1, 4),
    _EncoderInputMonAudioCfgChannel_Type()
)
encoderInputMonAudioCfgChannel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    encoderInputMonAudioCfgChannel.setStatus("current")


class _EncoderInputMonAudioType_Type(Integer32):
    """Custom type encoderInputMonAudioType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("analog", 1),
          ("aes", 2),
          ("embedded", 3))
    )


_EncoderInputMonAudioType_Type.__name__ = "Integer32"
_EncoderInputMonAudioType_Object = MibTableColumn
encoderInputMonAudioType = _EncoderInputMonAudioType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 2, 1, 5),
    _EncoderInputMonAudioType_Type()
)
encoderInputMonAudioType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonAudioType.setStatus("current")
_EncoderInputMonAudioLevel_Type = Integer32
_EncoderInputMonAudioLevel_Object = MibTableColumn
encoderInputMonAudioLevel = _EncoderInputMonAudioLevel_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 2, 1, 6),
    _EncoderInputMonAudioLevel_Type()
)
encoderInputMonAudioLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonAudioLevel.setStatus("current")
if mibBuilder.loadTexts:
    encoderInputMonAudioLevel.setUnits("dB")
_EncoderInputMonAudioReference_Type = Integer32
_EncoderInputMonAudioReference_Object = MibTableColumn
encoderInputMonAudioReference = _EncoderInputMonAudioReference_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 2, 1, 7),
    _EncoderInputMonAudioReference_Type()
)
encoderInputMonAudioReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    encoderInputMonAudioReference.setStatus("current")
if mibBuilder.loadTexts:
    encoderInputMonAudioReference.setUnits("dB")


class _EncoderInputMonAudioSilence_Type(Integer32):
    """Custom type encoderInputMonAudioSilence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("audioPresent", 1),
          ("silent", 2),
          ("notSupported", 3))
    )


_EncoderInputMonAudioSilence_Type.__name__ = "Integer32"
_EncoderInputMonAudioSilence_Object = MibTableColumn
encoderInputMonAudioSilence = _EncoderInputMonAudioSilence_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 2, 1, 8),
    _EncoderInputMonAudioSilence_Type()
)
encoderInputMonAudioSilence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonAudioSilence.setStatus("current")


class _EncoderInputMonAudioAesCk_Type(Integer32):
    """Custom type encoderInputMonAudioAesCk based on Integer32"""
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
        *(("locked", 1),
          ("notLocked", 2),
          ("intermittent", 3),
          ("notAes", 4))
    )


_EncoderInputMonAudioAesCk_Type.__name__ = "Integer32"
_EncoderInputMonAudioAesCk_Object = MibTableColumn
encoderInputMonAudioAesCk = _EncoderInputMonAudioAesCk_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 2, 1, 9),
    _EncoderInputMonAudioAesCk_Type()
)
encoderInputMonAudioAesCk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonAudioAesCk.setStatus("current")


class _EncoderInputMonAudioFraming_Type(Integer32):
    """Custom type encoderInputMonAudioFraming based on Integer32"""
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
        *(("locked", 1),
          ("notLocked", 2),
          ("intermittent", 3),
          ("notAes", 4))
    )


_EncoderInputMonAudioFraming_Type.__name__ = "Integer32"
_EncoderInputMonAudioFraming_Object = MibTableColumn
encoderInputMonAudioFraming = _EncoderInputMonAudioFraming_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 2, 1, 10),
    _EncoderInputMonAudioFraming_Type()
)
encoderInputMonAudioFraming.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonAudioFraming.setStatus("current")


class _EncoderInputMonAudioAesType_Type(Integer32):
    """Custom type encoderInputMonAudioAesType based on Integer32"""
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
        *(("other", 1),
          ("notRecognized", 2),
          ("smpte337", 3),
          ("pcm", 4))
    )


_EncoderInputMonAudioAesType_Type.__name__ = "Integer32"
_EncoderInputMonAudioAesType_Object = MibTableColumn
encoderInputMonAudioAesType = _EncoderInputMonAudioAesType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 2, 1, 11),
    _EncoderInputMonAudioAesType_Type()
)
encoderInputMonAudioAesType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonAudioAesType.setStatus("current")
_EncoderInputMonVbiTable_Object = MibTable
encoderInputMonVbiTable = _EncoderInputMonVbiTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    encoderInputMonVbiTable.setStatus("current")
_EncoderInputMonVbiEntry_Object = MibTableRow
encoderInputMonVbiEntry = _EncoderInputMonVbiEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 3, 1)
)
encoderInputMonVbiEntry.setIndexNames(
    (0, "SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonVbiIfIndex"),
    (0, "SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonVbiLineIndex"),
    (0, "SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonVbiFieldIndex"),
)
if mibBuilder.loadTexts:
    encoderInputMonVbiEntry.setStatus("current")
_EncoderInputMonVbiIfIndex_Type = InterfaceIndex
_EncoderInputMonVbiIfIndex_Object = MibTableColumn
encoderInputMonVbiIfIndex = _EncoderInputMonVbiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 3, 1, 1),
    _EncoderInputMonVbiIfIndex_Type()
)
encoderInputMonVbiIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    encoderInputMonVbiIfIndex.setStatus("current")
_EncoderInputMonVbiPhysIndex_Type = PhysicalIndex
_EncoderInputMonVbiPhysIndex_Object = MibTableColumn
encoderInputMonVbiPhysIndex = _EncoderInputMonVbiPhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 3, 1, 2),
    _EncoderInputMonVbiPhysIndex_Type()
)
encoderInputMonVbiPhysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonVbiPhysIndex.setStatus("current")


class _EncoderInputMonVbiLineIndex_Type(Unsigned32):
    """Custom type encoderInputMonVbiLineIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 23),
    )


_EncoderInputMonVbiLineIndex_Type.__name__ = "Unsigned32"
_EncoderInputMonVbiLineIndex_Object = MibTableColumn
encoderInputMonVbiLineIndex = _EncoderInputMonVbiLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 3, 1, 3),
    _EncoderInputMonVbiLineIndex_Type()
)
encoderInputMonVbiLineIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    encoderInputMonVbiLineIndex.setStatus("current")


class _EncoderInputMonVbiFieldIndex_Type(Unsigned32):
    """Custom type encoderInputMonVbiFieldIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_EncoderInputMonVbiFieldIndex_Type.__name__ = "Unsigned32"
_EncoderInputMonVbiFieldIndex_Object = MibTableColumn
encoderInputMonVbiFieldIndex = _EncoderInputMonVbiFieldIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 3, 1, 4),
    _EncoderInputMonVbiFieldIndex_Type()
)
encoderInputMonVbiFieldIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    encoderInputMonVbiFieldIndex.setStatus("current")


class _EncoderInputMonVbiType_Type(Integer32):
    """Custom type encoderInputMonVbiType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("correct", 1),
          ("mismatch", 2),
          ("notDiscriminated", 3))
    )


_EncoderInputMonVbiType_Type.__name__ = "Integer32"
_EncoderInputMonVbiType_Object = MibTableColumn
encoderInputMonVbiType = _EncoderInputMonVbiType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 3, 1, 5),
    _EncoderInputMonVbiType_Type()
)
encoderInputMonVbiType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonVbiType.setStatus("current")


class _EncoderInputMonVbiErrors_Type(Integer32):
    """Custom type encoderInputMonVbiErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("errors", 2),
          ("notChecked", 3))
    )


_EncoderInputMonVbiErrors_Type.__name__ = "Integer32"
_EncoderInputMonVbiErrors_Object = MibTableColumn
encoderInputMonVbiErrors = _EncoderInputMonVbiErrors_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 3, 1, 6),
    _EncoderInputMonVbiErrors_Type()
)
encoderInputMonVbiErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonVbiErrors.setStatus("current")
_EncoderInputMonVbiRate_Type = Integer32
_EncoderInputMonVbiRate_Object = MibTableColumn
encoderInputMonVbiRate = _EncoderInputMonVbiRate_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 3, 1, 7),
    _EncoderInputMonVbiRate_Type()
)
encoderInputMonVbiRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonVbiRate.setStatus("current")
_EncoderInputMonVbiTimeLastData_Type = TimeTicks
_EncoderInputMonVbiTimeLastData_Object = MibTableColumn
encoderInputMonVbiTimeLastData = _EncoderInputMonVbiTimeLastData_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 3, 1, 8),
    _EncoderInputMonVbiTimeLastData_Type()
)
encoderInputMonVbiTimeLastData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonVbiTimeLastData.setStatus("current")
_EncoderInputMonVancTable_Object = MibTable
encoderInputMonVancTable = _EncoderInputMonVancTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 4)
)
if mibBuilder.loadTexts:
    encoderInputMonVancTable.setStatus("current")
_EncoderInputMonVancEntry_Object = MibTableRow
encoderInputMonVancEntry = _EncoderInputMonVancEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 4, 1)
)
encoderInputMonVancEntry.setIndexNames(
    (0, "SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonVancIfIndex"),
    (0, "SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonVancServiceIndex"),
)
if mibBuilder.loadTexts:
    encoderInputMonVancEntry.setStatus("current")
_EncoderInputMonVancIfIndex_Type = InterfaceIndex
_EncoderInputMonVancIfIndex_Object = MibTableColumn
encoderInputMonVancIfIndex = _EncoderInputMonVancIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 4, 1, 1),
    _EncoderInputMonVancIfIndex_Type()
)
encoderInputMonVancIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    encoderInputMonVancIfIndex.setStatus("current")
_EncoderInputMonVancPhysIndex_Type = PhysicalIndex
_EncoderInputMonVancPhysIndex_Object = MibTableColumn
encoderInputMonVancPhysIndex = _EncoderInputMonVancPhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 4, 1, 2),
    _EncoderInputMonVancPhysIndex_Type()
)
encoderInputMonVancPhysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonVancPhysIndex.setStatus("current")


class _EncoderInputMonVancServiceIndex_Type(Unsigned32):
    """Custom type encoderInputMonVancServiceIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 23),
    )


_EncoderInputMonVancServiceIndex_Type.__name__ = "Unsigned32"
_EncoderInputMonVancServiceIndex_Object = MibTableColumn
encoderInputMonVancServiceIndex = _EncoderInputMonVancServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 4, 1, 3),
    _EncoderInputMonVancServiceIndex_Type()
)
encoderInputMonVancServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    encoderInputMonVancServiceIndex.setStatus("current")


class _EncoderInputMonVancType_Type(Integer32):
    """Custom type encoderInputMonVancType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("correct", 1),
          ("mismatch", 2),
          ("notDiscriminated", 3))
    )


_EncoderInputMonVancType_Type.__name__ = "Integer32"
_EncoderInputMonVancType_Object = MibTableColumn
encoderInputMonVancType = _EncoderInputMonVancType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 4, 1, 4),
    _EncoderInputMonVancType_Type()
)
encoderInputMonVancType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonVancType.setStatus("current")


class _EncoderInputMonVancErrors_Type(Integer32):
    """Custom type encoderInputMonVancErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("good", 1),
          ("errors", 2),
          ("notChecked", 3))
    )


_EncoderInputMonVancErrors_Type.__name__ = "Integer32"
_EncoderInputMonVancErrors_Object = MibTableColumn
encoderInputMonVancErrors = _EncoderInputMonVancErrors_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 4, 1, 5),
    _EncoderInputMonVancErrors_Type()
)
encoderInputMonVancErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonVancErrors.setStatus("current")
_EncoderInputMonVancRate_Type = Integer32
_EncoderInputMonVancRate_Object = MibTableColumn
encoderInputMonVancRate = _EncoderInputMonVancRate_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 4, 1, 6),
    _EncoderInputMonVancRate_Type()
)
encoderInputMonVancRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonVancRate.setStatus("current")
_EncoderInputMonVancTimeLastData_Type = TimeTicks
_EncoderInputMonVancTimeLastData_Object = MibTableColumn
encoderInputMonVancTimeLastData = _EncoderInputMonVancTimeLastData_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 4, 1, 7),
    _EncoderInputMonVancTimeLastData_Type()
)
encoderInputMonVancTimeLastData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonVancTimeLastData.setStatus("current")
_EncoderInputMonAncilTable_Object = MibTable
encoderInputMonAncilTable = _EncoderInputMonAncilTable_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 5)
)
if mibBuilder.loadTexts:
    encoderInputMonAncilTable.setStatus("current")
_EncoderInputMonAncilEntry_Object = MibTableRow
encoderInputMonAncilEntry = _EncoderInputMonAncilEntry_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 5, 1)
)
encoderInputMonAncilEntry.setIndexNames(
    (0, "SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonAncilIfIndex"),
    (0, "SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonAncilChannelIndex"),
)
if mibBuilder.loadTexts:
    encoderInputMonAncilEntry.setStatus("current")
_EncoderInputMonAncilIfIndex_Type = InterfaceIndex
_EncoderInputMonAncilIfIndex_Object = MibTableColumn
encoderInputMonAncilIfIndex = _EncoderInputMonAncilIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 5, 1, 1),
    _EncoderInputMonAncilIfIndex_Type()
)
encoderInputMonAncilIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    encoderInputMonAncilIfIndex.setStatus("current")
_EncoderInputMonAncilChannelIndex_Type = Unsigned32
_EncoderInputMonAncilChannelIndex_Object = MibTableColumn
encoderInputMonAncilChannelIndex = _EncoderInputMonAncilChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 5, 1, 2),
    _EncoderInputMonAncilChannelIndex_Type()
)
encoderInputMonAncilChannelIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    encoderInputMonAncilChannelIndex.setStatus("current")
_EncoderInputMonAncilPhysIndex_Type = PhysicalIndex
_EncoderInputMonAncilPhysIndex_Object = MibTableColumn
encoderInputMonAncilPhysIndex = _EncoderInputMonAncilPhysIndex_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 5, 1, 3),
    _EncoderInputMonAncilPhysIndex_Type()
)
encoderInputMonAncilPhysIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonAncilPhysIndex.setStatus("current")
_EncoderInputMonAncilCfgChannel_Type = Unsigned32
_EncoderInputMonAncilCfgChannel_Object = MibTableColumn
encoderInputMonAncilCfgChannel = _EncoderInputMonAncilCfgChannel_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 5, 1, 4),
    _EncoderInputMonAncilCfgChannel_Type()
)
encoderInputMonAncilCfgChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonAncilCfgChannel.setStatus("current")


class _EncoderInputMonAncilType_Type(Integer32):
    """Custom type encoderInputMonAncilType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("dsmcc", 2),
          ("scte104Ip", 3),
          ("scte104Vanc", 4),
          ("subtitles", 5),
          ("codeDownload", 6),
          ("smpte333", 7),
          ("vbiData", 8),
          ("vancData", 9))
    )


_EncoderInputMonAncilType_Type.__name__ = "Integer32"
_EncoderInputMonAncilType_Object = MibTableColumn
encoderInputMonAncilType = _EncoderInputMonAncilType_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 5, 1, 5),
    _EncoderInputMonAncilType_Type()
)
encoderInputMonAncilType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonAncilType.setStatus("current")
_EncoderInputMonAncilTimeLastPkt_Type = TimeTicks
_EncoderInputMonAncilTimeLastPkt_Object = MibTableColumn
encoderInputMonAncilTimeLastPkt = _EncoderInputMonAncilTimeLastPkt_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 5, 1, 6),
    _EncoderInputMonAncilTimeLastPkt_Type()
)
encoderInputMonAncilTimeLastPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonAncilTimeLastPkt.setStatus("current")
_EncoderInputMonAncilRate_Type = Integer32
_EncoderInputMonAncilRate_Object = MibTableColumn
encoderInputMonAncilRate = _EncoderInputMonAncilRate_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 5, 1, 7),
    _EncoderInputMonAncilRate_Type()
)
encoderInputMonAncilRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonAncilRate.setStatus("current")


class _EncoderInputMonAncilLock_Type(Integer32):
    """Custom type encoderInputMonAncilLock based on Integer32"""
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
        *(("good", 1),
          ("notLocked", 2),
          ("intermittent", 3),
          ("readyToAcquire", 4))
    )


_EncoderInputMonAncilLock_Type.__name__ = "Integer32"
_EncoderInputMonAncilLock_Object = MibTableColumn
encoderInputMonAncilLock = _EncoderInputMonAncilLock_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 5, 1, 8),
    _EncoderInputMonAncilLock_Type()
)
encoderInputMonAncilLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonAncilLock.setStatus("current")
_EncoderInputMonAncilError_Type = MpegErrorStatus
_EncoderInputMonAncilError_Object = MibTableColumn
encoderInputMonAncilError = _EncoderInputMonAncilError_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 5, 1, 9),
    _EncoderInputMonAncilError_Type()
)
encoderInputMonAncilError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonAncilError.setStatus("current")
_EncoderInputMonAncilHbMissed_Type = Counter32
_EncoderInputMonAncilHbMissed_Object = MibTableColumn
encoderInputMonAncilHbMissed = _EncoderInputMonAncilHbMissed_Object(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 2, 5, 1, 10),
    _EncoderInputMonAncilHbMissed_Type()
)
encoderInputMonAncilHbMissed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    encoderInputMonAncilHbMissed.setStatus("current")
_OutputMonitor_ObjectIdentity = ObjectIdentity
outputMonitor = _OutputMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 1, 3)
)
_MpegEncoderMIBConformance_ObjectIdentity = ObjectIdentity
mpegEncoderMIBConformance = _MpegEncoderMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 2)
)
_MpegEncoderMIBCompliances_ObjectIdentity = ObjectIdentity
mpegEncoderMIBCompliances = _MpegEncoderMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 2, 1)
)
_MpegEncoderMIBGroups_ObjectIdentity = ObjectIdentity
mpegEncoderMIBGroups = _MpegEncoderMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 2, 2)
)

# Managed Objects groups

encoderCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 2, 2, 1)
)
encoderCfgGroup.setObjects(
      *(("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgAncilEnabled"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgAncilServiceIndex"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgAncilLanguage"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgAncilPcrPid"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgAncilPid"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgAncilRate"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgAncilSourceType"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgAncilType"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgAudioDialogNorm"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgAudioEnabled"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgAudioInputType"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgAudioLanguageA"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgAudioLanguageB"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgAudioLipSync"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgAudioMode"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgAudioPcrPid"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgAudioPid"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgAudioRate"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgAudioPassThru"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgAudioInputLabel"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgAudioStandard"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgAudioServiceIndex"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgServiceId"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgServiceName"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgServiceTransportIndex"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgServiceType"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgTransportIpFec"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgTransportIpInterleave"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgTransportIpAddrgMode"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgTransportDestIpAddr"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgTransportDestUdpPort"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgTransportEnabled"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgTransportGatewayAddr"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgTransportId"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgTransportInetAddrType"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgTransportRate"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgTransportRateMode"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgTransportSiStd"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgTransportSubnetMask"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgTransportType"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgTransportIfIndex"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVancDid"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVancSdid"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVancType"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVancCarriage"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVancCompIndex"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVbiField"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVbiLine"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVbiType"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVbiCarriage"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVbiCompIndex"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVideoInputIf"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVideoInputFrameRate"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVideoInputScan"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVideoInputFormat"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVideoAspectRatio"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVideoBitrateAvg"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVideoBitrateMax"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVideoBitrateMin"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVideoBorderProcessing"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVideoCodingDelay"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVideoDeblockAlpha"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVideoDeblockBeta"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVideoDeblockEnable"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVideoFilmMode"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVideoIdrRate"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVideoPcrPid"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVideoPesAlignment"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVideoPid"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVideoHorzResolution"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVideoVertResolution"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVideoServiceIndex"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVideoType"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVideoCompression"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgVideoRateMode"))
)
if mibBuilder.loadTexts:
    encoderCfgGroup.setStatus("current")

encoderInputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 2, 2, 2)
)
encoderInputGroup.setObjects(
      *(("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonAncilError"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonAncilHbMissed"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonAncilLock"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonAncilRate"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonAncilCfgChannel"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonAncilTimeLastPkt"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonAncilType"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonVbiType"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonVbiErrors"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonVbiRate"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonVbiTimeLastData"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonVancType"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonVancErrors"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonVancRate"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonVancTimeLastData"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonAudioAesCk"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonAudioAesType"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonAudioFraming"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonAudioReference"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonAudioLevel"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonAudioSilence"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonAudioType"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonVideoBlack"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonVideoChromaStable"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonVideoLines"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderMonVideoInputFrameRate"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonVideoFrameLock"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonVideoSdiCk"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonVideoSyncLock"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonVideoType"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonVideoChannelIndex"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonVideoPhysIndex"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonAudioPhysIndex"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonVbiPhysIndex"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonVancPhysIndex"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputMonAncilPhysIndex"))
)
if mibBuilder.loadTexts:
    encoderInputGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mpegEncoderCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5591, 1, 11, 5, 4, 2, 2, 1, 1)
)
mpegEncoderCompliance.setObjects(
      *(("SCTE-HMS-MPEG-ENCODER-MIB", "encoderCfgGroup"),
        ("SCTE-HMS-MPEG-ENCODER-MIB", "encoderInputGroup"))
)
if mibBuilder.loadTexts:
    mpegEncoderCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SCTE-HMS-MPEG-ENCODER-MIB",
    **{"mpegEncoderMIB": mpegEncoderMIB,
       "mpegEncoderMIBObjects": mpegEncoderMIBObjects,
       "configurationReport": configurationReport,
       "encoderCfgVideoTable": encoderCfgVideoTable,
       "encoderCfgVideoEntry": encoderCfgVideoEntry,
       "encoderCfgVideoIndex": encoderCfgVideoIndex,
       "encoderCfgVideoType": encoderCfgVideoType,
       "encoderCfgVideoCompression": encoderCfgVideoCompression,
       "encoderCfgVideoPid": encoderCfgVideoPid,
       "encoderCfgVideoPcrPid": encoderCfgVideoPcrPid,
       "encoderCfgVideoServiceIndex": encoderCfgVideoServiceIndex,
       "encoderCfgVideoVertResolution": encoderCfgVideoVertResolution,
       "encoderCfgVideoHorzResolution": encoderCfgVideoHorzResolution,
       "encoderCfgVideoBitrateAvg": encoderCfgVideoBitrateAvg,
       "encoderCfgVideoBitrateMax": encoderCfgVideoBitrateMax,
       "encoderCfgVideoBitrateMin": encoderCfgVideoBitrateMin,
       "encoderCfgVideoFilmMode": encoderCfgVideoFilmMode,
       "encoderCfgVideoRateMode": encoderCfgVideoRateMode,
       "encoderCfgVideoBorderProcessing": encoderCfgVideoBorderProcessing,
       "encoderCfgVideoPesAlignment": encoderCfgVideoPesAlignment,
       "encoderCfgVideoCodingDelay": encoderCfgVideoCodingDelay,
       "encoderCfgVideoDeblockEnable": encoderCfgVideoDeblockEnable,
       "encoderCfgVideoDeblockAlpha": encoderCfgVideoDeblockAlpha,
       "encoderCfgVideoDeblockBeta": encoderCfgVideoDeblockBeta,
       "encoderCfgVideoIdrRate": encoderCfgVideoIdrRate,
       "encoderCfgVideoInputIf": encoderCfgVideoInputIf,
       "encoderCfgVideoInputFrameRate": encoderCfgVideoInputFrameRate,
       "encoderCfgVideoInputScan": encoderCfgVideoInputScan,
       "encoderCfgVideoInputFormat": encoderCfgVideoInputFormat,
       "encoderCfgVideoAspectRatio": encoderCfgVideoAspectRatio,
       "encoderCfgAudioTable": encoderCfgAudioTable,
       "encoderCfgAudioEntry": encoderCfgAudioEntry,
       "encoderCfgAudioChannelIndex": encoderCfgAudioChannelIndex,
       "encoderCfgAudioEnabled": encoderCfgAudioEnabled,
       "encoderCfgAudioStandard": encoderCfgAudioStandard,
       "encoderCfgAudioPid": encoderCfgAudioPid,
       "encoderCfgAudioPcrPid": encoderCfgAudioPcrPid,
       "encoderCfgAudioServiceIndex": encoderCfgAudioServiceIndex,
       "encoderCfgAudioMode": encoderCfgAudioMode,
       "encoderCfgAudioPassThru": encoderCfgAudioPassThru,
       "encoderCfgAudioRate": encoderCfgAudioRate,
       "encoderCfgAudioLanguageA": encoderCfgAudioLanguageA,
       "encoderCfgAudioLanguageB": encoderCfgAudioLanguageB,
       "encoderCfgAudioLipSync": encoderCfgAudioLipSync,
       "encoderCfgAudioDialogNorm": encoderCfgAudioDialogNorm,
       "encoderCfgAudioInputType": encoderCfgAudioInputType,
       "encoderCfgAudioInputLabel": encoderCfgAudioInputLabel,
       "encoderCfgVbiTable": encoderCfgVbiTable,
       "encoderCfgVbiEntry": encoderCfgVbiEntry,
       "encoderCfgVbiIndex": encoderCfgVbiIndex,
       "encoderCfgVbiField": encoderCfgVbiField,
       "encoderCfgVbiLine": encoderCfgVbiLine,
       "encoderCfgVbiType": encoderCfgVbiType,
       "encoderCfgVbiCarriage": encoderCfgVbiCarriage,
       "encoderCfgVbiCompIndex": encoderCfgVbiCompIndex,
       "encoderCfgVancTable": encoderCfgVancTable,
       "encoderCfgVancEntry": encoderCfgVancEntry,
       "encoderCfgVancServiceIndex": encoderCfgVancServiceIndex,
       "encoderCfgVancDid": encoderCfgVancDid,
       "encoderCfgVancSdid": encoderCfgVancSdid,
       "encoderCfgVancType": encoderCfgVancType,
       "encoderCfgVancCarriage": encoderCfgVancCarriage,
       "encoderCfgVancCompIndex": encoderCfgVancCompIndex,
       "encoderCfgAncilTable": encoderCfgAncilTable,
       "encoderCfgAncilEntry": encoderCfgAncilEntry,
       "encoderCfgAncilComponentIndex": encoderCfgAncilComponentIndex,
       "encoderCfgAncilEnabled": encoderCfgAncilEnabled,
       "encoderCfgAncilType": encoderCfgAncilType,
       "encoderCfgAncilSourceType": encoderCfgAncilSourceType,
       "encoderCfgAncilPid": encoderCfgAncilPid,
       "encoderCfgAncilPcrPid": encoderCfgAncilPcrPid,
       "encoderCfgAncilRate": encoderCfgAncilRate,
       "encoderCfgAncilLanguage": encoderCfgAncilLanguage,
       "encoderCfgAncilServiceIndex": encoderCfgAncilServiceIndex,
       "encoderCfgServiceTable": encoderCfgServiceTable,
       "encoderCfgServiceEntry": encoderCfgServiceEntry,
       "encoderCfgServiceInstIndex": encoderCfgServiceInstIndex,
       "encoderCfgServiceType": encoderCfgServiceType,
       "encoderCfgServiceId": encoderCfgServiceId,
       "encoderCfgServiceName": encoderCfgServiceName,
       "encoderCfgServiceTransportIndex": encoderCfgServiceTransportIndex,
       "encoderCfgTransportTable": encoderCfgTransportTable,
       "encoderCfgTransportEntry": encoderCfgTransportEntry,
       "encoderCfgTransportChannelIndex": encoderCfgTransportChannelIndex,
       "encoderCfgTransportIfIndex": encoderCfgTransportIfIndex,
       "encoderCfgTransportEnabled": encoderCfgTransportEnabled,
       "encoderCfgTransportType": encoderCfgTransportType,
       "encoderCfgTransportId": encoderCfgTransportId,
       "encoderCfgTransportSiStd": encoderCfgTransportSiStd,
       "encoderCfgTransportRate": encoderCfgTransportRate,
       "encoderCfgTransportRateMode": encoderCfgTransportRateMode,
       "encoderCfgTransportInetAddrType": encoderCfgTransportInetAddrType,
       "encoderCfgTransportDestIpAddr": encoderCfgTransportDestIpAddr,
       "encoderCfgTransportDestUdpPort": encoderCfgTransportDestUdpPort,
       "encoderCfgTransportGatewayAddr": encoderCfgTransportGatewayAddr,
       "encoderCfgTransportSubnetMask": encoderCfgTransportSubnetMask,
       "encoderCfgTransportIpFec": encoderCfgTransportIpFec,
       "encoderCfgTransportIpInterleave": encoderCfgTransportIpInterleave,
       "encoderCfgTransportIpAddrgMode": encoderCfgTransportIpAddrgMode,
       "inputMonitor": inputMonitor,
       "encoderInputMonVideoTable": encoderInputMonVideoTable,
       "encoderInputMonVideoEntry": encoderInputMonVideoEntry,
       "encoderInputMonVideoIfIndex": encoderInputMonVideoIfIndex,
       "encoderInputMonVideoChannelIndex": encoderInputMonVideoChannelIndex,
       "encoderInputMonVideoPhysIndex": encoderInputMonVideoPhysIndex,
       "encoderInputMonVideoType": encoderInputMonVideoType,
       "encoderInputMonVideoSyncLock": encoderInputMonVideoSyncLock,
       "encoderMonVideoInputFrameRate": encoderMonVideoInputFrameRate,
       "encoderInputMonVideoFrameLock": encoderInputMonVideoFrameLock,
       "encoderInputMonVideoChromaStable": encoderInputMonVideoChromaStable,
       "encoderInputMonVideoBlack": encoderInputMonVideoBlack,
       "encoderInputMonVideoLines": encoderInputMonVideoLines,
       "encoderInputMonVideoSdiCk": encoderInputMonVideoSdiCk,
       "encoderInputMonAudioTable": encoderInputMonAudioTable,
       "encoderInputMonAudioEntry": encoderInputMonAudioEntry,
       "encoderInputMonAudioIfIndex": encoderInputMonAudioIfIndex,
       "encoderInputMonAudioInputChanIndex": encoderInputMonAudioInputChanIndex,
       "encoderInputMonAudioPhysIndex": encoderInputMonAudioPhysIndex,
       "encoderInputMonAudioCfgChannel": encoderInputMonAudioCfgChannel,
       "encoderInputMonAudioType": encoderInputMonAudioType,
       "encoderInputMonAudioLevel": encoderInputMonAudioLevel,
       "encoderInputMonAudioReference": encoderInputMonAudioReference,
       "encoderInputMonAudioSilence": encoderInputMonAudioSilence,
       "encoderInputMonAudioAesCk": encoderInputMonAudioAesCk,
       "encoderInputMonAudioFraming": encoderInputMonAudioFraming,
       "encoderInputMonAudioAesType": encoderInputMonAudioAesType,
       "encoderInputMonVbiTable": encoderInputMonVbiTable,
       "encoderInputMonVbiEntry": encoderInputMonVbiEntry,
       "encoderInputMonVbiIfIndex": encoderInputMonVbiIfIndex,
       "encoderInputMonVbiPhysIndex": encoderInputMonVbiPhysIndex,
       "encoderInputMonVbiLineIndex": encoderInputMonVbiLineIndex,
       "encoderInputMonVbiFieldIndex": encoderInputMonVbiFieldIndex,
       "encoderInputMonVbiType": encoderInputMonVbiType,
       "encoderInputMonVbiErrors": encoderInputMonVbiErrors,
       "encoderInputMonVbiRate": encoderInputMonVbiRate,
       "encoderInputMonVbiTimeLastData": encoderInputMonVbiTimeLastData,
       "encoderInputMonVancTable": encoderInputMonVancTable,
       "encoderInputMonVancEntry": encoderInputMonVancEntry,
       "encoderInputMonVancIfIndex": encoderInputMonVancIfIndex,
       "encoderInputMonVancPhysIndex": encoderInputMonVancPhysIndex,
       "encoderInputMonVancServiceIndex": encoderInputMonVancServiceIndex,
       "encoderInputMonVancType": encoderInputMonVancType,
       "encoderInputMonVancErrors": encoderInputMonVancErrors,
       "encoderInputMonVancRate": encoderInputMonVancRate,
       "encoderInputMonVancTimeLastData": encoderInputMonVancTimeLastData,
       "encoderInputMonAncilTable": encoderInputMonAncilTable,
       "encoderInputMonAncilEntry": encoderInputMonAncilEntry,
       "encoderInputMonAncilIfIndex": encoderInputMonAncilIfIndex,
       "encoderInputMonAncilChannelIndex": encoderInputMonAncilChannelIndex,
       "encoderInputMonAncilPhysIndex": encoderInputMonAncilPhysIndex,
       "encoderInputMonAncilCfgChannel": encoderInputMonAncilCfgChannel,
       "encoderInputMonAncilType": encoderInputMonAncilType,
       "encoderInputMonAncilTimeLastPkt": encoderInputMonAncilTimeLastPkt,
       "encoderInputMonAncilRate": encoderInputMonAncilRate,
       "encoderInputMonAncilLock": encoderInputMonAncilLock,
       "encoderInputMonAncilError": encoderInputMonAncilError,
       "encoderInputMonAncilHbMissed": encoderInputMonAncilHbMissed,
       "outputMonitor": outputMonitor,
       "mpegEncoderMIBConformance": mpegEncoderMIBConformance,
       "mpegEncoderMIBCompliances": mpegEncoderMIBCompliances,
       "mpegEncoderCompliance": mpegEncoderCompliance,
       "mpegEncoderMIBGroups": mpegEncoderMIBGroups,
       "encoderCfgGroup": encoderCfgGroup,
       "encoderInputGroup": encoderInputGroup}
)
