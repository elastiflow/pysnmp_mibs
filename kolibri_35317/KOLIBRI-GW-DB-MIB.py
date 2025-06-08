# SNMP MIB module (KOLIBRI-GW-DB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-GW-DB-MIB.mib
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

(koliDB,
 kolibriControlAddress,
 kolibriInstanceName) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliDB",
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

koliDBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 15, 0)
)
if mibBuilder.loadTexts:
    koliDBModule.setRevisions(
        ("2017-04-19 09:00",
         "2017-04-19 08:00",
         "2015-07-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliDBTraps_ObjectIdentity = ObjectIdentity
koliDBTraps = _KoliDBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 15, 1)
)
_KoliDBTrap_ObjectIdentity = ObjectIdentity
koliDBTrap = _KoliDBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 15, 1, 0)
)

# Managed Objects groups


# Notification objects

koliDBServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 15, 1, 0, 1)
)
koliDBServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliDBServiceStart.setStatus(
        "current"
    )

koliDBServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 15, 1, 0, 2)
)
koliDBServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliDBServiceStop.setStatus(
        "current"
    )

koliDBGatewayConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 15, 1, 0, 5)
)
koliDBGatewayConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliDBGatewayConnected.setStatus(
        "current"
    )

koliDBGatewayDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 15, 1, 0, 6)
)
koliDBGatewayDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliDBGatewayDisconnected.setStatus(
        "current"
    )

koliDBGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 15, 1, 0, 7)
)
koliDBGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliDBGenericException.setStatus(
        "current"
    )


# Notifications groups

koliDBNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 15, 4)
)
koliDBNotifications.setObjects(
      *(("KOLIBRI-GW-DB-MIB", "koliDBServiceStart"),
        ("KOLIBRI-GW-DB-MIB", "koliDBServiceStop"),
        ("KOLIBRI-GW-DB-MIB", "koliDBGatewayConnected"),
        ("KOLIBRI-GW-DB-MIB", "koliDBGatewayDisconnected"),
        ("KOLIBRI-GW-DB-MIB", "koliDBGenericException"))
)
if mibBuilder.loadTexts:
    koliDBNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-GW-DB-MIB",
    **{"koliDBModule": koliDBModule,
       "koliDBTraps": koliDBTraps,
       "koliDBTrap": koliDBTrap,
       "koliDBServiceStart": koliDBServiceStart,
       "koliDBServiceStop": koliDBServiceStop,
       "koliDBGatewayConnected": koliDBGatewayConnected,
       "koliDBGatewayDisconnected": koliDBGatewayDisconnected,
       "koliDBGenericException": koliDBGenericException,
       "koliDBNotifications": koliDBNotifications}
)
