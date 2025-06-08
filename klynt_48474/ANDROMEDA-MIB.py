# SNMP MIB module (ANDROMEDA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/klynt_48474/ANDROMEDA-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 10:59:36 2025
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

moduleIdentityAndromeda = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 48474)
)
if mibBuilder.loadTexts:
    moduleIdentityAndromeda.setRevisions(
        ("2017-08-26 10:25",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AndromedaComponents_ObjectIdentity = ObjectIdentity
andromedaComponents = _AndromedaComponents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48474, 1)
)
_AndromedaSystem_ObjectIdentity = ObjectIdentity
andromedaSystem = _AndromedaSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48474, 1, 1)
)
_AndromedaVoIP_ObjectIdentity = ObjectIdentity
andromedaVoIP = _AndromedaVoIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48474, 1, 2)
)


class _AndromedaGrps_Type(Gauge32):
    """Custom type andromedaGrps based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AndromedaGrps_Type.__name__ = "Gauge32"
_AndromedaGrps_Object = MibScalar
andromedaGrps = _AndromedaGrps_Object(
    (1, 3, 6, 1, 4, 1, 48474, 1, 2, 1),
    _AndromedaGrps_Type()
)
andromedaGrps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    andromedaGrps.setStatus("current")


class _AndromedaSubs_Type(Gauge32):
    """Custom type andromedaSubs based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_AndromedaSubs_Type.__name__ = "Gauge32"
_AndromedaSubs_Object = MibScalar
andromedaSubs = _AndromedaSubs_Object(
    (1, 3, 6, 1, 4, 1, 48474, 1, 2, 2),
    _AndromedaSubs_Type()
)
andromedaSubs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    andromedaSubs.setStatus("current")
_AndromedaEmail_ObjectIdentity = ObjectIdentity
andromedaEmail = _AndromedaEmail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48474, 1, 3)
)
_AndromedaHttp_ObjectIdentity = ObjectIdentity
andromedaHttp = _AndromedaHttp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48474, 1, 4)
)
_AndromedaPgresql_ObjectIdentity = ObjectIdentity
andromedaPgresql = _AndromedaPgresql_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48474, 1, 5)
)
_AndromedaODBC_ObjectIdentity = ObjectIdentity
andromedaODBC = _AndromedaODBC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48474, 1, 6)
)
_AndromedaGroups_ObjectIdentity = ObjectIdentity
andromedaGroups = _AndromedaGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48474, 2)
)
_AndromedaTraps_ObjectIdentity = ObjectIdentity
andromedaTraps = _AndromedaTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48474, 3)
)
_AndromedaTrapsPrefix_ObjectIdentity = ObjectIdentity
andromedaTrapsPrefix = _AndromedaTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48474, 3, 0)
)
_AndromedaObjects_ObjectIdentity = ObjectIdentity
andromedaObjects = _AndromedaObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 48474, 4)
)


class _AndromedaString_Type(OctetString):
    """Custom type andromedaString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_AndromedaString_Type.__name__ = "OctetString"
_AndromedaString_Object = MibScalar
andromedaString = _AndromedaString_Object(
    (1, 3, 6, 1, 4, 1, 48474, 4, 1),
    _AndromedaString_Type()
)
andromedaString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    andromedaString.setStatus("current")
_AndromedaLogTable_Object = MibTable
andromedaLogTable = _AndromedaLogTable_Object(
    (1, 3, 6, 1, 4, 1, 48474, 4, 2)
)
if mibBuilder.loadTexts:
    andromedaLogTable.setStatus("current")
_AndromedaLogEntry_Object = MibTableRow
andromedaLogEntry = _AndromedaLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 48474, 4, 2, 1)
)
andromedaLogEntry.setIndexNames(
    (0, "ANDROMEDA-MIB", "logDescription"),
)
if mibBuilder.loadTexts:
    andromedaLogEntry.setStatus("current")
_LogDescription_Type = OctetString
_LogDescription_Object = MibTableColumn
logDescription = _LogDescription_Object(
    (1, 3, 6, 1, 4, 1, 48474, 4, 2, 1, 1),
    _LogDescription_Type()
)
logDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logDescription.setStatus("current")
_LogFatalities_Type = Counter32
_LogFatalities_Object = MibTableColumn
logFatalities = _LogFatalities_Object(
    (1, 3, 6, 1, 4, 1, 48474, 4, 2, 1, 2),
    _LogFatalities_Type()
)
logFatalities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logFatalities.setStatus("current")
_LogErrors_Type = Counter32
_LogErrors_Object = MibTableColumn
logErrors = _LogErrors_Object(
    (1, 3, 6, 1, 4, 1, 48474, 4, 2, 1, 3),
    _LogErrors_Type()
)
logErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logErrors.setStatus("current")
_LogWarnings_Type = Counter32
_LogWarnings_Object = MibTableColumn
logWarnings = _LogWarnings_Object(
    (1, 3, 6, 1, 4, 1, 48474, 4, 2, 1, 4),
    _LogWarnings_Type()
)
logWarnings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logWarnings.setStatus("current")

# Managed Objects groups

andromedaLogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48474, 2, 1)
)
andromedaLogGroup.setObjects(
      *(("ANDROMEDA-MIB", "logFatalities"),
        ("ANDROMEDA-MIB", "logErrors"),
        ("ANDROMEDA-MIB", "logWarnings"))
)
if mibBuilder.loadTexts:
    andromedaLogGroup.setStatus("current")

andromedaVoipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 48474, 2, 2)
)
andromedaVoipGroup.setObjects(
      *(("ANDROMEDA-MIB", "andromedaGrps"),
        ("ANDROMEDA-MIB", "andromedaSubs"))
)
if mibBuilder.loadTexts:
    andromedaVoipGroup.setStatus("current")


# Notification objects

andromedaWarnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 48474, 3, 0, 1)
)
andromedaWarnTrap.setObjects(
    ("ANDROMEDA-MIB", "andromedaString")
)
if mibBuilder.loadTexts:
    andromedaWarnTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ANDROMEDA-MIB",
    **{"moduleIdentityAndromeda": moduleIdentityAndromeda,
       "andromedaComponents": andromedaComponents,
       "andromedaSystem": andromedaSystem,
       "andromedaVoIP": andromedaVoIP,
       "andromedaGrps": andromedaGrps,
       "andromedaSubs": andromedaSubs,
       "andromedaEmail": andromedaEmail,
       "andromedaHttp": andromedaHttp,
       "andromedaPgresql": andromedaPgresql,
       "andromedaODBC": andromedaODBC,
       "andromedaGroups": andromedaGroups,
       "andromedaLogGroup": andromedaLogGroup,
       "andromedaVoipGroup": andromedaVoipGroup,
       "andromedaTraps": andromedaTraps,
       "andromedaTrapsPrefix": andromedaTrapsPrefix,
       "andromedaWarnTrap": andromedaWarnTrap,
       "andromedaObjects": andromedaObjects,
       "andromedaString": andromedaString,
       "andromedaLogTable": andromedaLogTable,
       "andromedaLogEntry": andromedaLogEntry,
       "logDescription": logDescription,
       "logFatalities": logFatalities,
       "logErrors": logErrors,
       "logWarnings": logWarnings}
)
