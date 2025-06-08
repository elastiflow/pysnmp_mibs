# SNMP MIB module (NDS-DTH3-VIDEO) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/news_digital_1855/NDS-DTH3-VIDEO.mib
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

_VideoEnc_ObjectIdentity = ObjectIdentity
videoEnc = _VideoEnc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5)
)


class _VideoHardwareRelease_Type(DisplayString):
    """Custom type videoHardwareRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_VideoHardwareRelease_Type.__name__ = "DisplayString"
_VideoHardwareRelease_Object = MibScalar
videoHardwareRelease = _VideoHardwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 1),
    _VideoHardwareRelease_Type()
)
videoHardwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoHardwareRelease.setStatus("current")


class _VideoSoftwareRelease_Type(DisplayString):
    """Custom type videoSoftwareRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_VideoSoftwareRelease_Type.__name__ = "DisplayString"
_VideoSoftwareRelease_Object = MibScalar
videoSoftwareRelease = _VideoSoftwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 2),
    _VideoSoftwareRelease_Type()
)
videoSoftwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoSoftwareRelease.setStatus("current")


class _VideoFirmwareRelease_Type(DisplayString):
    """Custom type videoFirmwareRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_VideoFirmwareRelease_Type.__name__ = "DisplayString"
_VideoFirmwareRelease_Object = MibScalar
videoFirmwareRelease = _VideoFirmwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 3),
    _VideoFirmwareRelease_Type()
)
videoFirmwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoFirmwareRelease.setStatus("current")


class _VideoVCMId_Type(Integer32):
    """Custom type videoVCMId based on Integer32"""
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
        *(("e3", 1),
          ("e4-DVExpert", 2),
          ("nDS-Hybrid", 3),
          ("e4-HD", 4),
          ("e5-Video", 5),
          ("ice-module", 6))
    )


_VideoVCMId_Type.__name__ = "Integer32"
_VideoVCMId_Object = MibScalar
videoVCMId = _VideoVCMId_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 4),
    _VideoVCMId_Type()
)
videoVCMId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoVCMId.setStatus("current")


class _VideoChipset_Type(Integer32):
    """Custom type videoChipset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VideoChipset_Type.__name__ = "Integer32"
_VideoChipset_Object = MibScalar
videoChipset = _VideoChipset_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 5),
    _VideoChipset_Type()
)
videoChipset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoChipset.setStatus("current")


class _VideoDelay_Type(Integer32):
    """Custom type videoDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VideoDelay_Type.__name__ = "Integer32"
_VideoDelay_Object = MibScalar
videoDelay = _VideoDelay_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 6),
    _VideoDelay_Type()
)
videoDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoDelay.setStatus("current")
_VideonextTimeDate_Type = DateAndTime
_VideonextTimeDate_Object = MibScalar
videonextTimeDate = _VideonextTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 7),
    _VideonextTimeDate_Type()
)
videonextTimeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videonextTimeDate.setStatus("current")
_VideoTable_Object = MibTable
videoTable = _VideoTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8)
)
if mibBuilder.loadTexts:
    videoTable.setStatus("current")
_VideoEntry_Object = MibTableRow
videoEntry = _VideoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1)
)
videoEntry.setIndexNames(
    (0, "NDS-DTH3-VIDEO", "videoCurrentNextIndex"),
)
if mibBuilder.loadTexts:
    videoEntry.setStatus("current")


class _VideoCurrentNextIndex_Type(Integer32):
    """Custom type videoCurrentNextIndex based on Integer32"""
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


_VideoCurrentNextIndex_Type.__name__ = "Integer32"
_VideoCurrentNextIndex_Object = MibTableColumn
videoCurrentNextIndex = _VideoCurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 1),
    _VideoCurrentNextIndex_Type()
)
videoCurrentNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoCurrentNextIndex.setStatus("current")


class _VideoProfileLevel_Type(Integer32):
    """Custom type videoProfileLevel based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("mainProfileMainLevel", 0),
          ("professionalProfileMainLevel", 1),
          ("mainProfileHighLevel", 2),
          ("professionalProfileHighLevel", 3),
          ("windows-media-simple", 4),
          ("windows-media-main", 5),
          ("windows-media-advanced-level-1", 6),
          ("windows-media-advanced-level-3", 7),
          ("mpeg-4-main-level-3", 8),
          ("mpeg-4-422-level-3", 9),
          ("mpeg-4-main-level-4-0", 10),
          ("mpeg-4-422-level-4-0", 11),
          ("mpeg-4-high-level-3", 12),
          ("mpeg-4-high-level-4-0", 13))
    )


_VideoProfileLevel_Type.__name__ = "Integer32"
_VideoProfileLevel_Object = MibTableColumn
videoProfileLevel = _VideoProfileLevel_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 2),
    _VideoProfileLevel_Type()
)
videoProfileLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoProfileLevel.setStatus("current")


