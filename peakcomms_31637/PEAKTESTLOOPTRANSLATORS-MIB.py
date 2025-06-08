# SNMP MIB module (PEAKTESTLOOPTRANSLATORS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKTESTLOOPTRANSLATORS-MIB.mib
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

(MuteType,
 converters) = mibBuilder.importSymbols(
    "PEAKDEFINITIONS-MIB",
    "MuteType",
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

peakTestLoopTranslatorModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 3)
)
if mibBuilder.loadTexts:
    peakTestLoopTranslatorModule.setRevisions(
        ("2015-09-25 10:00",
         "2015-09-15 10:00",
         "2015-02-17 12:00",
         "2013-04-04 12:00",
         "2012-07-30 12:00",
         "2010-08-19 12:00",
         "2009-10-26 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TltTable_Object = MibTable
tltTable = _TltTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tltTable.setStatus("current")
_TltTableEntry_Object = MibTableRow
tltTableEntry = _TltTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 3, 1, 1)
)
tltTableEntry.setIndexNames(
    (0, "PEAKTESTLOOPTRANSLATORS-MIB", "tltIndex"),
)
if mibBuilder.loadTexts:
    tltTableEntry.setStatus("current")


class _TltIndex_Type(Integer32):
    """Custom type tltIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TltIndex_Type.__name__ = "Integer32"
_TltIndex_Object = MibTableColumn
tltIndex = _TltIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 3, 1, 1, 1),
    _TltIndex_Type()
)
tltIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tltIndex.setStatus("current")
_TltAttenuation_Type = OctetString
_TltAttenuation_Object = MibTableColumn
tltAttenuation = _TltAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 3, 1, 1, 2),
    _TltAttenuation_Type()
)
tltAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tltAttenuation.setStatus("current")


class _TltBand_Type(Integer32):
    """Custom type tltBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_TltBand_Type.__name__ = "Integer32"
_TltBand_Object = MibTableColumn
tltBand = _TltBand_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 3, 1, 1, 3),
    _TltBand_Type()
)
tltBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tltBand.setStatus("current")
_TltMute_Type = MuteType
_TltMute_Object = MibTableColumn
tltMute = _TltMute_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 3, 1, 1, 4),
    _TltMute_Type()
)
tltMute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tltMute.setStatus("current")
_TltOKSince_Type = OctetString
_TltOKSince_Object = MibTableColumn
tltOKSince = _TltOKSince_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 3, 1, 1, 100),
    _TltOKSince_Type()
)
tltOKSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tltOKSince.setStatus("current")
_TltConvGroups_ObjectIdentity = ObjectIdentity
tltConvGroups = _TltConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 3, 10)
)
_TltConvConformance_ObjectIdentity = ObjectIdentity
tltConvConformance = _TltConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 3, 11)
)

# Managed Objects groups

tltCNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 3, 10, 1)
)
tltCNFReqGrp.setObjects(
    ("PEAKTESTLOOPTRANSLATORS-MIB", "tltOKSince")
)
if mibBuilder.loadTexts:
    tltCNFReqGrp.setStatus("current")

tltCNFAttGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 3, 10, 2)
)
tltCNFAttGrp.setObjects(
    ("PEAKTESTLOOPTRANSLATORS-MIB", "tltAttenuation")
)
if mibBuilder.loadTexts:
    tltCNFAttGrp.setStatus("current")

tltCNFBandGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 3, 10, 3)
)
tltCNFBandGrp.setObjects(
    ("PEAKTESTLOOPTRANSLATORS-MIB", "tltBand")
)
if mibBuilder.loadTexts:
    tltCNFBandGrp.setStatus("current")

tltCNFMuteGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 3, 10, 4)
)
tltCNFMuteGrp.setObjects(
    ("PEAKTESTLOOPTRANSLATORS-MIB", "tltMute")
)
if mibBuilder.loadTexts:
    tltCNFMuteGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tltCNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 3, 11, 1)
)
tltCNFCompliance.setObjects(
      *(("PEAKTESTLOOPTRANSLATORS-MIB", "tltCNFReqGrp"),
        ("PEAKTESTLOOPTRANSLATORS-MIB", "tltCNFAttGrp"),
        ("PEAKTESTLOOPTRANSLATORS-MIB", "tltCNFBandGrp"),
        ("PEAKTESTLOOPTRANSLATORS-MIB", "tltCNFMuteGrp"))
)
if mibBuilder.loadTexts:
    tltCNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKTESTLOOPTRANSLATORS-MIB",
    **{"peakTestLoopTranslatorModule": peakTestLoopTranslatorModule,
       "tltTable": tltTable,
       "tltTableEntry": tltTableEntry,
       "tltIndex": tltIndex,
       "tltAttenuation": tltAttenuation,
       "tltBand": tltBand,
       "tltMute": tltMute,
       "tltOKSince": tltOKSince,
       "tltConvGroups": tltConvGroups,
       "tltCNFReqGrp": tltCNFReqGrp,
       "tltCNFAttGrp": tltCNFAttGrp,
       "tltCNFBandGrp": tltCNFBandGrp,
       "tltCNFMuteGrp": tltCNFMuteGrp,
       "tltConvConformance": tltConvConformance,
       "tltCNFCompliance": tltCNFCompliance}
)
