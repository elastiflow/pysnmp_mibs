# SNMP MIB module (SNMP-SSH-TM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/Standards/IETF/SNMP-SSH-TM-MIB.mib
# Produced by pysmi-1.5.11 at Wed May 21 15:05:48 2025
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
 mib_2,
 snmpDomains) = mibBuilder.importSymbols(
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
    "mib-2",
    "snmpDomains")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

snmpSshtmMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 189)
)
if mibBuilder.loadTexts:
    snmpSshtmMIB.setRevisions(
        ("2009-06-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SnmpSSHAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "1a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



# MIB Managed Objects in the order of their OIDs

_SnmpSshtmNotifications_ObjectIdentity = ObjectIdentity
snmpSshtmNotifications = _SnmpSshtmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 189, 0)
)
_SnmpSshtmObjects_ObjectIdentity = ObjectIdentity
snmpSshtmObjects = _SnmpSshtmObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 189, 1)
)
_SnmpSshtmSession_ObjectIdentity = ObjectIdentity
snmpSshtmSession = _SnmpSshtmSession_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 189, 1, 1)
)
_SnmpSshtmSessionOpens_Type = Counter32
_SnmpSshtmSessionOpens_Object = MibScalar
snmpSshtmSessionOpens = _SnmpSshtmSessionOpens_Object(
    (1, 3, 6, 1, 2, 1, 189, 1, 1, 1),
    _SnmpSshtmSessionOpens_Type()
)
snmpSshtmSessionOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpSshtmSessionOpens.setStatus("current")
_SnmpSshtmSessionCloses_Type = Counter32
_SnmpSshtmSessionCloses_Object = MibScalar
snmpSshtmSessionCloses = _SnmpSshtmSessionCloses_Object(
    (1, 3, 6, 1, 2, 1, 189, 1, 1, 2),
    _SnmpSshtmSessionCloses_Type()
)
snmpSshtmSessionCloses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpSshtmSessionCloses.setStatus("current")
_SnmpSshtmSessionOpenErrors_Type = Counter32
_SnmpSshtmSessionOpenErrors_Object = MibScalar
snmpSshtmSessionOpenErrors = _SnmpSshtmSessionOpenErrors_Object(
    (1, 3, 6, 1, 2, 1, 189, 1, 1, 3),
    _SnmpSshtmSessionOpenErrors_Type()
)
snmpSshtmSessionOpenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpSshtmSessionOpenErrors.setStatus("current")
_SnmpSshtmSessionUserAuthFailures_Type = Counter32
_SnmpSshtmSessionUserAuthFailures_Object = MibScalar
snmpSshtmSessionUserAuthFailures = _SnmpSshtmSessionUserAuthFailures_Object(
    (1, 3, 6, 1, 2, 1, 189, 1, 1, 4),
    _SnmpSshtmSessionUserAuthFailures_Type()
)
snmpSshtmSessionUserAuthFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpSshtmSessionUserAuthFailures.setStatus("current")
_SnmpSshtmSessionNoChannels_Type = Counter32
_SnmpSshtmSessionNoChannels_Object = MibScalar
snmpSshtmSessionNoChannels = _SnmpSshtmSessionNoChannels_Object(
    (1, 3, 6, 1, 2, 1, 189, 1, 1, 5),
    _SnmpSshtmSessionNoChannels_Type()
)
snmpSshtmSessionNoChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpSshtmSessionNoChannels.setStatus("current")
_SnmpSshtmSessionNoSubsystems_Type = Counter32
_SnmpSshtmSessionNoSubsystems_Object = MibScalar
snmpSshtmSessionNoSubsystems = _SnmpSshtmSessionNoSubsystems_Object(
    (1, 3, 6, 1, 2, 1, 189, 1, 1, 6),
    _SnmpSshtmSessionNoSubsystems_Type()
)
snmpSshtmSessionNoSubsystems.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpSshtmSessionNoSubsystems.setStatus("current")
_SnmpSshtmSessionNoSessions_Type = Counter32
_SnmpSshtmSessionNoSessions_Object = MibScalar
snmpSshtmSessionNoSessions = _SnmpSshtmSessionNoSessions_Object(
    (1, 3, 6, 1, 2, 1, 189, 1, 1, 7),
    _SnmpSshtmSessionNoSessions_Type()
)
snmpSshtmSessionNoSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpSshtmSessionNoSessions.setStatus("current")
_SnmpSshtmSessionInvalidCaches_Type = Counter32
_SnmpSshtmSessionInvalidCaches_Object = MibScalar
snmpSshtmSessionInvalidCaches = _SnmpSshtmSessionInvalidCaches_Object(
    (1, 3, 6, 1, 2, 1, 189, 1, 1, 8),
    _SnmpSshtmSessionInvalidCaches_Type()
)
snmpSshtmSessionInvalidCaches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpSshtmSessionInvalidCaches.setStatus("current")
_SnmpSshtmConformance_ObjectIdentity = ObjectIdentity
snmpSshtmConformance = _SnmpSshtmConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 189, 2)
)
_SnmpSshtmCompliances_ObjectIdentity = ObjectIdentity
snmpSshtmCompliances = _SnmpSshtmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 189, 2, 1)
)
_SnmpSshtmGroups_ObjectIdentity = ObjectIdentity
snmpSshtmGroups = _SnmpSshtmGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 189, 2, 2)
)
_SnmpSSHDomain_ObjectIdentity = ObjectIdentity
snmpSSHDomain = _SnmpSSHDomain_ObjectIdentity(
    (1, 3, 6, 1, 6, 1, 7)
)
if mibBuilder.loadTexts:
    snmpSSHDomain.setStatus("current")

