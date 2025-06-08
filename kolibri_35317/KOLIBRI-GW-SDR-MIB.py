# SNMP MIB module (KOLIBRI-GW-SDR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-GW-SDR-MIB.mib
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

(koliSDR,
 kolibriControlAddress,
 kolibriInstanceName) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliSDR",
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

koliSDRModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 6, 0)
)
if mibBuilder.loadTexts:
    koliSDRModule.setRevisions(
        ("2017-04-19 09:00",
         "2017-04-19 08:00",
         "2015-07-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliSDRTraps_ObjectIdentity = ObjectIdentity
koliSDRTraps = _KoliSDRTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 6, 1)
)
_KoliSDRTrap_ObjectIdentity = ObjectIdentity
koliSDRTrap = _KoliSDRTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 6, 1, 0)
)
_KoliSDRValue_ObjectIdentity = ObjectIdentity
koliSDRValue = _KoliSDRValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 6, 2)
)
_KoliSDRAddress_Type = IpAddress
_KoliSDRAddress_Object = MibScalar
koliSDRAddress = _KoliSDRAddress_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 6, 2, 1),
    _KoliSDRAddress_Type()
)
koliSDRAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    koliSDRAddress.setStatus("current")

# Managed Objects groups

koliSDRObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 6, 3)
)
koliSDRObjects.setObjects(
    ("KOLIBRI-GW-SDR-MIB", "koliSDRAddress")
)
if mibBuilder.loadTexts:
    koliSDRObjects.setStatus("current")


# Notification objects

koliSDRServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 6, 1, 0, 1)
)
koliSDRServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliSDRServiceStart.setStatus(
        "current"
    )

koliSDRServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 6, 1, 0, 2)
)
koliSDRServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliSDRServiceStop.setStatus(
        "current"
    )

koliSDRGatewayConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 6, 1, 0, 5)
)
koliSDRGatewayConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliSDRGatewayConnected.setStatus(
        "current"
    )

koliSDRGatewayDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 6, 1, 0, 6)
)
koliSDRGatewayDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliSDRGatewayDisconnected.setStatus(
        "current"
    )

koliSDRGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 6, 1, 0, 7)
)
koliSDRGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliSDRGenericException.setStatus(
        "current"
    )

koliSDRConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 6, 1, 0, 11)
)
koliSDRConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-GW-SDR-MIB", "koliSDRAddress"))
)
if mibBuilder.loadTexts:
    koliSDRConnected.setStatus(
        "current"
    )

koliSDRDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 6, 1, 0, 12)
)
koliSDRDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-GW-SDR-MIB", "koliSDRAddress"))
)
if mibBuilder.loadTexts:
    koliSDRDisconnected.setStatus(
        "current"
    )


# Notifications groups

koliSDRNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 6, 4)
)
koliSDRNotifications.setObjects(
      *(("KOLIBRI-GW-SDR-MIB", "koliSDRServiceStart"),
        ("KOLIBRI-GW-SDR-MIB", "koliSDRServiceStop"),
        ("KOLIBRI-GW-SDR-MIB", "koliSDRGatewayConnected"),
        ("KOLIBRI-GW-SDR-MIB", "koliSDRGatewayDisconnected"),
        ("KOLIBRI-GW-SDR-MIB", "koliSDRGenericException"),
        ("KOLIBRI-GW-SDR-MIB", "koliSDRConnected"),
        ("KOLIBRI-GW-SDR-MIB", "koliSDRDisconnected"))
)
if mibBuilder.loadTexts:
    koliSDRNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-GW-SDR-MIB",
    **{"koliSDRModule": koliSDRModule,
       "koliSDRTraps": koliSDRTraps,
       "koliSDRTrap": koliSDRTrap,
       "koliSDRServiceStart": koliSDRServiceStart,
       "koliSDRServiceStop": koliSDRServiceStop,
       "koliSDRGatewayConnected": koliSDRGatewayConnected,
       "koliSDRGatewayDisconnected": koliSDRGatewayDisconnected,
       "koliSDRGenericException": koliSDRGenericException,
       "koliSDRConnected": koliSDRConnected,
       "koliSDRDisconnected": koliSDRDisconnected,
       "koliSDRValue": koliSDRValue,
       "koliSDRAddress": koliSDRAddress,
       "koliSDRObjects": koliSDRObjects,
       "koliSDRNotifications": koliSDRNotifications}
)
