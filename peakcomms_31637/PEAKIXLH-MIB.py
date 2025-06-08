# SNMP MIB module (PEAKIXLH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKIXLH-MIB.mib
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

(RedundancyModeType,
 YesNoType,
 converters) = mibBuilder.importSymbols(
    "PEAKDEFINITIONS-MIB",
    "RedundancyModeType",
    "YesNoType",
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

peakIXLHModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 15)
)
if mibBuilder.loadTexts:
    peakIXLHModule.setRevisions(
        ("2015-09-11 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class IXLHChannelType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("splitter", 1),
          ("combiner", 2),
          ("undefined", 3))
    )



class IXLHAmpId(TextualConvention, Integer32):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_IxlhCTable_Object = MibTable
ixlhCTable = _IxlhCTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 15, 1)
)
if mibBuilder.loadTexts:
    ixlhCTable.setStatus("current")
_IxlhCTableEntry_Object = MibTableRow
ixlhCTableEntry = _IxlhCTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 15, 1, 1)
)
ixlhCTableEntry.setIndexNames(
    (0, "PEAKIXLH-MIB", "ixlhCIndex"),
)
if mibBuilder.loadTexts:
    ixlhCTableEntry.setStatus("current")


class _IxlhCIndex_Type(Integer32):
    """Custom type ixlhCIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_IxlhCIndex_Type.__name__ = "Integer32"
_IxlhCIndex_Object = MibTableColumn
ixlhCIndex = _IxlhCIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 15, 1, 1, 1),
    _IxlhCIndex_Type()
)
ixlhCIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ixlhCIndex.setStatus("current")
_IxlhCChannelNo_Type = Integer32
_IxlhCChannelNo_Object = MibTableColumn
ixlhCChannelNo = _IxlhCChannelNo_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 15, 1, 1, 2),
    _IxlhCChannelNo_Type()
)
ixlhCChannelNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ixlhCChannelNo.setStatus("current")
_IxlhCType_Type = IXLHChannelType
_IxlhCType_Object = MibTableColumn
ixlhCType = _IxlhCType_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 15, 1, 1, 3),
    _IxlhCType_Type()
)
ixlhCType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ixlhCType.setStatus("current")
_IxlhCAttenuation_Type = OctetString
_IxlhCAttenuation_Object = MibTableColumn
ixlhCAttenuation = _IxlhCAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 15, 1, 1, 4),
    _IxlhCAttenuation_Type()
)
ixlhCAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ixlhCAttenuation.setStatus("current")


class _IxlhCRedundancy_Type(RedundancyModeType):
    """Custom type ixlhCRedundancy based on RedundancyModeType"""
    subtypeSpec = RedundancyModeType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("auto", 2))
    )


_IxlhCRedundancy_Type.__name__ = "RedundancyModeType"
_IxlhCRedundancy_Object = MibTableColumn
ixlhCRedundancy = _IxlhCRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 15, 1, 1, 5),
    _IxlhCRedundancy_Type()
)
ixlhCRedundancy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ixlhCRedundancy.setStatus("current")
_IxlhCAmpOnline_Type = IXLHAmpId
_IxlhCAmpOnline_Object = MibTableColumn
ixlhCAmpOnline = _IxlhCAmpOnline_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 15, 1, 1, 6),
    _IxlhCAmpOnline_Type()
)
ixlhCAmpOnline.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ixlhCAmpOnline.setStatus("current")
_IxlhCOkSince_Type = OctetString
_IxlhCOkSince_Object = MibTableColumn
ixlhCOkSince = _IxlhCOkSince_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 15, 1, 1, 7),
    _IxlhCOkSince_Type()
)
ixlhCOkSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ixlhCOkSince.setStatus("current")
_IxlhPTable_Object = MibTable
ixlhPTable = _IxlhPTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 15, 2)
)
if mibBuilder.loadTexts:
    ixlhPTable.setStatus("current")
_IxlhPTableEntry_Object = MibTableRow
ixlhPTableEntry = _IxlhPTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 15, 2, 1)
)
ixlhPTableEntry.setIndexNames(
    (0, "PEAKIXLH-MIB", "ixlhPIndex"),
)
if mibBuilder.loadTexts:
    ixlhPTableEntry.setStatus("current")


class _IxlhPIndex_Type(Integer32):
    """Custom type ixlhPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_IxlhPIndex_Type.__name__ = "Integer32"
