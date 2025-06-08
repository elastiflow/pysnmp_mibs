# SNMP MIB module (NDS-DTH3-PREPROCESSOR) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/news_digital_1855/NDS-DTH3-PREPROCESSOR.mib
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

_VidpreEnc_ObjectIdentity = ObjectIdentity
vidpreEnc = _VidpreEnc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3)
)


class _VidpreHardwareRelease_Type(DisplayString):
    """Custom type vidpreHardwareRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VidpreHardwareRelease_Type.__name__ = "DisplayString"
_VidpreHardwareRelease_Object = MibScalar
vidpreHardwareRelease = _VidpreHardwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 1),
    _VidpreHardwareRelease_Type()
)
vidpreHardwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidpreHardwareRelease.setStatus("current")


class _VidpreSoftwareRelease_Type(DisplayString):
    """Custom type vidpreSoftwareRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VidpreSoftwareRelease_Type.__name__ = "DisplayString"
_VidpreSoftwareRelease_Object = MibScalar
vidpreSoftwareRelease = _VidpreSoftwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 2),
    _VidpreSoftwareRelease_Type()
)
vidpreSoftwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidpreSoftwareRelease.setStatus("current")


class _VidpreFirmwareRelease_Type(DisplayString):
    """Custom type vidpreFirmwareRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_VidpreFirmwareRelease_Type.__name__ = "DisplayString"
_VidpreFirmwareRelease_Object = MibScalar
vidpreFirmwareRelease = _VidpreFirmwareRelease_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 3),
    _VidpreFirmwareRelease_Type()
)
vidpreFirmwareRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidpreFirmwareRelease.setStatus("current")


class _VidpreNoEmbAudDIDExtractors_Type(Integer32):
    """Custom type vidpreNoEmbAudDIDExtractors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_VidpreNoEmbAudDIDExtractors_Type.__name__ = "Integer32"
_VidpreNoEmbAudDIDExtractors_Object = MibScalar
vidpreNoEmbAudDIDExtractors = _VidpreNoEmbAudDIDExtractors_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 4),
    _VidpreNoEmbAudDIDExtractors_Type()
)
vidpreNoEmbAudDIDExtractors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidpreNoEmbAudDIDExtractors.setStatus("current")
_VidprenextTimeDate_Type = DateAndTime
_VidprenextTimeDate_Object = MibScalar
vidprenextTimeDate = _VidprenextTimeDate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 5),
    _VidprenextTimeDate_Type()
)
vidprenextTimeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidprenextTimeDate.setStatus("current")


class _VidpreTimeCode_Type(OctetString):
    """Custom type vidpreTimeCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_VidpreTimeCode_Type.__name__ = "OctetString"
_VidpreTimeCode_Object = MibScalar
vidpreTimeCode = _VidpreTimeCode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 6),
    _VidpreTimeCode_Type()
)
vidpreTimeCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidpreTimeCode.setStatus("current")
_VidpreTable_Object = MibTable
vidpreTable = _VidpreTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7)
)
if mibBuilder.loadTexts:
    vidpreTable.setStatus("current")
_VidpreEntry_Object = MibTableRow
vidpreEntry = _VidpreEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1)
)
vidpreEntry.setIndexNames(
    (0, "NDS-DTH3-PREPROCESSOR", "vidpreCurrentNextIndex"),
)
if mibBuilder.loadTexts:
    vidpreEntry.setStatus("current")


class _VidpreCurrentNextIndex_Type(Integer32):
    """Custom type vidpreCurrentNextIndex based on Integer32"""
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


_VidpreCurrentNextIndex_Type.__name__ = "Integer32"
_VidpreCurrentNextIndex_Object = MibTableColumn
vidpreCurrentNextIndex = _VidpreCurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 1),
    _VidpreCurrentNextIndex_Type()
)
vidpreCurrentNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidpreCurrentNextIndex.setStatus("current")


class _VidpreSource_Type(Integer32):
    """Custom type vidpreSource based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("serialDigital", 1),
          ("parallelDigital", 2),
          ("analogue", 3),
          ("testpattern-bars-and-red", 4),
          ("testpattern-moving-pattern", 5),
          ("testpattern-noise", 6),
          ("testpattern-colour-bars", 7),
          ("testpattern-ident", 8),
          ("testpattern-black", 9),
          ("analogue-PAL-I", 10),
          ("analogue-PAL-M", 11),
          ("analogue-PAL-N", 12),
          ("analogue-PAL-N-Jamaica", 13),
          ("analogue-PAL-D", 14),
          ("analogue-NTSC-Pedestal", 15),
          ("analogue-NTSC-No-Pedestal", 16),
          ("component-YCrCb", 17),
          ("component-YPrPb-Pedastal", 18),
          ("component-YPrPb-BetaLevels", 19),
          ("hd-SDI", 20),
          ("hd-testpattern-monitor", 21),
          ("hd-testpattern-black", 22))
    )


_VidpreSource_Type.__name__ = "Integer32"
_VidpreSource_Object = MibTableColumn
vidpreSource = _VidpreSource_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 2),
    _VidpreSource_Type()
)
vidpreSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreSource.setStatus("current")


