# SNMP MIB module (KOLIBRI-SERVICE-VIDEO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-SERVICE-VIDEO-MIB.mib
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

(koliVideo,
 kolibriClientAddress,
 kolibriClientConnection,
 kolibriInstanceName) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliVideo",
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

koliVideoModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 12, 0)
)
if mibBuilder.loadTexts:
    koliVideoModule.setRevisions(
        ("2017-04-19 09:00",
         "2017-04-19 08:00",
         "2017-04-11 15:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliVideoTraps_ObjectIdentity = ObjectIdentity
koliVideoTraps = _KoliVideoTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 12, 1)
)
_KoliVideoTrap_ObjectIdentity = ObjectIdentity
koliVideoTrap = _KoliVideoTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 12, 1, 0)
)

# Managed Objects groups


# Notification objects

koliVideoServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 12, 1, 0, 1)
)
koliVideoServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliVideoServiceStart.setStatus(
        "current"
    )

koliVideoServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 12, 1, 0, 2)
)
koliVideoServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliVideoServiceStop.setStatus(
        "current"
    )

koliVideoClientConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 12, 1, 0, 3)
)
koliVideoClientConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriClientConnection"),
        ("KOLIBRI-MIB", "kolibriClientAddress"))
)
if mibBuilder.loadTexts:
    koliVideoClientConnected.setStatus(
        "current"
    )

koliVideoClientDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 12, 1, 0, 4)
)
koliVideoClientDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriClientConnection"),
        ("KOLIBRI-MIB", "kolibriClientAddress"))
)
if mibBuilder.loadTexts:
    koliVideoClientDisconnected.setStatus(
        "current"
    )

koliVideoGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 12, 1, 0, 7)
)
koliVideoGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliVideoGenericException.setStatus(
        "current"
    )


# Notifications groups

koliVideoNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 12, 4)
)
koliVideoNotifications.setObjects(
      *(("KOLIBRI-SERVICE-VIDEO-MIB", "koliVideoServiceStart"),
        ("KOLIBRI-SERVICE-VIDEO-MIB", "koliVideoServiceStop"),
        ("KOLIBRI-SERVICE-VIDEO-MIB", "koliVideoClientConnected"),
        ("KOLIBRI-SERVICE-VIDEO-MIB", "koliVideoClientDisconnected"),
        ("KOLIBRI-SERVICE-VIDEO-MIB", "koliVideoGenericException"))
)
if mibBuilder.loadTexts:
    koliVideoNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-SERVICE-VIDEO-MIB",
    **{"koliVideoModule": koliVideoModule,
       "koliVideoTraps": koliVideoTraps,
       "koliVideoTrap": koliVideoTrap,
       "koliVideoServiceStart": koliVideoServiceStart,
       "koliVideoServiceStop": koliVideoServiceStop,
       "koliVideoClientConnected": koliVideoClientConnected,
       "koliVideoClientDisconnected": koliVideoClientDisconnected,
       "koliVideoGenericException": koliVideoGenericException,
       "koliVideoNotifications": koliVideoNotifications}
)
