# SNMP MIB module (SNMP-TSM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/SNMP-TSM-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 15:05:58 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

snmpTsmMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 190)
)
if mibBuilder.loadTexts:
    snmpTsmMIB.setRevisions(
        ("2009-06-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnmpTsmNotifications_ObjectIdentity = ObjectIdentity
snmpTsmNotifications = _SnmpTsmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 190, 0)
)
_SnmpTsmMIBObjects_ObjectIdentity = ObjectIdentity
snmpTsmMIBObjects = _SnmpTsmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 190, 1)
)
_SnmpTsmStats_ObjectIdentity = ObjectIdentity
snmpTsmStats = _SnmpTsmStats_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 190, 1, 1)
)
_SnmpTsmInvalidCaches_Type = Counter32
_SnmpTsmInvalidCaches_Object = MibScalar
snmpTsmInvalidCaches = _SnmpTsmInvalidCaches_Object(
    (1, 3, 6, 1, 2, 1, 190, 1, 1, 1),
    _SnmpTsmInvalidCaches_Type()
)
snmpTsmInvalidCaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTsmInvalidCaches.setStatus("current")
_SnmpTsmInadequateSecurityLevels_Type = Counter32
_SnmpTsmInadequateSecurityLevels_Object = MibScalar
snmpTsmInadequateSecurityLevels = _SnmpTsmInadequateSecurityLevels_Object(
    (1, 3, 6, 1, 2, 1, 190, 1, 1, 2),
    _SnmpTsmInadequateSecurityLevels_Type()
)
snmpTsmInadequateSecurityLevels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTsmInadequateSecurityLevels.setStatus("current")
_SnmpTsmUnknownPrefixes_Type = Counter32
_SnmpTsmUnknownPrefixes_Object = MibScalar
snmpTsmUnknownPrefixes = _SnmpTsmUnknownPrefixes_Object(
    (1, 3, 6, 1, 2, 1, 190, 1, 1, 3),
    _SnmpTsmUnknownPrefixes_Type()
)
snmpTsmUnknownPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTsmUnknownPrefixes.setStatus("current")
_SnmpTsmInvalidPrefixes_Type = Counter32
_SnmpTsmInvalidPrefixes_Object = MibScalar
snmpTsmInvalidPrefixes = _SnmpTsmInvalidPrefixes_Object(
    (1, 3, 6, 1, 2, 1, 190, 1, 1, 4),
    _SnmpTsmInvalidPrefixes_Type()
)
snmpTsmInvalidPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpTsmInvalidPrefixes.setStatus("current")
_SnmpTsmConfiguration_ObjectIdentity = ObjectIdentity
snmpTsmConfiguration = _SnmpTsmConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 190, 1, 2)
)


class _SnmpTsmConfigurationUsePrefix_Type(TruthValue):
    """Custom type snmpTsmConfigurationUsePrefix based on TruthValue"""
    defaultValue = 2


_SnmpTsmConfigurationUsePrefix_Type.__name__ = "TruthValue"
_SnmpTsmConfigurationUsePrefix_Object = MibScalar
snmpTsmConfigurationUsePrefix = _SnmpTsmConfigurationUsePrefix_Object(
    (1, 3, 6, 1, 2, 1, 190, 1, 2, 1),
    _SnmpTsmConfigurationUsePrefix_Type()
)
snmpTsmConfigurationUsePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTsmConfigurationUsePrefix.setStatus("current")
_SnmpTsmConformance_ObjectIdentity = ObjectIdentity
snmpTsmConformance = _SnmpTsmConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 190, 2)
)
_SnmpTsmCompliances_ObjectIdentity = ObjectIdentity
snmpTsmCompliances = _SnmpTsmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 190, 2, 1)
)
_SnmpTsmGroups_ObjectIdentity = ObjectIdentity
snmpTsmGroups = _SnmpTsmGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 190, 2, 2)
)

# Managed Objects groups

snmpTsmGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 190, 2, 2, 2)
)
snmpTsmGroup.setObjects(
      *(("SNMP-TSM-MIB", "snmpTsmInvalidCaches"),
        ("SNMP-TSM-MIB", "snmpTsmInadequateSecurityLevels"),
        ("SNMP-TSM-MIB", "snmpTsmUnknownPrefixes"),
        ("SNMP-TSM-MIB", "snmpTsmInvalidPrefixes"),
        ("SNMP-TSM-MIB", "snmpTsmConfigurationUsePrefix"))
)
if mibBuilder.loadTexts:
    snmpTsmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

snmpTsmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 190, 2, 1, 1)
)
snmpTsmCompliance.setObjects(
    ("SNMP-TSM-MIB", "snmpTsmGroup")
)
if mibBuilder.loadTexts:
    snmpTsmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMP-TSM-MIB",
    **{"snmpTsmMIB": snmpTsmMIB,
       "snmpTsmNotifications": snmpTsmNotifications,
       "snmpTsmMIBObjects": snmpTsmMIBObjects,
       "snmpTsmStats": snmpTsmStats,
       "snmpTsmInvalidCaches": snmpTsmInvalidCaches,
       "snmpTsmInadequateSecurityLevels": snmpTsmInadequateSecurityLevels,
       "snmpTsmUnknownPrefixes": snmpTsmUnknownPrefixes,
       "snmpTsmInvalidPrefixes": snmpTsmInvalidPrefixes,
       "snmpTsmConfiguration": snmpTsmConfiguration,
       "snmpTsmConfigurationUsePrefix": snmpTsmConfigurationUsePrefix,
       "snmpTsmConformance": snmpTsmConformance,
       "snmpTsmCompliances": snmpTsmCompliances,
       "snmpTsmCompliance": snmpTsmCompliance,
       "snmpTsmGroups": snmpTsmGroups,
       "snmpTsmGroup": snmpTsmGroup}
)