class _VidpreOPVideoLoss_Type(Integer32):
    """Custom type vidpreOPVideoLoss based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("freezeFrame", 0),
          ("black", 1),
          ("barsandRed", 2),
          ("freezeFrameplusText", 3),
          ("blackplusText", 4),
          ("barsandRedplusText", 5),
          ("storedOSD", 6),
          ("noVideoPID", 7),
          ("noASIOutput", 8))
    )


_VidpreOPVideoLoss_Type.__name__ = "Integer32"
_VidpreOPVideoLoss_Object = MibTableColumn
vidpreOPVideoLoss = _VidpreOPVideoLoss_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 3),
    _VidpreOPVideoLoss_Type()
)
vidpreOPVideoLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreOPVideoLoss.setStatus("current")


class _VidpreNoiseReduction_Type(Integer32):
    """Custom type vidpreNoiseReduction based on Integer32"""
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
        *(("off", 0),
          ("adaptive-level-1", 1),
          ("adaptive-level-2", 2),
          ("adaptive-level-3", 3),
          ("adaptive-level-4", 4),
          ("fixed-level-1", 5),
          ("fixed-level-2", 6),
          ("fixed-level-3", 7))
    )


_VidpreNoiseReduction_Type.__name__ = "Integer32"
_VidpreNoiseReduction_Object = MibTableColumn
vidpreNoiseReduction = _VidpreNoiseReduction_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 4),
    _VidpreNoiseReduction_Type()
)
vidpreNoiseReduction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreNoiseReduction.setStatus("current")


class _VidpreFrameSync_Type(Integer32):
    """Custom type vidpreFrameSync based on Integer32"""
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


_VidpreFrameSync_Type.__name__ = "Integer32"
_VidpreFrameSync_Object = MibTableColumn
vidpreFrameSync = _VidpreFrameSync_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 5),
    _VidpreFrameSync_Type()
)
vidpreFrameSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreFrameSync.setStatus("current")


class _VidpreEmbAudioSource1_Type(Integer32):
    """Custom type vidpreEmbAudioSource1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_VidpreEmbAudioSource1_Type.__name__ = "Integer32"
_VidpreEmbAudioSource1_Object = MibTableColumn
vidpreEmbAudioSource1 = _VidpreEmbAudioSource1_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 6),
    _VidpreEmbAudioSource1_Type()
)
vidpreEmbAudioSource1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreEmbAudioSource1.setStatus("current")


class _VidpreEmbAudioSource2_Type(Integer32):
    """Custom type vidpreEmbAudioSource2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_VidpreEmbAudioSource2_Type.__name__ = "Integer32"
_VidpreEmbAudioSource2_Object = MibTableColumn
vidpreEmbAudioSource2 = _VidpreEmbAudioSource2_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 7),
    _VidpreEmbAudioSource2_Type()
)
vidpreEmbAudioSource2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreEmbAudioSource2.setStatus("current")


class _VidpreEmbAudioSource3_Type(Integer32):
    """Custom type vidpreEmbAudioSource3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_VidpreEmbAudioSource3_Type.__name__ = "Integer32"
_VidpreEmbAudioSource3_Object = MibTableColumn
vidpreEmbAudioSource3 = _VidpreEmbAudioSource3_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 8),
    _VidpreEmbAudioSource3_Type()
)
vidpreEmbAudioSource3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreEmbAudioSource3.setStatus("current")


class _VidpreEmbAudioSource4_Type(Integer32):
    """Custom type vidpreEmbAudioSource4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_VidpreEmbAudioSource4_Type.__name__ = "Integer32"
_VidpreEmbAudioSource4_Object = MibTableColumn
vidpreEmbAudioSource4 = _VidpreEmbAudioSource4_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 9),
    _VidpreEmbAudioSource4_Type()
)
vidpreEmbAudioSource4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreEmbAudioSource4.setStatus("current")


class _VidpreLogo_Type(Integer32):
    """Custom type vidpreLogo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hide", 0),
          ("show", 1))
    )


_VidpreLogo_Type.__name__ = "Integer32"
_VidpreLogo_Object = MibTableColumn
vidpreLogo = _VidpreLogo_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 10),
    _VidpreLogo_Type()
)
vidpreLogo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreLogo.setStatus("current")


class _VidpreVertRes_Type(Integer32):
    """Custom type vidpreVertRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1088),
    )


_VidpreVertRes_Type.__name__ = "Integer32"
_VidpreVertRes_Object = MibTableColumn
vidpreVertRes = _VidpreVertRes_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 11),
    _VidpreVertRes_Type()
)
vidpreVertRes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreVertRes.setStatus("current")


class _VidpreFrameRate_Type(Integer32):
    """Custom type vidpreFrameRate based on Integer32"""
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


_VidpreFrameRate_Type.__name__ = "Integer32"
_VidpreFrameRate_Object = MibTableColumn
vidpreFrameRate = _VidpreFrameRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 12),
    _VidpreFrameRate_Type()
)
vidpreFrameRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreFrameRate.setStatus("current")


class _VidpreProgressive_Type(Integer32):
    """Custom type vidpreProgressive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("interlace", 0),
          ("progressive", 1))
    )