class _VideoOpMode_Type(Integer32):
    """Custom type videoOpMode based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("seamless1", 0),
          ("seamless2", 1),
          ("seamless3", 2),
          ("seamless4", 3),
          ("standardDelay", 4),
          ("lowDelay", 5),
          ("veryLowDelay", 6),
          ("megaLowDelay", 7),
          ("sifLowBitRate", 8),
          ("sifLowDelay", 9),
          ("seamless5", 10),
          ("seamless6", 11))
    )


_VideoOpMode_Type.__name__ = "Integer32"
_VideoOpMode_Object = MibTableColumn
videoOpMode = _VideoOpMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 3),
    _VideoOpMode_Type()
)
videoOpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoOpMode.setStatus("current")


class _VideoStatMux_Type(Integer32):
    """Custom type videoStatMux based on Integer32"""
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


_VideoStatMux_Type.__name__ = "Integer32"
_VideoStatMux_Object = MibTableColumn
videoStatMux = _VideoStatMux_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 4),
    _VideoStatMux_Type()
)
videoStatMux.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoStatMux.setStatus("current")


class _VideoChromaMode_Type(Integer32):
    """Custom type videoChromaMode based on Integer32"""
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
        *(("chroma-420-subsampling-off", 0),
          ("chroma-420-subsampling-preproc", 1),
          ("chroma-420-subsampling-chipset", 2),
          ("chroma-422", 3),
          ("chroma-411", 4))
    )


_VideoChromaMode_Type.__name__ = "Integer32"
_VideoChromaMode_Object = MibTableColumn
videoChromaMode = _VideoChromaMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 5),
    _VideoChromaMode_Type()
)
videoChromaMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoChromaMode.setStatus("current")


class _VideoFrameRate_Type(Integer32):
    """Custom type videoFrameRate based on Integer32"""
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
        *(("frameRate23pt976Hz", 1),
          ("frameRate24Hz", 2),
          ("frameRate25Hz", 3),
          ("frameRate29pt97Hz", 4),
          ("frameRate30Hz", 5),
          ("frameRate50Hz", 6),
          ("frameRate59pt94Hz", 7),
          ("frameRate60Hz", 8))
    )


_VideoFrameRate_Type.__name__ = "Integer32"
_VideoFrameRate_Object = MibTableColumn
videoFrameRate = _VideoFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 6),
    _VideoFrameRate_Type()
)
videoFrameRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoFrameRate.setStatus("current")


class _VideoProgSequence_Type(Integer32):
    """Custom type videoProgSequence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interlaced", 0),
          ("progressive", 1),
          ("auto-progressive-wm-video", 2))
    )


_VideoProgSequence_Type.__name__ = "Integer32"
_VideoProgSequence_Object = MibTableColumn
videoProgSequence = _VideoProgSequence_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 7),
    _VideoProgSequence_Type()
)
videoProgSequence.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoProgSequence.setStatus("current")


class _VideoVertRes_Type(Integer32):
    """Custom type videoVertRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_VideoVertRes_Type.__name__ = "Integer32"
_VideoVertRes_Object = MibTableColumn
videoVertRes = _VideoVertRes_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 8),
    _VideoVertRes_Type()
)
videoVertRes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoVertRes.setStatus("current")


class _VideoHorRes_Type(Integer32):
    """Custom type videoHorRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_VideoHorRes_Type.__name__ = "Integer32"
_VideoHorRes_Object = MibTableColumn
videoHorRes = _VideoHorRes_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 9),
    _VideoHorRes_Type()
)
videoHorRes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoHorRes.setStatus("current")


class _VideoVBIinPicture_Type(Integer32):
    """Custom type videoVBIinPicture based on Integer32"""
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


_VideoVBIinPicture_Type.__name__ = "Integer32"
_VideoVBIinPicture_Object = MibTableColumn
videoVBIinPicture = _VideoVBIinPicture_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 10),
    _VideoVBIinPicture_Type()
)
videoVBIinPicture.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoVBIinPicture.setStatus("current")


class _VideoPanScanVectors_Type(Integer32):
    """Custom type videoPanScanVectors based on Integer32"""
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


_VideoPanScanVectors_Type.__name__ = "Integer32"
_VideoPanScanVectors_Object = MibTableColumn
videoPanScanVectors = _VideoPanScanVectors_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 11),
    _VideoPanScanVectors_Type()
)
videoPanScanVectors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoPanScanVectors.setStatus("current")


class _VideoAspectRatio_Type(Integer32):
    """Custom type videoAspectRatio based on Integer32"""
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
        *(("aspect-1-0", 1),
          ("aspect-4-3", 2),
          ("aspect-16-9", 3),
          ("aspect-2pt21-1", 4))
    )


_VideoAspectRatio_Type.__name__ = "Integer32"
_VideoAspectRatio_Object = MibTableColumn
videoAspectRatio = _VideoAspectRatio_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 12),
    _VideoAspectRatio_Type()
)
videoAspectRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoAspectRatio.setStatus("current")


class _VideoGOPLength_Type(Integer32):
    """Custom type videoGOPLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_VideoGOPLength_Type.__name__ = "Integer32"
_VideoGOPLength_Object = MibTableColumn
videoGOPLength = _VideoGOPLength_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 13),
    _VideoGOPLength_Type()
)
videoGOPLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoGOPLength.setStatus("current")


class _VideoGOPStructure_Type(Integer32):
    """Custom type videoGOPStructure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_VideoGOPStructure_Type.__name__ = "Integer32"
_VideoGOPStructure_Object = MibTableColumn
videoGOPStructure = _VideoGOPStructure_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 14),
    _VideoGOPStructure_Type()
)
videoGOPStructure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoGOPStructure.setStatus("current")


class _VideoCloseGOPs_Type(Integer32):
    """Custom type videoCloseGOPs based on Integer32"""
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


_VideoCloseGOPs_Type.__name__ = "Integer32"
_VideoCloseGOPs_Object = MibTableColumn
videoCloseGOPs = _VideoCloseGOPs_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 15),
    _VideoCloseGOPs_Type()
)
videoCloseGOPs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoCloseGOPs.setStatus("current")


class _VideoInsertIFrame_Type(OctetString):
    """Custom type videoInsertIFrame based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_VideoInsertIFrame_Type.__name__ = "OctetString"
_VideoInsertIFrame_Object = MibTableColumn
videoInsertIFrame = _VideoInsertIFrame_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 16),
    _VideoInsertIFrame_Type()
)
videoInsertIFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoInsertIFrame.setStatus("current")


class _VideoPullDown_Type(Integer32):
    """Custom type videoPullDown based on Integer32"""
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
          ("chipsetControl", 1),
          ("preProcessorControl", 2))
    )


_VideoPullDown_Type.__name__ = "Integer32"
_VideoPullDown_Object = MibTableColumn
videoPullDown = _VideoPullDown_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 17),
    _VideoPullDown_Type()
)
videoPullDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoPullDown.setStatus("current")


class _VideoFieldFrame_Type(Integer32):
    """Custom type videoFieldFrame based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto-AdaptiveFrameFiltering", 0),
          ("fieldBased", 1),
          ("frameBased", 2))
    )


