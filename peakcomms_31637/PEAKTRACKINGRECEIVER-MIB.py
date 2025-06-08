# SNMP MIB module (PEAKTRACKINGRECEIVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKTRACKINGRECEIVER-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:49:02 2025
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

(OnOffType,
 converters) = mibBuilder.importSymbols(
    "PEAKDEFINITIONS-MIB",
    "OnOffType",
    "converters")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

peakTrackingReceiverModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7)
)
if mibBuilder.loadTexts:
    peakTrackingReceiverModule.setRevisions(
        ("2016-06-20 09:00",
         "2016-03-03 10:00",
         "2015-09-15 10:00",
         "2015-02-18 12:00",
         "2013-05-21 12:00",
         "2013-04-04 12:00",
         "2012-12-18 09:00",
         "2011-06-03 12:00",
         "2011-05-05 12:00",
         "2010-12-15 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class BWResolutionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bw1kHz", 1),
          ("bw6kHz", 2))
    )



class SweepRateType(TextualConvention, Integer32):
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("sr2o5kHzPerS", 1),
          ("sr5kHzPerS", 2),
          ("sr10kHzPerS", 3),
          ("sr20kHzPerS", 4),
          ("sr40kHzPerS", 5),
          ("sr80kHzPerS", 6),
          ("sr120kHzPerS", 7),
          ("sr240kHzPerS", 8))
    )



class SweepWidthType(TextualConvention, Integer32):
    status = "current"
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
        *(("sr20kHz", 1),
          ("sr50kHz", 2),
          ("sr100kHz", 3),
          ("sr200kHz", 4),
          ("sr500kHz", 5))
    )



class DBVoltType(TextualConvention, Integer32):
    status = "current"
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
        *(("db0o5", 1),
          ("db1", 2),
          ("db2", 3),
          ("db5", 4),
          ("db10", 5))
    )



# MIB Managed Objects in the order of their OIDs

_TrackRTable_Object = MibTable
trackRTable = _TrackRTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    trackRTable.setStatus("current")
_TrackRTableEntry_Object = MibTableRow
trackRTableEntry = _TrackRTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1, 1)
)
trackRTableEntry.setIndexNames(
    (0, "PEAKTRACKINGRECEIVER-MIB", "trackRIndex"),
)
if mibBuilder.loadTexts:
    trackRTableEntry.setStatus("current")


class _TrackRIndex_Type(Integer32):
    """Custom type trackRIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TrackRIndex_Type.__name__ = "Integer32"
_TrackRIndex_Object = MibTableColumn
trackRIndex = _TrackRIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1, 1, 1),
    _TrackRIndex_Type()
)
trackRIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trackRIndex.setStatus("current")
_TrackRCentreFrequency_Type = OctetString
_TrackRCentreFrequency_Object = MibTableColumn
trackRCentreFrequency = _TrackRCentreFrequency_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1, 1, 2),
    _TrackRCentreFrequency_Type()
)
trackRCentreFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trackRCentreFrequency.setStatus("current")
_TrackRSpan_Type = OctetString
_TrackRSpan_Object = MibTableColumn
trackRSpan = _TrackRSpan_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1, 1, 3),
    _TrackRSpan_Type()
)
trackRSpan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trackRSpan.setStatus("current")
_TrackRRefLevel_Type = Integer32
_TrackRRefLevel_Object = MibTableColumn
trackRRefLevel = _TrackRRefLevel_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1, 1, 4),
    _TrackRRefLevel_Type()
)
trackRRefLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trackRRefLevel.setStatus("current")
_TrackRBWResolution_Type = BWResolutionType
_TrackRBWResolution_Object = MibTableColumn
trackRBWResolution = _TrackRBWResolution_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1, 1, 5),
    _TrackRBWResolution_Type()
)
trackRBWResolution.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trackRBWResolution.setStatus("deprecated")
_TrackRPad10dB_Type = OnOffType
_TrackRPad10dB_Object = MibTableColumn
trackRPad10dB = _TrackRPad10dB_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1, 1, 6),
    _TrackRPad10dB_Type()
)
trackRPad10dB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trackRPad10dB.setStatus("current")
_TrackRSweepRate_Type = SweepRateType
_TrackRSweepRate_Object = MibTableColumn
trackRSweepRate = _TrackRSweepRate_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1, 1, 7),
    _TrackRSweepRate_Type()
)
trackRSweepRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trackRSweepRate.setStatus("current")
_TrackRSweepWidth_Type = SweepWidthType
_TrackRSweepWidth_Object = MibTableColumn
trackRSweepWidth = _TrackRSweepWidth_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1, 1, 8),
    _TrackRSweepWidth_Type()
)
trackRSweepWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trackRSweepWidth.setStatus("current")
_TrackRLogdBVolt_Type = DBVoltType
_TrackRLogdBVolt_Object = MibTableColumn
trackRLogdBVolt = _TrackRLogdBVolt_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1, 1, 9),
    _TrackRLogdBVolt_Type()
)
trackRLogdBVolt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trackRLogdBVolt.setStatus("current")


class _TrackRLogOffset_Type(Integer32):
    """Custom type trackRLogOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_TrackRLogOffset_Type.__name__ = "Integer32"
