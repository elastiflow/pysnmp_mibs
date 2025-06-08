# SNMP MIB module (PEAKUPCONVERTERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKUPCONVERTERS-MIB.mib
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

peakUpConverterModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 1)
)
if mibBuilder.loadTexts:
    peakUpConverterModule.setRevisions(
        ("2015-09-15 10:00",
         "2013-04-04 12:00",
         "2010-06-02 09:00",
         "2008-12-03 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UpCTable_Object = MibTable
upCTable = _UpCTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    upCTable.setStatus("current")
_UpCTableEntry_Object = MibTableRow
upCTableEntry = _UpCTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 1, 1, 1)
)
upCTableEntry.setIndexNames(
    (0, "PEAKUPCONVERTERS-MIB", "upCIndex"),
)
if mibBuilder.loadTexts:
    upCTableEntry.setStatus("current")


class _UpCIndex_Type(Integer32):
    """Custom type upCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_UpCIndex_Type.__name__ = "Integer32"
_UpCIndex_Object = MibTableColumn
upCIndex = _UpCIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 1, 1, 1, 1),
    _UpCIndex_Type()
)
upCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    upCIndex.setStatus("current")
_UpCFrequency_Type = OctetString
_UpCFrequency_Object = MibTableColumn
upCFrequency = _UpCFrequency_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 1, 1, 1, 2),
    _UpCFrequency_Type()
)
upCFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upCFrequency.setStatus("current")
_UpCGain_Type = OctetString
_UpCGain_Object = MibTableColumn
upCGain = _UpCGain_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 1, 1, 1, 3),
    _UpCGain_Type()
)
upCGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upCGain.setStatus("current")
_UpCCarrier_Type = OnOffType
_UpCCarrier_Object = MibTableColumn
upCCarrier = _UpCCarrier_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 1, 1, 1, 5),
    _UpCCarrier_Type()
)
upCCarrier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upCCarrier.setStatus("current")
_UpC10MHz_Type = OnOffType
_UpC10MHz_Object = MibTableColumn
upC10MHz = _UpC10MHz_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 1, 1, 1, 6),
    _UpC10MHz_Type()
)
upC10MHz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upC10MHz.setStatus("current")
_UpCDCFeed_Type = OnOffType
_UpCDCFeed_Object = MibTableColumn
upCDCFeed = _UpCDCFeed_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 1, 1, 1, 7),
    _UpCDCFeed_Type()
)
upCDCFeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upCDCFeed.setStatus("current")
_UpCIF_Type = Integer32
_UpCIF_Object = MibTableColumn
upCIF = _UpCIF_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 1, 1, 1, 8),
    _UpCIF_Type()
)
upCIF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upCIF.setStatus("current")
_UpCSHFOnOff_Type = OnOffType
_UpCSHFOnOff_Object = MibTableColumn
upCSHFOnOff = _UpCSHFOnOff_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 1, 1, 1, 9),
    _UpCSHFOnOff_Type()
)
upCSHFOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upCSHFOnOff.setStatus("current")
_UpCSHFFrequency_Type = OctetString
_UpCSHFFrequency_Object = MibTableColumn
upCSHFFrequency = _UpCSHFFrequency_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 1, 1, 1, 10),
    _UpCSHFFrequency_Type()
)
upCSHFFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upCSHFFrequency.setStatus("current")
_UpCSHFGainOnOff_Type = OnOffType
_UpCSHFGainOnOff_Object = MibTableColumn
upCSHFGainOnOff = _UpCSHFGainOnOff_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 1, 1, 1, 11),
    _UpCSHFGainOnOff_Type()
)
upCSHFGainOnOff.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upCSHFGainOnOff.setStatus("current")
_UpCSHFGain_Type = OctetString
_UpCSHFGain_Object = MibTableColumn
upCSHFGain = _UpCSHFGain_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 1, 1, 1, 12),
    _UpCSHFGain_Type()
)
upCSHFGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upCSHFGain.setStatus("current")
_UpCSHFGainIP_Type = OctetString
_UpCSHFGainIP_Object = MibTableColumn
upCSHFGainIP = _UpCSHFGainIP_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 1, 1, 1, 13),
    _UpCSHFGainIP_Type()
)
upCSHFGainIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upCSHFGainIP.setStatus("current")
_UpCLKuGain_Type = OctetString
_UpCLKuGain_Object = MibTableColumn
upCLKuGain = _UpCLKuGain_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 1, 1, 1, 14),
    _UpCLKuGain_Type()
)
upCLKuGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upCLKuGain.setStatus("current")
_UpCOKSince_Type = OctetString
_UpCOKSince_Object = MibTableColumn
upCOKSince = _UpCOKSince_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 1, 1, 1, 100),
    _UpCOKSince_Type()
)
upCOKSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    upCOKSince.setStatus("current")
_UpConvGroups_ObjectIdentity = ObjectIdentity
upConvGroups = _UpConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 1, 10)
)
_UpConvConformance_ObjectIdentity = ObjectIdentity
upConvConformance = _UpConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 1, 11)
)

# Managed Objects groups

upCNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 1, 10, 1)
)
upCNFReqGrp.setObjects(
      *(("PEAKUPCONVERTERS-MIB", "upCGain"),
        ("PEAKUPCONVERTERS-MIB", "upCCarrier"),
        ("PEAKUPCONVERTERS-MIB", "upCOKSince"))
)
if mibBuilder.loadTexts:
    upCNFReqGrp.setStatus("current")

upCNFFreqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 1, 10, 2)
)
upCNFFreqGrp.setObjects(
    ("PEAKUPCONVERTERS-MIB", "upCFrequency")
)
if mibBuilder.loadTexts:
    upCNFFreqGrp.setStatus("current")

upCNF10MHzGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 1, 10, 3)
)
upCNF10MHzGrp.setObjects(
    ("PEAKUPCONVERTERS-MIB", "upC10MHz")
)
if mibBuilder.loadTexts:
    upCNF10MHzGrp.setStatus("current")

upCNFDCFeedGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 1, 10, 4)
)
upCNFDCFeedGrp.setObjects(
    ("PEAKUPCONVERTERS-MIB", "upCDCFeed")
)
if mibBuilder.loadTexts:
    upCNFDCFeedGrp.setStatus("current")

upCNFSHFGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 1, 10, 5)
)
upCNFSHFGrp.setObjects(
      *(("PEAKUPCONVERTERS-MIB", "upCSHFOnOff"),
        ("PEAKUPCONVERTERS-MIB", "upCSHFFrequency"),
        ("PEAKUPCONVERTERS-MIB", "upCSHFGainOnOff"),
        ("PEAKUPCONVERTERS-MIB", "upCSHFGain"),
        ("PEAKUPCONVERTERS-MIB", "upCSHFGainIP"))
)
if mibBuilder.loadTexts:
    upCNFSHFGrp.setStatus("current")

upCNFIFGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 1, 10, 6)
)
upCNFIFGrp.setObjects(
    ("PEAKUPCONVERTERS-MIB", "upCIF")
)
if mibBuilder.loadTexts:
    upCNFIFGrp.setStatus("current")

upCNFupCLKuGainGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 1, 10, 7)
)
upCNFupCLKuGainGrp.setObjects(
    ("PEAKUPCONVERTERS-MIB", "upCLKuGain")
)
if mibBuilder.loadTexts:
    upCNFupCLKuGainGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

upCNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 1, 11, 1)
)
upCNFCompliance.setObjects(
      *(("PEAKUPCONVERTERS-MIB", "upCNFReqGrp"),
        ("PEAKUPCONVERTERS-MIB", "upCNFFreqGrp"),
        ("PEAKUPCONVERTERS-MIB", "upCNF10MHzGrp"),
        ("PEAKUPCONVERTERS-MIB", "upCNFDCFeedGrp"),
        ("PEAKUPCONVERTERS-MIB", "upCNFSHFGrp"),
        ("PEAKUPCONVERTERS-MIB", "upCNFIFGrp"),
        ("PEAKUPCONVERTERS-MIB", "upCNFupCLKuGainGrp"))
)
if mibBuilder.loadTexts:
    upCNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKUPCONVERTERS-MIB",
    **{"peakUpConverterModule": peakUpConverterModule,
       "upCTable": upCTable,
       "upCTableEntry": upCTableEntry,
       "upCIndex": upCIndex,
       "upCFrequency": upCFrequency,
       "upCGain": upCGain,
       "upCCarrier": upCCarrier,
       "upC10MHz": upC10MHz,
       "upCDCFeed": upCDCFeed,
       "upCIF": upCIF,
       "upCSHFOnOff": upCSHFOnOff,
       "upCSHFFrequency": upCSHFFrequency,
       "upCSHFGainOnOff": upCSHFGainOnOff,
       "upCSHFGain": upCSHFGain,
       "upCSHFGainIP": upCSHFGainIP,
       "upCLKuGain": upCLKuGain,
       "upCOKSince": upCOKSince,
       "upConvGroups": upConvGroups,
       "upCNFReqGrp": upCNFReqGrp,
       "upCNFFreqGrp": upCNFFreqGrp,
       "upCNF10MHzGrp": upCNF10MHzGrp,
       "upCNFDCFeedGrp": upCNFDCFeedGrp,
       "upCNFSHFGrp": upCNFSHFGrp,
       "upCNFIFGrp": upCNFIFGrp,
       "upCNFupCLKuGainGrp": upCNFupCLKuGainGrp,
       "upConvConformance": upConvConformance,
       "upCNFCompliance": upCNFCompliance}
)
