# SNMP MIB module (PEAKRCU1XXX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKRCU1XXX-MIB.mib
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
 converters) = mibBuilder.importSymbols(
    "PEAKDEFINITIONS-MIB",
    "RedundancyModeType",
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

peakRCU1XXXModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 5)
)
if mibBuilder.loadTexts:
    peakRCU1XXXModule.setRevisions(
        ("2016-09-13 10:00",
         "2015-09-15 10:00",
         "2013-05-23 12:00",
         "2013-04-04 12:00",
         "2010-10-04 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Rcu1XXXRedundancyMode_Type = RedundancyModeType
_Rcu1XXXRedundancyMode_Object = MibScalar
rcu1XXXRedundancyMode = _Rcu1XXXRedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 5, 1),
    _Rcu1XXXRedundancyMode_Type()
)
rcu1XXXRedundancyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcu1XXXRedundancyMode.setStatus("current")


class _Rcu1XXXStandbyPosition_Type(OctetString):
    """Custom type rcu1XXXStandbyPosition based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_Rcu1XXXStandbyPosition_Type.__name__ = "OctetString"
_Rcu1XXXStandbyPosition_Object = MibScalar
rcu1XXXStandbyPosition = _Rcu1XXXStandbyPosition_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 5, 2),
    _Rcu1XXXStandbyPosition_Type()
)
rcu1XXXStandbyPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcu1XXXStandbyPosition.setStatus("current")
_Rcu1XXXAttenuation_Type = OctetString
_Rcu1XXXAttenuation_Object = MibScalar
rcu1XXXAttenuation = _Rcu1XXXAttenuation_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 5, 3),
    _Rcu1XXXAttenuation_Type()
)
rcu1XXXAttenuation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcu1XXXAttenuation.setStatus("current")
_Rcu1XXXConvGroups_ObjectIdentity = ObjectIdentity
rcu1XXXConvGroups = _Rcu1XXXConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 5, 110)
)
_Rcu1XXXConvConformance_ObjectIdentity = ObjectIdentity
rcu1XXXConvConformance = _Rcu1XXXConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 5, 111)
)

# Managed Objects groups

rcu1XXXCNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 5, 110, 1)
)
rcu1XXXCNFReqGrp.setObjects(
      *(("PEAKRCU1XXX-MIB", "rcu1XXXRedundancyMode"),
        ("PEAKRCU1XXX-MIB", "rcu1XXXStandbyPosition"))
)
if mibBuilder.loadTexts:
    rcu1XXXCNFReqGrp.setStatus("current")

rcu1XXXCNFRAttenuationGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 5, 110, 2)
)
rcu1XXXCNFRAttenuationGrp.setObjects(
    ("PEAKRCU1XXX-MIB", "rcu1XXXAttenuation")
)
if mibBuilder.loadTexts:
    rcu1XXXCNFRAttenuationGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rcu1XXXCNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 5, 111, 1)
)
rcu1XXXCNFCompliance.setObjects(
      *(("PEAKRCU1XXX-MIB", "rcu1XXXCNFReqGrp"),
        ("PEAKRCU1XXX-MIB", "rcu1XXXCNFRAttenuationGrp"))
)
if mibBuilder.loadTexts:
    rcu1XXXCNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKRCU1XXX-MIB",
    **{"peakRCU1XXXModule": peakRCU1XXXModule,
       "rcu1XXXRedundancyMode": rcu1XXXRedundancyMode,
       "rcu1XXXStandbyPosition": rcu1XXXStandbyPosition,
       "rcu1XXXAttenuation": rcu1XXXAttenuation,
       "rcu1XXXConvGroups": rcu1XXXConvGroups,
       "rcu1XXXCNFReqGrp": rcu1XXXCNFReqGrp,
       "rcu1XXXCNFRAttenuationGrp": rcu1XXXCNFRAttenuationGrp,
       "rcu1XXXConvConformance": rcu1XXXConvConformance,
       "rcu1XXXCNFCompliance": rcu1XXXCNFCompliance}
)
