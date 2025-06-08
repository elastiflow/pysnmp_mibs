# SNMP MIB module (PEAKREMOTETRACKINGRECEIVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKREMOTETRACKINGRECEIVER-MIB.mib
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

peakRemoteTrackingReceiverModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16)
)
if mibBuilder.loadTexts:
    peakRemoteTrackingReceiverModule.setRevisions(
        ("2016-03-02 10:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RemoteSweepRateType(TextualConvention, Integer32):
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



class RemoteSweepWidthType(TextualConvention, Integer32):
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



class RemoteDBVoltType(TextualConvention, Integer32):
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

_RemoteTrackRTable_Object = MibTable
remoteTrackRTable = _RemoteTrackRTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 1)
)
if mibBuilder.loadTexts:
    remoteTrackRTable.setStatus("current")
_RemoteTrackRTableEntry_Object = MibTableRow
remoteTrackRTableEntry = _RemoteTrackRTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 1, 1)
)
remoteTrackRTableEntry.setIndexNames(
    (0, "PEAKREMOTETRACKINGRECEIVER-MIB", "remoteTrackRIndex"),
)
if mibBuilder.loadTexts:
    remoteTrackRTableEntry.setStatus("current")


class _RemoteTrackRIndex_Type(Integer32):
    """Custom type remoteTrackRIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RemoteTrackRIndex_Type.__name__ = "Integer32"
_RemoteTrackRIndex_Object = MibTableColumn
remoteTrackRIndex = _RemoteTrackRIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 1, 1, 1),
    _RemoteTrackRIndex_Type()
)
remoteTrackRIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    remoteTrackRIndex.setStatus("current")
_RemoteTrackRSweepRate_Type = RemoteSweepRateType
_RemoteTrackRSweepRate_Object = MibTableColumn
remoteTrackRSweepRate = _RemoteTrackRSweepRate_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 1, 1, 2),
    _RemoteTrackRSweepRate_Type()
)
remoteTrackRSweepRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteTrackRSweepRate.setStatus("current")
_RemoteTrackRSweepWidth_Type = RemoteSweepWidthType
_RemoteTrackRSweepWidth_Object = MibTableColumn
remoteTrackRSweepWidth = _RemoteTrackRSweepWidth_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 1, 1, 3),
    _RemoteTrackRSweepWidth_Type()
)
remoteTrackRSweepWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteTrackRSweepWidth.setStatus("current")
_RemoteTrackRLogdBVolt_Type = RemoteDBVoltType
_RemoteTrackRLogdBVolt_Object = MibTableColumn
remoteTrackRLogdBVolt = _RemoteTrackRLogdBVolt_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 1, 1, 4),
    _RemoteTrackRLogdBVolt_Type()
)
remoteTrackRLogdBVolt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteTrackRLogdBVolt.setStatus("current")


class _RemoteTrackRLogOffset_Type(Integer32):
    """Custom type remoteTrackRLogOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_RemoteTrackRLogOffset_Type.__name__ = "Integer32"
