# SNMP MIB module (AIRBUSDS-AGENT511-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/vesta_46389/AIRBUSDS-AGENT511-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 12:06:26 2025
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

agent511 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 46389, 201)
)
if mibBuilder.loadTexts:
    agent511.setRevisions(
        ("2017-09-25 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Vesta_ObjectIdentity = ObjectIdentity
vesta = _Vesta_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46389)
)
_Agent511Objects_ObjectIdentity = ObjectIdentity
agent511Objects = _Agent511Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46389, 201, 10)
)
_Agent511Common_ObjectIdentity = ObjectIdentity
agent511Common = _Agent511Common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46389, 201, 10, 1)
)


class _Agent511Product_Type(DisplayString):
    """Custom type agent511Product based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Agent511Product_Type.__name__ = "DisplayString"
_Agent511Product_Object = MibScalar
agent511Product = _Agent511Product_Object(
    (1, 3, 6, 1, 4, 1, 46389, 201, 10, 1, 1),
    _Agent511Product_Type()
)
agent511Product.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agent511Product.setStatus("current")


class _Agent511Version_Type(DisplayString):
    """Custom type agent511Version based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_Agent511Version_Type.__name__ = "DisplayString"
_Agent511Version_Object = MibScalar
agent511Version = _Agent511Version_Object(
    (1, 3, 6, 1, 4, 1, 46389, 201, 10, 1, 2),
    _Agent511Version_Type()
)
agent511Version.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agent511Version.setStatus("current")


class _Agent511BaseURL_Type(DisplayString):
    """Custom type agent511BaseURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Agent511BaseURL_Type.__name__ = "DisplayString"
_Agent511BaseURL_Object = MibScalar
agent511BaseURL = _Agent511BaseURL_Object(
    (1, 3, 6, 1, 4, 1, 46389, 201, 10, 1, 3),
    _Agent511BaseURL_Type()
)
agent511BaseURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agent511BaseURL.setStatus("current")


class _Agent511TestURL_Type(DisplayString):
    """Custom type agent511TestURL based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Agent511TestURL_Type.__name__ = "DisplayString"
_Agent511TestURL_Object = MibScalar
agent511TestURL = _Agent511TestURL_Object(
    (1, 3, 6, 1, 4, 1, 46389, 201, 10, 1, 4),
    _Agent511TestURL_Type()
)
agent511TestURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agent511TestURL.setStatus("current")
_Agent511Alarm_ObjectIdentity = ObjectIdentity
agent511Alarm = _Agent511Alarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46389, 201, 10, 2)
)


class _Agent511EventDate_Type(DisplayString):
    """Custom type agent511EventDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Agent511EventDate_Type.__name__ = "DisplayString"
_Agent511EventDate_Object = MibScalar
agent511EventDate = _Agent511EventDate_Object(
    (1, 3, 6, 1, 4, 1, 46389, 201, 10, 2, 1),
    _Agent511EventDate_Type()
)
agent511EventDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agent511EventDate.setStatus("current")


class _Agent511Summary_Type(DisplayString):
    """Custom type agent511Summary based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_Agent511Summary_Type.__name__ = "DisplayString"
_Agent511Summary_Object = MibScalar
agent511Summary = _Agent511Summary_Object(
    (1, 3, 6, 1, 4, 1, 46389, 201, 10, 2, 2),
    _Agent511Summary_Type()
)
agent511Summary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agent511Summary.setStatus("current")