_VideoFieldFrame_Type.__name__ = "Integer32"
_VideoFieldFrame_Object = MibTableColumn
videoFieldFrame = _VideoFieldFrame_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 18),
    _VideoFieldFrame_Type()
)
videoFieldFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoFieldFrame.setStatus("current")


class _VideoNoiseReduction_Type(Integer32):
    """Custom type videoNoiseReduction based on Integer32"""
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
        *(("off", 0),
          ("level-1", 1),
          ("level-2", 2),
          ("level-3", 3),
          ("level-4", 4))
    )


_VideoNoiseReduction_Type.__name__ = "Integer32"
_VideoNoiseReduction_Object = MibTableColumn
videoNoiseReduction = _VideoNoiseReduction_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 19),
    _VideoNoiseReduction_Type()
)
videoNoiseReduction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoNoiseReduction.setStatus("current")


class _VideoEncode_Type(Integer32):
    """Custom type videoEncode based on Integer32"""
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


_VideoEncode_Type.__name__ = "Integer32"
_VideoEncode_Object = MibTableColumn
videoEncode = _VideoEncode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 20),
    _VideoEncode_Type()
)
videoEncode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoEncode.setStatus("current")


class _VideoBitRate_Type(Integer32):
    """Custom type videoBitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90000),
    )


_VideoBitRate_Type.__name__ = "Integer32"
_VideoBitRate_Object = MibTableColumn
videoBitRate = _VideoBitRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 21),
    _VideoBitRate_Type()
)
videoBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoBitRate.setStatus("current")


class _VideoCopyright_Type(Integer32):
    """Custom type videoCopyright based on Integer32"""
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


_VideoCopyright_Type.__name__ = "Integer32"
_VideoCopyright_Object = MibTableColumn
videoCopyright = _VideoCopyright_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 22),
    _VideoCopyright_Type()
)
videoCopyright.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoCopyright.setStatus("current")


class _VideoOriginal_Type(Integer32):
    """Custom type videoOriginal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("copy", 0),
          ("original", 1))
    )


_VideoOriginal_Type.__name__ = "Integer32"
_VideoOriginal_Object = MibTableColumn
videoOriginal = _VideoOriginal_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 23),
    _VideoOriginal_Type()
)
videoOriginal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoOriginal.setStatus("current")


class _VideoPID_Type(Integer32):
    """Custom type videoPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_VideoPID_Type.__name__ = "Integer32"
_VideoPID_Object = MibTableColumn
videoPID = _VideoPID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 24),
    _VideoPID_Type()
)
videoPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoPID.setStatus("current")


class _VideoStartOfActiveVideo_Type(Integer32):
    """Custom type videoStartOfActiveVideo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("line22", 0),
          ("line23", 1))
    )


_VideoStartOfActiveVideo_Type.__name__ = "Integer32"
_VideoStartOfActiveVideo_Object = MibTableColumn
videoStartOfActiveVideo = _VideoStartOfActiveVideo_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 25),
    _VideoStartOfActiveVideo_Type()
)
videoStartOfActiveVideo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoStartOfActiveVideo.setStatus("current")


class _VideoIFrameOnSceneCut_Type(Integer32):
    """Custom type videoIFrameOnSceneCut based on Integer32"""
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


_VideoIFrameOnSceneCut_Type.__name__ = "Integer32"
_VideoIFrameOnSceneCut_Object = MibTableColumn
videoIFrameOnSceneCut = _VideoIFrameOnSceneCut_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 26),
    _VideoIFrameOnSceneCut_Type()
)
videoIFrameOnSceneCut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoIFrameOnSceneCut.setStatus("current")


class _VideoRateBufferMode_Type(Integer32):
    """Custom type videoRateBufferMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("small", 0),
          ("medium", 1),
          ("large", 2))
    )


_VideoRateBufferMode_Type.__name__ = "Integer32"
_VideoRateBufferMode_Object = MibTableColumn
videoRateBufferMode = _VideoRateBufferMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 27),
    _VideoRateBufferMode_Type()
)
videoRateBufferMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoRateBufferMode.setStatus("current")


class _VideoSplicePoint_Type(Integer32):
    """Custom type videoSplicePoint based on Integer32"""
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
        *(("normal", 0),
          ("start-at-time-code", 1),
          ("stop-at-time-code", 2),
          ("out", 3),
          ("in-out", 4))
    )


_VideoSplicePoint_Type.__name__ = "Integer32"
_VideoSplicePoint_Object = MibTableColumn
videoSplicePoint = _VideoSplicePoint_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 28),
    _VideoSplicePoint_Type()
)
videoSplicePoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoSplicePoint.setStatus("current")


class _VideoSpliceFormat_Type(Integer32):
    """Custom type videoSpliceFormat based on Integer32"""
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
        *(("non-seamless", 0),
          ("near-seamless", 1),
          ("seamless-a", 2),
          ("seamless-b", 3))
    )


_VideoSpliceFormat_Type.__name__ = "Integer32"
_VideoSpliceFormat_Object = MibTableColumn
videoSpliceFormat = _VideoSpliceFormat_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 29),
    _VideoSpliceFormat_Type()
)
videoSpliceFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoSpliceFormat.setStatus("current")


class _VideoSpliceTimeCode_Type(OctetString):
    """Custom type videoSpliceTimeCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_VideoSpliceTimeCode_Type.__name__ = "OctetString"
_VideoSpliceTimeCode_Object = MibTableColumn
videoSpliceTimeCode = _VideoSpliceTimeCode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 30),
    _VideoSpliceTimeCode_Type()
)
videoSpliceTimeCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoSpliceTimeCode.setStatus("current")


