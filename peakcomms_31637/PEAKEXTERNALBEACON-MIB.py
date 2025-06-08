# SNMP MIB module (PEAKEXTERNALBEACON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKEXTERNALBEACON-MIB.mib
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

peakExternalBeaconModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 10)
)
if mibBuilder.loadTexts:
    peakExternalBeaconModule.setRevisions(
        ("2015-09-15 09:00",
         "2013-10-10 12:00",
         "2013-04-04 12:00",
         "2013-01-10 12:00",
         "2011-12-21 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ExtBeaconSlopeType(TextualConvention, Integer32):
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



class ExtBeaconInputRangeType(TextualConvention, Integer32):
    status = "current"
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
        *(("rp10V", 1),
          ("rpm10V", 2),
          ("rpm5V", 3),
          ("rm10V", 4))
    )



# MIB Managed Objects in the order of their OIDs

_ExternalBeaconTable_Object = MibTable
externalBeaconTable = _ExternalBeaconTable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    externalBeaconTable.setStatus("current")
_ExternalBeaconTableEntry_Object = MibTableRow
externalBeaconTableEntry = _ExternalBeaconTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 10, 1, 1)
)
externalBeaconTableEntry.setIndexNames(
    (0, "PEAKEXTERNALBEACON-MIB", "externalBeaconIndex"),
)
if mibBuilder.loadTexts:
    externalBeaconTableEntry.setStatus("current")


class _ExternalBeaconIndex_Type(Integer32):
    """Custom type externalBeaconIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ExternalBeaconIndex_Type.__name__ = "Integer32"
_ExternalBeaconIndex_Object = MibTableColumn
externalBeaconIndex = _ExternalBeaconIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 10, 1, 1, 1),
    _ExternalBeaconIndex_Type()
)
externalBeaconIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    externalBeaconIndex.setStatus("current")
_ExternalBeaconInputRange_Type = ExtBeaconInputRangeType
_ExternalBeaconInputRange_Object = MibTableColumn
externalBeaconInputRange = _ExternalBeaconInputRange_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 10, 1, 1, 2),
    _ExternalBeaconInputRange_Type()
)
externalBeaconInputRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalBeaconInputRange.setStatus("current")
_ExternalBeaconSlope_Type = ExtBeaconSlopeType
_ExternalBeaconSlope_Object = MibTableColumn
externalBeaconSlope = _ExternalBeaconSlope_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 10, 1, 1, 3),
    _ExternalBeaconSlope_Type()
)
externalBeaconSlope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalBeaconSlope.setStatus("current")
_ExternalBeaconLevel_Type = OctetString
_ExternalBeaconLevel_Object = MibTableColumn
externalBeaconLevel = _ExternalBeaconLevel_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 10, 1, 1, 4),
    _ExternalBeaconLevel_Type()
)
externalBeaconLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalBeaconLevel.setStatus("current")
_ExternalBeaconOffset_Type = OctetString
_ExternalBeaconOffset_Object = MibTableColumn
externalBeaconOffset = _ExternalBeaconOffset_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 10, 1, 1, 5),
    _ExternalBeaconOffset_Type()
)
externalBeaconOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalBeaconOffset.setStatus("current")
_ExternalBeaconOKSince_Type = OctetString
_ExternalBeaconOKSince_Object = MibTableColumn
externalBeaconOKSince = _ExternalBeaconOKSince_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 10, 1, 1, 100),
    _ExternalBeaconOKSince_Type()
)
externalBeaconOKSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalBeaconOKSince.setStatus("current")
_ExternalBeaconIntegers_ObjectIdentity = ObjectIdentity
externalBeaconIntegers = _ExternalBeaconIntegers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 10, 9)
)
_ExternalBeaconITable_Object = MibTable
externalBeaconITable = _ExternalBeaconITable_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 10, 9, 1)
)
if mibBuilder.loadTexts:
    externalBeaconITable.setStatus("current")
_ExternalBeaconITableEntry_Object = MibTableRow
externalBeaconITableEntry = _ExternalBeaconITableEntry_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 10, 9, 1, 1)
)
externalBeaconITableEntry.setIndexNames(
    (0, "PEAKEXTERNALBEACON-MIB", "externalBeaconIIndex"),
)
if mibBuilder.loadTexts:
    externalBeaconITableEntry.setStatus("current")


class _ExternalBeaconIIndex_Type(Integer32):
    """Custom type externalBeaconIIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ExternalBeaconIIndex_Type.__name__ = "Integer32"