_RemoteTrackRLogOffset_Object = MibTableColumn
remoteTrackRLogOffset = _RemoteTrackRLogOffset_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 1, 1, 5),
    _RemoteTrackRLogOffset_Type()
)
remoteTrackRLogOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteTrackRLogOffset.setStatus("current")
_RemoteTrackRASB_Type = OnOffType
_RemoteTrackRASB_Object = MibTableColumn
remoteTrackRASB = _RemoteTrackRASB_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 1, 1, 6),
    _RemoteTrackRASB_Type()
)
remoteTrackRASB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteTrackRASB.setStatus("current")
_RemoteTrackRDCOutput_Type = OctetString
_RemoteTrackRDCOutput_Object = MibTableColumn
remoteTrackRDCOutput = _RemoteTrackRDCOutput_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 1, 1, 7),
    _RemoteTrackRDCOutput_Type()
)
remoteTrackRDCOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteTrackRDCOutput.setStatus("current")
_RemoteTrackRRxLevel_Type = OctetString
_RemoteTrackRRxLevel_Object = MibTableColumn
remoteTrackRRxLevel = _RemoteTrackRRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 1, 1, 8),
    _RemoteTrackRRxLevel_Type()
)
remoteTrackRRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteTrackRRxLevel.setStatus("current")
_RemoteTrackRFrequency_Type = OctetString
_RemoteTrackRFrequency_Object = MibTableColumn
remoteTrackRFrequency = _RemoteTrackRFrequency_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 1, 1, 9),
    _RemoteTrackRFrequency_Type()
)
remoteTrackRFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteTrackRFrequency.setStatus("current")
_RemoteTrackRAttenuation_Type = OctetString
_RemoteTrackRAttenuation_Object = MibTableColumn
remoteTrackRAttenuation = _RemoteTrackRAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 1, 1, 10),
    _RemoteTrackRAttenuation_Type()
)
remoteTrackRAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteTrackRAttenuation.setStatus("current")
_RemoteTrackR1stIFAttenuation_Type = OctetString
_RemoteTrackR1stIFAttenuation_Object = MibTableColumn
remoteTrackR1stIFAttenuation = _RemoteTrackR1stIFAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 1, 1, 11),
    _RemoteTrackR1stIFAttenuation_Type()
)
remoteTrackR1stIFAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteTrackR1stIFAttenuation.setStatus("current")
_RemoteTrackRDCFeed_Type = OnOffType
_RemoteTrackRDCFeed_Object = MibTableColumn
remoteTrackRDCFeed = _RemoteTrackRDCFeed_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 1, 1, 13),
    _RemoteTrackRDCFeed_Type()
)
remoteTrackRDCFeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteTrackRDCFeed.setStatus("current")
_RemoteTrackRSHFOnOff_Type = OnOffType
_RemoteTrackRSHFOnOff_Object = MibTableColumn
remoteTrackRSHFOnOff = _RemoteTrackRSHFOnOff_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 1, 1, 14),
    _RemoteTrackRSHFOnOff_Type()
)
remoteTrackRSHFOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteTrackRSHFOnOff.setStatus("current")
_RemoteTrackRSHFFrequency_Type = OctetString
_RemoteTrackRSHFFrequency_Object = MibTableColumn
remoteTrackRSHFFrequency = _RemoteTrackRSHFFrequency_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 1, 1, 15),
    _RemoteTrackRSHFFrequency_Type()
)
remoteTrackRSHFFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteTrackRSHFFrequency.setStatus("current")
_RemoteTrackRSHFSpectrumInvert_Type = OnOffType
_RemoteTrackRSHFSpectrumInvert_Object = MibTableColumn
remoteTrackRSHFSpectrumInvert = _RemoteTrackRSHFSpectrumInvert_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 1, 1, 16),
    _RemoteTrackRSHFSpectrumInvert_Type()
)
remoteTrackRSHFSpectrumInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteTrackRSHFSpectrumInvert.setStatus("current")
_RemoteTrackROKSince_Type = OctetString
_RemoteTrackROKSince_Object = MibTableColumn
remoteTrackROKSince = _RemoteTrackROKSince_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 1, 1, 100),
    _RemoteTrackROKSince_Type()
)
remoteTrackROKSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteTrackROKSince.setStatus("current")
_RemoteTrackRecIntegers_ObjectIdentity = ObjectIdentity
remoteTrackRecIntegers = _RemoteTrackRecIntegers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 9)
)
_RemoteTrackRITable_Object = MibTable
remoteTrackRITable = _RemoteTrackRITable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 9, 1)
)
if mibBuilder.loadTexts:
    remoteTrackRITable.setStatus("current")
