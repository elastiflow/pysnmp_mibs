# SNMP MIB module (KOLIBRI-COMM-DCS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-COMM-DCS-MIB.mib
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

(koliDCS,
 kolibriAudioAddress,
 kolibriClientAddress,
 kolibriClientConnection,
 kolibriCommGateway,
 kolibriInstanceName) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliDCS",
    "kolibriAudioAddress",
    "kolibriClientAddress",
    "kolibriClientConnection",
    "kolibriCommGateway",
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

koliDCSModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 5, 0)
)
if mibBuilder.loadTexts:
    koliDCSModule.setRevisions(
        ("2017-04-19 09:00",
         "2017-04-19 08:00",
         "2017-04-18 08:00",
         "2015-12-01 09:15")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliDCSTraps_ObjectIdentity = ObjectIdentity
koliDCSTraps = _KoliDCSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 5, 1)
)
_KoliDCSTrap_ObjectIdentity = ObjectIdentity
koliDCSTrap = _KoliDCSTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 5, 1, 0)
)

# Managed Objects groups


# Notification objects

koliDCSServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 5, 1, 0, 1)
)
koliDCSServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliDCSServiceStart.setStatus(
        "current"
    )

koliDCSServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 5, 1, 0, 2)
)
koliDCSServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliDCSServiceStop.setStatus(
        "current"
    )

koliDCSClientConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 5, 1, 0, 3)
)
koliDCSClientConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriClientConnection"),
        ("KOLIBRI-MIB", "kolibriClientAddress"))
)
if mibBuilder.loadTexts:
    koliDCSClientConnected.setStatus(
        "current"
    )

koliDCSClientDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 5, 1, 0, 4)
)
koliDCSClientDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriClientConnection"),
        ("KOLIBRI-MIB", "kolibriClientAddress"))
)
if mibBuilder.loadTexts:
    koliDCSClientDisconnected.setStatus(
        "current"
    )

koliDCSGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 5, 1, 0, 7)
)
koliDCSGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliDCSGenericException.setStatus(
        "current"
    )

koliDCSGatewayConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 5, 1, 0, 13)
)
koliDCSGatewayConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriCommGateway"))
)
if mibBuilder.loadTexts:
    koliDCSGatewayConnected.setStatus(
        "current"
    )

koliDCSGatewayDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 5, 1, 0, 14)
)
koliDCSGatewayDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriCommGateway"))
)
if mibBuilder.loadTexts:
    koliDCSGatewayDisconnected.setStatus(
        "current"
    )

koliDCSAudioConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 5, 1, 0, 21)
)
koliDCSAudioConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriAudioAddress"))
)
if mibBuilder.loadTexts:
    koliDCSAudioConnected.setStatus(
        "current"
    )

koliDCSAudioDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 5, 1, 0, 22)
)
koliDCSAudioDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriAudioAddress"))
)
if mibBuilder.loadTexts:
    koliDCSAudioDisconnected.setStatus(
        "current"
    )


# Notifications groups

koliDCSNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 5, 4)
)
koliDCSNotifications.setObjects(
      *(("KOLIBRI-COMM-DCS-MIB", "koliDCSServiceStart"),
        ("KOLIBRI-COMM-DCS-MIB", "koliDCSServiceStop"),
        ("KOLIBRI-COMM-DCS-MIB", "koliDCSClientConnected"),
        ("KOLIBRI-COMM-DCS-MIB", "koliDCSClientDisconnected"),
        ("KOLIBRI-COMM-DCS-MIB", "koliDCSGenericException"),
        ("KOLIBRI-COMM-DCS-MIB", "koliDCSGatewayConnected"),
        ("KOLIBRI-COMM-DCS-MIB", "koliDCSGatewayDisconnected"),
        ("KOLIBRI-COMM-DCS-MIB", "koliDCSAudioConnected"),
        ("KOLIBRI-COMM-DCS-MIB", "koliDCSAudioDisconnected"))
)
if mibBuilder.loadTexts:
    koliDCSNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-COMM-DCS-MIB",
    **{"koliDCSModule": koliDCSModule,
       "koliDCSTraps": koliDCSTraps,
       "koliDCSTrap": koliDCSTrap,
       "koliDCSServiceStart": koliDCSServiceStart,
       "koliDCSServiceStop": koliDCSServiceStop,
       "koliDCSClientConnected": koliDCSClientConnected,
       "koliDCSClientDisconnected": koliDCSClientDisconnected,
       "koliDCSGenericException": koliDCSGenericException,
       "koliDCSGatewayConnected": koliDCSGatewayConnected,
       "koliDCSGatewayDisconnected": koliDCSGatewayDisconnected,
       "koliDCSAudioConnected": koliDCSAudioConnected,
       "koliDCSAudioDisconnected": koliDCSAudioDisconnected,
       "koliDCSNotifications": koliDCSNotifications}
)
