# SNMP MIB module (KOLIBRI-SERVICE-AUDIO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-SERVICE-AUDIO-MIB.mib
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

(koliAudio,
 kolibriClientAddress,
 kolibriClientConnection,
 kolibriInstanceName) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliAudio",
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

koliAudioModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 1, 0)
)
if mibBuilder.loadTexts:
    koliAudioModule.setRevisions(
        ("2017-04-19 09:00",
         "2017-04-19 08:00",
         "2015-07-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliAudioTraps_ObjectIdentity = ObjectIdentity
koliAudioTraps = _KoliAudioTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 1, 1)
)
_KoliAudioTrap_ObjectIdentity = ObjectIdentity
koliAudioTrap = _KoliAudioTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 1, 1, 0)
)

# Managed Objects groups


# Notification objects

koliAudioServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 1, 1, 0, 1)
)
koliAudioServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliAudioServiceStart.setStatus(
        "current"
    )

koliAudioServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 1, 1, 0, 2)
)
koliAudioServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliAudioServiceStop.setStatus(
        "current"
    )

koliAudioClientConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 1, 1, 0, 3)
)
koliAudioClientConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriClientConnection"),
        ("KOLIBRI-MIB", "kolibriClientAddress"))
)
if mibBuilder.loadTexts:
    koliAudioClientConnected.setStatus(
        "current"
    )

koliAudioClientDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 1, 1, 0, 4)
)
koliAudioClientDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriClientConnection"),
        ("KOLIBRI-MIB", "kolibriClientAddress"))
)
if mibBuilder.loadTexts:
    koliAudioClientDisconnected.setStatus(
        "current"
    )

koliAudioGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 1, 1, 0, 7)
)
koliAudioGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliAudioGenericException.setStatus(
        "current"
    )

koliAudioDeviceFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 1, 1, 0, 13)
)
koliAudioDeviceFailure.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliAudioDeviceFailure.setStatus(
        "current"
    )


# Notifications groups

koliAudioNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 1, 4)
)
koliAudioNotifications.setObjects(
      *(("KOLIBRI-SERVICE-AUDIO-MIB", "koliAudioServiceStart"),
        ("KOLIBRI-SERVICE-AUDIO-MIB", "koliAudioServiceStop"),
        ("KOLIBRI-SERVICE-AUDIO-MIB", "koliAudioClientConnected"),
        ("KOLIBRI-SERVICE-AUDIO-MIB", "koliAudioClientDisconnected"),
        ("KOLIBRI-SERVICE-AUDIO-MIB", "koliAudioGenericException"),
        ("KOLIBRI-SERVICE-AUDIO-MIB", "koliAudioDeviceFailure"))
)
if mibBuilder.loadTexts:
    koliAudioNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-SERVICE-AUDIO-MIB",
    **{"koliAudioModule": koliAudioModule,
       "koliAudioTraps": koliAudioTraps,
       "koliAudioTrap": koliAudioTrap,
       "koliAudioServiceStart": koliAudioServiceStart,
       "koliAudioServiceStop": koliAudioServiceStop,
       "koliAudioClientConnected": koliAudioClientConnected,
       "koliAudioClientDisconnected": koliAudioClientDisconnected,
       "koliAudioGenericException": koliAudioGenericException,
       "koliAudioDeviceFailure": koliAudioDeviceFailure,
       "koliAudioNotifications": koliAudioNotifications}
)