_VidpreProgressive_Type.__name__ = "Integer32"
_VidpreProgressive_Object = MibTableColumn
vidpreProgressive = _VidpreProgressive_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 13),
    _VidpreProgressive_Type()
)
vidpreProgressive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreProgressive.setStatus("current")


class _VidpreHorRes_Type(Integer32):
    """Custom type vidpreHorRes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1920),
    )


_VidpreHorRes_Type.__name__ = "Integer32"
_VidpreHorRes_Object = MibTableColumn
vidpreHorRes = _VidpreHorRes_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 14),
    _VidpreHorRes_Type()
)
vidpreHorRes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreHorRes.setStatus("current")


class _VidpreEmbeddedAudInput_Type(Integer32):
    """Custom type vidpreEmbeddedAudInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("sDI", 0),
          ("hD-SDI", 1))
    )


_VidpreEmbeddedAudInput_Type.__name__ = "Integer32"
_VidpreEmbeddedAudInput_Object = MibTableColumn
vidpreEmbeddedAudInput = _VidpreEmbeddedAudInput_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 15),
    _VidpreEmbeddedAudInput_Type()
)
vidpreEmbeddedAudInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreEmbeddedAudInput.setStatus("current")


class _VidprePALPlusEnable_Type(Integer32):
    """Custom type vidprePALPlusEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("auto", 1))
    )


_VidprePALPlusEnable_Type.__name__ = "Integer32"
_VidprePALPlusEnable_Object = MibTableColumn
vidprePALPlusEnable = _VidprePALPlusEnable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 16),
    _VidprePALPlusEnable_Type()
)
vidprePALPlusEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidprePALPlusEnable.setStatus("current")


class _VidpreAutoVITCDetect_Type(Integer32):
    """Custom type vidpreAutoVITCDetect based on Integer32"""
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


_VidpreAutoVITCDetect_Type.__name__ = "Integer32"
_VidpreAutoVITCDetect_Object = MibTableColumn
vidpreAutoVITCDetect = _VidpreAutoVITCDetect_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 17),
    _VidpreAutoVITCDetect_Type()
)
vidpreAutoVITCDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreAutoVITCDetect.setStatus("current")


class _VidpreVBIField1_Type(OctetString):
    """Custom type vidpreVBIField1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 18),
    )


_VidpreVBIField1_Type.__name__ = "OctetString"
_VidpreVBIField1_Object = MibTableColumn
vidpreVBIField1 = _VidpreVBIField1_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 18),
    _VidpreVBIField1_Type()
)
vidpreVBIField1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreVBIField1.setStatus("current")


class _VidpreVBIField2_Type(OctetString):
    """Custom type vidpreVBIField2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(13, 18),
    )


_VidpreVBIField2_Type.__name__ = "OctetString"
_VidpreVBIField2_Object = MibTableColumn
vidpreVBIField2 = _VidpreVBIField2_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 19),
    _VidpreVBIField2_Type()
)
vidpreVBIField2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreVBIField2.setStatus("current")


class _VidpreClosedCaptions_Type(Integer32):
    """Custom type vidpreClosedCaptions based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on-video-line-21", 1),
          ("on-video-line-21-284", 2),
          ("on-SMPTE-333M", 4),
          ("on-test-data-EIA-608", 5),
          ("on-SDI-SMPTE-334M", 7))
    )


_VidpreClosedCaptions_Type.__name__ = "Integer32"
_VidpreClosedCaptions_Object = MibTableColumn
vidpreClosedCaptions = _VidpreClosedCaptions_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 20),
    _VidpreClosedCaptions_Type()
)
vidpreClosedCaptions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreClosedCaptions.setStatus("current")


class _VidpreCCDescriptor_Type(Integer32):
    """Custom type vidpreCCDescriptor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("line-21-only", 0),
          ("line-21-and-advanced", 1),
          ("advanced-only", 2))
    )


_VidpreCCDescriptor_Type.__name__ = "Integer32"
_VidpreCCDescriptor_Object = MibTableColumn
vidpreCCDescriptor = _VidpreCCDescriptor_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 21),
    _VidpreCCDescriptor_Type()
)
vidpreCCDescriptor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreCCDescriptor.setStatus("current")


class _VidpreBlankLine23_Type(Integer32):
    """Custom type vidpreBlankLine23 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("full", 2))
    )


_VidpreBlankLine23_Type.__name__ = "Integer32"
_VidpreBlankLine23_Object = MibTableColumn
vidpreBlankLine23 = _VidpreBlankLine23_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 22),
    _VidpreBlankLine23_Type()
)
vidpreBlankLine23.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreBlankLine23.setStatus("current")


class _VidpreCCPenSize_Type(Integer32):
    """Custom type vidpreCCPenSize based on Integer32"""
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
          ("normal", 1),
          ("large", 2))
    )


_VidpreCCPenSize_Type.__name__ = "Integer32"
_VidpreCCPenSize_Object = MibTableColumn
vidpreCCPenSize = _VidpreCCPenSize_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 23),
    _VidpreCCPenSize_Type()
)
vidpreCCPenSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreCCPenSize.setStatus("current")


