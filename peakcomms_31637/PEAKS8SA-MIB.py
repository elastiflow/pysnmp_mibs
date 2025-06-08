# SNMP MIB module (PEAKS8SA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/peakcomms_31637/PEAKS8SA-MIB.mib
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

(indvUnits,) = mibBuilder.importSymbols(
    "PEAKDEFINITIONS-MIB",
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

peakS8SAModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8029)
)
if mibBuilder.loadTexts:
    peakS8SAModule.setRevisions(
        ("2015-09-15 10:00",
         "2013-06-21 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _S8SAInput_Type(OctetString):
    """Custom type s8SAInput based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_S8SAInput_Type.__name__ = "OctetString"
_S8SAInput_Object = MibScalar
s8SAInput = _S8SAInput_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8029, 1),
    _S8SAInput_Type()
)
s8SAInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s8SAInput.setStatus("current")


class _S8SAWantedInput_Type(OctetString):
    """Custom type s8SAWantedInput based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_S8SAWantedInput_Type.__name__ = "OctetString"
_S8SAWantedInput_Object = MibScalar
s8SAWantedInput = _S8SAWantedInput_Object(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8029, 2),
    _S8SAWantedInput_Type()
)
s8SAWantedInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s8SAWantedInput.setStatus("current")
_S8SAConvGroups_ObjectIdentity = ObjectIdentity
s8SAConvGroups = _S8SAConvGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8029, 110)
)
_S8SAConvConformance_ObjectIdentity = ObjectIdentity
s8SAConvConformance = _S8SAConvConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8029, 111)
)

# Managed Objects groups

s8SACNFReqGrp = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8029, 110, 1)
)
s8SACNFReqGrp.setObjects(
      *(("PEAKS8SA-MIB", "s8SAInput"),
        ("PEAKS8SA-MIB", "s8SAWantedInput"))
)
if mibBuilder.loadTexts:
    s8SACNFReqGrp.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

s8SACNFCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 31637, 1, 3, 8029, 111, 1)
)
s8SACNFCompliance.setObjects(
    ("PEAKS8SA-MIB", "s8SACNFReqGrp")
)
if mibBuilder.loadTexts:
    s8SACNFCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PEAKS8SA-MIB",
    **{"peakS8SAModule": peakS8SAModule,
       "s8SAInput": s8SAInput,
       "s8SAWantedInput": s8SAWantedInput,
       "s8SAConvGroups": s8SAConvGroups,
       "s8SACNFReqGrp": s8SACNFReqGrp,
       "s8SAConvConformance": s8SAConvConformance,
       "s8SACNFCompliance": s8SACNFCompliance}
)
