# SNMP MIB module (PEAKP7025BSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKP7025BSE-MIB.mib
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
 indvUnits) = mibBuilder.importSymbols(
    "PEAKDEFINITIONS-MIB",
    "OnOffType",
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

peakP7025BSEModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 1046)
)
if mibBuilder.loadTexts:
    peakP7025BSEModule.setRevisions(
        ("2015-09-15 10:00",
         "2013-04-04 12:00",
         "2013-01-02 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_P7025bseFrequency_Type = OctetString
_P7025bseFrequency_Object = MibScalar
p7025bseFrequency = _P7025bseFrequency_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 1046, 1),
    _P7025bseFrequency_Type()
)
p7025bseFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p7025bseFrequency.setStatus("current")
_P7025bseGainA_Type = OctetString
_P7025bseGainA_Object = MibScalar
p7025bseGainA = _P7025bseGainA_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 1046, 2),
    _P7025bseGainA_Type()
)
p7025bseGainA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p7025bseGainA.setStatus("current")
_P7025bseGainB_Type = OctetString
_P7025bseGainB_Object = MibScalar
p7025bseGainB = _P7025bseGainB_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 1046, 3),
    _P7025bseGainB_Type()
)
p7025bseGainB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p7025bseGainB.setStatus("current")
_P7025bseSpectrumInvert_Type = OnOffType
_P7025bseSpectrumInvert_Object = MibScalar
p7025bseSpectrumInvert = _P7025bseSpectrumInvert_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 1046, 4),
    _P7025bseSpectrumInvert_Type()
)
p7025bseSpectrumInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    p7025bseSpectrumInvert.setStatus("current")
_P7025bseConvGroups_ObjectIdentity = ObjectIdentity
p7025bseConvGroups = _P7025bseConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 1046, 110)
)
_P7025bseConvConformance_ObjectIdentity = ObjectIdentity
p7025bseConvConformance = _P7025bseConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 1046, 111)
)

# Managed Objects groups

p7025bseCNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 1046, 110, 1)
)
p7025bseCNFReqGrp.setObjects(
      *(("PEAKP7025BSE-MIB", "p7025bseFrequency"),
        ("PEAKP7025BSE-MIB", "p7025bseGainA"),
        ("PEAKP7025BSE-MIB", "p7025bseGainB"),
        ("PEAKP7025BSE-MIB", "p7025bseSpectrumInvert"))
)
if mibBuilder.loadTexts:
    p7025bseCNFReqGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

p7025bseCNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 1046, 111, 1)
)
p7025bseCNFCompliance.setObjects(
    ("PEAKP7025BSE-MIB", "p7025bseCNFReqGrp")
)
if mibBuilder.loadTexts:
    p7025bseCNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKP7025BSE-MIB",
    **{"peakP7025BSEModule": peakP7025BSEModule,
       "p7025bseFrequency": p7025bseFrequency,
       "p7025bseGainA": p7025bseGainA,
       "p7025bseGainB": p7025bseGainB,
       "p7025bseSpectrumInvert": p7025bseSpectrumInvert,
       "p7025bseConvGroups": p7025bseConvGroups,
       "p7025bseCNFReqGrp": p7025bseCNFReqGrp,
       "p7025bseConvConformance": p7025bseConvConformance,
       "p7025bseCNFCompliance": p7025bseCNFCompliance}
)
