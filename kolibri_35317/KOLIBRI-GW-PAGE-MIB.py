# SNMP MIB module (KOLIBRI-GW-PAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-GW-PAGE-MIB.mib
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

(koliPage,
 kolibriControlAddress,
 kolibriInstanceName) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliPage",
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

koliPageModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 7, 0)
)
if mibBuilder.loadTexts:
    koliPageModule.setRevisions(
        ("2017-04-19 09:00",
         "2017-04-19 08:00",
         "2015-07-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliPageTraps_ObjectIdentity = ObjectIdentity
koliPageTraps = _KoliPageTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 7, 1)
)
_KoliPageTrap_ObjectIdentity = ObjectIdentity
koliPageTrap = _KoliPageTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 7, 1, 0)
)

# Managed Objects groups


# Notification objects

koliPageServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 7, 1, 0, 1)
)
koliPageServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliPageServiceStart.setStatus(
        "current"
    )

koliPageServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 7, 1, 0, 2)
)
koliPageServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliPageServiceStop.setStatus(
        "current"
    )

koliPageGatewayConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 7, 1, 0, 5)
)
koliPageGatewayConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliPageGatewayConnected.setStatus(
        "current"
    )

koliPageGatewayDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 7, 1, 0, 6)
)
koliPageGatewayDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliPageGatewayDisconnected.setStatus(
        "current"
    )

koliPageGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 7, 1, 0, 7)
)
koliPageGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliPageGenericException.setStatus(
        "current"
    )


# Notifications groups

koliPageNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 7, 4)
)
koliPageNotifications.setObjects(
      *(("KOLIBRI-GW-PAGE-MIB", "koliPageServiceStart"),
        ("KOLIBRI-GW-PAGE-MIB", "koliPageServiceStop"),
        ("KOLIBRI-GW-PAGE-MIB", "koliPageGatewayConnected"),
        ("KOLIBRI-GW-PAGE-MIB", "koliPageGatewayDisconnected"),
        ("KOLIBRI-GW-PAGE-MIB", "koliPageGenericException"))
)
if mibBuilder.loadTexts:
    koliPageNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-GW-PAGE-MIB",
    **{"koliPageModule": koliPageModule,
       "koliPageTraps": koliPageTraps,
       "koliPageTrap": koliPageTrap,
       "koliPageServiceStart": koliPageServiceStart,
       "koliPageServiceStop": koliPageServiceStop,
       "koliPageGatewayConnected": koliPageGatewayConnected,
       "koliPageGatewayDisconnected": koliPageGatewayDisconnected,
       "koliPageGenericException": koliPageGenericException,
       "koliPageNotifications": koliPageNotifications}
)