class _VidpreCCFont_Type(Integer32):
    """Custom type vidpreCCFont based on Integer32"""
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
        *(("default", 0),
          ("courier", 1),
          ("times-new-roman", 2),
          ("helvetica", 3),
          ("arial", 4),
          ("casual", 5),
          ("cursive", 6),
          ("small-capitals", 7))
    )


_VidpreCCFont_Type.__name__ = "Integer32"
_VidpreCCFont_Object = MibTableColumn
vidpreCCFont = _VidpreCCFont_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 24),
    _VidpreCCFont_Type()
)
vidpreCCFont.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreCCFont.setStatus("current")


class _VidpreCCForeground_Type(Integer32):
    """Custom type vidpreCCForeground based on Integer32"""
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
        *(("white", 0),
          ("yellow", 1),
          ("cyan", 2),
          ("green", 3),
          ("red", 4),
          ("magenta", 5),
          ("blue", 6),
          ("black", 7))
    )


_VidpreCCForeground_Type.__name__ = "Integer32"
_VidpreCCForeground_Object = MibTableColumn
vidpreCCForeground = _VidpreCCForeground_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 25),
    _VidpreCCForeground_Type()
)
vidpreCCForeground.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreCCForeground.setStatus("current")


class _VidpreCCBackground_Type(Integer32):
    """Custom type vidpreCCBackground based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("solid", 0),
          ("translucent", 2),
          ("transparent", 3))
    )


_VidpreCCBackground_Type.__name__ = "Integer32"
_VidpreCCBackground_Object = MibTableColumn
vidpreCCBackground = _VidpreCCBackground_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 26),
    _VidpreCCBackground_Type()
)
vidpreCCBackground.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreCCBackground.setStatus("current")


class _VidpreStillFrameTrigger_Type(Integer32):
    """Custom type vidpreStillFrameTrigger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VidpreStillFrameTrigger_Type.__name__ = "Integer32"
_VidpreStillFrameTrigger_Object = MibTableColumn
vidpreStillFrameTrigger = _VidpreStillFrameTrigger_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 27),
    _VidpreStillFrameTrigger_Type()
)
vidpreStillFrameTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreStillFrameTrigger.setStatus("current")


class _VidpreStillFrameSensitivity_Type(Integer32):
    """Custom type vidpreStillFrameSensitivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_VidpreStillFrameSensitivity_Type.__name__ = "Integer32"
_VidpreStillFrameSensitivity_Object = MibTableColumn
vidpreStillFrameSensitivity = _VidpreStillFrameSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 28),
    _VidpreStillFrameSensitivity_Type()
)
vidpreStillFrameSensitivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreStillFrameSensitivity.setStatus("current")


class _VidprePredictiveProcessing_Type(Integer32):
    """Custom type vidprePredictiveProcessing based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("advanced", 1))
    )


_VidprePredictiveProcessing_Type.__name__ = "Integer32"
_VidprePredictiveProcessing_Object = MibTableColumn
vidprePredictiveProcessing = _VidprePredictiveProcessing_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 29),
    _VidprePredictiveProcessing_Type()
)
vidprePredictiveProcessing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidprePredictiveProcessing.setStatus("current")


class _VidpreMotionCompensatedNoiseReduction_Type(Integer32):
    """Custom type vidpreMotionCompensatedNoiseReduction based on Integer32"""
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
          ("level-1", 1),
          ("level-2", 2),
          ("level-3", 3),
          ("level-4", 4),
          ("level-5", 5),
          ("level-6", 6),
          ("level-7", 7),
          ("level-8", 8),
          ("level-9", 9),
          ("level-10", 10))
    )


_VidpreMotionCompensatedNoiseReduction_Type.__name__ = "Integer32"
_VidpreMotionCompensatedNoiseReduction_Object = MibTableColumn
vidpreMotionCompensatedNoiseReduction = _VidpreMotionCompensatedNoiseReduction_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 30),
    _VidpreMotionCompensatedNoiseReduction_Type()
)
vidpreMotionCompensatedNoiseReduction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreMotionCompensatedNoiseReduction.setStatus("current")


class _VidpreVITConPES_Type(Integer32):
    """Custom type vidpreVITConPES based on Integer32"""
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


_VidpreVITConPES_Type.__name__ = "Integer32"
_VidpreVITConPES_Object = MibTableColumn
vidpreVITConPES = _VidpreVITConPES_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 31),
    _VidpreVITConPES_Type()
)
vidpreVITConPES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreVITConPES.setStatus("current")


