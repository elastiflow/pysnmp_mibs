# SNMP MIB module (KOLIBRI-GW-ATIA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-GW-ATIA-MIB.mib
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

(koliATIA,
 kolibriControlAddress,
 kolibriInstanceName) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliATIA",
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

koliATIAModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 4, 0)
)
if mibBuilder.loadTexts:
    koliATIAModule.setRevisions(
        ("2017-04-19 09:00",
         "2017-04-19 08:00",
         "2015-07-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliATIATraps_ObjectIdentity = ObjectIdentity
koliATIATraps = _KoliATIATraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 4, 1)
)
_KoliATIATrap_ObjectIdentity = ObjectIdentity
koliATIATrap = _KoliATIATrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 4, 1, 0)
)

# Managed Objects groups


# Notification objects

koliATIAServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 4, 1, 0, 1)
)
koliATIAServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliATIAServiceStart.setStatus(
        "current"
    )

koliATIAServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 4, 1, 0, 2)
)
koliATIAServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliATIAServiceStop.setStatus(
        "current"
    )

koliATIAGatewayConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 4, 1, 0, 5)
)
koliATIAGatewayConnected.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliATIAGatewayConnected.setStatus(
        "current"
    )

koliATIAGatewayDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 4, 1, 0, 6)
)
koliATIAGatewayDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliATIAGatewayDisconnected.setStatus(
        "current"
    )

koliATIAGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 4, 1, 0, 7)
)
koliATIAGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliATIAGenericException.setStatus(
        "current"
    )

koliATIAFirstPacketReceived = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 4, 1, 0, 11)
)
koliATIAFirstPacketReceived.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliATIAFirstPacketReceived.setStatus(
        "current"
    )

koliATIAPacketTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 4, 1, 0, 12)
)
koliATIAPacketTimeout.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliATIAPacketTimeout.setStatus(
        "current"
    )


# Notifications groups

koliATIANotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 4, 4)
)
koliATIANotifications.setObjects(
      *(("KOLIBRI-GW-ATIA-MIB", "koliATIAServiceStart"),
        ("KOLIBRI-GW-ATIA-MIB", "koliATIAServiceStop"),
        ("KOLIBRI-GW-ATIA-MIB", "koliATIAGatewayConnected"),
        ("KOLIBRI-GW-ATIA-MIB", "koliATIAGatewayDisconnected"),
        ("KOLIBRI-GW-ATIA-MIB", "koliATIAGenericException"),
        ("KOLIBRI-GW-ATIA-MIB", "koliATIAFirstPacketReceived"),
        ("KOLIBRI-GW-ATIA-MIB", "koliATIAPacketTimeout"))
)
if mibBuilder.loadTexts:
    koliATIANotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-GW-ATIA-MIB",
    **{"koliATIAModule": koliATIAModule,
       "koliATIATraps": koliATIATraps,
       "koliATIATrap": koliATIATrap,
       "koliATIAServiceStart": koliATIAServiceStart,
       "koliATIAServiceStop": koliATIAServiceStop,
       "koliATIAGatewayConnected": koliATIAGatewayConnected,
       "koliATIAGatewayDisconnected": koliATIAGatewayDisconnected,
       "koliATIAGenericException": koliATIAGenericException,
       "koliATIAFirstPacketReceived": koliATIAFirstPacketReceived,
       "koliATIAPacketTimeout": koliATIAPacketTimeout,
       "koliATIANotifications": koliATIANotifications}
)