# Managed Objects groups

snmpSshtmGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 189, 2, 2, 2)
)
snmpSshtmGroup.setObjects(
      *(("SNMP-SSH-TM-MIB", "snmpSshtmSessionOpens"),
        ("SNMP-SSH-TM-MIB", "snmpSshtmSessionCloses"),
        ("SNMP-SSH-TM-MIB", "snmpSshtmSessionOpenErrors"),
        ("SNMP-SSH-TM-MIB", "snmpSshtmSessionUserAuthFailures"),
        ("SNMP-SSH-TM-MIB", "snmpSshtmSessionNoChannels"),
        ("SNMP-SSH-TM-MIB", "snmpSshtmSessionNoSubsystems"),
        ("SNMP-SSH-TM-MIB", "snmpSshtmSessionNoSessions"),
        ("SNMP-SSH-TM-MIB", "snmpSshtmSessionInvalidCaches"))
)
if mibBuilder.loadTexts:
    snmpSshtmGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

snmpSshtmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 189, 2, 1, 1)
)
snmpSshtmCompliance.setObjects(
    ("SNMP-SSH-TM-MIB", "snmpSshtmGroup")
)
if mibBuilder.loadTexts:
    snmpSshtmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SNMP-SSH-TM-MIB",
    **{"SnmpSSHAddress": SnmpSSHAddress,
       "snmpSshtmMIB": snmpSshtmMIB,
       "snmpSshtmNotifications": snmpSshtmNotifications,
       "snmpSshtmObjects": snmpSshtmObjects,
       "snmpSshtmSession": snmpSshtmSession,
       "snmpSshtmSessionOpens": snmpSshtmSessionOpens,
       "snmpSshtmSessionCloses": snmpSshtmSessionCloses,
       "snmpSshtmSessionOpenErrors": snmpSshtmSessionOpenErrors,
       "snmpSshtmSessionUserAuthFailures": snmpSshtmSessionUserAuthFailures,
       "snmpSshtmSessionNoChannels": snmpSshtmSessionNoChannels,
       "snmpSshtmSessionNoSubsystems": snmpSshtmSessionNoSubsystems,
       "snmpSshtmSessionNoSessions": snmpSshtmSessionNoSessions,
       "snmpSshtmSessionInvalidCaches": snmpSshtmSessionInvalidCaches,
       "snmpSshtmConformance": snmpSshtmConformance,
       "snmpSshtmCompliances": snmpSshtmCompliances,
       "snmpSshtmCompliance": snmpSshtmCompliance,
       "snmpSshtmGroups": snmpSshtmGroups,
       "snmpSshtmGroup": snmpSshtmGroup,
       "snmpSSHDomain": snmpSSHDomain}
)