_ExternalBeaconIIndex_Object = MibTableColumn
externalBeaconIIndex = _ExternalBeaconIIndex_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 10, 9, 1, 1, 1),
    _ExternalBeaconIIndex_Type()
)
externalBeaconIIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    externalBeaconIIndex.setStatus("current")
_ExternalBeaconILevel_Type = Integer32
_ExternalBeaconILevel_Object = MibTableColumn
externalBeaconILevel = _ExternalBeaconILevel_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 10, 9, 1, 1, 2),
    _ExternalBeaconILevel_Type()
)
externalBeaconILevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalBeaconILevel.setStatus("current")
_ExternalBeaconGroups_ObjectIdentity = ObjectIdentity
externalBeaconGroups = _ExternalBeaconGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 10, 10)
)
_ExternalBeaconConformance_ObjectIdentity = ObjectIdentity
externalBeaconConformance = _ExternalBeaconConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 10, 11)
)

# Managed Objects groups

externalbeaconCNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 10, 10, 1)
)
externalbeaconCNFReqGrp.setObjects(
      *(("PEAKEXTERNALBEACON-MIB", "externalBeaconInputRange"),
        ("PEAKEXTERNALBEACON-MIB", "externalBeaconSlope"),
        ("PEAKEXTERNALBEACON-MIB", "externalBeaconLevel"),
        ("PEAKEXTERNALBEACON-MIB", "externalBeaconOffset"),
        ("PEAKEXTERNALBEACON-MIB", "externalBeaconOKSince"))
)
if mibBuilder.loadTexts:
    externalbeaconCNFReqGrp.setStatus("current")

externalbeaconICNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 10, 10, 2)
)
externalbeaconICNFReqGrp.setObjects(
    ("PEAKEXTERNALBEACON-MIB", "externalBeaconILevel")
)
if mibBuilder.loadTexts:
    externalbeaconICNFReqGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

externalbeaconCNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 10, 11, 1)
)
externalbeaconCNFCompliance.setObjects(
      *(("PEAKEXTERNALBEACON-MIB", "externalbeaconCNFReqGrp"),
        ("PEAKEXTERNALBEACON-MIB", "externalbeaconICNFReqGrp"))
)
if mibBuilder.loadTexts:
    externalbeaconCNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKEXTERNALBEACON-MIB",
    **{"ExtBeaconSlopeType": ExtBeaconSlopeType,
       "ExtBeaconInputRangeType": ExtBeaconInputRangeType,
       "peakExternalBeaconModule": peakExternalBeaconModule,
       "externalBeaconTable": externalBeaconTable,
       "externalBeaconTableEntry": externalBeaconTableEntry,
       "externalBeaconIndex": externalBeaconIndex,
       "externalBeaconInputRange": externalBeaconInputRange,
       "externalBeaconSlope": externalBeaconSlope,
       "externalBeaconLevel": externalBeaconLevel,
       "externalBeaconOffset": externalBeaconOffset,
       "externalBeaconOKSince": externalBeaconOKSince,
       "externalBeaconIntegers": externalBeaconIntegers,
       "externalBeaconITable": externalBeaconITable,
       "externalBeaconITableEntry": externalBeaconITableEntry,
       "externalBeaconIIndex": externalBeaconIIndex,
       "externalBeaconILevel": externalBeaconILevel,
       "externalBeaconGroups": externalBeaconGroups,
       "externalbeaconCNFReqGrp": externalbeaconCNFReqGrp,
       "externalbeaconICNFReqGrp": externalbeaconICNFReqGrp,
       "externalBeaconConformance": externalBeaconConformance,
       "externalbeaconCNFCompliance": externalbeaconCNFCompliance}
)