class _VideoCCFormat_Type(Integer32):
    """Custom type videoCCFormat based on Integer32"""
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
        *(("proprietary", 0),
          ("tandberg", 1),
          ("atsc-format", 2),
          ("c-cube", 3),
          ("tv-com", 4),
          ("sa", 5),
          ("echostar", 6),
          ("skyPerfect", 7),
          ("scte-20", 8),
          ("scte-21", 9),
          ("scte-20-21", 10))
    )


_VideoCCFormat_Type.__name__ = "Integer32"
_VideoCCFormat_Object = MibTableColumn
videoCCFormat = _VideoCCFormat_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 31),
    _VideoCCFormat_Type()
)
videoCCFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoCCFormat.setStatus("current")


class _VideoDroppedFrameMode_Type(Integer32):
    """Custom type videoDroppedFrameMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dropped-frame-mode-in-NTSC", 0),
          ("non-dropped-frame-mode-in-NTSC", 1))
    )


_VideoDroppedFrameMode_Type.__name__ = "Integer32"
_VideoDroppedFrameMode_Object = MibTableColumn
videoDroppedFrameMode = _VideoDroppedFrameMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 32),
    _VideoDroppedFrameMode_Type()
)
videoDroppedFrameMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoDroppedFrameMode.setStatus("current")


class _VideoActiveFormatDescriptor_Type(Integer32):
    """Custom type videoActiveFormatDescriptor based on Integer32"""
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
          ("on-no-action-on-error", 1),
          ("on", 2))
    )


_VideoActiveFormatDescriptor_Type.__name__ = "Integer32"
_VideoActiveFormatDescriptor_Object = MibTableColumn
videoActiveFormatDescriptor = _VideoActiveFormatDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 33),
    _VideoActiveFormatDescriptor_Type()
)
videoActiveFormatDescriptor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoActiveFormatDescriptor.setStatus("current")


class _VideoEncoderConcatenation_Type(Integer32):
    """Custom type videoEncoderConcatenation based on Integer32"""
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


_VideoEncoderConcatenation_Type.__name__ = "Integer32"
_VideoEncoderConcatenation_Object = MibTableColumn
videoEncoderConcatenation = _VideoEncoderConcatenation_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 34),
    _VideoEncoderConcatenation_Type()
)
videoEncoderConcatenation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoEncoderConcatenation.setStatus("current")


class _VideoVBRMode_Type(Integer32):
    """Custom type videoVBRMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off-constant", 0),
          ("on-stuffing-off", 1),
          ("on-variable", 2))
    )


_VideoVBRMode_Type.__name__ = "Integer32"
_VideoVBRMode_Object = MibTableColumn
videoVBRMode = _VideoVBRMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 35),
    _VideoVBRMode_Type()
)
videoVBRMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoVBRMode.setStatus("current")


class _VideoBandwidth_Type(Integer32):
    """Custom type videoBandwidth based on Integer32"""
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
        *(("soft", 0),
          ("medium", 1),
          ("sharp", 2),
          ("auto", 3))
    )


_VideoBandwidth_Type.__name__ = "Integer32"
_VideoBandwidth_Object = MibTableColumn
videoBandwidth = _VideoBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 36),
    _VideoBandwidth_Type()
)
videoBandwidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoBandwidth.setStatus("current")


class _VideoVBRTargetQuality_Type(Integer32):
    """Custom type videoVBRTargetQuality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_VideoVBRTargetQuality_Type.__name__ = "Integer32"
_VideoVBRTargetQuality_Object = MibTableColumn
videoVBRTargetQuality = _VideoVBRTargetQuality_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 37),
    _VideoVBRTargetQuality_Type()
)
videoVBRTargetQuality.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoVBRTargetQuality.setStatus("current")


class _VideoShortList_Type(OctetString):
    """Custom type videoShortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )
    fixed_length = 22


_VideoShortList_Type.__name__ = "OctetString"
_VideoShortList_Object = MibTableColumn
videoShortList = _VideoShortList_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 38),
    _VideoShortList_Type()
)
videoShortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoShortList.setStatus("current")


class _VideoComponentTag_Type(Integer32):
    """Custom type videoComponentTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VideoComponentTag_Type.__name__ = "Integer32"
_VideoComponentTag_Object = MibTableColumn
videoComponentTag = _VideoComponentTag_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 39),
    _VideoComponentTag_Type()
)
videoComponentTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoComponentTag.setStatus("current")


class _VideoVBVDelay_Type(Integer32):
    """Custom type videoVBVDelay based on Integer32"""
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


_VideoVBVDelay_Type.__name__ = "Integer32"
_VideoVBVDelay_Object = MibTableColumn
videoVBVDelay = _VideoVBVDelay_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 40),
    _VideoVBVDelay_Type()
)
videoVBVDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoVBVDelay.setStatus("current")


class _VideoPESHeader_Type(Integer32):
    """Custom type videoPESHeader based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("perGOPSequence", 0),
          ("perPictureHeader", 1))
    )


_VideoPESHeader_Type.__name__ = "Integer32"
_VideoPESHeader_Object = MibTableColumn
videoPESHeader = _VideoPESHeader_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 41),
    _VideoPESHeader_Type()
)
videoPESHeader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoPESHeader.setStatus("current")


class _VideoAFDLocation_Type(Integer32):
    """Custom type videoAFDLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sequenceHeader", 0),
          ("pictureHeader", 1))
    )


_VideoAFDLocation_Type.__name__ = "Integer32"
_VideoAFDLocation_Object = MibTableColumn
videoAFDLocation = _VideoAFDLocation_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 42),
    _VideoAFDLocation_Type()
)
videoAFDLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoAFDLocation.setStatus("current")


class _VideoIndicatedBitRate_Type(Integer32):
    """Custom type videoIndicatedBitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("maximumBitRate", 0),
          ("actualBitRate", 1),
          ("indicate-2MBit-s", 2))
    )


