# SNMP MIB module (KOLIBRI-SERVICE-LOGGING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-SERVICE-LOGGING-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 10:59:40 2025
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

(koliLogging,
 kolibriClientAddress,
 kolibriClientConnection,
 kolibriInstanceName) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliLogging",
    "kolibriClientAddress",
    "kolibriClientConnection",
    "kolibriInstanceName")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

koliLoggingModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 11, 0)
)
if mibBuilder.loadTexts:
    koliLoggingModule.setRevisions(
        ("2017-04-19 09:00",
         "2017-04-19 08:00",
         "2015-07-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliLoggingTraps_ObjectIdentity = ObjectIdentity
koliLoggingTraps = _KoliLoggingTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 11, 1)
)
_KoliLoggingTrap_ObjectIdentity = ObjectIdentity
koliLoggingTrap = _KoliLoggingTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 11, 1, 0)
)

# Managed Objects groups


# Notification objects

koliLoggingServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 11, 1, 0, 1)
)
koliLoggingServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliLoggingServiceStart.setStatus(
        "current"
    )

koliLoggingServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 11, 1, 0, 2)
)
koliLoggingServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliLoggingServiceStop.setStatus(
        "current"
    )

koliLoggingClientConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 11, 1, 0, 3)
)
koliLoggingClientConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriClientConnection"),
        ("KOLIBRI-MIB", "kolibriClientAddress"))
)
if mibBuilder.loadTexts:
    koliLoggingClientConnected.setStatus(
        "current"
    )

koliLoggingClientDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 11, 1, 0, 4)
)
koliLoggingClientDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriClientConnection"),
        ("KOLIBRI-MIB", "kolibriClientAddress"))
)
if mibBuilder.loadTexts:
    koliLoggingClientDisconnected.setStatus(
        "current"
    )

koliLoggingGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 11, 1, 0, 7)
)
koliLoggingGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliLoggingGenericException.setStatus(
        "current"
    )

koliLoggingDBConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 11, 1, 0, 11)
)
koliLoggingDBConnected.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliLoggingDBConnected.setStatus(
        "current"
    )

koliLoggingDBDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 11, 1, 0, 12)
)
koliLoggingDBDisconnected.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliLoggingDBDisconnected.setStatus(
        "current"
    )


# Notifications groups

koliLoggingNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 11, 4)
)
koliLoggingNotifications.setObjects(
      *(("KOLIBRI-SERVICE-LOGGING-MIB", "koliLoggingServiceStart"),
        ("KOLIBRI-SERVICE-LOGGING-MIB", "koliLoggingServiceStop"),
        ("KOLIBRI-SERVICE-LOGGING-MIB", "koliLoggingClientConnected"),
        ("KOLIBRI-SERVICE-LOGGING-MIB", "koliLoggingClientDisconnected"),
        ("KOLIBRI-SERVICE-LOGGING-MIB", "koliLoggingGenericException"),
        ("KOLIBRI-SERVICE-LOGGING-MIB", "koliLoggingDBConnected"),
        ("KOLIBRI-SERVICE-LOGGING-MIB", "koliLoggingDBDisconnected"))
)
if mibBuilder.loadTexts:
    koliLoggingNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-SERVICE-LOGGING-MIB",
    **{"koliLoggingModule": koliLoggingModule,
       "koliLoggingTraps": koliLoggingTraps,
       "koliLoggingTrap": koliLoggingTrap,
       "koliLoggingServiceStart": koliLoggingServiceStart,
       "koliLoggingServiceStop": koliLoggingServiceStop,
       "koliLoggingClientConnected": koliLoggingClientConnected,
       "koliLoggingClientDisconnected": koliLoggingClientDisconnected,
       "koliLoggingGenericException": koliLoggingGenericException,
       "koliLoggingDBConnected": koliLoggingDBConnected,
       "koliLoggingDBDisconnected": koliLoggingDBDisconnected,
       "koliLoggingNotifications": koliLoggingNotifications}
)
