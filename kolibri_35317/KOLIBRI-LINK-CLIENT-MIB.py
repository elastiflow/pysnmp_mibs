# SNMP MIB module (KOLIBRI-LINK-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-LINK-CLIENT-MIB.mib
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

(koliLinkClient,
 kolibriControlAddress,
 kolibriInstanceName,
 kolibriLinkAddress) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliLinkClient",
    "kolibriControlAddress",
    "kolibriInstanceName",
    "kolibriLinkAddress")

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

koliLinkClientModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 1, 0)
)
if mibBuilder.loadTexts:
    koliLinkClientModule.setRevisions(
        ("2017-04-19 09:00",
         "2015-07-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliLinkClientTraps_ObjectIdentity = ObjectIdentity
koliLinkClientTraps = _KoliLinkClientTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 1, 1)
)
_KoliLinkClientTrap_ObjectIdentity = ObjectIdentity
koliLinkClientTrap = _KoliLinkClientTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 1, 1, 0)
)

# Managed Objects groups


# Notification objects

koliLinkClientServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 1, 1, 0, 1)
)
koliLinkClientServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliLinkClientServiceStart.setStatus(
        "current"
    )

koliLinkClientServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 1, 1, 0, 2)
)
koliLinkClientServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliLinkClientServiceStop.setStatus(
        "current"
    )

koliLinkClientGatewayConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 1, 1, 0, 5)
)
koliLinkClientGatewayConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliLinkClientGatewayConnected.setStatus(
        "current"
    )

koliLinkClientGatewayDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 1, 1, 0, 6)
)
koliLinkClientGatewayDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliLinkClientGatewayDisconnected.setStatus(
        "current"
    )

koliLinkClientGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 1, 1, 0, 7)
)
koliLinkClientGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliLinkClientGenericException.setStatus(
        "current"
    )

koliLinkClientLinkConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 1, 1, 0, 11)
)
koliLinkClientLinkConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriLinkAddress"))
)
if mibBuilder.loadTexts:
    koliLinkClientLinkConnected.setStatus(
        "current"
    )

koliLinkClientLinkDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 1, 1, 0, 12)
)
koliLinkClientLinkDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriLinkAddress"))
)
if mibBuilder.loadTexts:
    koliLinkClientLinkDisconnected.setStatus(
        "current"
    )


# Notifications groups

koliLinkClientNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 5, 1, 4)
)
koliLinkClientNotifications.setObjects(
      *(("KOLIBRI-LINK-CLIENT-MIB", "koliLinkClientServiceStart"),
        ("KOLIBRI-LINK-CLIENT-MIB", "koliLinkClientServiceStop"),
        ("KOLIBRI-LINK-CLIENT-MIB", "koliLinkClientGatewayConnected"),
        ("KOLIBRI-LINK-CLIENT-MIB", "koliLinkClientGatewayDisconnected"),
        ("KOLIBRI-LINK-CLIENT-MIB", "koliLinkClientGenericException"),
        ("KOLIBRI-LINK-CLIENT-MIB", "koliLinkClientLinkConnected"),
        ("KOLIBRI-LINK-CLIENT-MIB", "koliLinkClientLinkDisconnected"))
)
if mibBuilder.loadTexts:
    koliLinkClientNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-LINK-CLIENT-MIB",
    **{"koliLinkClientModule": koliLinkClientModule,
       "koliLinkClientTraps": koliLinkClientTraps,
       "koliLinkClientTrap": koliLinkClientTrap,
       "koliLinkClientServiceStart": koliLinkClientServiceStart,
       "koliLinkClientServiceStop": koliLinkClientServiceStop,
       "koliLinkClientGatewayConnected": koliLinkClientGatewayConnected,
       "koliLinkClientGatewayDisconnected": koliLinkClientGatewayDisconnected,
       "koliLinkClientGenericException": koliLinkClientGenericException,
       "koliLinkClientLinkConnected": koliLinkClientLinkConnected,
       "koliLinkClientLinkDisconnected": koliLinkClientLinkDisconnected,
       "koliLinkClientNotifications": koliLinkClientNotifications}
)
