# SNMP MIB module (KOLIBRI-SERVICE-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-SERVICE-CONFIG-MIB.mib
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

(koliConfig,
 kolibriClientAddress,
 kolibriClientConnection,
 kolibriConfigAddress,
 kolibriInstanceName) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliConfig",
    "kolibriClientAddress",
    "kolibriClientConnection",
    "kolibriConfigAddress",
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

koliConfigModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 3, 0)
)
if mibBuilder.loadTexts:
    koliConfigModule.setRevisions(
        ("2017-04-19 09:00",
         "2017-04-19 08:00",
         "2015-07-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliConfigTraps_ObjectIdentity = ObjectIdentity
koliConfigTraps = _KoliConfigTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 3, 1)
)
_KoliConfigTrap_ObjectIdentity = ObjectIdentity
koliConfigTrap = _KoliConfigTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 3, 1, 0)
)

# Managed Objects groups


# Notification objects

koliConfigServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 3, 1, 0, 1)
)
koliConfigServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliConfigServiceStart.setStatus(
        "current"
    )

koliConfigServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 3, 1, 0, 2)
)
koliConfigServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliConfigServiceStop.setStatus(
        "current"
    )

koliConfigClientConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 3, 1, 0, 3)
)
koliConfigClientConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriClientConnection"),
        ("KOLIBRI-MIB", "kolibriClientAddress"))
)
if mibBuilder.loadTexts:
    koliConfigClientConnected.setStatus(
        "current"
    )

koliConfigClientDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 3, 1, 0, 4)
)
koliConfigClientDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriClientConnection"),
        ("KOLIBRI-MIB", "kolibriClientAddress"))
)
if mibBuilder.loadTexts:
    koliConfigClientDisconnected.setStatus(
        "current"
    )

koliConfigGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 3, 1, 0, 7)
)
koliConfigGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliConfigGenericException.setStatus(
        "current"
    )

koliConfigDBConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 3, 1, 0, 11)
)
koliConfigDBConnected.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliConfigDBConnected.setStatus(
        "current"
    )

koliConfigDBDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 3, 1, 0, 12)
)
koliConfigDBDisconnected.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliConfigDBDisconnected.setStatus(
        "current"
    )

koliConfigSyncConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 3, 1, 0, 13)
)
koliConfigSyncConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriConfigAddress"))
)
if mibBuilder.loadTexts:
    koliConfigSyncConnected.setStatus(
        "current"
    )

koliConfigSyncDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 3, 1, 0, 14)
)
koliConfigSyncDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriConfigAddress"))
)
if mibBuilder.loadTexts:
    koliConfigSyncDisconnected.setStatus(
        "current"
    )


# Notifications groups

koliConfigNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 3, 4)
)
koliConfigNotifications.setObjects(
      *(("KOLIBRI-SERVICE-CONFIG-MIB", "koliConfigServiceStart"),
        ("KOLIBRI-SERVICE-CONFIG-MIB", "koliConfigServiceStop"),
        ("KOLIBRI-SERVICE-CONFIG-MIB", "koliConfigClientConnected"),
        ("KOLIBRI-SERVICE-CONFIG-MIB", "koliConfigClientDisconnected"),
        ("KOLIBRI-SERVICE-CONFIG-MIB", "koliConfigGenericException"),
        ("KOLIBRI-SERVICE-CONFIG-MIB", "koliConfigDBConnected"),
        ("KOLIBRI-SERVICE-CONFIG-MIB", "koliConfigDBDisconnected"),
        ("KOLIBRI-SERVICE-CONFIG-MIB", "koliConfigSyncConnected"),
        ("KOLIBRI-SERVICE-CONFIG-MIB", "koliConfigSyncDisconnected"))
)
if mibBuilder.loadTexts:
    koliConfigNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-SERVICE-CONFIG-MIB",
    **{"koliConfigModule": koliConfigModule,
       "koliConfigTraps": koliConfigTraps,
       "koliConfigTrap": koliConfigTrap,
       "koliConfigServiceStart": koliConfigServiceStart,
       "koliConfigServiceStop": koliConfigServiceStop,
       "koliConfigClientConnected": koliConfigClientConnected,
       "koliConfigClientDisconnected": koliConfigClientDisconnected,
       "koliConfigGenericException": koliConfigGenericException,
       "koliConfigDBConnected": koliConfigDBConnected,
       "koliConfigDBDisconnected": koliConfigDBDisconnected,
       "koliConfigSyncConnected": koliConfigSyncConnected,
       "koliConfigSyncDisconnected": koliConfigSyncDisconnected,
       "koliConfigNotifications": koliConfigNotifications}
)