class _VidpreE5EstimatedBitRate_Type(Integer32):
    """Custom type vidpreE5EstimatedBitRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000000),
    )


_VidpreE5EstimatedBitRate_Type.__name__ = "Integer32"
_VidpreE5EstimatedBitRate_Object = MibTableColumn
vidpreE5EstimatedBitRate = _VidpreE5EstimatedBitRate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 7, 1, 32),
    _VidpreE5EstimatedBitRate_Type()
)
vidpreE5EstimatedBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidpreE5EstimatedBitRate.setStatus("current")
_VbiTable_Object = MibTable
vbiTable = _VbiTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 8)
)
if mibBuilder.loadTexts:
    vbiTable.setStatus("current")
_VbiEntry_Object = MibTableRow
vbiEntry = _VbiEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 8, 1)
)
vbiEntry.setIndexNames(
    (0, "NDS-DTH3-PREPROCESSOR", "vbiCurrentNextIndex"),
    (0, "NDS-DTH3-PREPROCESSOR", "vbiLineIndex"),
)
if mibBuilder.loadTexts:
    vbiEntry.setStatus("current")


class _VbiCurrentNextIndex_Type(Integer32):
    """Custom type vbiCurrentNextIndex based on Integer32"""
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


_VbiCurrentNextIndex_Type.__name__ = "Integer32"
_VbiCurrentNextIndex_Object = MibTableColumn
vbiCurrentNextIndex = _VbiCurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 8, 1, 1),
    _VbiCurrentNextIndex_Type()
)
vbiCurrentNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vbiCurrentNextIndex.setStatus("current")


class _VbiLineIndex_Type(Integer32):
    """Custom type vbiLineIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(6, 335),
    )


_VbiLineIndex_Type.__name__ = "Integer32"
_VbiLineIndex_Object = MibTableColumn
vbiLineIndex = _VbiLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 8, 1, 2),
    _VbiLineIndex_Type()
)
vbiLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vbiLineIndex.setStatus("current")


class _VbiCode_Type(Integer32):
    """Custom type vbiCode based on Integer32"""
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
        *(("off", 0),
          ("closedCaption", 1),
          ("nielsenAMOLI", 2),
          ("nielsenAMOLII", 3),
          ("vPS", 4),
          ("wSS", 5),
          ("vITC-SMPTE", 6),
          ("vITC-EBU", 7),
          ("pDC-Packet", 8),
          ("iDS-EBU", 9),
          ("teletextB", 10),
          ("monochrome422", 11),
          ("videoIndex", 12),
          ("reserved2", 13),
          ("invertedTeletext", 14),
          ("serialRS232ClosedCaptions", 15),
          ("wSS-AFD", 16),
          ("gemstar2x", 17),
          ("nABTS", 18))
    )


_VbiCode_Type.__name__ = "Integer32"
_VbiCode_Object = MibTableColumn
vbiCode = _VbiCode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 8, 1, 3),
    _VbiCode_Type()
)
vbiCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vbiCode.setStatus("current")
_TeletextTable_Object = MibTable
teletextTable = _TeletextTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 9)
)
if mibBuilder.loadTexts:
    teletextTable.setStatus("current")
_TeletextEntry_Object = MibTableRow
teletextEntry = _TeletextEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 9, 1)
)
teletextEntry.setIndexNames(
    (0, "NDS-DTH3-PREPROCESSOR", "teletextCurrentNextIndex"),
)
if mibBuilder.loadTexts:
    teletextEntry.setStatus("current")


class _TeletextCurrentNextIndex_Type(Integer32):
    """Custom type teletextCurrentNextIndex based on Integer32"""
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


_TeletextCurrentNextIndex_Type.__name__ = "Integer32"
_TeletextCurrentNextIndex_Object = MibTableColumn
teletextCurrentNextIndex = _TeletextCurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 9, 1, 1),
    _TeletextCurrentNextIndex_Type()
)
teletextCurrentNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    teletextCurrentNextIndex.setStatus("current")


class _TeletextEncode_Type(Integer32):
    """Custom type teletextEncode based on Integer32"""
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


_TeletextEncode_Type.__name__ = "Integer32"
_TeletextEncode_Object = MibTableColumn
teletextEncode = _TeletextEncode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 9, 1, 2),
    _TeletextEncode_Type()
)
teletextEncode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teletextEncode.setStatus("current")


class _TeletextPID_Type(Integer32):
    """Custom type teletextPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_TeletextPID_Type.__name__ = "Integer32"
_TeletextPID_Object = MibTableColumn
teletextPID = _TeletextPID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 9, 1, 3),
    _TeletextPID_Type()
)
teletextPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teletextPID.setStatus("current")


class _TeletextDelay_Type(Integer32):
    """Custom type teletextDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3630),
    )


_TeletextDelay_Type.__name__ = "Integer32"
_TeletextDelay_Object = MibTableColumn
teletextDelay = _TeletextDelay_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 9, 1, 4),
    _TeletextDelay_Type()
)
teletextDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teletextDelay.setStatus("current")


class _TeletextSync_Type(Integer32):
    """Custom type teletextSync based on Integer32"""
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


_TeletextSync_Type.__name__ = "Integer32"
_TeletextSync_Object = MibTableColumn
teletextSync = _TeletextSync_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 9, 1, 5),
    _TeletextSync_Type()
)
teletextSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teletextSync.setStatus("current")


class _TeletextComponentTag_Type(Integer32):
    """Custom type teletextComponentTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_TeletextComponentTag_Type.__name__ = "Integer32"
_TeletextComponentTag_Object = MibTableColumn
teletextComponentTag = _TeletextComponentTag_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 9, 1, 6),
    _TeletextComponentTag_Type()
)
teletextComponentTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teletextComponentTag.setStatus("current")


class _TeletextMinNoPackets_Type(Integer32):
    """Custom type teletextMinNoPackets based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_TeletextMinNoPackets_Type.__name__ = "Integer32"
