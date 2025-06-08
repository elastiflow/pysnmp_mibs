# SNMP MIB module (KOLIBRI-GW-UCGW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-GW-UCGW-MIB.mib
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

(koliUCGW,
 kolibriControlAddress,
 kolibriInstanceName) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliUCGW",
    "kolibriControlAddress",
    "kolibriInstanceName")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

koliUCGWModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 2, 0)
)
if mibBuilder.loadTexts:
    koliUCGWModule.setRevisions(
        ("2017-04-19 09:00",
         "2017-04-19 08:00",
         "2015-07-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliUCGWTraps_ObjectIdentity = ObjectIdentity
koliUCGWTraps = _KoliUCGWTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 2, 1)
)
_KoliUCGWTrap_ObjectIdentity = ObjectIdentity
koliUCGWTrap = _KoliUCGWTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 2, 1, 0)
)
_KoliUCGWValue_ObjectIdentity = ObjectIdentity
koliUCGWValue = _KoliUCGWValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 2, 2)
)
_KoliUCGWAddress_Type = IpAddress
_KoliUCGWAddress_Object = MibScalar
koliUCGWAddress = _KoliUCGWAddress_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 2, 2, 1),
    _KoliUCGWAddress_Type()
)
koliUCGWAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    koliUCGWAddress.setStatus("current")

# Managed Objects groups

koliUCGWObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 2, 3)
)
koliUCGWObjects.setObjects(
    ("KOLIBRI-GW-UCGW-MIB", "koliUCGWAddress")
)
if mibBuilder.loadTexts:
    koliUCGWObjects.setStatus("current")


# Notification objects

koliUCGWServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 2, 1, 0, 1)
)
koliUCGWServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliUCGWServiceStart.setStatus(
        "current"
    )

koliUCGWServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 2, 1, 0, 2)
)
koliUCGWServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliUCGWServiceStop.setStatus(
        "current"
    )

koliUCGWGatewayConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 2, 1, 0, 5)
)
koliUCGWGatewayConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliUCGWGatewayConnected.setStatus(
        "current"
    )

koliUCGWGatewayDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 2, 1, 0, 6)
)
koliUCGWGatewayDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliUCGWGatewayDisconnected.setStatus(
        "current"
    )

koliUCGWGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 2, 1, 0, 7)
)
koliUCGWGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliUCGWGenericException.setStatus(
        "current"
    )

koliUCGWConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 2, 1, 0, 11)
)
koliUCGWConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-GW-UCGW-MIB", "koliUCGWAddress"))
)
if mibBuilder.loadTexts:
    koliUCGWConnected.setStatus(
        "current"
    )

koliUCGWDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 2, 1, 0, 12)
)
koliUCGWDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-GW-UCGW-MIB", "koliUCGWAddress"))
)
if mibBuilder.loadTexts:
    koliUCGWDisconnected.setStatus(
        "current"
    )


# Notifications groups

koliUCGWNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 2, 4)
)
koliUCGWNotifications.setObjects(
      *(("KOLIBRI-GW-UCGW-MIB", "koliUCGWServiceStart"),
        ("KOLIBRI-GW-UCGW-MIB", "koliUCGWServiceStop"),
        ("KOLIBRI-GW-UCGW-MIB", "koliUCGWGatewayConnected"),
        ("KOLIBRI-GW-UCGW-MIB", "koliUCGWGatewayDisconnected"),
        ("KOLIBRI-GW-UCGW-MIB", "koliUCGWGenericException"),
        ("KOLIBRI-GW-UCGW-MIB", "koliUCGWConnected"),
        ("KOLIBRI-GW-UCGW-MIB", "koliUCGWDisconnected"))
)
if mibBuilder.loadTexts:
    koliUCGWNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-GW-UCGW-MIB",
    **{"koliUCGWModule": koliUCGWModule,
       "koliUCGWTraps": koliUCGWTraps,
       "koliUCGWTrap": koliUCGWTrap,
       "koliUCGWServiceStart": koliUCGWServiceStart,
       "koliUCGWServiceStop": koliUCGWServiceStop,
       "koliUCGWGatewayConnected": koliUCGWGatewayConnected,
       "koliUCGWGatewayDisconnected": koliUCGWGatewayDisconnected,
       "koliUCGWGenericException": koliUCGWGenericException,
       "koliUCGWConnected": koliUCGWConnected,
       "koliUCGWDisconnected": koliUCGWDisconnected,
       "koliUCGWValue": koliUCGWValue,
       "koliUCGWAddress": koliUCGWAddress,
       "koliUCGWObjects": koliUCGWObjects,
       "koliUCGWNotifications": koliUCGWNotifications}
)
