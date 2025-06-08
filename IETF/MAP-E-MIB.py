# SNMP MIB module (MAP-E-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/MAP-E-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 20:19:28 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddressIPv4,
 InetAddressIPv6,
 InetAddressPrefixLength) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6",
    "InetAddressPrefixLength")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

mapMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 242)
)
if mibBuilder.loadTexts:
    mapMIB.setRevisions(
        ("2018-11-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RulePSID(TextualConvention, OctetString):
    status = "current"
    displayHint = "0x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixedLength = 2



class RuleType(TextualConvention, Integer32):
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
        *(("bmr", 1),
          ("fmr", 2),
          ("bmrAndfmr", 3))
    )



# MIB Managed Objects in the order of their OIDs

_MapMIBObjects_ObjectIdentity = ObjectIdentity
mapMIBObjects = _MapMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 242, 1)
)
_MapRule_ObjectIdentity = ObjectIdentity
mapRule = _MapRule_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 242, 1, 1)
)
_MapRuleTable_Object = MibTable
mapRuleTable = _MapRuleTable_Object(
    (1, 3, 6, 1, 2, 1, 242, 1, 1, 1)
)
if mibBuilder.loadTexts:
    mapRuleTable.setStatus("current")
_MapRuleEntry_Object = MibTableRow
mapRuleEntry = _MapRuleEntry_Object(
    (1, 3, 6, 1, 2, 1, 242, 1, 1, 1, 1)
)
mapRuleEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "MAP-E-MIB", "mapRuleID"),
)
if mibBuilder.loadTexts:
    mapRuleEntry.setStatus("current")


class _MapRuleID_Type(Unsigned32):
    """Custom type mapRuleID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_MapRuleID_Type.__name__ = "Unsigned32"
_MapRuleID_Object = MibTableColumn
mapRuleID = _MapRuleID_Object(
    (1, 3, 6, 1, 2, 1, 242, 1, 1, 1, 1, 1),
    _MapRuleID_Type()
)
mapRuleID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mapRuleID.setStatus("current")
_MapRuleIPv6Prefix_Type = InetAddressIPv6
_MapRuleIPv6Prefix_Object = MibTableColumn
mapRuleIPv6Prefix = _MapRuleIPv6Prefix_Object(
    (1, 3, 6, 1, 2, 1, 242, 1, 1, 1, 1, 2),
    _MapRuleIPv6Prefix_Type()
)
mapRuleIPv6Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapRuleIPv6Prefix.setStatus("current")
_MapRuleIPv6PrefixLen_Type = InetAddressPrefixLength
_MapRuleIPv6PrefixLen_Object = MibTableColumn
mapRuleIPv6PrefixLen = _MapRuleIPv6PrefixLen_Object(
    (1, 3, 6, 1, 2, 1, 242, 1, 1, 1, 1, 3),
    _MapRuleIPv6PrefixLen_Type()
)
mapRuleIPv6PrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapRuleIPv6PrefixLen.setStatus("current")
_MapRuleIPv4Prefix_Type = InetAddressIPv4
_MapRuleIPv4Prefix_Object = MibTableColumn
mapRuleIPv4Prefix = _MapRuleIPv4Prefix_Object(
    (1, 3, 6, 1, 2, 1, 242, 1, 1, 1, 1, 4),
    _MapRuleIPv4Prefix_Type()
)
mapRuleIPv4Prefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapRuleIPv4Prefix.setStatus("current")
_MapRuleIPv4PrefixLen_Type = InetAddressPrefixLength
_MapRuleIPv4PrefixLen_Object = MibTableColumn
mapRuleIPv4PrefixLen = _MapRuleIPv4PrefixLen_Object(
    (1, 3, 6, 1, 2, 1, 242, 1, 1, 1, 1, 5),
    _MapRuleIPv4PrefixLen_Type()
)
mapRuleIPv4PrefixLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapRuleIPv4PrefixLen.setStatus("current")
_MapRuleBRIPv6Address_Type = InetAddressIPv6
_MapRuleBRIPv6Address_Object = MibTableColumn
mapRuleBRIPv6Address = _MapRuleBRIPv6Address_Object(
    (1, 3, 6, 1, 2, 1, 242, 1, 1, 1, 1, 6),
    _MapRuleBRIPv6Address_Type()
)
mapRuleBRIPv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapRuleBRIPv6Address.setStatus("current")
_MapRulePSID_Type = RulePSID
_MapRulePSID_Object = MibTableColumn
mapRulePSID = _MapRulePSID_Object(
    (1, 3, 6, 1, 2, 1, 242, 1, 1, 1, 1, 7),
    _MapRulePSID_Type()
)
mapRulePSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapRulePSID.setStatus("current")


class _MapRulePSIDLen_Type(Unsigned32):
    """Custom type mapRulePSIDLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_MapRulePSIDLen_Type.__name__ = "Unsigned32"
