# SNMP MIB module (KOLIBRI-LINK-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-LINK-SERVER-MIB.mib
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

(koliLinkServer,
 kolibriClientAddress,
 kolibriClientConnection,
 kolibriConfigAddress,
 kolibriControlAddress,
 kolibriInstanceName) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliLinkServer",
    "kolibriClientAddress",
    "kolibriClientConnection",
    "kolibriConfigAddress",
    "kolibriControlAddress",
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

koliLinkServerModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 2, 0)
)
if mibBuilder.loadTexts:
    koliLinkServerModule.setRevisions(
        ("2017-04-19 09:00",
         "2017-04-19 08:00",
         "2015-07-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliLinkServerTraps_ObjectIdentity = ObjectIdentity
koliLinkServerTraps = _KoliLinkServerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 2, 1)
)
_KoliLinkServerTrap_ObjectIdentity = ObjectIdentity
koliLinkServerTrap = _KoliLinkServerTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 2, 1, 0)
)

# Managed Objects groups


# Notification objects

koliLinkServerServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 2, 1, 0, 1)
)
koliLinkServerServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliLinkServerServiceStart.setStatus(
        "current"
    )

koliLinkServerServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 2, 1, 0, 2)
)
koliLinkServerServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliLinkServerServiceStop.setStatus(
        "current"
    )

koliLinkServerClientConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 2, 1, 0, 3)
)
koliLinkServerClientConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriClientConnection"),
        ("KOLIBRI-MIB", "kolibriClientAddress"))
)
if mibBuilder.loadTexts:
    koliLinkServerClientConnected.setStatus(
        "current"
    )

koliLinkServerClientDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 2, 1, 0, 4)
)
koliLinkServerClientDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriClientConnection"),
        ("KOLIBRI-MIB", "kolibriClientAddress"))
)
if mibBuilder.loadTexts:
    koliLinkServerClientDisconnected.setStatus(
        "current"
    )

koliLinkServerGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 2, 1, 0, 7)
)
koliLinkServerGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliLinkServerGenericException.setStatus(
        "current"
    )

koliLinkServerConfigConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 2, 1, 0, 11)
)
koliLinkServerConfigConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriConfigAddress"))
)
if mibBuilder.loadTexts:
    koliLinkServerConfigConnected.setStatus(
        "current"
    )

koliLinkServerConfigDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 2, 1, 0, 12)
)
koliLinkServerConfigDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriConfigAddress"))
)
if mibBuilder.loadTexts:
    koliLinkServerConfigDisconnected.setStatus(
        "current"
    )

koliLinkServerControlConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 2, 1, 0, 13)
)
koliLinkServerControlConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliLinkServerControlConnected.setStatus(
        "current"
    )

koliLinkServerControlDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 2, 1, 0, 14)
)
koliLinkServerControlDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliLinkServerControlDisconnected.setStatus(
        "current"
    )


# Notifications groups

koliLinkServerNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 2, 4)
)
koliLinkServerNotifications.setObjects(
      *(("KOLIBRI-LINK-SERVER-MIB", "koliLinkServerServiceStart"),
        ("KOLIBRI-LINK-SERVER-MIB", "koliLinkServerServiceStop"),
        ("KOLIBRI-LINK-SERVER-MIB", "koliLinkServerClientConnected"),
        ("KOLIBRI-LINK-SERVER-MIB", "koliLinkServerClientDisconnected"),
        ("KOLIBRI-LINK-SERVER-MIB", "koliLinkServerGenericException"),
        ("KOLIBRI-LINK-SERVER-MIB", "koliLinkServerConfigConnected"),
        ("KOLIBRI-LINK-SERVER-MIB", "koliLinkServerConfigDisconnected"),
        ("KOLIBRI-LINK-SERVER-MIB", "koliLinkServerControlConnected"),
        ("KOLIBRI-LINK-SERVER-MIB", "koliLinkServerControlDisconnected"))
)
if mibBuilder.loadTexts:
    koliLinkServerNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-LINK-SERVER-MIB",
    **{"koliLinkServerModule": koliLinkServerModule,
       "koliLinkServerTraps": koliLinkServerTraps,
       "koliLinkServerTrap": koliLinkServerTrap,
       "koliLinkServerServiceStart": koliLinkServerServiceStart,
       "koliLinkServerServiceStop": koliLinkServerServiceStop,
       "koliLinkServerClientConnected": koliLinkServerClientConnected,
       "koliLinkServerClientDisconnected": koliLinkServerClientDisconnected,
       "koliLinkServerGenericException": koliLinkServerGenericException,
       "koliLinkServerConfigConnected": koliLinkServerConfigConnected,
       "koliLinkServerConfigDisconnected": koliLinkServerConfigDisconnected,
       "koliLinkServerControlConnected": koliLinkServerControlConnected,
       "koliLinkServerControlDisconnected": koliLinkServerControlDisconnected,
       "koliLinkServerNotifications": koliLinkServerNotifications}
)
