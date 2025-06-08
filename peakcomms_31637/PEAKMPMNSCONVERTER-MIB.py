# SNMP MIB module (PEAKMPMNSCONVERTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKMPMNSCONVERTER-MIB.mib
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

(nsConverters,) = mibBuilder.importSymbols(
    "PEAKDEFINITIONS-MIB",
    "nsConverters")

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

peakMPMNSConverterModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 1)
)
if mibBuilder.loadTexts:
    peakMPMNSConverterModule.setRevisions(
        ("2015-09-15 10:00",
         "2013-04-04 12:00",
         "2012-07-02 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MPMBandType(TextualConvention, Integer32):
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
        *(("fc2", 1),
          ("fc3", 2),
          ("unknown", 3))
    )



# MIB Managed Objects in the order of their OIDs

_MpmUpGain_Type = OctetString
_MpmUpGain_Object = MibScalar
mpmUpGain = _MpmUpGain_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 1, 1),
    _MpmUpGain_Type()
)
mpmUpGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpmUpGain.setStatus("current")
_MpmDownGain_Type = OctetString
_MpmDownGain_Object = MibScalar
mpmDownGain = _MpmDownGain_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 1, 2),
    _MpmDownGain_Type()
)
mpmDownGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpmDownGain.setStatus("current")
_MpmBand_Type = MPMBandType
_MpmBand_Object = MibScalar
mpmBand = _MpmBand_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 1, 3),
    _MpmBand_Type()
)
mpmBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mpmBand.setStatus("current")
_MpmOKSince_Type = OctetString
_MpmOKSince_Object = MibScalar
mpmOKSince = _MpmOKSince_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 1, 4),
    _MpmOKSince_Type()
)
mpmOKSince.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mpmOKSince.setStatus("current")
_MpmConvGroups_ObjectIdentity = ObjectIdentity
mpmConvGroups = _MpmConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 1, 10)
)
_MpmConvConformance_ObjectIdentity = ObjectIdentity
mpmConvConformance = _MpmConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 1, 11)
)

# Managed Objects groups

mpmCNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 1, 10, 1)
)
mpmCNFReqGrp.setObjects(
      *(("PEAKMPMNSCONVERTER-MIB", "mpmUpGain"),
        ("PEAKMPMNSCONVERTER-MIB", "mpmDownGain"),
        ("PEAKMPMNSCONVERTER-MIB", "mpmBand"),
        ("PEAKMPMNSCONVERTER-MIB", "mpmOKSince"))
)
if mibBuilder.loadTexts:
    mpmCNFReqGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mpmCNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 1, 11, 1)
)
mpmCNFCompliance.setObjects(
    ("PEAKMPMNSCONVERTER-MIB", "mpmCNFReqGrp")
)
if mibBuilder.loadTexts:
    mpmCNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKMPMNSCONVERTER-MIB",
    **{"MPMBandType": MPMBandType,
       "peakMPMNSConverterModule": peakMPMNSConverterModule,
       "mpmUpGain": mpmUpGain,
       "mpmDownGain": mpmDownGain,
       "mpmBand": mpmBand,
       "mpmOKSince": mpmOKSince,
       "mpmConvGroups": mpmConvGroups,
       "mpmCNFReqGrp": mpmCNFReqGrp,
       "mpmConvConformance": mpmConvConformance,
       "mpmCNFCompliance": mpmCNFCompliance}
)