_TeletextMinNoPackets_Object = MibTableColumn
teletextMinNoPackets = _TeletextMinNoPackets_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 9, 1, 7),
    _TeletextMinNoPackets_Type()
)
teletextMinNoPackets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    teletextMinNoPackets.setStatus("current")


class _VidpreTextColour_Type(Integer32):
    """Custom type vidpreTextColour based on Integer32"""
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
        *(("black", 0),
          ("blue", 1),
          ("red", 2),
          ("magenta", 3),
          ("green", 4),
          ("cyan", 5),
          ("orange", 6),
          ("yellow", 7),
          ("grey", 8),
          ("white", 9),
          ("pink", 10))
    )


_VidpreTextColour_Type.__name__ = "Integer32"
_VidpreTextColour_Object = MibScalar
vidpreTextColour = _VidpreTextColour_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 10),
    _VidpreTextColour_Type()
)
vidpreTextColour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreTextColour.setStatus("current")


class _VidpreTextBackground_Type(Integer32):
    """Custom type vidpreTextBackground based on Integer32"""
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
        *(("black", 0),
          ("blue", 1),
          ("red", 2),
          ("magenta", 3),
          ("green", 4),
          ("cyan", 5),
          ("orange", 6),
          ("yellow", 7),
          ("grey", 8),
          ("white", 9),
          ("pink", 10))
    )


_VidpreTextBackground_Type.__name__ = "Integer32"
_VidpreTextBackground_Object = MibScalar
vidpreTextBackground = _VidpreTextBackground_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 11),
    _VidpreTextBackground_Type()
)
vidpreTextBackground.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreTextBackground.setStatus("current")
_VbiPIDTable_Object = MibTable
vbiPIDTable = _VbiPIDTable_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 12)
)
if mibBuilder.loadTexts:
    vbiPIDTable.setStatus("current")
_VbiPIDEntry_Object = MibTableRow
vbiPIDEntry = _VbiPIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 12, 1)
)
vbiPIDEntry.setIndexNames(
    (0, "NDS-DTH3-PREPROCESSOR", "vbiPIDCurrentNextIndex"),
)
if mibBuilder.loadTexts:
    vbiPIDEntry.setStatus("current")


class _VbiPIDCurrentNextIndex_Type(Integer32):
    """Custom type vbiPIDCurrentNextIndex based on Integer32"""
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


_VbiPIDCurrentNextIndex_Type.__name__ = "Integer32"
_VbiPIDCurrentNextIndex_Object = MibTableColumn
vbiPIDCurrentNextIndex = _VbiPIDCurrentNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 12, 1, 1),
    _VbiPIDCurrentNextIndex_Type()
)
vbiPIDCurrentNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vbiPIDCurrentNextIndex.setStatus("current")


class _VbiEncode_Type(Integer32):
    """Custom type vbiEncode based on Integer32"""
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


_VbiEncode_Type.__name__ = "Integer32"
_VbiEncode_Object = MibTableColumn
vbiEncode = _VbiEncode_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 12, 1, 2),
    _VbiEncode_Type()
)
vbiEncode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vbiEncode.setStatus("current")


class _VbiPID_Type(Integer32):
    """Custom type vbiPID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_VbiPID_Type.__name__ = "Integer32"
_VbiPID_Object = MibTableColumn
vbiPID = _VbiPID_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 12, 1, 3),
    _VbiPID_Type()
)
vbiPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vbiPID.setStatus("current")


class _VbiComponentTag_Type(Integer32):
    """Custom type vbiComponentTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VbiComponentTag_Type.__name__ = "Integer32"
_VbiComponentTag_Object = MibTableColumn
vbiComponentTag = _VbiComponentTag_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 12, 1, 4),
    _VbiComponentTag_Type()
)
vbiComponentTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vbiComponentTag.setStatus("current")


class _VidpreSyncSource_Type(Integer32):
    """Custom type vidpreSyncSource based on Integer32"""
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
        *(("internal", 0),
          ("external", 1),
          ("internal-video", 2),
          ("internal-local", 3))
    )


_VidpreSyncSource_Type.__name__ = "Integer32"
_VidpreSyncSource_Object = MibScalar
vidpreSyncSource = _VidpreSyncSource_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 13),
    _VidpreSyncSource_Type()
)
vidpreSyncSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreSyncSource.setStatus("current")