_VideoIndicatedBitRate_Type.__name__ = "Integer32"
_VideoIndicatedBitRate_Object = MibTableColumn
videoIndicatedBitRate = _VideoIndicatedBitRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 43),
    _VideoIndicatedBitRate_Type()
)
videoIndicatedBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoIndicatedBitRate.setStatus("current")


class _VideoHDReflexMode_Type(Integer32):
    """Custom type videoHDReflexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal-sd-or-HD-only", 0),
          ("single-sd-and-single-HD", 1),
          ("multi-sd-and-HD", 2))
    )


_VideoHDReflexMode_Type.__name__ = "Integer32"
_VideoHDReflexMode_Object = MibTableColumn
videoHDReflexMode = _VideoHDReflexMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 44),
    _VideoHDReflexMode_Type()
)
videoHDReflexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoHDReflexMode.setStatus("current")


class _VideoMuxRateTracking_Type(Integer32):
    """Custom type videoMuxRateTracking based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("max-video-bit-rate", 1))
    )


_VideoMuxRateTracking_Type.__name__ = "Integer32"
_VideoMuxRateTracking_Object = MibTableColumn
videoMuxRateTracking = _VideoMuxRateTracking_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 45),
    _VideoMuxRateTracking_Type()
)
videoMuxRateTracking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoMuxRateTracking.setStatus("current")


class _VideoAdaptiveGOP_Type(Integer32):
    """Custom type videoAdaptiveGOP based on Integer32"""
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


_VideoAdaptiveGOP_Type.__name__ = "Integer32"
_VideoAdaptiveGOP_Object = MibTableColumn
videoAdaptiveGOP = _VideoAdaptiveGOP_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 46),
    _VideoAdaptiveGOP_Type()
)
videoAdaptiveGOP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoAdaptiveGOP.setStatus("current")


class _VideoSeamlessDelay_Type(Integer32):
    """Custom type videoSeamlessDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_VideoSeamlessDelay_Type.__name__ = "Integer32"
_VideoSeamlessDelay_Object = MibTableColumn
videoSeamlessDelay = _VideoSeamlessDelay_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 47),
    _VideoSeamlessDelay_Type()
)
videoSeamlessDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoSeamlessDelay.setStatus("current")


class _VideoBorderProcessing_Type(Integer32):
    """Custom type videoBorderProcessing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on-level-1", 1))
    )


_VideoBorderProcessing_Type.__name__ = "Integer32"
_VideoBorderProcessing_Object = MibTableColumn
videoBorderProcessing = _VideoBorderProcessing_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 48),
    _VideoBorderProcessing_Type()
)
videoBorderProcessing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoBorderProcessing.setStatus("current")


class _VideoPCRinVideo_Type(Integer32):
    """Custom type videoPCRinVideo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("type-2", 0),
          ("type-3", 1))
    )


_VideoPCRinVideo_Type.__name__ = "Integer32"
_VideoPCRinVideo_Object = MibTableColumn
videoPCRinVideo = _VideoPCRinVideo_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 8, 1, 49),
    _VideoPCRinVideo_Type()
)
videoPCRinVideo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoPCRinVideo.setStatus("current")
_ItsTable_Object = MibTable
itsTable = _ItsTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 9)
)
if mibBuilder.loadTexts:
    itsTable.setStatus("current")
_ItsEntry_Object = MibTableRow
itsEntry = _ItsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 9, 1)
)
itsEntry.setIndexNames(
    (0, "NDS-DTH3-VIDEO", "itsCurrentNextIndex"),
    (0, "NDS-DTH3-VIDEO", "itsLineIndex"),
)
if mibBuilder.loadTexts:
    itsEntry.setStatus("current")


class _ItsCurrentNextIndex_Type(Integer32):
    """Custom type itsCurrentNextIndex based on Integer32"""
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


_ItsCurrentNextIndex_Type.__name__ = "Integer32"
_ItsCurrentNextIndex_Object = MibTableColumn
itsCurrentNextIndex = _ItsCurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 9, 1, 1),
    _ItsCurrentNextIndex_Type()
)
itsCurrentNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsCurrentNextIndex.setStatus("current")


class _ItsLineIndex_Type(Integer32):
    """Custom type itsLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ItsLineIndex_Type.__name__ = "Integer32"
_ItsLineIndex_Object = MibTableColumn
itsLineIndex = _ItsLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 9, 1, 2),
    _ItsLineIndex_Type()
)
itsLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    itsLineIndex.setStatus("current")


class _ItsLine_Type(Integer32):
    """Custom type itsLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 335),
    )


_ItsLine_Type.__name__ = "Integer32"
_ItsLine_Object = MibTableColumn
itsLine = _ItsLine_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 9, 1, 3),
    _ItsLine_Type()
)
itsLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsLine.setStatus("current")


class _ItsCode_Type(Integer32):
    """Custom type itsCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            0
        )
    )
    namedValues = NamedValues(
        ("off", 0)
    )


_ItsCode_Type.__name__ = "Integer32"
_ItsCode_Object = MibTableColumn
itsCode = _ItsCode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 9, 1, 4),
    _ItsCode_Type()
)
itsCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    itsCode.setStatus("current")
_VideoSpliceTable_Object = MibTable
videoSpliceTable = _VideoSpliceTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 10)
)
if mibBuilder.loadTexts:
    videoSpliceTable.setStatus("current")
_VideoSpliceEntry_Object = MibTableRow
videoSpliceEntry = _VideoSpliceEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 10, 1)
)
videoSpliceEntry.setIndexNames(
    (0, "NDS-DTH3-VIDEO", "videoSplicePointIndex"),
)
if mibBuilder.loadTexts:
    videoSpliceEntry.setStatus("current")