_IxlhPIndex_Object = MibTableColumn
ixlhPIndex = _IxlhPIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 15, 2, 1, 1),
    _IxlhPIndex_Type()
)
ixlhPIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ixlhPIndex.setStatus("current")
_IxlhPPresent_Type = YesNoType
_IxlhPPresent_Object = MibTableColumn
ixlhPPresent = _IxlhPPresent_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 15, 2, 1, 2),
    _IxlhPPresent_Type()
)
ixlhPPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ixlhPPresent.setStatus("current")
_IxlhPPowered_Type = YesNoType
_IxlhPPowered_Object = MibTableColumn
ixlhPPowered = _IxlhPPowered_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 15, 2, 1, 3),
    _IxlhPPowered_Type()
)
ixlhPPowered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ixlhPPowered.setStatus("current")
_IxlhIntegers_ObjectIdentity = ObjectIdentity
ixlhIntegers = _IxlhIntegers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 15, 109)
)
_IxlhConvGroups_ObjectIdentity = ObjectIdentity
ixlhConvGroups = _IxlhConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 15, 110)
)
_IxlhConvConformance_ObjectIdentity = ObjectIdentity
ixlhConvConformance = _IxlhConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 15, 111)
)

# Managed Objects groups

ixlhCNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 15, 110, 1)
)
ixlhCNFReqGrp.setObjects(
      *(("PEAKIXLH-MIB", "ixlhPPresent"),
        ("PEAKIXLH-MIB", "ixlhPPowered"),
        ("PEAKIXLH-MIB", "ixlhCChannelNo"),
        ("PEAKIXLH-MIB", "ixlhCType"),
        ("PEAKIXLH-MIB", "ixlhCOkSince"))
)
if mibBuilder.loadTexts:
    ixlhCNFReqGrp.setStatus("current")

ixlhCNFAttenuationGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 15, 110, 2)
)
ixlhCNFAttenuationGrp.setObjects(
    ("PEAKIXLH-MIB", "ixlhCAttenuation")
)
if mibBuilder.loadTexts:
    ixlhCNFAttenuationGrp.setStatus("current")

ixlhCNFAmpGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 15, 110, 3)
)
ixlhCNFAmpGrp.setObjects(
      *(("PEAKIXLH-MIB", "ixlhCRedundancy"),
        ("PEAKIXLH-MIB", "ixlhCAmpOnline"))
)
if mibBuilder.loadTexts:
    ixlhCNFAmpGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ixlhCNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 15, 111, 1)
)
ixlhCNFCompliance.setObjects(
      *(("PEAKIXLH-MIB", "ixlhCNFReqGrp"),
        ("PEAKIXLH-MIB", "ixlhCNFAttenuationGrp"),
        ("PEAKIXLH-MIB", "ixlhCNFAmpGrp"))
)
if mibBuilder.loadTexts:
    ixlhCNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKIXLH-MIB",
    **{"IXLHChannelType": IXLHChannelType,
       "IXLHAmpId": IXLHAmpId,
       "peakIXLHModule": peakIXLHModule,
       "ixlhCTable": ixlhCTable,
       "ixlhCTableEntry": ixlhCTableEntry,
       "ixlhCIndex": ixlhCIndex,
       "ixlhCChannelNo": ixlhCChannelNo,
       "ixlhCType": ixlhCType,
       "ixlhCAttenuation": ixlhCAttenuation,
       "ixlhCRedundancy": ixlhCRedundancy,
       "ixlhCAmpOnline": ixlhCAmpOnline,
       "ixlhCOkSince": ixlhCOkSince,
       "ixlhPTable": ixlhPTable,
       "ixlhPTableEntry": ixlhPTableEntry,
       "ixlhPIndex": ixlhPIndex,
       "ixlhPPresent": ixlhPPresent,
       "ixlhPPowered": ixlhPPowered,
       "ixlhIntegers": ixlhIntegers,
       "ixlhConvGroups": ixlhConvGroups,
       "ixlhCNFReqGrp": ixlhCNFReqGrp,
       "ixlhCNFAttenuationGrp": ixlhCNFAttenuationGrp,
       "ixlhCNFAmpGrp": ixlhCNFAmpGrp,
       "ixlhConvConformance": ixlhConvConformance,
       "ixlhCNFCompliance": ixlhCNFCompliance}
)