class _VidpreSyncTermination_Type(Integer32):
    """Custom type vidpreSyncTermination based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("termination-75-Ohms", 0),
          ("high-impedance", 1))
    )


_VidpreSyncTermination_Type.__name__ = "Integer32"
_VidpreSyncTermination_Object = MibScalar
vidpreSyncTermination = _VidpreSyncTermination_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 14),
    _VidpreSyncTermination_Type()
)
vidpreSyncTermination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreSyncTermination.setStatus("current")


class _VidprePalPlusDetect_Type(Integer32):
    """Custom type vidprePalPlusDetect based on Integer32"""
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


_VidprePalPlusDetect_Type.__name__ = "Integer32"
_VidprePalPlusDetect_Object = MibScalar
vidprePalPlusDetect = _VidprePalPlusDetect_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 15),
    _VidprePalPlusDetect_Type()
)
vidprePalPlusDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidprePalPlusDetect.setStatus("current")


class _VidprePanScanDetect_Type(Integer32):
    """Custom type vidprePanScanDetect based on Integer32"""
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


_VidprePanScanDetect_Type.__name__ = "Integer32"
_VidprePanScanDetect_Object = MibScalar
vidprePanScanDetect = _VidprePanScanDetect_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 16),
    _VidprePanScanDetect_Type()
)
vidprePanScanDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidprePanScanDetect.setStatus("current")


class _VidpreVITCDetect_Type(Integer32):
    """Custom type vidpreVITCDetect based on Integer32"""
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


_VidpreVITCDetect_Type.__name__ = "Integer32"
_VidpreVITCDetect_Object = MibScalar
vidpreVITCDetect = _VidpreVITCDetect_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 17),
    _VidpreVITCDetect_Type()
)
vidpreVITCDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidpreVITCDetect.setStatus("current")


class _VidpreOSDDebug_Type(Integer32):
    """Custom type vidpreOSDDebug based on Integer32"""
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("release", 1),
          ("fpga-version", 2),
          ("video-input", 3),
          ("audio-DIDs", 4),
          ("time-code", 5),
          ("field-count", 6),
          ("noise-reduction", 7),
          ("edh-status", 8),
          ("font", 9),
          ("video", 10),
          ("i-frame-detection", 11),
          ("splice-point", 12),
          ("reflex", 13),
          ("reflex-bit-rate", 14),
          ("osd-space", 15),
          ("full-screen-translucent", 16),
          ("full-screen-opaque", 17),
          ("wss-data", 18),
          ("serial-cc-codes", 19),
          ("splice-scte-35", 20),
          ("skyPerfect-Closed-Captions", 21),
          ("pcr-and-milliseconds-avc-encoding", 22))
    )


_VidpreOSDDebug_Type.__name__ = "Integer32"
_VidpreOSDDebug_Object = MibScalar
vidpreOSDDebug = _VidpreOSDDebug_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 18),
    _VidpreOSDDebug_Type()
)
vidpreOSDDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreOSDDebug.setStatus("current")


class _VidpreVideoCalibration_Type(OctetString):
    """Custom type vidpreVideoCalibration based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_VidpreVideoCalibration_Type.__name__ = "OctetString"
_VidpreVideoCalibration_Object = MibScalar
vidpreVideoCalibration = _VidpreVideoCalibration_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 19),
    _VidpreVideoCalibration_Type()
)
vidpreVideoCalibration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreVideoCalibration.setStatus("current")


class _VidpreVideoCalibrate_Type(Integer32):
    """Custom type vidpreVideoCalibrate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal-operation", 0),
          ("calibratePAL", 1),
          ("calibrateNTSC", 2))
    )


_VidpreVideoCalibrate_Type.__name__ = "Integer32"
_VidpreVideoCalibrate_Object = MibScalar
vidpreVideoCalibrate = _VidpreVideoCalibrate_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 20),
    _VidpreVideoCalibrate_Type()
)
vidpreVideoCalibrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreVideoCalibrate.setStatus("current")


class _VidpreVideoCalibrateStatus_Type(Integer32):
    """Custom type vidpreVideoCalibrateStatus based on Integer32"""
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
        *(("normal-operation", 0),
          ("calibrating-PAL", 1),
          ("pass-PAL-setup-NTSC", 2),
          ("calibrating-NTSC", 3),
          ("pass-PAL-and-NTSC", 4),
          ("fail-PAL", 5),
          ("fail-NTSC", 6))
    )


_VidpreVideoCalibrateStatus_Type.__name__ = "Integer32"
_VidpreVideoCalibrateStatus_Object = MibScalar
vidpreVideoCalibrateStatus = _VidpreVideoCalibrateStatus_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 21),
    _VidpreVideoCalibrateStatus_Type()
)
vidpreVideoCalibrateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidpreVideoCalibrateStatus.setStatus("current")


class _VidpreFrameResynchroniserDelay_Type(Integer32):
    """Custom type vidpreFrameResynchroniserDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_VidpreFrameResynchroniserDelay_Type.__name__ = "Integer32"
_VidpreFrameResynchroniserDelay_Object = MibScalar
vidpreFrameResynchroniserDelay = _VidpreFrameResynchroniserDelay_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 22),
    _VidpreFrameResynchroniserDelay_Type()
)
vidpreFrameResynchroniserDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vidpreFrameResynchroniserDelay.setStatus("current")


class _VidpreVideoInputSelect_Type(Integer32):
    """Custom type vidpreVideoInputSelect based on Integer32"""
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
        *(("manual", 0),
          ("auto-frame-rate", 1),
          ("auto-input", 2),
          ("auto-config-select", 3))
    )


