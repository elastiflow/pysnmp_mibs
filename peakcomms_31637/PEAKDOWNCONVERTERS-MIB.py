# SNMP MIB module (PEAKDOWNCONVERTERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKDOWNCONVERTERS-MIB.mib
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

peakDownConverterModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 2)
)
if mibBuilder.loadTexts:
    peakDownConverterModule.setRevisions(
        ("2015-12-03 09:00",
         "2015-09-15 09:00",
         "2013-04-04 12:00",
         "2008-12-03 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DCFeedVoltageType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dc18v", 1),
          ("dc13v", 2))
    )



# MIB Managed Objects in the order of their OIDs

_DownCTable_Object = MibTable
downCTable = _DownCTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    downCTable.setStatus("current")
_DownCTableEntry_Object = MibTableRow
downCTableEntry = _DownCTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 2, 1, 1)
)
downCTableEntry.setIndexNames(
    (0, "PEAKDOWNCONVERTERS-MIB", "downCIndex"),
)
if mibBuilder.loadTexts:
    downCTableEntry.setStatus("current")


class _DownCIndex_Type(Integer32):
    """Custom type downCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_DownCIndex_Type.__name__ = "Integer32"
_DownCIndex_Object = MibTableColumn
downCIndex = _DownCIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 2, 1, 1, 1),
    _DownCIndex_Type()
)
downCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    downCIndex.setStatus("current")
_DownCFrequency_Type = OctetString
_DownCFrequency_Object = MibTableColumn
downCFrequency = _DownCFrequency_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 2, 1, 1, 2),
    _DownCFrequency_Type()
)
downCFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downCFrequency.setStatus("current")
_DownCGain_Type = OctetString
_DownCGain_Object = MibTableColumn
downCGain = _DownCGain_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 2, 1, 1, 3),
    _DownCGain_Type()
)
downCGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downCGain.setStatus("current")
_DownCSpectrumInvert_Type = OnOffType
_DownCSpectrumInvert_Object = MibTableColumn
downCSpectrumInvert = _DownCSpectrumInvert_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 2, 1, 1, 4),
    _DownCSpectrumInvert_Type()
)
downCSpectrumInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downCSpectrumInvert.setStatus("current")
_DownC10MHz_Type = OnOffType
_DownC10MHz_Object = MibTableColumn
downC10MHz = _DownC10MHz_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 2, 1, 1, 5),
    _DownC10MHz_Type()
)
downC10MHz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downC10MHz.setStatus("current")
_DownCDCFeed_Type = OnOffType
_DownCDCFeed_Object = MibTableColumn
downCDCFeed = _DownCDCFeed_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 2, 1, 1, 6),
    _DownCDCFeed_Type()
)
downCDCFeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downCDCFeed.setStatus("current")
_DownCIF_Type = Integer32
_DownCIF_Object = MibTableColumn
downCIF = _DownCIF_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 2, 1, 1, 7),
    _DownCIF_Type()
)
downCIF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downCIF.setStatus("current")
_DownCSHFOnOff_Type = OnOffType
_DownCSHFOnOff_Object = MibTableColumn
downCSHFOnOff = _DownCSHFOnOff_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 2, 1, 1, 8),
    _DownCSHFOnOff_Type()
)
downCSHFOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downCSHFOnOff.setStatus("current")
_DownCSHFFrequency_Type = OctetString
_DownCSHFFrequency_Object = MibTableColumn
downCSHFFrequency = _DownCSHFFrequency_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 2, 1, 1, 9),
    _DownCSHFFrequency_Type()
)
downCSHFFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downCSHFFrequency.setStatus("current")
_DownCSHFSpectrumInvert_Type = OnOffType
_DownCSHFSpectrumInvert_Object = MibTableColumn
downCSHFSpectrumInvert = _DownCSHFSpectrumInvert_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 2, 1, 1, 10),
    _DownCSHFSpectrumInvert_Type()
)
downCSHFSpectrumInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downCSHFSpectrumInvert.setStatus("current")
_DownCDCFeedVoltage_Type = DCFeedVoltageType
_DownCDCFeedVoltage_Object = MibTableColumn
downCDCFeedVoltage = _DownCDCFeedVoltage_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 2, 1, 1, 11),
    _DownCDCFeedVoltage_Type()
)
downCDCFeedVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    downCDCFeedVoltage.setStatus("current")
_DownCOKSince_Type = OctetString
_DownCOKSince_Object = MibTableColumn
downCOKSince = _DownCOKSince_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 2, 1, 1, 100),
    _DownCOKSince_Type()
)
downCOKSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    downCOKSince.setStatus("current")
_DownConvGroups_ObjectIdentity = ObjectIdentity
downConvGroups = _DownConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 2, 10)
)
_DownConvConformance_ObjectIdentity = ObjectIdentity
downConvConformance = _DownConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 2, 11)
)

# Managed Objects groups

downCNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 2, 10, 1)
)
downCNFReqGrp.setObjects(
      *(("PEAKDOWNCONVERTERS-MIB", "downCGain"),
        ("PEAKDOWNCONVERTERS-MIB", "downCOKSince"))
)
if mibBuilder.loadTexts:
    downCNFReqGrp.setStatus("current")

downCNFFreqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 2, 10, 2)
)
downCNFFreqGrp.setObjects(
    ("PEAKDOWNCONVERTERS-MIB", "downCFrequency")
)
if mibBuilder.loadTexts:
    downCNFFreqGrp.setStatus("current")

downCNF10MHzGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 2, 10, 3)
)
downCNF10MHzGrp.setObjects(
    ("PEAKDOWNCONVERTERS-MIB", "downC10MHz")
)
if mibBuilder.loadTexts:
    downCNF10MHzGrp.setStatus("current")

downCNFDCFeedGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 2, 10, 4)
)
downCNFDCFeedGrp.setObjects(
    ("PEAKDOWNCONVERTERS-MIB", "downCDCFeed")
)
if mibBuilder.loadTexts:
    downCNFDCFeedGrp.setStatus("current")

downCNFSpectrumInvertGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 2, 10, 5)
)
downCNFSpectrumInvertGrp.setObjects(
    ("PEAKDOWNCONVERTERS-MIB", "downCSpectrumInvert")
)
if mibBuilder.loadTexts:
    downCNFSpectrumInvertGrp.setStatus("current")

downCNFSHFGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 2, 10, 6)
)
downCNFSHFGrp.setObjects(
      *(("PEAKDOWNCONVERTERS-MIB", "downCSHFOnOff"),
        ("PEAKDOWNCONVERTERS-MIB", "downCSHFFrequency"),
        ("PEAKDOWNCONVERTERS-MIB", "downCSHFSpectrumInvert"))
)
if mibBuilder.loadTexts:
    downCNFSHFGrp.setStatus("current")

downCNFIFGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 2, 10, 7)
)
downCNFIFGrp.setObjects(
    ("PEAKDOWNCONVERTERS-MIB", "downCIF")
)
if mibBuilder.loadTexts:
    downCNFIFGrp.setStatus("current")

downCNFDCFeedVoltagesGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 2, 10, 8)
)
downCNFDCFeedVoltagesGrp.setObjects(
    ("PEAKDOWNCONVERTERS-MIB", "downCDCFeedVoltage")
)
if mibBuilder.loadTexts:
    downCNFDCFeedVoltagesGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

downCNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 2, 11, 1)
)
downCNFCompliance.setObjects(
      *(("PEAKDOWNCONVERTERS-MIB", "downCNFReqGrp"),
        ("PEAKDOWNCONVERTERS-MIB", "downCNFFreqGrp"),
        ("PEAKDOWNCONVERTERS-MIB", "downCNF10MHzGrp"),
        ("PEAKDOWNCONVERTERS-MIB", "downCNFDCFeedGrp"),
        ("PEAKDOWNCONVERTERS-MIB", "downCNFDCFeedVoltagesGrp"),
        ("PEAKDOWNCONVERTERS-MIB", "downCNFSpectrumInvertGrp"),
        ("PEAKDOWNCONVERTERS-MIB", "downCNFSHFGrp"),
        ("PEAKDOWNCONVERTERS-MIB", "downCNFIFGrp"))
)
if mibBuilder.loadTexts:
    downCNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKDOWNCONVERTERS-MIB",
    **{"DCFeedVoltageType": DCFeedVoltageType,
       "peakDownConverterModule": peakDownConverterModule,
       "downCTable": downCTable,
       "downCTableEntry": downCTableEntry,
       "downCIndex": downCIndex,
       "downCFrequency": downCFrequency,
       "downCGain": downCGain,
       "downCSpectrumInvert": downCSpectrumInvert,
       "downC10MHz": downC10MHz,
       "downCDCFeed": downCDCFeed,
       "downCIF": downCIF,
       "downCSHFOnOff": downCSHFOnOff,
       "downCSHFFrequency": downCSHFFrequency,
       "downCSHFSpectrumInvert": downCSHFSpectrumInvert,
       "downCDCFeedVoltage": downCDCFeedVoltage,
       "downCOKSince": downCOKSince,
       "downConvGroups": downConvGroups,
       "downCNFReqGrp": downCNFReqGrp,
       "downCNFFreqGrp": downCNFFreqGrp,
       "downCNF10MHzGrp": downCNF10MHzGrp,
       "downCNFDCFeedGrp": downCNFDCFeedGrp,
       "downCNFSpectrumInvertGrp": downCNFSpectrumInvertGrp,
       "downCNFSHFGrp": downCNFSHFGrp,
       "downCNFIFGrp": downCNFIFGrp,
       "downCNFDCFeedVoltagesGrp": downCNFDCFeedVoltagesGrp,
       "downConvConformance": downConvConformance,
       "downCNFCompliance": downCNFCompliance}
)