class _VideoSplicePointIndex_Type(Integer32):
    """Custom type videoSplicePointIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_VideoSplicePointIndex_Type.__name__ = "Integer32"
_VideoSplicePointIndex_Object = MibTableColumn
videoSplicePointIndex = _VideoSplicePointIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 10, 1, 1),
    _VideoSplicePointIndex_Type()
)
videoSplicePointIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoSplicePointIndex.setStatus("current")


class _VideoSplice_Type(OctetString):
    """Custom type videoSplice based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_VideoSplice_Type.__name__ = "OctetString"
_VideoSplice_Object = MibTableColumn
videoSplice = _VideoSplice_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 10, 1, 2),
    _VideoSplice_Type()
)
videoSplice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoSplice.setStatus("current")


class _VideoMinBitRate_Type(Integer32):
    """Custom type videoMinBitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_VideoMinBitRate_Type.__name__ = "Integer32"
_VideoMinBitRate_Object = MibScalar
videoMinBitRate = _VideoMinBitRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 11),
    _VideoMinBitRate_Type()
)
videoMinBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoMinBitRate.setStatus("current")


class _VideoMaxBitRate_Type(Integer32):
    """Custom type videoMaxBitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 90000),
    )


_VideoMaxBitRate_Type.__name__ = "Integer32"
_VideoMaxBitRate_Object = MibScalar
videoMaxBitRate = _VideoMaxBitRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 12),
    _VideoMaxBitRate_Type()
)
videoMaxBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoMaxBitRate.setStatus("current")


class _VideoFunctionality_Type(Integer32):
    """Custom type videoFunctionality based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("standard", 0),
          ("high-performance", 1))
    )


_VideoFunctionality_Type.__name__ = "Integer32"
_VideoFunctionality_Object = MibScalar
videoFunctionality = _VideoFunctionality_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 13),
    _VideoFunctionality_Type()
)
videoFunctionality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoFunctionality.setStatus("current")


class _VideoCodingFormat_Type(Integer32):
    """Custom type videoCodingFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mpeg-2", 1),
          ("windows-media-wmv9", 2),
          ("h-264-avc", 3))
    )


_VideoCodingFormat_Type.__name__ = "Integer32"
_VideoCodingFormat_Object = MibScalar
videoCodingFormat = _VideoCodingFormat_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 16),
    _VideoCodingFormat_Type()
)
videoCodingFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoCodingFormat.setStatus("current")
_VideoSCTE35Table_Object = MibTable
videoSCTE35Table = _VideoSCTE35Table_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 17)
)
if mibBuilder.loadTexts:
    videoSCTE35Table.setStatus("current")
_VideoSCTE35Entry_Object = MibTableRow
videoSCTE35Entry = _VideoSCTE35Entry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 17, 1)
)
videoSCTE35Entry.setIndexNames(
    (0, "NDS-DTH3-VIDEO", "videoSCTE35CurrentNextIndex"),
)
if mibBuilder.loadTexts:
    videoSCTE35Entry.setStatus("current")


class _VideoSCTE35CurrentNextIndex_Type(Integer32):
    """Custom type videoSCTE35CurrentNextIndex based on Integer32"""
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


_VideoSCTE35CurrentNextIndex_Type.__name__ = "Integer32"
_VideoSCTE35CurrentNextIndex_Object = MibTableColumn
videoSCTE35CurrentNextIndex = _VideoSCTE35CurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 17, 1, 1),
    _VideoSCTE35CurrentNextIndex_Type()
)
videoSCTE35CurrentNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    videoSCTE35CurrentNextIndex.setStatus("current")


class _VideoSCTE35ControlBy_Type(Integer32):
    """Custom type videoSCTE35ControlBy based on Integer32"""
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
        *(("gpicard", 0),
          ("dvs525", 1),
          ("smpte", 2),
          ("dvs525compel", 3))
    )


_VideoSCTE35ControlBy_Type.__name__ = "Integer32"
_VideoSCTE35ControlBy_Object = MibTableColumn
videoSCTE35ControlBy = _VideoSCTE35ControlBy_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 17, 1, 2),
    _VideoSCTE35ControlBy_Type()
)
videoSCTE35ControlBy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoSCTE35ControlBy.setStatus("current")


class _VideoSCTE35GPIInputSelection_Type(Integer32):
    """Custom type videoSCTE35GPIInputSelection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_VideoSCTE35GPIInputSelection_Type.__name__ = "Integer32"
_VideoSCTE35GPIInputSelection_Object = MibTableColumn
videoSCTE35GPIInputSelection = _VideoSCTE35GPIInputSelection_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 17, 1, 3),
    _VideoSCTE35GPIInputSelection_Type()
)
videoSCTE35GPIInputSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoSCTE35GPIInputSelection.setStatus("current")


class _VideoSCTE35GPIOutOfNetworkPolarity_Type(Integer32):
    """Custom type videoSCTE35GPIOutOfNetworkPolarity based on Integer32"""
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


_VideoSCTE35GPIOutOfNetworkPolarity_Type.__name__ = "Integer32"
_VideoSCTE35GPIOutOfNetworkPolarity_Object = MibTableColumn
videoSCTE35GPIOutOfNetworkPolarity = _VideoSCTE35GPIOutOfNetworkPolarity_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 17, 1, 4),
    _VideoSCTE35GPIOutOfNetworkPolarity_Type()
)
videoSCTE35GPIOutOfNetworkPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoSCTE35GPIOutOfNetworkPolarity.setStatus("current")


class _VideoSCTE35OutPreRollTime_Type(Integer32):
    """Custom type videoSCTE35OutPreRollTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_VideoSCTE35OutPreRollTime_Type.__name__ = "Integer32"
_VideoSCTE35OutPreRollTime_Object = MibTableColumn
videoSCTE35OutPreRollTime = _VideoSCTE35OutPreRollTime_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 17, 1, 5),
    _VideoSCTE35OutPreRollTime_Type()
)
videoSCTE35OutPreRollTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoSCTE35OutPreRollTime.setStatus("current")


