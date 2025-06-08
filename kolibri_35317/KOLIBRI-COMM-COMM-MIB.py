# SNMP MIB module (KOLIBRI-COMM-COMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-COMM-COMM-MIB.mib
# Produced by pysmi-1.6.1 at Sat Jun  7 10:59:39 2025
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

(koliComm,
 kolibriAudioAddress,
 kolibriClientAddress,
 kolibriClientConnection,
 kolibriCommDevice,
 kolibriInstanceName) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliComm",
    "kolibriAudioAddress",
    "kolibriClientAddress",
    "kolibriClientConnection",
    "kolibriCommDevice",
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

koliCommModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 1, 0)
)
if mibBuilder.loadTexts:
    koliCommModule.setRevisions(
        ("2017-04-19 09:00",
         "2017-04-19 08:00",
         "2017-04-18 08:00",
         "2015-07-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliCommTraps_ObjectIdentity = ObjectIdentity
koliCommTraps = _KoliCommTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 1, 1)
)
_KoliCommTrap_ObjectIdentity = ObjectIdentity
koliCommTrap = _KoliCommTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 1, 1, 0)
)

# Managed Objects groups


# Notification objects

koliCommServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 1, 1, 0, 1)
)
koliCommServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliCommServiceStart.setStatus(
        "current"
    )

koliCommServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 1, 1, 0, 2)
)
koliCommServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliCommServiceStop.setStatus(
        "current"
    )

koliCommClientConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 1, 1, 0, 3)
)
koliCommClientConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriClientConnection"),
        ("KOLIBRI-MIB", "kolibriClientAddress"))
)
if mibBuilder.loadTexts:
    koliCommClientConnected.setStatus(
        "current"
    )

koliCommClientDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 1, 1, 0, 4)
)
koliCommClientDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriClientConnection"),
        ("KOLIBRI-MIB", "kolibriClientAddress"))
)
if mibBuilder.loadTexts:
    koliCommClientDisconnected.setStatus(
        "current"
    )

koliCommGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 1, 1, 0, 7)
)
koliCommGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliCommGenericException.setStatus(
        "current"
    )

koliCommDeviceConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 1, 1, 0, 11)
)
koliCommDeviceConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriCommDevice"))
)
if mibBuilder.loadTexts:
    koliCommDeviceConnected.setStatus(
        "current"
    )

koliCommDeviceDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 1, 1, 0, 12)
)
koliCommDeviceDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriCommDevice"))
)
if mibBuilder.loadTexts:
    koliCommDeviceDisconnected.setStatus(
        "current"
    )

koliCommAudioConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 1, 1, 0, 21)
)
koliCommAudioConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriAudioAddress"))
)
if mibBuilder.loadTexts:
    koliCommAudioConnected.setStatus(
        "current"
    )

koliCommAudioDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 1, 1, 0, 22)
)
koliCommAudioDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriAudioAddress"))
)
if mibBuilder.loadTexts:
    koliCommAudioDisconnected.setStatus(
        "current"
    )


# Notifications groups

koliCommNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 1, 4)
)
koliCommNotifications.setObjects(
      *(("KOLIBRI-COMM-COMM-MIB", "koliCommServiceStart"),
        ("KOLIBRI-COMM-COMM-MIB", "koliCommServiceStop"),
        ("KOLIBRI-COMM-COMM-MIB", "koliCommClientConnected"),
        ("KOLIBRI-COMM-COMM-MIB", "koliCommClientDisconnected"),
        ("KOLIBRI-COMM-COMM-MIB", "koliCommGenericException"),
        ("KOLIBRI-COMM-COMM-MIB", "koliCommDeviceConnected"),
        ("KOLIBRI-COMM-COMM-MIB", "koliCommDeviceDisconnected"),
        ("KOLIBRI-COMM-COMM-MIB", "koliCommAudioConnected"),
        ("KOLIBRI-COMM-COMM-MIB", "koliCommAudioDisconnected"))
)
if mibBuilder.loadTexts:
    koliCommNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-COMM-COMM-MIB",
    **{"koliCommModule": koliCommModule,
       "koliCommTraps": koliCommTraps,
       "koliCommTrap": koliCommTrap,
       "koliCommServiceStart": koliCommServiceStart,
       "koliCommServiceStop": koliCommServiceStop,
       "koliCommClientConnected": koliCommClientConnected,
       "koliCommClientDisconnected": koliCommClientDisconnected,
       "koliCommGenericException": koliCommGenericException,
       "koliCommDeviceConnected": koliCommDeviceConnected,
       "koliCommDeviceDisconnected": koliCommDeviceDisconnected,
       "koliCommAudioConnected": koliCommAudioConnected,
       "koliCommAudioDisconnected": koliCommAudioDisconnected,
       "koliCommNotifications": koliCommNotifications}
)
