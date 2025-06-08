# SNMP MIB module (PEAKISB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKISB-MIB.mib
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

peakISBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 4)
)
if mibBuilder.loadTexts:
    peakISBModule.setRevisions(
        ("2015-09-18 09:00",
         "2015-09-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _IsbWantedSwitchPosition_Type(OctetString):
    """Custom type isbWantedSwitchPosition based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_IsbWantedSwitchPosition_Type.__name__ = "OctetString"
_IsbWantedSwitchPosition_Object = MibScalar
isbWantedSwitchPosition = _IsbWantedSwitchPosition_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 4, 1),
    _IsbWantedSwitchPosition_Type()
)
isbWantedSwitchPosition.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    isbWantedSwitchPosition.setStatus("current")


class _IsbActualSwitchPosition_Type(OctetString):
    """Custom type isbActualSwitchPosition based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_IsbActualSwitchPosition_Type.__name__ = "OctetString"
_IsbActualSwitchPosition_Object = MibScalar
isbActualSwitchPosition = _IsbActualSwitchPosition_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 4, 2),
    _IsbActualSwitchPosition_Type()
)
isbActualSwitchPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    isbActualSwitchPosition.setStatus("current")
_IsbConvGroups_ObjectIdentity = ObjectIdentity
isbConvGroups = _IsbConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 4, 110)
)
_IsbConvConformance_ObjectIdentity = ObjectIdentity
isbConvConformance = _IsbConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 4, 111)
)

# Managed Objects groups

isbCNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 4, 110, 1)
)
isbCNFReqGrp.setObjects(
      *(("PEAKISB-MIB", "isbWantedSwitchPosition"),
        ("PEAKISB-MIB", "isbActualSwitchPosition"))
)
if mibBuilder.loadTexts:
    isbCNFReqGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

isbCNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 1, 100, 4, 111, 1)
)
isbCNFCompliance.setObjects(
    ("PEAKISB-MIB", "isbCNFReqGrp")
)
if mibBuilder.loadTexts:
    isbCNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKISB-MIB",
    **{"peakISBModule": peakISBModule,
       "isbWantedSwitchPosition": isbWantedSwitchPosition,
       "isbActualSwitchPosition": isbActualSwitchPosition,
       "isbConvGroups": isbConvGroups,
       "isbCNFReqGrp": isbCNFReqGrp,
       "isbConvConformance": isbConvConformance,
       "isbCNFCompliance": isbCNFCompliance}
)