class _VideoSCTE35RetPreRollTime_Type(Integer32):
    """Custom type videoSCTE35RetPreRollTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_VideoSCTE35RetPreRollTime_Type.__name__ = "Integer32"
_VideoSCTE35RetPreRollTime_Object = MibTableColumn
videoSCTE35RetPreRollTime = _VideoSCTE35RetPreRollTime_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 17, 1, 6),
    _VideoSCTE35RetPreRollTime_Type()
)
videoSCTE35RetPreRollTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoSCTE35RetPreRollTime.setStatus("current")


class _VideoSCTE35NumberOfOutMessages_Type(Integer32):
    """Custom type videoSCTE35NumberOfOutMessages based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("single", 0),
          ("multiple", 1))
    )


_VideoSCTE35NumberOfOutMessages_Type.__name__ = "Integer32"
_VideoSCTE35NumberOfOutMessages_Object = MibTableColumn
videoSCTE35NumberOfOutMessages = _VideoSCTE35NumberOfOutMessages_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 17, 1, 7),
    _VideoSCTE35NumberOfOutMessages_Type()
)
videoSCTE35NumberOfOutMessages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoSCTE35NumberOfOutMessages.setStatus("current")


class _VideoSCTE35NumberOfRetMessages_Type(Integer32):
    """Custom type videoSCTE35NumberOfRetMessages based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("single", 0),
          ("multiple", 1))
    )


_VideoSCTE35NumberOfRetMessages_Type.__name__ = "Integer32"
_VideoSCTE35NumberOfRetMessages_Object = MibTableColumn
videoSCTE35NumberOfRetMessages = _VideoSCTE35NumberOfRetMessages_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 17, 1, 8),
    _VideoSCTE35NumberOfRetMessages_Type()
)
videoSCTE35NumberOfRetMessages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoSCTE35NumberOfRetMessages.setStatus("current")


class _VideoSCTE35Avail_Type(Integer32):
    """Custom type videoSCTE35Avail based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("present", 1))
    )


_VideoSCTE35Avail_Type.__name__ = "Integer32"
_VideoSCTE35Avail_Object = MibTableColumn
videoSCTE35Avail = _VideoSCTE35Avail_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 17, 1, 9),
    _VideoSCTE35Avail_Type()
)
videoSCTE35Avail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoSCTE35Avail.setStatus("current")


class _VideoSCTE35AvailId_Type(Unsigned32):
    """Custom type videoSCTE35AvailId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_VideoSCTE35AvailId_Type.__name__ = "Unsigned32"
_VideoSCTE35AvailId_Object = MibTableColumn
videoSCTE35AvailId = _VideoSCTE35AvailId_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 17, 1, 10),
    _VideoSCTE35AvailId_Type()
)
videoSCTE35AvailId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoSCTE35AvailId.setStatus("current")


class _VideoSCTE35PID_Type(Integer32):
    """Custom type videoSCTE35PID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8190),
    )


_VideoSCTE35PID_Type.__name__ = "Integer32"
_VideoSCTE35PID_Object = MibTableColumn
videoSCTE35PID = _VideoSCTE35PID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 17, 1, 11),
    _VideoSCTE35PID_Type()
)
videoSCTE35PID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoSCTE35PID.setStatus("current")


class _VideoSCTE35SpliceDuration_Type(Integer32):
    """Custom type videoSCTE35SpliceDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_VideoSCTE35SpliceDuration_Type.__name__ = "Integer32"
_VideoSCTE35SpliceDuration_Object = MibTableColumn
videoSCTE35SpliceDuration = _VideoSCTE35SpliceDuration_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 17, 1, 12),
    _VideoSCTE35SpliceDuration_Type()
)
videoSCTE35SpliceDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoSCTE35SpliceDuration.setStatus("current")


class _VideoSCTE35FixedDelay_Type(Integer32):
    """Custom type videoSCTE35FixedDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
    )


_VideoSCTE35FixedDelay_Type.__name__ = "Integer32"
_VideoSCTE35FixedDelay_Object = MibTableColumn
videoSCTE35FixedDelay = _VideoSCTE35FixedDelay_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 17, 1, 13),
    _VideoSCTE35FixedDelay_Type()
)
videoSCTE35FixedDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoSCTE35FixedDelay.setStatus("current")


class _VideoSCTE35SpliceIDIncrentMode_Type(Integer32):
    """Custom type videoSCTE35SpliceIDIncrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("availIncrementMode", 0),
          ("msgIncrementMode", 1))
    )


_VideoSCTE35SpliceIDIncrentMode_Type.__name__ = "Integer32"
_VideoSCTE35SpliceIDIncrentMode_Object = MibTableColumn
videoSCTE35SpliceIDIncrentMode = _VideoSCTE35SpliceIDIncrentMode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 17, 1, 14),
    _VideoSCTE35SpliceIDIncrentMode_Type()
)
videoSCTE35SpliceIDIncrentMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoSCTE35SpliceIDIncrentMode.setStatus("current")


class _VideoSCTE35PreRollAdjustment_Type(Integer32):
    """Custom type videoSCTE35PreRollAdjustment based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_VideoSCTE35PreRollAdjustment_Type.__name__ = "Integer32"
_VideoSCTE35PreRollAdjustment_Object = MibTableColumn
videoSCTE35PreRollAdjustment = _VideoSCTE35PreRollAdjustment_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 17, 1, 15),
    _VideoSCTE35PreRollAdjustment_Type()
)
videoSCTE35PreRollAdjustment.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoSCTE35PreRollAdjustment.setStatus("current")