_VidpreVideoInputSelect_Type.__name__ = "Integer32"
_VidpreVideoInputSelect_Object = MibScalar
vidpreVideoInputSelect = _VidpreVideoInputSelect_Object(
    (1, 3, 6, 1, 4, 1, 1855, 2, 2, 3, 23),
    _VidpreVideoInputSelect_Type()
)
vidpreVideoInputSelect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vidpreVideoInputSelect.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NDS-DTH3-PREPROCESSOR",
    **{"ndsDTH3Encoder": ndsDTH3Encoder,
       "vidpreEnc": vidpreEnc,
       "vidpreHardwareRelease": vidpreHardwareRelease,
       "vidpreSoftwareRelease": vidpreSoftwareRelease,
       "vidpreFirmwareRelease": vidpreFirmwareRelease,
       "vidpreNoEmbAudDIDExtractors": vidpreNoEmbAudDIDExtractors,
       "vidprenextTimeDate": vidprenextTimeDate,
       "vidpreTimeCode": vidpreTimeCode,
       "vidpreTable": vidpreTable,
       "vidpreEntry": vidpreEntry,
       "vidpreCurrentNextIndex": vidpreCurrentNextIndex,
       "vidpreSource": vidpreSource,
       "vidpreOPVideoLoss": vidpreOPVideoLoss,
       "vidpreNoiseReduction": vidpreNoiseReduction,
       "vidpreFrameSync": vidpreFrameSync,
       "vidpreEmbAudioSource1": vidpreEmbAudioSource1,
       "vidpreEmbAudioSource2": vidpreEmbAudioSource2,
       "vidpreEmbAudioSource3": vidpreEmbAudioSource3,
       "vidpreEmbAudioSource4": vidpreEmbAudioSource4,
       "vidpreLogo": vidpreLogo,
       "vidpreVertRes": vidpreVertRes,
       "vidpreFrameRate": vidpreFrameRate,
       "vidpreProgressive": vidpreProgressive,
       "vidpreHorRes": vidpreHorRes,
       "vidpreEmbeddedAudInput": vidpreEmbeddedAudInput,
       "vidprePALPlusEnable": vidprePALPlusEnable,
       "vidpreAutoVITCDetect": vidpreAutoVITCDetect,
       "vidpreVBIField1": vidpreVBIField1,
       "vidpreVBIField2": vidpreVBIField2,
       "vidpreClosedCaptions": vidpreClosedCaptions,
       "vidpreCCDescriptor": vidpreCCDescriptor,
       "vidpreBlankLine23": vidpreBlankLine23,
       "vidpreCCPenSize": vidpreCCPenSize,
       "vidpreCCFont": vidpreCCFont,
       "vidpreCCForeground": vidpreCCForeground,
       "vidpreCCBackground": vidpreCCBackground,
       "vidpreStillFrameTrigger": vidpreStillFrameTrigger,
       "vidpreStillFrameSensitivity": vidpreStillFrameSensitivity,
       "vidprePredictiveProcessing": vidprePredictiveProcessing,
       "vidpreMotionCompensatedNoiseReduction": vidpreMotionCompensatedNoiseReduction,
       "vidpreVITConPES": vidpreVITConPES,
       "vidpreE5EstimatedBitRate": vidpreE5EstimatedBitRate,
       "vbiTable": vbiTable,
       "vbiEntry": vbiEntry,
       "vbiCurrentNextIndex": vbiCurrentNextIndex,
       "vbiLineIndex": vbiLineIndex,
       "vbiCode": vbiCode,
       "teletextTable": teletextTable,
       "teletextEntry": teletextEntry,
       "teletextCurrentNextIndex": teletextCurrentNextIndex,
       "teletextEncode": teletextEncode,
       "teletextPID": teletextPID,
       "teletextDelay": teletextDelay,
       "teletextSync": teletextSync,
       "teletextComponentTag": teletextComponentTag,
       "teletextMinNoPackets": teletextMinNoPackets,
       "vidpreTextColour": vidpreTextColour,
       "vidpreTextBackground": vidpreTextBackground,
       "vbiPIDTable": vbiPIDTable,
       "vbiPIDEntry": vbiPIDEntry,
       "vbiPIDCurrentNextIndex": vbiPIDCurrentNextIndex,
       "vbiEncode": vbiEncode,
       "vbiPID": vbiPID,
       "vbiComponentTag": vbiComponentTag,
       "vidpreSyncSource": vidpreSyncSource,
       "vidpreSyncTermination": vidpreSyncTermination,
       "vidprePalPlusDetect": vidprePalPlusDetect,
       "vidprePanScanDetect": vidprePanScanDetect,
       "vidpreVITCDetect": vidpreVITCDetect,
       "vidpreOSDDebug": vidpreOSDDebug,
       "vidpreVideoCalibration": vidpreVideoCalibration,
       "vidpreVideoCalibrate": vidpreVideoCalibrate,
       "vidpreVideoCalibrateStatus": vidpreVideoCalibrateStatus,
       "vidpreFrameResynchroniserDelay": vidpreFrameResynchroniserDelay,
       "vidpreVideoInputSelect": vidpreVideoInputSelect}
)