class _Agent511Severity_Type(Integer32):
    """Custom type agent511Severity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_Agent511Severity_Type.__name__ = "Integer32"
_Agent511Severity_Object = MibScalar
agent511Severity = _Agent511Severity_Object(
    (1, 3, 6, 1, 4, 1, 46389, 201, 10, 2, 3),
    _Agent511Severity_Type()
)
agent511Severity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agent511Severity.setStatus("current")
_Agent511System_ObjectIdentity = ObjectIdentity
agent511System = _Agent511System_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46389, 201, 10, 3)
)
_Agent511Site_ObjectIdentity = ObjectIdentity
agent511Site = _Agent511Site_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46389, 201, 10, 4)
)
_Agent511Case_ObjectIdentity = ObjectIdentity
agent511Case = _Agent511Case_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46389, 201, 10, 5)
)
_Agent511Notifications_ObjectIdentity = ObjectIdentity
agent511Notifications = _Agent511Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46389, 201, 20)
)
_Agent511Traps_ObjectIdentity = ObjectIdentity
agent511Traps = _Agent511Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46389, 201, 20, 0)
)
_Agent511Conformance_ObjectIdentity = ObjectIdentity
agent511Conformance = _Agent511Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46389, 201, 100)
)
_Agent511Compliances_ObjectIdentity = ObjectIdentity
agent511Compliances = _Agent511Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46389, 201, 100, 1)
)
_Agent511ConformanceGroups_ObjectIdentity = ObjectIdentity
agent511ConformanceGroups = _Agent511ConformanceGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 46389, 201, 100, 2)
)

# Managed Objects groups

agent511ObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 46389, 201, 100, 2, 1)
)
agent511ObjectGroup.setObjects(
      *(("AIRBUSDS-AGENT511-MIB", "agent511Product"),
        ("AIRBUSDS-AGENT511-MIB", "agent511Version"),
        ("AIRBUSDS-AGENT511-MIB", "agent511EventDate"),
        ("AIRBUSDS-AGENT511-MIB", "agent511Summary"),
        ("AIRBUSDS-AGENT511-MIB", "agent511Severity"),
        ("AIRBUSDS-AGENT511-MIB", "agent511BaseURL"),
        ("AIRBUSDS-AGENT511-MIB", "agent511TestURL"))
)
if mibBuilder.loadTexts:
    agent511ObjectGroup.setStatus("current")


# Notification objects

agent511HealthStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 46389, 201, 20, 0, 1)
)
agent511HealthStatusDown.setObjects(
      *(("AIRBUSDS-AGENT511-MIB", "agent511Product"),
        ("AIRBUSDS-AGENT511-MIB", "agent511Version"),
        ("AIRBUSDS-AGENT511-MIB", "agent511EventDate"),
        ("AIRBUSDS-AGENT511-MIB", "agent511Summary"),
        ("AIRBUSDS-AGENT511-MIB", "agent511Severity"),
        ("AIRBUSDS-AGENT511-MIB", "agent511BaseURL"),
        ("AIRBUSDS-AGENT511-MIB", "agent511TestURL"))
)
if mibBuilder.loadTexts:
    agent511HealthStatusDown.setStatus(
        "current"
    )

agent511HealthStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 46389, 201, 20, 0, 2)
)
agent511HealthStatusUp.setObjects(
      *(("AIRBUSDS-AGENT511-MIB", "agent511Product"),
        ("AIRBUSDS-AGENT511-MIB", "agent511Version"),
        ("AIRBUSDS-AGENT511-MIB", "agent511EventDate"),
        ("AIRBUSDS-AGENT511-MIB", "agent511Summary"),
        ("AIRBUSDS-AGENT511-MIB", "agent511Severity"),
        ("AIRBUSDS-AGENT511-MIB", "agent511BaseURL"),
        ("AIRBUSDS-AGENT511-MIB", "agent511TestURL"))
)
if mibBuilder.loadTexts:
    agent511HealthStatusUp.setStatus(
        "current"
    )

agent511DataSourceStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 46389, 201, 20, 0, 11)
)
agent511DataSourceStatusDown.setObjects(
      *(("AIRBUSDS-AGENT511-MIB", "agent511Product"),
        ("AIRBUSDS-AGENT511-MIB", "agent511Version"),
        ("AIRBUSDS-AGENT511-MIB", "agent511EventDate"),
        ("AIRBUSDS-AGENT511-MIB", "agent511Summary"),
        ("AIRBUSDS-AGENT511-MIB", "agent511Severity"),
        ("AIRBUSDS-AGENT511-MIB", "agent511BaseURL"),
        ("AIRBUSDS-AGENT511-MIB", "agent511TestURL"))
)
if mibBuilder.loadTexts:
    agent511DataSourceStatusDown.setStatus(
        "current"
    )

agent511DataSourceStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 46389, 201, 20, 0, 12)
)
agent511DataSourceStatusUp.setObjects(
      *(("AIRBUSDS-AGENT511-MIB", "agent511Product"),
        ("AIRBUSDS-AGENT511-MIB", "agent511Version"),
        ("AIRBUSDS-AGENT511-MIB", "agent511EventDate"),
        ("AIRBUSDS-AGENT511-MIB", "agent511Summary"),
        ("AIRBUSDS-AGENT511-MIB", "agent511Severity"),
        ("AIRBUSDS-AGENT511-MIB", "agent511BaseURL"),
        ("AIRBUSDS-AGENT511-MIB", "agent511TestURL"))
)
if mibBuilder.loadTexts:
    agent511DataSourceStatusUp.setStatus(
        "current"
    )


# Notifications groups

agent511NotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 46389, 201, 100, 2, 2)
)
agent511NotificationGroup.setObjects(
      *(("AIRBUSDS-AGENT511-MIB", "agent511HealthStatusDown"),
        ("AIRBUSDS-AGENT511-MIB", "agent511HealthStatusUp"),
        ("AIRBUSDS-AGENT511-MIB", "agent511DataSourceStatusDown"),
        ("AIRBUSDS-AGENT511-MIB", "agent511DataSourceStatusUp"))
)
if mibBuilder.loadTexts:
    agent511NotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

agent511Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 46389, 201, 100, 1, 1)
)
agent511Compliance.setObjects(
      *(("AIRBUSDS-AGENT511-MIB", "agent511ObjectGroup"),
        ("AIRBUSDS-AGENT511-MIB", "agent511NotificationGroup"))
)
if mibBuilder.loadTexts:
    agent511Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AIRBUSDS-AGENT511-MIB",
    **{"vesta": vesta,
       "agent511": agent511,
       "agent511Objects": agent511Objects,
       "agent511Common": agent511Common,
       "agent511Product": agent511Product,
       "agent511Version": agent511Version,
       "agent511BaseURL": agent511BaseURL,
       "agent511TestURL": agent511TestURL,
       "agent511Alarm": agent511Alarm,
       "agent511EventDate": agent511EventDate,
       "agent511Summary": agent511Summary,
       "agent511Severity": agent511Severity,
       "agent511System": agent511System,
       "agent511Site": agent511Site,
       "agent511Case": agent511Case,
       "agent511Notifications": agent511Notifications,
       "agent511Traps": agent511Traps,
       "agent511HealthStatusDown": agent511HealthStatusDown,
       "agent511HealthStatusUp": agent511HealthStatusUp,
       "agent511DataSourceStatusDown": agent511DataSourceStatusDown,
       "agent511DataSourceStatusUp": agent511DataSourceStatusUp,
       "agent511Conformance": agent511Conformance,
       "agent511Compliances": agent511Compliances,
       "agent511Compliance": agent511Compliance,
       "agent511ConformanceGroups": agent511ConformanceGroups,
       "agent511ObjectGroup": agent511ObjectGroup,
       "agent511NotificationGroup": agent511NotificationGroup}
)
