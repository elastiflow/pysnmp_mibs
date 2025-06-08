# SNMP MIB module (KOLIBRI-SERVICE-DAI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-SERVICE-DAI-MIB.mib
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

(koliDAI,
 kolibriClientAddress,
 kolibriClientConnection) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliDAI",
    "kolibriClientAddress",
    "kolibriClientConnection")

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

koliDAIModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 5, 0)
)
if mibBuilder.loadTexts:
    koliDAIModule.setRevisions(
        ("2015-07-17 09:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliDAITraps_ObjectIdentity = ObjectIdentity
koliDAITraps = _KoliDAITraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 5, 1)
)
_KoliDAITrap_ObjectIdentity = ObjectIdentity
koliDAITrap = _KoliDAITrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 5, 1, 0)
)

# Managed Objects groups


# Notification objects

koliDAIServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 5, 1, 0, 1)
)
if mibBuilder.loadTexts:
    koliDAIServiceStart.setStatus(
        "current"
    )

koliDAIServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 5, 1, 0, 2)
)
if mibBuilder.loadTexts:
    koliDAIServiceStop.setStatus(
        "current"
    )

koliDAIClientConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 5, 1, 0, 3)
)
koliDAIClientConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriClientConnection"),
        ("KOLIBRI-MIB", "kolibriClientAddress"))
)
if mibBuilder.loadTexts:
    koliDAIClientConnected.setStatus(
        "current"
    )

koliDAIClientDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 5, 1, 0, 4)
)
koliDAIClientDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriClientConnection"),
        ("KOLIBRI-MIB", "kolibriClientAddress"))
)
if mibBuilder.loadTexts:
    koliDAIClientDisconnected.setStatus(
        "current"
    )

koliDAIDeviceConnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 5, 1, 0, 11)
)
if mibBuilder.loadTexts:
    koliDAIDeviceConnect.setStatus(
        "current"
    )

koliDAIDeviceDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 5, 1, 0, 12)
)
if mibBuilder.loadTexts:
    koliDAIDeviceDisconnect.setStatus(
        "current"
    )


# Notifications groups

koliDAINotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 2, 5, 4)
)
koliDAINotifications.setObjects(
      *(("KOLIBRI-SERVICE-DAI-MIB", "koliDAIServiceStart"),
        ("KOLIBRI-SERVICE-DAI-MIB", "koliDAIServiceStop"),
        ("KOLIBRI-SERVICE-DAI-MIB", "koliDAIClientConnected"),
        ("KOLIBRI-SERVICE-DAI-MIB", "koliDAIClientDisconnected"),
        ("KOLIBRI-SERVICE-DAI-MIB", "koliDAIDeviceConnect"),
        ("KOLIBRI-SERVICE-DAI-MIB", "koliDAIDeviceDisconnect"))
)
if mibBuilder.loadTexts:
    koliDAINotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-SERVICE-DAI-MIB",
    **{"koliDAIModule": koliDAIModule,
       "koliDAITraps": koliDAITraps,
       "koliDAITrap": koliDAITrap,
       "koliDAIServiceStart": koliDAIServiceStart,
       "koliDAIServiceStop": koliDAIServiceStop,
       "koliDAIClientConnected": koliDAIClientConnected,
       "koliDAIClientDisconnected": koliDAIClientDisconnected,
       "koliDAIDeviceConnect": koliDAIDeviceConnect,
       "koliDAIDeviceDisconnect": koliDAIDeviceDisconnect,
       "koliDAINotifications": koliDAINotifications}
)