_TrackRLogOffset_Object = MibTableColumn
trackRLogOffset = _TrackRLogOffset_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1, 1, 10),
    _TrackRLogOffset_Type()
)
trackRLogOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trackRLogOffset.setStatus("current")
_TrackRASB_Type = OnOffType
_TrackRASB_Object = MibTableColumn
trackRASB = _TrackRASB_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1, 1, 11),
    _TrackRASB_Type()
)
trackRASB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trackRASB.setStatus("current")
_TrackRDCOutput_Type = OctetString
_TrackRDCOutput_Object = MibTableColumn
trackRDCOutput = _TrackRDCOutput_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1, 1, 12),
    _TrackRDCOutput_Type()
)
trackRDCOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trackRDCOutput.setStatus("current")
_TrackRRxLevel_Type = OctetString
_TrackRRxLevel_Object = MibTableColumn
trackRRxLevel = _TrackRRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1, 1, 13),
    _TrackRRxLevel_Type()
)
trackRRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trackRRxLevel.setStatus("current")
_TrackRFrequency_Type = OctetString
_TrackRFrequency_Object = MibTableColumn
trackRFrequency = _TrackRFrequency_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1, 1, 14),
    _TrackRFrequency_Type()
)
trackRFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trackRFrequency.setStatus("current")
_TrackRGain_Type = OctetString
_TrackRGain_Object = MibTableColumn
trackRGain = _TrackRGain_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1, 1, 15),
    _TrackRGain_Type()
)
trackRGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trackRGain.setStatus("current")
_TrackR10MHz_Type = OnOffType
_TrackR10MHz_Object = MibTableColumn
trackR10MHz = _TrackR10MHz_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1, 1, 16),
    _TrackR10MHz_Type()
)
trackR10MHz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trackR10MHz.setStatus("current")
_TrackRDCFeed_Type = OnOffType
_TrackRDCFeed_Object = MibTableColumn
trackRDCFeed = _TrackRDCFeed_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1, 1, 17),
    _TrackRDCFeed_Type()
)
trackRDCFeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trackRDCFeed.setStatus("current")
_TrackRSHFOnOff_Type = OnOffType
_TrackRSHFOnOff_Object = MibTableColumn
trackRSHFOnOff = _TrackRSHFOnOff_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1, 1, 18),
    _TrackRSHFOnOff_Type()
)
trackRSHFOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trackRSHFOnOff.setStatus("current")
_TrackRSHFFrequency_Type = OctetString
_TrackRSHFFrequency_Object = MibTableColumn
trackRSHFFrequency = _TrackRSHFFrequency_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1, 1, 19),
    _TrackRSHFFrequency_Type()
)
trackRSHFFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trackRSHFFrequency.setStatus("current")
_TrackRSHFSpectrumInvert_Type = OnOffType
_TrackRSHFSpectrumInvert_Object = MibTableColumn
trackRSHFSpectrumInvert = _TrackRSHFSpectrumInvert_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1, 1, 20),
    _TrackRSHFSpectrumInvert_Type()
)
trackRSHFSpectrumInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trackRSHFSpectrumInvert.setStatus("current")
_TrackRAttenuation_Type = OctetString
_TrackRAttenuation_Object = MibTableColumn
trackRAttenuation = _TrackRAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1, 1, 21),
    _TrackRAttenuation_Type()
)
trackRAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trackRAttenuation.setStatus("current")
_TrackRFirstIFAttenuation_Type = OctetString
_TrackRFirstIFAttenuation_Object = MibTableColumn
trackRFirstIFAttenuation = _TrackRFirstIFAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1, 1, 22),
    _TrackRFirstIFAttenuation_Type()
)
trackRFirstIFAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trackRFirstIFAttenuation.setStatus("current")
_TrackRKuAttenuation_Type = OctetString
_TrackRKuAttenuation_Object = MibTableColumn
trackRKuAttenuation = _TrackRKuAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1, 1, 23),
    _TrackRKuAttenuation_Type()
)
trackRKuAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trackRKuAttenuation.setStatus("current")
_TrackRIfCompositePower_Type = OctetString
_TrackRIfCompositePower_Object = MibTableColumn
trackRIfCompositePower = _TrackRIfCompositePower_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1, 1, 24),
    _TrackRIfCompositePower_Type()
)
trackRIfCompositePower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trackRIfCompositePower.setStatus("current")
_TrackRLAttenuation_Type = OctetString
_TrackRLAttenuation_Object = MibTableColumn
trackRLAttenuation = _TrackRLAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1, 1, 25),
    _TrackRLAttenuation_Type()
)
trackRLAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trackRLAttenuation.setStatus("current")
_TrackROKSince_Type = OctetString
_TrackROKSince_Object = MibTableColumn
trackROKSince = _TrackROKSince_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 1, 1, 100),
    _TrackROKSince_Type()
)
trackROKSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trackROKSince.setStatus("current")
_TrackRecIntegers_ObjectIdentity = ObjectIdentity
trackRecIntegers = _TrackRecIntegers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 9)
)
_TrackRITable_Object = MibTable
trackRITable = _TrackRITable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 9, 1)
)
if mibBuilder.loadTexts:
    trackRITable.setStatus("current")
