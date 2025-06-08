# SNMP MIB module (AIRCELL-AIRLINE-SNMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/aircell_28382/AIRCELL-AIRLINE-SNMP-MIB.mib
# Produced by pysmi-1.6.1 at Fri Jun  6 09:18:40 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

aircellLLC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 28382)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AircellABS_ObjectIdentity = ObjectIdentity
aircellABS = _AircellABS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1)
)
_AbsAirlineGroup_ObjectIdentity = ObjectIdentity
absAirlineGroup = _AbsAirlineGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 10)
)
_AbsAirlineSystems_ObjectIdentity = ObjectIdentity
absAirlineSystems = _AbsAirlineSystems_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 28382, 1, 10, 1)
)


class _AbsWifiState_Type(Integer32):
    """Custom type absWifiState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("degraded", 3))
    )


_AbsWifiState_Type.__name__ = "Integer32"
_AbsWifiState_Object = MibScalar
absWifiState = _AbsWifiState_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 10, 1, 1),
    _AbsWifiState_Type()
)
absWifiState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absWifiState.setStatus("current")


class _AbsCrewSSIDState_Type(Integer32):
    """Custom type absCrewSSIDState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AbsCrewSSIDState_Type.__name__ = "Integer32"
_AbsCrewSSIDState_Object = MibScalar
absCrewSSIDState = _AbsCrewSSIDState_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 10, 1, 2),
    _AbsCrewSSIDState_Type()
)
absCrewSSIDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absCrewSSIDState.setStatus("current")


class _AbsPaxSSIDState_Type(Integer32):
    """Custom type absPaxSSIDState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AbsPaxSSIDState_Type.__name__ = "Integer32"
_AbsPaxSSIDState_Object = MibScalar
absPaxSSIDState = _AbsPaxSSIDState_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 10, 1, 3),
    _AbsPaxSSIDState_Type()
)
absPaxSSIDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absPaxSSIDState.setStatus("current")


class _AbsAirlineSystemReset_Type(Integer32):
    """Custom type absAirlineSystemReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("enable", 1)
    )


_AbsAirlineSystemReset_Type.__name__ = "Integer32"
_AbsAirlineSystemReset_Object = MibScalar
absAirlineSystemReset = _AbsAirlineSystemReset_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 10, 1, 4),
    _AbsAirlineSystemReset_Type()
)
absAirlineSystemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    absAirlineSystemReset.setStatus("current")
_AbsSystemVersion_Type = DisplayString
_AbsSystemVersion_Object = MibScalar
absSystemVersion = _AbsSystemVersion_Object(
    (1, 3, 6, 1, 4, 1, 28382, 1, 10, 1, 5),
    _AbsSystemVersion_Type()
)
absSystemVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    absSystemVersion.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AIRCELL-AIRLINE-SNMP-MIB",
    **{"aircellLLC": aircellLLC,
       "aircellABS": aircellABS,
       "absAirlineGroup": absAirlineGroup,
       "absAirlineSystems": absAirlineSystems,
       "absWifiState": absWifiState,
       "absCrewSSIDState": absCrewSSIDState,
       "absPaxSSIDState": absPaxSSIDState,
       "absAirlineSystemReset": absAirlineSystemReset,
       "absSystemVersion": absSystemVersion}
)