_RemoteTrackRITableEntry_Object = MibTableRow
remoteTrackRITableEntry = _RemoteTrackRITableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 9, 1, 1)
)
remoteTrackRITableEntry.setIndexNames(
    (0, "PEAKREMOTETRACKINGRECEIVER-MIB", "remoteTrackRIIndex"),
)
if mibBuilder.loadTexts:
    remoteTrackRITableEntry.setStatus("current")


class _RemoteTrackRIIndex_Type(Integer32):
    """Custom type remoteTrackRIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_RemoteTrackRIIndex_Type.__name__ = "Integer32"
_RemoteTrackRIIndex_Object = MibTableColumn
remoteTrackRIIndex = _RemoteTrackRIIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 9, 1, 1, 1),
    _RemoteTrackRIIndex_Type()
)
remoteTrackRIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    remoteTrackRIIndex.setStatus("current")
_RemoteTrackRIDCOutput_Type = Integer32
_RemoteTrackRIDCOutput_Object = MibTableColumn
remoteTrackRIDCOutput = _RemoteTrackRIDCOutput_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 9, 1, 1, 2),
    _RemoteTrackRIDCOutput_Type()
)
remoteTrackRIDCOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteTrackRIDCOutput.setStatus("current")
_RemoteTrackRIRxLevel_Type = Integer32
_RemoteTrackRIRxLevel_Object = MibTableColumn
remoteTrackRIRxLevel = _RemoteTrackRIRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 9, 1, 1, 3),
    _RemoteTrackRIRxLevel_Type()
)
remoteTrackRIRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remoteTrackRIRxLevel.setStatus("current")
_RemoteTrackRecGroups_ObjectIdentity = ObjectIdentity
remoteTrackRecGroups = _RemoteTrackRecGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 10)
)
_RemoteTrackRecConformance_ObjectIdentity = ObjectIdentity
remoteTrackRecConformance = _RemoteTrackRecConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 11)
)

# Managed Objects groups

remoteTrackCNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 10, 1)
)
remoteTrackCNFReqGrp.setObjects(
      *(("PEAKREMOTETRACKINGRECEIVER-MIB", "remoteTrackRSweepRate"),
        ("PEAKREMOTETRACKINGRECEIVER-MIB", "remoteTrackRLogdBVolt"),
        ("PEAKREMOTETRACKINGRECEIVER-MIB", "remoteTrackRLogOffset"),
        ("PEAKREMOTETRACKINGRECEIVER-MIB", "remoteTrackRASB"),
        ("PEAKREMOTETRACKINGRECEIVER-MIB", "remoteTrackRDCOutput"),
        ("PEAKREMOTETRACKINGRECEIVER-MIB", "remoteTrackRSweepWidth"),
        ("PEAKREMOTETRACKINGRECEIVER-MIB", "remoteTrackRRxLevel"),
        ("PEAKREMOTETRACKINGRECEIVER-MIB", "remoteTrackRFrequency"),
        ("PEAKREMOTETRACKINGRECEIVER-MIB", "remoteTrackRAttenuation"),
        ("PEAKREMOTETRACKINGRECEIVER-MIB", "remoteTrackR1stIFAttenuation"),
        ("PEAKREMOTETRACKINGRECEIVER-MIB", "remoteTrackROKSince"))
)
if mibBuilder.loadTexts:
    remoteTrackCNFReqGrp.setStatus("current")

remoteTrackCNFDCFeedGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 10, 2)
)
remoteTrackCNFDCFeedGrp.setObjects(
    ("PEAKREMOTETRACKINGRECEIVER-MIB", "remoteTrackRDCFeed")
)
if mibBuilder.loadTexts:
    remoteTrackCNFDCFeedGrp.setStatus("current")

remoteTrackCNFSHFGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 10, 3)
)
remoteTrackCNFSHFGrp.setObjects(
      *(("PEAKREMOTETRACKINGRECEIVER-MIB", "remoteTrackRSHFOnOff"),
        ("PEAKREMOTETRACKINGRECEIVER-MIB", "remoteTrackRSHFFrequency"),
        ("PEAKREMOTETRACKINGRECEIVER-MIB", "remoteTrackRSHFSpectrumInvert"))
)
if mibBuilder.loadTexts:
    remoteTrackCNFSHFGrp.setStatus("current")

remoteTrackICNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 10, 4)
)
remoteTrackICNFReqGrp.setObjects(
      *(("PEAKREMOTETRACKINGRECEIVER-MIB", "remoteTrackRIDCOutput"),
        ("PEAKREMOTETRACKINGRECEIVER-MIB", "remoteTrackRIRxLevel"))
)
if mibBuilder.loadTexts:
    remoteTrackICNFReqGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

remoteTrackCNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 16, 11, 1)
)
remoteTrackCNFCompliance.setObjects(
      *(("PEAKREMOTETRACKINGRECEIVER-MIB", "remoteTrackCNFReqGrp"),
        ("PEAKREMOTETRACKINGRECEIVER-MIB", "remoteTrackICNFReqGrp"),
        ("PEAKREMOTETRACKINGRECEIVER-MIB", "remoteTrackCNFDCFeedGrp"),
        ("PEAKREMOTETRACKINGRECEIVER-MIB", "remoteTrackCNFSHFGrp"))
)
if mibBuilder.loadTexts:
    remoteTrackCNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKREMOTETRACKINGRECEIVER-MIB",
    **{"RemoteSweepRateType": RemoteSweepRateType,
       "RemoteSweepWidthType": RemoteSweepWidthType,
       "RemoteDBVoltType": RemoteDBVoltType,
       "peakRemoteTrackingReceiverModule": peakRemoteTrackingReceiverModule,
       "remoteTrackRTable": remoteTrackRTable,
       "remoteTrackRTableEntry": remoteTrackRTableEntry,
       "remoteTrackRIndex": remoteTrackRIndex,
       "remoteTrackRSweepRate": remoteTrackRSweepRate,
       "remoteTrackRSweepWidth": remoteTrackRSweepWidth,
       "remoteTrackRLogdBVolt": remoteTrackRLogdBVolt,
       "remoteTrackRLogOffset": remoteTrackRLogOffset,
       "remoteTrackRASB": remoteTrackRASB,
       "remoteTrackRDCOutput": remoteTrackRDCOutput,
       "remoteTrackRRxLevel": remoteTrackRRxLevel,
       "remoteTrackRFrequency": remoteTrackRFrequency,
       "remoteTrackRAttenuation": remoteTrackRAttenuation,
       "remoteTrackR1stIFAttenuation": remoteTrackR1stIFAttenuation,
       "remoteTrackRDCFeed": remoteTrackRDCFeed,
       "remoteTrackRSHFOnOff": remoteTrackRSHFOnOff,
       "remoteTrackRSHFFrequency": remoteTrackRSHFFrequency,
       "remoteTrackRSHFSpectrumInvert": remoteTrackRSHFSpectrumInvert,
       "remoteTrackROKSince": remoteTrackROKSince,
       "remoteTrackRecIntegers": remoteTrackRecIntegers,
       "remoteTrackRITable": remoteTrackRITable,
       "remoteTrackRITableEntry": remoteTrackRITableEntry,
       "remoteTrackRIIndex": remoteTrackRIIndex,
       "remoteTrackRIDCOutput": remoteTrackRIDCOutput,
       "remoteTrackRIRxLevel": remoteTrackRIRxLevel,
       "remoteTrackRecGroups": remoteTrackRecGroups,
       "remoteTrackCNFReqGrp": remoteTrackCNFReqGrp,
       "remoteTrackCNFDCFeedGrp": remoteTrackCNFDCFeedGrp,
       "remoteTrackCNFSHFGrp": remoteTrackCNFSHFGrp,
       "remoteTrackICNFReqGrp": remoteTrackICNFReqGrp,
       "remoteTrackRecConformance": remoteTrackRecConformance,
       "remoteTrackCNFCompliance": remoteTrackCNFCompliance}
)