class _VideoSCTE35ReturnToNetwork_Type(Integer32):
    """Custom type videoSCTE35ReturnToNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 0),
          ("externalControl", 1))
    )


_VideoSCTE35ReturnToNetwork_Type.__name__ = "Integer32"
_VideoSCTE35ReturnToNetwork_Object = MibTableColumn
videoSCTE35ReturnToNetwork = _VideoSCTE35ReturnToNetwork_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 5, 17, 1, 16),
    _VideoSCTE35ReturnToNetwork_Type()
)
videoSCTE35ReturnToNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    videoSCTE35ReturnToNetwork.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NDS-DTH3-VIDEO",
    **{"ndsDTH3Encoder": ndsDTH3Encoder,
       "videoEnc": videoEnc,
       "videoHardwareRelease": videoHardwareRelease,
       "videoSoftwareRelease": videoSoftwareRelease,
       "videoFirmwareRelease": videoFirmwareRelease,
       "videoVCMId": videoVCMId,
       "videoChipset": videoChipset,
       "videoDelay": videoDelay,
       "videonextTimeDate": videonextTimeDate,
       "videoTable": videoTable,
       "videoEntry": videoEntry,
       "videoCurrentNextIndex": videoCurrentNextIndex,
       "videoProfileLevel": videoProfileLevel,
       "videoOpMode": videoOpMode,
       "videoStatMux": videoStatMux,
       "videoChromaMode": videoChromaMode,
       "videoFrameRate": videoFrameRate,
       "videoProgSequence": videoProgSequence,
       "videoVertRes": videoVertRes,
       "videoHorRes": videoHorRes,
       "videoVBIinPicture": videoVBIinPicture,
       "videoPanScanVectors": videoPanScanVectors,
       "videoAspectRatio": videoAspectRatio,
       "videoGOPLength": videoGOPLength,
       "videoGOPStructure": videoGOPStructure,
       "videoCloseGOPs": videoCloseGOPs,
       "videoInsertIFrame": videoInsertIFrame,
       "videoPullDown": videoPullDown,
       "videoFieldFrame": videoFieldFrame,
       "videoNoiseReduction": videoNoiseReduction,
       "videoEncode": videoEncode,
       "videoBitRate": videoBitRate,
       "videoCopyright": videoCopyright,
       "videoOriginal": videoOriginal,
       "videoPID": videoPID,
       "videoStartOfActiveVideo": videoStartOfActiveVideo,
       "videoIFrameOnSceneCut": videoIFrameOnSceneCut,
       "videoRateBufferMode": videoRateBufferMode,
       "videoSplicePoint": videoSplicePoint,
       "videoSpliceFormat": videoSpliceFormat,
       "videoSpliceTimeCode": videoSpliceTimeCode,
       "videoCCFormat": videoCCFormat,
       "videoDroppedFrameMode": videoDroppedFrameMode,
       "videoActiveFormatDescriptor": videoActiveFormatDescriptor,
       "videoEncoderConcatenation": videoEncoderConcatenation,
       "videoVBRMode": videoVBRMode,
       "videoBandwidth": videoBandwidth,
       "videoVBRTargetQuality": videoVBRTargetQuality,
       "videoShortList": videoShortList,
       "videoComponentTag": videoComponentTag,
       "videoVBVDelay": videoVBVDelay,
       "videoPESHeader": videoPESHeader,
       "videoAFDLocation": videoAFDLocation,
       "videoIndicatedBitRate": videoIndicatedBitRate,
       "videoHDReflexMode": videoHDReflexMode,
       "videoMuxRateTracking": videoMuxRateTracking,
       "videoAdaptiveGOP": videoAdaptiveGOP,
       "videoSeamlessDelay": videoSeamlessDelay,
       "videoBorderProcessing": videoBorderProcessing,
       "videoPCRinVideo": videoPCRinVideo,
       "itsTable": itsTable,
       "itsEntry": itsEntry,
       "itsCurrentNextIndex": itsCurrentNextIndex,
       "itsLineIndex": itsLineIndex,
       "itsLine": itsLine,
       "itsCode": itsCode,
       "videoSpliceTable": videoSpliceTable,
       "videoSpliceEntry": videoSpliceEntry,
       "videoSplicePointIndex": videoSplicePointIndex,
       "videoSplice": videoSplice,
       "videoMinBitRate": videoMinBitRate,
       "videoMaxBitRate": videoMaxBitRate,
       "videoFunctionality": videoFunctionality,
       "videoCodingFormat": videoCodingFormat,
       "videoSCTE35Table": videoSCTE35Table,
       "videoSCTE35Entry": videoSCTE35Entry,
       "videoSCTE35CurrentNextIndex": videoSCTE35CurrentNextIndex,
       "videoSCTE35ControlBy": videoSCTE35ControlBy,
       "videoSCTE35GPIInputSelection": videoSCTE35GPIInputSelection,
       "videoSCTE35GPIOutOfNetworkPolarity": videoSCTE35GPIOutOfNetworkPolarity,
       "videoSCTE35OutPreRollTime": videoSCTE35OutPreRollTime,
       "videoSCTE35RetPreRollTime": videoSCTE35RetPreRollTime,
       "videoSCTE35NumberOfOutMessages": videoSCTE35NumberOfOutMessages,
       "videoSCTE35NumberOfRetMessages": videoSCTE35NumberOfRetMessages,
       "videoSCTE35Avail": videoSCTE35Avail,
       "videoSCTE35AvailId": videoSCTE35AvailId,
       "videoSCTE35PID": videoSCTE35PID,
       "videoSCTE35SpliceDuration": videoSCTE35SpliceDuration,
       "videoSCTE35FixedDelay": videoSCTE35FixedDelay,
       "videoSCTE35SpliceIDIncrentMode": videoSCTE35SpliceIDIncrentMode,
       "videoSCTE35PreRollAdjustment": videoSCTE35PreRollAdjustment,
       "videoSCTE35ReturnToNetwork": videoSCTE35ReturnToNetwork}
)
