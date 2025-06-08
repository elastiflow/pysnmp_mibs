# SNMP MIB module (KOLIBRI-GW-GPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-GW-GPS-MIB.mib
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

(koliGPS,
 kolibriControlAddress,
 kolibriInstanceName) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliGPS",
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

koliGPSModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 10, 0)
)
if mibBuilder.loadTexts:
    koliGPSModule.setRevisions(
        ("2017-04-19 09:00",
         "2017-04-19 08:00",
         "2015-07-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliGPSTraps_ObjectIdentity = ObjectIdentity
koliGPSTraps = _KoliGPSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 10, 1)
)
_KoliGPSTrap_ObjectIdentity = ObjectIdentity
koliGPSTrap = _KoliGPSTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 10, 1, 0)
)

# Managed Objects groups


# Notification objects

koliGPSServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 10, 1, 0, 1)
)
koliGPSServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliGPSServiceStart.setStatus(
        "current"
    )

koliGPSServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 10, 1, 0, 2)
)
koliGPSServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliGPSServiceStop.setStatus(
        "current"
    )

koliGPSGatewayConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 10, 1, 0, 5)
)
koliGPSGatewayConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliGPSGatewayConnected.setStatus(
        "current"
    )

koliGPSGatewayDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 10, 1, 0, 6)
)
koliGPSGatewayDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliGPSGatewayDisconnected.setStatus(
        "current"
    )

koliGPSGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 10, 1, 0, 7)
)
koliGPSGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliGPSGenericException.setStatus(
        "current"
    )


# Notifications groups

koliGPSNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 10, 4)
)
koliGPSNotifications.setObjects(
      *(("KOLIBRI-GW-GPS-MIB", "koliGPSServiceStart"),
        ("KOLIBRI-GW-GPS-MIB", "koliGPSServiceStop"),
        ("KOLIBRI-GW-GPS-MIB", "koliGPSGatewayConnected"),
        ("KOLIBRI-GW-GPS-MIB", "koliGPSGatewayDisconnected"),
        ("KOLIBRI-GW-GPS-MIB", "koliGPSGenericException"))
)
if mibBuilder.loadTexts:
    koliGPSNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-GW-GPS-MIB",
    **{"koliGPSModule": koliGPSModule,
       "koliGPSTraps": koliGPSTraps,
       "koliGPSTrap": koliGPSTrap,
       "koliGPSServiceStart": koliGPSServiceStart,
       "koliGPSServiceStop": koliGPSServiceStop,
       "koliGPSGatewayConnected": koliGPSGatewayConnected,
       "koliGPSGatewayDisconnected": koliGPSGatewayDisconnected,
       "koliGPSGenericException": koliGPSGenericException,
       "koliGPSNotifications": koliGPSNotifications}
)
