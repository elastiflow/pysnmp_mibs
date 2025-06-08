# SNMP MIB module (KOLIBRI-GW-JTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-GW-JTS-MIB.mib
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

(koliJTS,
 kolibriControlAddress,
 kolibriInstanceName) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliJTS",
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

koliJTSModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 9, 0)
)
if mibBuilder.loadTexts:
    koliJTSModule.setRevisions(
        ("2017-04-19 09:00",
         "2017-04-19 08:00",
         "2015-07-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliJTSTraps_ObjectIdentity = ObjectIdentity
koliJTSTraps = _KoliJTSTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 9, 1)
)
_KoliJTSTrap_ObjectIdentity = ObjectIdentity
koliJTSTrap = _KoliJTSTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 9, 1, 0)
)

# Managed Objects groups


# Notification objects

koliJTSServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 9, 1, 0, 1)
)
koliJTSServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliJTSServiceStart.setStatus(
        "current"
    )

koliJTSServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 9, 1, 0, 2)
)
koliJTSServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliJTSServiceStop.setStatus(
        "current"
    )

koliJTSGatewayConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 9, 1, 0, 5)
)
koliJTSGatewayConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliJTSGatewayConnected.setStatus(
        "current"
    )

koliJTSGatewayDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 9, 1, 0, 6)
)
koliJTSGatewayDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliJTSGatewayDisconnected.setStatus(
        "current"
    )

koliJTSGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 9, 1, 0, 7)
)
koliJTSGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliJTSGenericException.setStatus(
        "current"
    )


# Notifications groups

koliJTSNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 9, 4)
)
koliJTSNotifications.setObjects(
      *(("KOLIBRI-GW-JTS-MIB", "koliJTSServiceStart"),
        ("KOLIBRI-GW-JTS-MIB", "koliJTSServiceStop"),
        ("KOLIBRI-GW-JTS-MIB", "koliJTSGatewayConnected"),
        ("KOLIBRI-GW-JTS-MIB", "koliJTSGatewayDisconnected"),
        ("KOLIBRI-GW-JTS-MIB", "koliJTSGenericException"))
)
if mibBuilder.loadTexts:
    koliJTSNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-GW-JTS-MIB",
    **{"koliJTSModule": koliJTSModule,
       "koliJTSTraps": koliJTSTraps,
       "koliJTSTrap": koliJTSTrap,
       "koliJTSServiceStart": koliJTSServiceStart,
       "koliJTSServiceStop": koliJTSServiceStop,
       "koliJTSGatewayConnected": koliJTSGatewayConnected,
       "koliJTSGatewayDisconnected": koliJTSGatewayDisconnected,
       "koliJTSGenericException": koliJTSGenericException,
       "koliJTSNotifications": koliJTSNotifications}
)
