# SNMP MIB module (KOLIBRI-COMM-DAMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-COMM-DAMM-MIB.mib
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

(koliDAMM,
 kolibriAudioAddress,
 kolibriClientAddress,
 kolibriClientConnection,
 kolibriCommGateway,
 kolibriInstanceName) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliDAMM",
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

koliDAMMModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 3, 0)
)
if mibBuilder.loadTexts:
    koliDAMMModule.setRevisions(
        ("2017-04-19 09:00",
         "2017-04-19 08:00",
         "2017-04-18 08:00",
         "2015-11-30 14:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliDAMMTraps_ObjectIdentity = ObjectIdentity
koliDAMMTraps = _KoliDAMMTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 3, 1)
)
_KoliDAMMTrap_ObjectIdentity = ObjectIdentity
koliDAMMTrap = _KoliDAMMTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 3, 1, 0)
)

# Managed Objects groups


# Notification objects

koliDAMMServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 3, 1, 0, 1)
)
koliDAMMServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliDAMMServiceStart.setStatus(
        "current"
    )

koliDAMMServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 3, 1, 0, 2)
)
koliDAMMServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliDAMMServiceStop.setStatus(
        "current"
    )

koliDAMMClientConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 3, 1, 0, 3)
)
koliDAMMClientConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriClientConnection"),
        ("KOLIBRI-MIB", "kolibriClientAddress"))
)
if mibBuilder.loadTexts:
    koliDAMMClientConnected.setStatus(
        "current"
    )

koliDAMMClientDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 3, 1, 0, 4)
)
koliDAMMClientDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriClientConnection"),
        ("KOLIBRI-MIB", "kolibriClientAddress"))
)
if mibBuilder.loadTexts:
    koliDAMMClientDisconnected.setStatus(
        "current"
    )

koliDAMMGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 3, 1, 0, 7)
)
koliDAMMGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliDAMMGenericException.setStatus(
        "current"
    )

koliDAMMGatewayConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 3, 1, 0, 13)
)
koliDAMMGatewayConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriCommGateway"))
)
if mibBuilder.loadTexts:
    koliDAMMGatewayConnected.setStatus(
        "current"
    )

koliDAMMGatewayDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 3, 1, 0, 14)
)
koliDAMMGatewayDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriCommGateway"))
)
if mibBuilder.loadTexts:
    koliDAMMGatewayDisconnected.setStatus(
        "current"
    )

koliDAMMAudioConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 3, 1, 0, 21)
)
koliDAMMAudioConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriAudioAddress"))
)
if mibBuilder.loadTexts:
    koliDAMMAudioConnected.setStatus(
        "current"
    )

koliDAMMAudioDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 3, 1, 0, 22)
)
koliDAMMAudioDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriAudioAddress"))
)
if mibBuilder.loadTexts:
    koliDAMMAudioDisconnected.setStatus(
        "current"
    )


# Notifications groups

koliDAMMNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 4, 3, 4)
)
koliDAMMNotifications.setObjects(
      *(("KOLIBRI-COMM-DAMM-MIB", "koliDAMMServiceStart"),
        ("KOLIBRI-COMM-DAMM-MIB", "koliDAMMServiceStop"),
        ("KOLIBRI-COMM-DAMM-MIB", "koliDAMMClientConnected"),
        ("KOLIBRI-COMM-DAMM-MIB", "koliDAMMClientDisconnected"),
        ("KOLIBRI-COMM-DAMM-MIB", "koliDAMMGenericException"),
        ("KOLIBRI-COMM-DAMM-MIB", "koliDAMMGatewayConnected"),
        ("KOLIBRI-COMM-DAMM-MIB", "koliDAMMGatewayDisconnected"),
        ("KOLIBRI-COMM-DAMM-MIB", "koliDAMMAudioConnected"),
        ("KOLIBRI-COMM-DAMM-MIB", "koliDAMMAudioDisconnected"))
)
if mibBuilder.loadTexts:
    koliDAMMNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-COMM-DAMM-MIB",
    **{"koliDAMMModule": koliDAMMModule,
       "koliDAMMTraps": koliDAMMTraps,
       "koliDAMMTrap": koliDAMMTrap,
       "koliDAMMServiceStart": koliDAMMServiceStart,
       "koliDAMMServiceStop": koliDAMMServiceStop,
       "koliDAMMClientConnected": koliDAMMClientConnected,
       "koliDAMMClientDisconnected": koliDAMMClientDisconnected,
       "koliDAMMGenericException": koliDAMMGenericException,
       "koliDAMMGatewayConnected": koliDAMMGatewayConnected,
       "koliDAMMGatewayDisconnected": koliDAMMGatewayDisconnected,
       "koliDAMMAudioConnected": koliDAMMAudioConnected,
       "koliDAMMAudioDisconnected": koliDAMMAudioDisconnected,
       "koliDAMMNotifications": koliDAMMNotifications}
)