_TrackRITableEntry_Object = MibTableRow
trackRITableEntry = _TrackRITableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 9, 1, 1)
)
trackRITableEntry.setIndexNames(
    (0, "PEAKTRACKINGRECEIVER-MIB", "trackRIIndex"),
)
if mibBuilder.loadTexts:
    trackRITableEntry.setStatus("current")


class _TrackRIIndex_Type(Integer32):
    """Custom type trackRIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TrackRIIndex_Type.__name__ = "Integer32"
_TrackRIIndex_Object = MibTableColumn
trackRIIndex = _TrackRIIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 9, 1, 1, 1),
    _TrackRIIndex_Type()
)
trackRIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trackRIIndex.setStatus("current")
_TrackRIDCOutput_Type = Integer32
_TrackRIDCOutput_Object = MibTableColumn
trackRIDCOutput = _TrackRIDCOutput_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 9, 1, 1, 2),
    _TrackRIDCOutput_Type()
)
trackRIDCOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trackRIDCOutput.setStatus("current")
_TrackRIRxLevel_Type = Integer32
_TrackRIRxLevel_Object = MibTableColumn
trackRIRxLevel = _TrackRIRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 9, 1, 1, 3),
    _TrackRIRxLevel_Type()
)
trackRIRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trackRIRxLevel.setStatus("current")
_TrackRecGroups_ObjectIdentity = ObjectIdentity
trackRecGroups = _TrackRecGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 10)
)
_TrackRecConformance_ObjectIdentity = ObjectIdentity
trackRecConformance = _TrackRecConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 11)
)

# Managed Objects groups

trackCNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 10, 1)
)
trackCNFReqGrp.setObjects(
      *(("PEAKTRACKINGRECEIVER-MIB", "trackRCentreFrequency"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackRSpan"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackRRefLevel"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackRPad10dB"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackRSweepRate"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackRLogdBVolt"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackRLogOffset"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackRASB"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackRDCOutput"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackRSweepWidth"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackRRxLevel"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackRFrequency"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackRGain"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackROKSince"))
)
if mibBuilder.loadTexts:
    trackCNFReqGrp.setStatus("current")

trackCNF10MHzGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 10, 2)
)
trackCNF10MHzGrp.setObjects(
    ("PEAKTRACKINGRECEIVER-MIB", "trackR10MHz")
)
if mibBuilder.loadTexts:
    trackCNF10MHzGrp.setStatus("current")

trackCNFDCFeedGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 10, 3)
)
trackCNFDCFeedGrp.setObjects(
    ("PEAKTRACKINGRECEIVER-MIB", "trackRDCFeed")
)
if mibBuilder.loadTexts:
    trackCNFDCFeedGrp.setStatus("current")

trackCNFSHFGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 10, 4)
)
trackCNFSHFGrp.setObjects(
      *(("PEAKTRACKINGRECEIVER-MIB", "trackRSHFOnOff"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackRSHFFrequency"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackRSHFSpectrumInvert"))
)
if mibBuilder.loadTexts:
    trackCNFSHFGrp.setStatus("current")

trackICNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 10, 5)
)
trackICNFReqGrp.setObjects(
      *(("PEAKTRACKINGRECEIVER-MIB", "trackRIDCOutput"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackRIRxLevel"))
)
if mibBuilder.loadTexts:
    trackICNFReqGrp.setStatus("current")

trackRemoteCNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 10, 6)
)
trackRemoteCNFReqGrp.setObjects(
      *(("PEAKTRACKINGRECEIVER-MIB", "trackRSweepRate"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackRSweepWidth"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackRLogdBVolt"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackRLogOffset"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackRASB"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackRDCOutput"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackRRxLevel"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackRFrequency"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackRAttenuation"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackRFirstIFAttenuation"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackROKSince"))
)
if mibBuilder.loadTexts:
    trackRemoteCNFReqGrp.setStatus("current")

trackCNFKuAttenuationGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 10, 7)
)
trackCNFKuAttenuationGrp.setObjects(
      *(("PEAKTRACKINGRECEIVER-MIB", "trackRKuAttenuation"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackRIfCompositePower"))
)
if mibBuilder.loadTexts:
    trackCNFKuAttenuationGrp.setStatus("current")

trackCNFLAttenuationGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 10, 8)
)
trackCNFLAttenuationGrp.setObjects(
    ("PEAKTRACKINGRECEIVER-MIB", "trackRLAttenuation")
)
if mibBuilder.loadTexts:
    trackCNFLAttenuationGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

trackCNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 11, 1)
)
trackCNFCompliance.setObjects(
      *(("PEAKTRACKINGRECEIVER-MIB", "trackCNFReqGrp"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackICNFReqGrp"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackCNF10MHzGrp"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackCNFDCFeedGrp"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackCNFSHFGrp"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackCNFKuAttenuationGrp"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackCNFLAttenuationGrp"))
)
if mibBuilder.loadTexts:
    trackCNFCompliance.setStatus(
        "current"
    )

trackRemoteCNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 7, 11, 2)
)
trackRemoteCNFCompliance.setObjects(
      *(("PEAKTRACKINGRECEIVER-MIB", "trackRemoteCNFReqGrp"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackICNFReqGrp"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackCNFDCFeedGrp"),
        ("PEAKTRACKINGRECEIVER-MIB", "trackCNFSHFGrp"))
)
if mibBuilder.loadTexts:
    trackRemoteCNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKTRACKINGRECEIVER-MIB",
    **{"BWResolutionType": BWResolutionType,
       "SweepRateType": SweepRateType,
       "SweepWidthType": SweepWidthType,
       "DBVoltType": DBVoltType,
       "peakTrackingReceiverModule": peakTrackingReceiverModule,
       "trackRTable": trackRTable,
       "trackRTableEntry": trackRTableEntry,
       "trackRIndex": trackRIndex,
       "trackRCentreFrequency": trackRCentreFrequency,
       "trackRSpan": trackRSpan,
       "trackRRefLevel": trackRRefLevel,
       "trackRBWResolution": trackRBWResolution,
       "trackRPad10dB": trackRPad10dB,
       "trackRSweepRate": trackRSweepRate,
       "trackRSweepWidth": trackRSweepWidth,
       "trackRLogdBVolt": trackRLogdBVolt,
       "trackRLogOffset": trackRLogOffset,
       "trackRASB": trackRASB,
       "trackRDCOutput": trackRDCOutput,
       "trackRRxLevel": trackRRxLevel,
       "trackRFrequency": trackRFrequency,
       "trackRGain": trackRGain,
       "trackR10MHz": trackR10MHz,
       "trackRDCFeed": trackRDCFeed,
       "trackRSHFOnOff": trackRSHFOnOff,
       "trackRSHFFrequency": trackRSHFFrequency,
       "trackRSHFSpectrumInvert": trackRSHFSpectrumInvert,
       "trackRAttenuation": trackRAttenuation,
       "trackRFirstIFAttenuation": trackRFirstIFAttenuation,
       "trackRKuAttenuation": trackRKuAttenuation,
       "trackRIfCompositePower": trackRIfCompositePower,
       "trackRLAttenuation": trackRLAttenuation,
       "trackROKSince": trackROKSince,
       "trackRecIntegers": trackRecIntegers,
       "trackRITable": trackRITable,
       "trackRITableEntry": trackRITableEntry,
       "trackRIIndex": trackRIIndex,
       "trackRIDCOutput": trackRIDCOutput,
       "trackRIRxLevel": trackRIRxLevel,
       "trackRecGroups": trackRecGroups,
       "trackCNFReqGrp": trackCNFReqGrp,
       "trackCNF10MHzGrp": trackCNF10MHzGrp,
       "trackCNFDCFeedGrp": trackCNFDCFeedGrp,
       "trackCNFSHFGrp": trackCNFSHFGrp,
       "trackICNFReqGrp": trackICNFReqGrp,
       "trackRemoteCNFReqGrp": trackRemoteCNFReqGrp,
       "trackCNFKuAttenuationGrp": trackCNFKuAttenuationGrp,
       "trackCNFLAttenuationGrp": trackCNFLAttenuationGrp,
       "trackRecConformance": trackRecConformance,
       "trackCNFCompliance": trackCNFCompliance,
       "trackRemoteCNFCompliance": trackRemoteCNFCompliance}
)
