# SNMP MIB module (KOLIBRI-GW-CADI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-GW-CADI-MIB.mib
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

(koliCADI,
 kolibriControlAddress,
 kolibriInstanceName) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliCADI",
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

koliCADIModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 5, 0)
)
if mibBuilder.loadTexts:
    koliCADIModule.setRevisions(
        ("2017-04-19 09:00",
         "2017-04-19 08:00",
         "2015-07-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliCADITraps_ObjectIdentity = ObjectIdentity
koliCADITraps = _KoliCADITraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 5, 1)
)
_KoliCADITrap_ObjectIdentity = ObjectIdentity
koliCADITrap = _KoliCADITrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 5, 1, 0)
)
_KoliCADIValue_ObjectIdentity = ObjectIdentity
koliCADIValue = _KoliCADIValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 5, 2)
)
_KoliCADIAddress_Type = IpAddress
_KoliCADIAddress_Object = MibScalar
koliCADIAddress = _KoliCADIAddress_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 5, 2, 1),
    _KoliCADIAddress_Type()
)
koliCADIAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    koliCADIAddress.setStatus("current")

# Managed Objects groups

koliCADIObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 5, 3)
)
koliCADIObjects.setObjects(
    ("KOLIBRI-GW-CADI-MIB", "koliCADIAddress")
)
if mibBuilder.loadTexts:
    koliCADIObjects.setStatus("current")


# Notification objects

koliCADIServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 5, 1, 0, 1)
)
koliCADIServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliCADIServiceStart.setStatus(
        "current"
    )

koliCADIServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 5, 1, 0, 2)
)
koliCADIServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliCADIServiceStop.setStatus(
        "current"
    )

koliCADIGatewayConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 5, 1, 0, 5)
)
koliCADIGatewayConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliCADIGatewayConnected.setStatus(
        "current"
    )

koliCADIGatewayDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 5, 1, 0, 6)
)
koliCADIGatewayDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliCADIGatewayDisconnected.setStatus(
        "current"
    )

koliCADIGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 5, 1, 0, 7)
)
koliCADIGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliCADIGenericException.setStatus(
        "current"
    )

koliCADIConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 5, 1, 0, 11)
)
koliCADIConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-GW-CADI-MIB", "koliCADIAddress"))
)
if mibBuilder.loadTexts:
    koliCADIConnected.setStatus(
        "current"
    )

koliCADIDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 5, 1, 0, 12)
)
koliCADIDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-GW-CADI-MIB", "koliCADIAddress"))
)
if mibBuilder.loadTexts:
    koliCADIDisconnected.setStatus(
        "current"
    )


# Notifications groups

koliCADINotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 5, 4)
)
koliCADINotifications.setObjects(
      *(("KOLIBRI-GW-CADI-MIB", "koliCADIServiceStart"),
        ("KOLIBRI-GW-CADI-MIB", "koliCADIServiceStop"),
        ("KOLIBRI-GW-CADI-MIB", "koliCADIGatewayConnected"),
        ("KOLIBRI-GW-CADI-MIB", "koliCADIGatewayDisconnected"),
        ("KOLIBRI-GW-CADI-MIB", "koliCADIGenericException"),
        ("KOLIBRI-GW-CADI-MIB", "koliCADIConnected"),
        ("KOLIBRI-GW-CADI-MIB", "koliCADIDisconnected"))
)
if mibBuilder.loadTexts:
    koliCADINotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-GW-CADI-MIB",
    **{"koliCADIModule": koliCADIModule,
       "koliCADITraps": koliCADITraps,
       "koliCADITrap": koliCADITrap,
       "koliCADIServiceStart": koliCADIServiceStart,
       "koliCADIServiceStop": koliCADIServiceStop,
       "koliCADIGatewayConnected": koliCADIGatewayConnected,
       "koliCADIGatewayDisconnected": koliCADIGatewayDisconnected,
       "koliCADIGenericException": koliCADIGenericException,
       "koliCADIConnected": koliCADIConnected,
       "koliCADIDisconnected": koliCADIDisconnected,
       "koliCADIValue": koliCADIValue,
       "koliCADIAddress": koliCADIAddress,
       "koliCADIObjects": koliCADIObjects,
       "koliCADINotifications": koliCADINotifications}
)
