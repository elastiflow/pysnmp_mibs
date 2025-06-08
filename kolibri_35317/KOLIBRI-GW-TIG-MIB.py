# SNMP MIB module (KOLIBRI-GW-TIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-GW-TIG-MIB.mib
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

(koliTIG,
 kolibriControlAddress,
 kolibriInstanceName) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliTIG",
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

koliTIGModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 1, 0)
)
if mibBuilder.loadTexts:
    koliTIGModule.setRevisions(
        ("2017-04-19 09:00",
         "2017-04-19 08:00",
         "2015-07-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliTIGTraps_ObjectIdentity = ObjectIdentity
koliTIGTraps = _KoliTIGTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 1, 1)
)
_KoliTIGTrap_ObjectIdentity = ObjectIdentity
koliTIGTrap = _KoliTIGTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 1, 1, 0)
)
_KoliTIGValue_ObjectIdentity = ObjectIdentity
koliTIGValue = _KoliTIGValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 1, 2)
)
_KoliTIGAddress_Type = IpAddress
_KoliTIGAddress_Object = MibScalar
koliTIGAddress = _KoliTIGAddress_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 1, 2, 1),
    _KoliTIGAddress_Type()
)
koliTIGAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    koliTIGAddress.setStatus("current")

# Managed Objects groups

koliTIGObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 1, 3)
)
koliTIGObjects.setObjects(
    ("KOLIBRI-GW-TIG-MIB", "koliTIGAddress")
)
if mibBuilder.loadTexts:
    koliTIGObjects.setStatus("current")


# Notification objects

koliTIGServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 1, 1, 0, 1)
)
koliTIGServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliTIGServiceStart.setStatus(
        "current"
    )

koliTIGServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 1, 1, 0, 2)
)
koliTIGServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliTIGServiceStop.setStatus(
        "current"
    )

koliTIGGatewayConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 1, 1, 0, 5)
)
koliTIGGatewayConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliTIGGatewayConnected.setStatus(
        "current"
    )

koliTIGGatewayDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 1, 1, 0, 6)
)
koliTIGGatewayDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliTIGGatewayDisconnected.setStatus(
        "current"
    )

koliTIGGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 1, 1, 0, 7)
)
koliTIGGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliTIGGenericException.setStatus(
        "current"
    )

koliTIGConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 1, 1, 0, 11)
)
koliTIGConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-GW-TIG-MIB", "koliTIGAddress"))
)
if mibBuilder.loadTexts:
    koliTIGConnected.setStatus(
        "current"
    )

koliTIGDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 1, 1, 0, 12)
)
koliTIGDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-GW-TIG-MIB", "koliTIGAddress"))
)
if mibBuilder.loadTexts:
    koliTIGDisconnected.setStatus(
        "current"
    )

koliTIGSCLConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 1, 1, 0, 13)
)
koliTIGSCLConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-GW-TIG-MIB", "koliTIGAddress"))
)
if mibBuilder.loadTexts:
    koliTIGSCLConnected.setStatus(
        "current"
    )

koliTIGSCLDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 1, 1, 0, 14)
)
koliTIGSCLDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-GW-TIG-MIB", "koliTIGAddress"))
)
if mibBuilder.loadTexts:
    koliTIGSCLDisconnected.setStatus(
        "current"
    )


# Notifications groups

koliTIGNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 1, 4)
)
koliTIGNotifications.setObjects(
      *(("KOLIBRI-GW-TIG-MIB", "koliTIGServiceStart"),
        ("KOLIBRI-GW-TIG-MIB", "koliTIGServiceStop"),
        ("KOLIBRI-GW-TIG-MIB", "koliTIGGatewayConnected"),
        ("KOLIBRI-GW-TIG-MIB", "koliTIGGatewayDisconnected"),
        ("KOLIBRI-GW-TIG-MIB", "koliTIGGenericException"),
        ("KOLIBRI-GW-TIG-MIB", "koliTIGConnected"),
        ("KOLIBRI-GW-TIG-MIB", "koliTIGDisconnected"),
        ("KOLIBRI-GW-TIG-MIB", "koliTIGSCLConnected"),
        ("KOLIBRI-GW-TIG-MIB", "koliTIGSCLDisconnected"))
)
if mibBuilder.loadTexts:
    koliTIGNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-GW-TIG-MIB",
    **{"koliTIGModule": koliTIGModule,
       "koliTIGTraps": koliTIGTraps,
       "koliTIGTrap": koliTIGTrap,
       "koliTIGServiceStart": koliTIGServiceStart,
       "koliTIGServiceStop": koliTIGServiceStop,
       "koliTIGGatewayConnected": koliTIGGatewayConnected,
       "koliTIGGatewayDisconnected": koliTIGGatewayDisconnected,
       "koliTIGGenericException": koliTIGGenericException,
       "koliTIGConnected": koliTIGConnected,
       "koliTIGDisconnected": koliTIGDisconnected,
       "koliTIGSCLConnected": koliTIGSCLConnected,
       "koliTIGSCLDisconnected": koliTIGSCLDisconnected,
       "koliTIGValue": koliTIGValue,
       "koliTIGAddress": koliTIGAddress,
       "koliTIGObjects": koliTIGObjects,
       "koliTIGNotifications": koliTIGNotifications}
)