_MapRulePSIDLen_Object = MibTableColumn
mapRulePSIDLen = _MapRulePSIDLen_Object(
    (1, 3, 6, 1, 2, 1, 242, 1, 1, 1, 1, 8),
    _MapRulePSIDLen_Type()
)
mapRulePSIDLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapRulePSIDLen.setStatus("current")


class _MapRuleOffset_Type(Unsigned32):
    """Custom type mapRuleOffset based on Unsigned32"""
    defaultValue = 6

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MapRuleOffset_Type.__name__ = "Unsigned32"
_MapRuleOffset_Object = MibTableColumn
mapRuleOffset = _MapRuleOffset_Object(
    (1, 3, 6, 1, 2, 1, 242, 1, 1, 1, 1, 9),
    _MapRuleOffset_Type()
)
mapRuleOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapRuleOffset.setStatus("current")


class _MapRuleEALen_Type(Unsigned32):
    """Custom type mapRuleEALen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 48),
    )


_MapRuleEALen_Type.__name__ = "Unsigned32"
_MapRuleEALen_Object = MibTableColumn
mapRuleEALen = _MapRuleEALen_Object(
    (1, 3, 6, 1, 2, 1, 242, 1, 1, 1, 1, 10),
    _MapRuleEALen_Type()
)
mapRuleEALen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapRuleEALen.setStatus("current")
_MapRuleType_Type = RuleType
_MapRuleType_Object = MibTableColumn
mapRuleType = _MapRuleType_Object(
    (1, 3, 6, 1, 2, 1, 242, 1, 1, 1, 1, 11),
    _MapRuleType_Type()
)
mapRuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapRuleType.setStatus("current")
_MapSecurityCheck_ObjectIdentity = ObjectIdentity
mapSecurityCheck = _MapSecurityCheck_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 242, 1, 2)
)
_MapSecurityCheckTable_Object = MibTable
mapSecurityCheckTable = _MapSecurityCheckTable_Object(
    (1, 3, 6, 1, 2, 1, 242, 1, 2, 1)
)
if mibBuilder.loadTexts:
    mapSecurityCheckTable.setStatus("current")
_MapSecurityCheckEntry_Object = MibTableRow
mapSecurityCheckEntry = _MapSecurityCheckEntry_Object(
    (1, 3, 6, 1, 2, 1, 242, 1, 2, 1, 1)
)
mapSecurityCheckEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mapSecurityCheckEntry.setStatus("current")
_MapSecurityCheckInvalidv4_Type = Counter64
_MapSecurityCheckInvalidv4_Object = MibTableColumn
mapSecurityCheckInvalidv4 = _MapSecurityCheckInvalidv4_Object(
    (1, 3, 6, 1, 2, 1, 242, 1, 2, 1, 1, 1),
    _MapSecurityCheckInvalidv4_Type()
)
mapSecurityCheckInvalidv4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapSecurityCheckInvalidv4.setStatus("current")
_MapSecurityCheckInvalidv6_Type = Counter64
_MapSecurityCheckInvalidv6_Object = MibTableColumn
mapSecurityCheckInvalidv6 = _MapSecurityCheckInvalidv6_Object(
    (1, 3, 6, 1, 2, 1, 242, 1, 2, 1, 1, 2),
    _MapSecurityCheckInvalidv6_Type()
)
mapSecurityCheckInvalidv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mapSecurityCheckInvalidv6.setStatus("current")
_MapMIBConformance_ObjectIdentity = ObjectIdentity
mapMIBConformance = _MapMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 242, 2)
)
_MapMIBCompliances_ObjectIdentity = ObjectIdentity
mapMIBCompliances = _MapMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 242, 2, 1)
)
_MapMIBGroups_ObjectIdentity = ObjectIdentity
mapMIBGroups = _MapMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 242, 2, 2)
)

# Managed Objects groups

mapMIBRuleGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 242, 2, 2, 1)
)
mapMIBRuleGroup.setObjects(
      *(("MAP-E-MIB", "mapRuleIPv6Prefix"),
        ("MAP-E-MIB", "mapRuleIPv6PrefixLen"),
        ("MAP-E-MIB", "mapRuleIPv4Prefix"),
        ("MAP-E-MIB", "mapRuleIPv4PrefixLen"),
        ("MAP-E-MIB", "mapRuleBRIPv6Address"),
        ("MAP-E-MIB", "mapRulePSID"),
        ("MAP-E-MIB", "mapRulePSIDLen"),
        ("MAP-E-MIB", "mapRuleOffset"),
        ("MAP-E-MIB", "mapRuleEALen"),
        ("MAP-E-MIB", "mapRuleType"))
)
if mibBuilder.loadTexts:
    mapMIBRuleGroup.setStatus("current")

mapMIBSecurityGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 242, 2, 2, 2)
)
mapMIBSecurityGroup.setObjects(
      *(("MAP-E-MIB", "mapSecurityCheckInvalidv4"),
        ("MAP-E-MIB", "mapSecurityCheckInvalidv6"))
)
if mibBuilder.loadTexts:
    mapMIBSecurityGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mapMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 242, 2, 1, 1)
)
mapMIBCompliance.setObjects(
      *(("MAP-E-MIB", "mapMIBRuleGroup"),
        ("MAP-E-MIB", "mapMIBSecurityGroup"))
)
if mibBuilder.loadTexts:
    mapMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MAP-E-MIB",
    **{"RulePSID": RulePSID,
       "RuleType": RuleType,
       "mapMIB": mapMIB,
       "mapMIBObjects": mapMIBObjects,
       "mapRule": mapRule,
       "mapRuleTable": mapRuleTable,
       "mapRuleEntry": mapRuleEntry,
       "mapRuleID": mapRuleID,
       "mapRuleIPv6Prefix": mapRuleIPv6Prefix,
       "mapRuleIPv6PrefixLen": mapRuleIPv6PrefixLen,
       "mapRuleIPv4Prefix": mapRuleIPv4Prefix,
       "mapRuleIPv4PrefixLen": mapRuleIPv4PrefixLen,
       "mapRuleBRIPv6Address": mapRuleBRIPv6Address,
       "mapRulePSID": mapRulePSID,
       "mapRulePSIDLen": mapRulePSIDLen,
       "mapRuleOffset": mapRuleOffset,
       "mapRuleEALen": mapRuleEALen,
       "mapRuleType": mapRuleType,
       "mapSecurityCheck": mapSecurityCheck,
       "mapSecurityCheckTable": mapSecurityCheckTable,
       "mapSecurityCheckEntry": mapSecurityCheckEntry,
       "mapSecurityCheckInvalidv4": mapSecurityCheckInvalidv4,
       "mapSecurityCheckInvalidv6": mapSecurityCheckInvalidv6,
       "mapMIBConformance": mapMIBConformance,
       "mapMIBCompliances": mapMIBCompliances,
       "mapMIBCompliance": mapMIBCompliance,
       "mapMIBGroups": mapMIBGroups,
       "mapMIBRuleGroup": mapMIBRuleGroup,
       "mapMIBSecurityGroup": mapMIBSecurityGroup}
)
