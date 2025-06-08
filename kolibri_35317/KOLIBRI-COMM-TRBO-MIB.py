# SNMP MIB module (KOLIBRI-COMM-TRBO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-COMM-TRBO-MIB.mib
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

(koliTRBO,
 kolibriAudioAddress,
 kolibriClientAddress,
 kolibriClientConnection,
 kolibriCommGateway,
 kolibriExtClientConnection,
 kolibriExtClientName,
 kolibriExtClientTargetPort,
 kolibriInstanceName) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliTRBO",
    "kolibriAudioAddress",
    "kolibriClientAddress",
    "kolibriClientConnection",
    "kolibriCommGateway",
    "kolibriExtClientConnection",
    "kolibriExtClientName",
    "kolibriExtClientTargetPort",
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

koliTRBOModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 4, 0)
)
if mibBuilder.loadTexts:
    koliTRBOModule.setRevisions(
        ("2017-04-19 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliTRBOTraps_ObjectIdentity = ObjectIdentity
koliTRBOTraps = _KoliTRBOTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 4, 1)
)
_KoliTRBOTrap_ObjectIdentity = ObjectIdentity
koliTRBOTrap = _KoliTRBOTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 4, 1, 0)
)

# Managed Objects groups


# Notification objects

koliTRBOServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 4, 1, 0, 1)
)
koliTRBOServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliTRBOServiceStart.setStatus(
        "current"
    )

koliTRBOServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 4, 1, 0, 2)
)
koliTRBOServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliTRBOServiceStop.setStatus(
        "current"
    )

koliTRBOClientConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 4, 1, 0, 3)
)
koliTRBOClientConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriClientConnection"),
        ("KOLIBRI-MIB", "kolibriClientAddress"))
)
if mibBuilder.loadTexts:
    koliTRBOClientConnected.setStatus(
        "current"
    )

koliTRBOClientDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 4, 1, 0, 4)
)
koliTRBOClientDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriClientConnection"),
        ("KOLIBRI-MIB", "kolibriClientAddress"))
)
if mibBuilder.loadTexts:
    koliTRBOClientDisconnected.setStatus(
        "current"
    )

koliTRBOGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 4, 1, 0, 7)
)
koliTRBOGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliTRBOGenericException.setStatus(
        "current"
    )

koliTRBOGatewayConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 4, 1, 0, 13)
)
koliTRBOGatewayConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriCommGateway"))
)
if mibBuilder.loadTexts:
    koliTRBOGatewayConnected.setStatus(
        "current"
    )

koliTRBOGatewayDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 4, 1, 0, 14)
)
koliTRBOGatewayDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriCommGateway"))
)
if mibBuilder.loadTexts:
    koliTRBOGatewayDisconnected.setStatus(
        "current"
    )

koliTRBOAudioConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 4, 1, 0, 21)
)
koliTRBOAudioConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriAudioAddress"))
)
if mibBuilder.loadTexts:
    koliTRBOAudioConnected.setStatus(
        "current"
    )

koliTRBOAudioDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 4, 1, 0, 22)
)
koliTRBOAudioDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriAudioAddress"))
)
if mibBuilder.loadTexts:
    koliTRBOAudioDisconnected.setStatus(
        "current"
    )

koliTRBOExtClientConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 4, 1, 0, 49)
)
koliTRBOExtClientConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriExtClientConnection"),
        ("KOLIBRI-MIB", "kolibriExtClientName"),
        ("KOLIBRI-MIB", "kolibriExtClientTargetPort"))
)
if mibBuilder.loadTexts:
    koliTRBOExtClientConnected.setStatus(
        "current"
    )

koliTRBOExtClientDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 4, 1, 0, 50)
)
koliTRBOExtClientDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriExtClientConnection"),
        ("KOLIBRI-MIB", "kolibriExtClientName"),
        ("KOLIBRI-MIB", "kolibriExtClientTargetPort"))
)
if mibBuilder.loadTexts:
    koliTRBOExtClientDisconnected.setStatus(
        "current"
    )


# Notifications groups

koliTRBONotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 4, 4)
)
koliTRBONotifications.setObjects(
      *(("KOLIBRI-COMM-TRBO-MIB", "koliTRBOServiceStart"),
        ("KOLIBRI-COMM-TRBO-MIB", "koliTRBOServiceStop"),
        ("KOLIBRI-COMM-TRBO-MIB", "koliTRBOClientConnected"),
        ("KOLIBRI-COMM-TRBO-MIB", "koliTRBOClientDisconnected"),
        ("KOLIBRI-COMM-TRBO-MIB", "koliTRBOGenericException"),
        ("KOLIBRI-COMM-TRBO-MIB", "koliTRBOGatewayConnected"),
        ("KOLIBRI-COMM-TRBO-MIB", "koliTRBOGatewayDisconnected"),
        ("KOLIBRI-COMM-TRBO-MIB", "koliTRBOAudioConnected"),
        ("KOLIBRI-COMM-TRBO-MIB", "koliTRBOAudioDisconnected"),
        ("KOLIBRI-COMM-TRBO-MIB", "koliTRBOExtClientConnected"),
        ("KOLIBRI-COMM-TRBO-MIB", "koliTRBOExtClientDisconnected"))
)
if mibBuilder.loadTexts:
    koliTRBONotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-COMM-TRBO-MIB",
    **{"koliTRBOModule": koliTRBOModule,
       "koliTRBOTraps": koliTRBOTraps,
       "koliTRBOTrap": koliTRBOTrap,
       "koliTRBOServiceStart": koliTRBOServiceStart,
       "koliTRBOServiceStop": koliTRBOServiceStop,
       "koliTRBOClientConnected": koliTRBOClientConnected,
       "koliTRBOClientDisconnected": koliTRBOClientDisconnected,
       "koliTRBOGenericException": koliTRBOGenericException,
       "koliTRBOGatewayConnected": koliTRBOGatewayConnected,
       "koliTRBOGatewayDisconnected": koliTRBOGatewayDisconnected,
       "koliTRBOAudioConnected": koliTRBOAudioConnected,
       "koliTRBOAudioDisconnected": koliTRBOAudioDisconnected,
       "koliTRBOExtClientConnected": koliTRBOExtClientConnected,
       "koliTRBOExtClientDisconnected": koliTRBOExtClientDisconnected,
       "koliTRBONotifications": koliTRBONotifications}
)
