# SNMP MIB module (PEAKD600-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKD600-MIB.mib
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

(OnOffType,
 RemoteLocalType,
 indvUnits) = mibBuilder.importSymbols(
    "PEAKDEFINITIONS-MIB",
    "OnOffType",
    "RemoteLocalType",
    "indvUnits")

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

peakD600Module = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8000)
)
if mibBuilder.loadTexts:
    peakD600Module.setRevisions(
        ("2015-09-15 09:00",
         "2013-04-04 12:00",
         "2010-06-16 16:06")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class D600BandType(TextualConvention, Integer32):
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
        *(("band1", 1),
          ("band2", 2),
          ("unknown", 3))
    )



class D600WantedBandType(TextualConvention, Integer32):
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
        *(("band1", 1),
          ("band2", 2),
          ("unknown", 3))
    )



# MIB Managed Objects in the order of their OIDs

_D600Type_Type = OctetString
_D600Type_Object = MibScalar
d600Type = _D600Type_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8000, 1),
    _D600Type_Type()
)
d600Type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d600Type.setStatus("current")


class _D600SerialNo_Type(Integer32):
    """Custom type d600SerialNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99999),
    )


_D600SerialNo_Type.__name__ = "Integer32"
_D600SerialNo_Object = MibScalar
d600SerialNo = _D600SerialNo_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8000, 2),
    _D600SerialNo_Type()
)
d600SerialNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d600SerialNo.setStatus("current")
_D600SoftwareVersion_Type = OctetString
_D600SoftwareVersion_Object = MibScalar
d600SoftwareVersion = _D600SoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8000, 3),
    _D600SoftwareVersion_Type()
)
d600SoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d600SoftwareVersion.setStatus("current")
_D600Remote_Type = RemoteLocalType
_D600Remote_Object = MibScalar
d600Remote = _D600Remote_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8000, 4),
    _D600Remote_Type()
)
d600Remote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d600Remote.setStatus("current")
_D600Band_Type = D600BandType
_D600Band_Object = MibScalar
d600Band = _D600Band_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8000, 5),
    _D600Band_Type()
)
d600Band.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d600Band.setStatus("current")
_D600UnitA_Type = OnOffType
_D600UnitA_Object = MibScalar
d600UnitA = _D600UnitA_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8000, 6),
    _D600UnitA_Type()
)
d600UnitA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d600UnitA.setStatus("current")
_D600UnitB_Type = OnOffType
_D600UnitB_Object = MibScalar
d600UnitB = _D600UnitB_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8000, 7),
    _D600UnitB_Type()
)
d600UnitB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    d600UnitB.setStatus("current")
_D600WantedBand_Type = D600WantedBandType
_D600WantedBand_Object = MibScalar
d600WantedBand = _D600WantedBand_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8000, 8),
    _D600WantedBand_Type()
)
d600WantedBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    d600WantedBand.setStatus("current")
_D600ConvGroups_ObjectIdentity = ObjectIdentity
d600ConvGroups = _D600ConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8000, 110)
)
_D600ConvConformance_ObjectIdentity = ObjectIdentity
d600ConvConformance = _D600ConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8000, 111)
)

# Managed Objects groups

d600CNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8000, 110, 1)
)
d600CNFReqGrp.setObjects(
      *(("PEAKD600-MIB", "d600Type"),
        ("PEAKD600-MIB", "d600SerialNo"),
        ("PEAKD600-MIB", "d600SoftwareVersion"),
        ("PEAKD600-MIB", "d600Remote"),
        ("PEAKD600-MIB", "d600UnitA"),
        ("PEAKD600-MIB", "d600UnitB"))
)
if mibBuilder.loadTexts:
    d600CNFReqGrp.setStatus("current")

d600CNFReqBandGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8000, 110, 2)
)
d600CNFReqBandGrp.setObjects(
      *(("PEAKD600-MIB", "d600Band"),
        ("PEAKD600-MIB", "d600WantedBand"))
)
if mibBuilder.loadTexts:
    d600CNFReqBandGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

d600Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8000, 111, 1)
)
d600Compliance.setObjects(
      *(("PEAKD600-MIB", "d600CNFReqGrp"),
        ("PEAKD600-MIB", "d600CNFReqBandGrp"))
)
if mibBuilder.loadTexts:
    d600Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKD600-MIB",
    **{"D600BandType": D600BandType,
       "D600WantedBandType": D600WantedBandType,
       "peakD600Module": peakD600Module,
       "d600Type": d600Type,
       "d600SerialNo": d600SerialNo,
       "d600SoftwareVersion": d600SoftwareVersion,
       "d600Remote": d600Remote,
       "d600Band": d600Band,
       "d600UnitA": d600UnitA,
       "d600UnitB": d600UnitB,
       "d600WantedBand": d600WantedBand,
       "d600ConvGroups": d600ConvGroups,
       "d600CNFReqGrp": d600CNFReqGrp,
       "d600CNFReqBandGrp": d600CNFReqBandGrp,
       "d600ConvConformance": d600ConvConformance,
       "d600Compliance": d600Compliance}
)
