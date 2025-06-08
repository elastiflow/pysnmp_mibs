# SNMP MIB module (PEAKBLOCKDOWNCONVERTERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKBLOCKDOWNCONVERTERS-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 11:49:01 2025
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

(converters,) = mibBuilder.importSymbols(
    "PEAKDEFINITIONS-MIB",
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

peakBlockDownConverterModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 6)
)
if mibBuilder.loadTexts:
    peakBlockDownConverterModule.setRevisions(
        ("2015-09-15 09:00",
         "2013-04-04 12:00",
         "2011-10-31 12:00",
         "2011-01-02 12:00",
         "2010-11-10 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BlockdownTable_Object = MibTable
blockdownTable = _BlockdownTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    blockdownTable.setStatus("current")
_BlockdownTableEntry_Object = MibTableRow
blockdownTableEntry = _BlockdownTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 6, 1, 1)
)
blockdownTableEntry.setIndexNames(
    (0, "PEAKBLOCKDOWNCONVERTERS-MIB", "blockdownIndex"),
)
if mibBuilder.loadTexts:
    blockdownTableEntry.setStatus("current")


class _BlockdownIndex_Type(Integer32):
    """Custom type blockdownIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BlockdownIndex_Type.__name__ = "Integer32"
_BlockdownIndex_Object = MibTableColumn
blockdownIndex = _BlockdownIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 6, 1, 1, 1),
    _BlockdownIndex_Type()
)
blockdownIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    blockdownIndex.setStatus("current")
_BlockdownAttenuation_Type = OctetString
_BlockdownAttenuation_Object = MibTableColumn
blockdownAttenuation = _BlockdownAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 6, 1, 1, 2),
    _BlockdownAttenuation_Type()
)
blockdownAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blockdownAttenuation.setStatus("current")


class _BlockdownBand_Type(Integer32):
    """Custom type blockdownBand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BlockdownBand_Type.__name__ = "Integer32"
_BlockdownBand_Object = MibTableColumn
blockdownBand = _BlockdownBand_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 6, 1, 1, 3),
    _BlockdownBand_Type()
)
blockdownBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blockdownBand.setStatus("current")
_BlockdownName_Type = OctetString
_BlockdownName_Object = MibTableColumn
blockdownName = _BlockdownName_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 6, 1, 1, 4),
    _BlockdownName_Type()
)
blockdownName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blockdownName.setStatus("current")
_BlockdownOKSince_Type = OctetString
_BlockdownOKSince_Object = MibTableColumn
blockdownOKSince = _BlockdownOKSince_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 6, 1, 1, 100),
    _BlockdownOKSince_Type()
)
blockdownOKSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    blockdownOKSince.setStatus("current")
_BlockdownConvGroups_ObjectIdentity = ObjectIdentity
blockdownConvGroups = _BlockdownConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 6, 10)
)
_BlockdownConvConformance_ObjectIdentity = ObjectIdentity
blockdownConvConformance = _BlockdownConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 6, 11)
)

# Managed Objects groups

blockdownCNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 6, 10, 1)
)
blockdownCNFReqGrp.setObjects(
    ("PEAKBLOCKDOWNCONVERTERS-MIB", "blockdownOKSince")
)
if mibBuilder.loadTexts:
    blockdownCNFReqGrp.setStatus("current")

blockdownCNFAttGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 6, 10, 2)
)
blockdownCNFAttGrp.setObjects(
    ("PEAKBLOCKDOWNCONVERTERS-MIB", "blockdownAttenuation")
)
if mibBuilder.loadTexts:
    blockdownCNFAttGrp.setStatus("current")

blockdownCNFBandGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 6, 10, 3)
)
blockdownCNFBandGrp.setObjects(
    ("PEAKBLOCKDOWNCONVERTERS-MIB", "blockdownBand")
)
if mibBuilder.loadTexts:
    blockdownCNFBandGrp.setStatus("current")

blockdownCNFNameGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 6, 10, 4)
)
blockdownCNFNameGrp.setObjects(
    ("PEAKBLOCKDOWNCONVERTERS-MIB", "blockdownName")
)
if mibBuilder.loadTexts:
    blockdownCNFNameGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

blockdownCNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 6, 11, 1)
)
blockdownCNFCompliance.setObjects(
      *(("PEAKBLOCKDOWNCONVERTERS-MIB", "blockdownCNFReqGrp"),
        ("PEAKBLOCKDOWNCONVERTERS-MIB", "blockdownCNFNameGrp"),
        ("PEAKBLOCKDOWNCONVERTERS-MIB", "blockdownCNFAttGrp"),
        ("PEAKBLOCKDOWNCONVERTERS-MIB", "blockdownCNFBandGrp"))
)
if mibBuilder.loadTexts:
    blockdownCNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKBLOCKDOWNCONVERTERS-MIB",
    **{"peakBlockDownConverterModule": peakBlockDownConverterModule,
       "blockdownTable": blockdownTable,
       "blockdownTableEntry": blockdownTableEntry,
       "blockdownIndex": blockdownIndex,
       "blockdownAttenuation": blockdownAttenuation,
       "blockdownBand": blockdownBand,
       "blockdownName": blockdownName,
       "blockdownOKSince": blockdownOKSince,
       "blockdownConvGroups": blockdownConvGroups,
       "blockdownCNFReqGrp": blockdownCNFReqGrp,
       "blockdownCNFAttGrp": blockdownCNFAttGrp,
       "blockdownCNFBandGrp": blockdownCNFBandGrp,
       "blockdownCNFNameGrp": blockdownCNFNameGrp,
       "blockdownConvConformance": blockdownConvConformance,
       "blockdownCNFCompliance": blockdownCNFCompliance}
)
