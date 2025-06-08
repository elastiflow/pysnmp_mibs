# SNMP MIB module (KOLIBRI-GW-WEB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-GW-WEB-MIB.mib
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

(koliWeb,
 kolibriControlAddress,
 kolibriInstanceName) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliWeb",
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

koliWebModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 3, 0)
)
if mibBuilder.loadTexts:
    koliWebModule.setRevisions(
        ("2017-04-19 09:00",
         "2017-04-19 08:00",
         "2015-07-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliWebTraps_ObjectIdentity = ObjectIdentity
koliWebTraps = _KoliWebTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 3, 1)
)
_KoliWebTrap_ObjectIdentity = ObjectIdentity
koliWebTrap = _KoliWebTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 3, 1, 0)
)
_KoliWebValue_ObjectIdentity = ObjectIdentity
koliWebValue = _KoliWebValue_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 3, 2)
)
_KoliWebRequestAddress_Type = IpAddress
_KoliWebRequestAddress_Object = MibScalar
koliWebRequestAddress = _KoliWebRequestAddress_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 3, 2, 1),
    _KoliWebRequestAddress_Type()
)
koliWebRequestAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    koliWebRequestAddress.setStatus("current")


class _KoliWebRequestPort_Type(Integer32):
    """Custom type koliWebRequestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_KoliWebRequestPort_Type.__name__ = "Integer32"
_KoliWebRequestPort_Object = MibScalar
koliWebRequestPort = _KoliWebRequestPort_Object(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 3, 2, 2),
    _KoliWebRequestPort_Type()
)
koliWebRequestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    koliWebRequestPort.setStatus("current")

# Managed Objects groups

koliWebObjects = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 3, 3)
)
koliWebObjects.setObjects(
      *(("KOLIBRI-GW-WEB-MIB", "koliWebRequestAddress"),
        ("KOLIBRI-GW-WEB-MIB", "koliWebRequestPort"))
)
if mibBuilder.loadTexts:
    koliWebObjects.setStatus("current")


# Notification objects

koliWebServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 3, 1, 0, 1)
)
koliWebServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliWebServiceStart.setStatus(
        "current"
    )

koliWebServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 3, 1, 0, 2)
)
koliWebServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliWebServiceStop.setStatus(
        "current"
    )

koliWebGatewayConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 3, 1, 0, 5)
)
koliWebGatewayConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliWebGatewayConnected.setStatus(
        "current"
    )

koliWebGatewayDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 3, 1, 0, 6)
)
koliWebGatewayDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliWebGatewayDisconnected.setStatus(
        "current"
    )

koliWebGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 3, 1, 0, 7)
)
koliWebGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliWebGenericException.setStatus(
        "current"
    )

koliWebConnectFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 3, 1, 0, 11)
)
koliWebConnectFail.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-GW-WEB-MIB", "koliWebRequestAddress"),
        ("KOLIBRI-GW-WEB-MIB", "koliWebRequestPort"))
)
if mibBuilder.loadTexts:
    koliWebConnectFail.setStatus(
        "current"
    )

koliWebRequestFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 3, 1, 0, 13)
)
koliWebRequestFail.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-GW-WEB-MIB", "koliWebRequestAddress"),
        ("KOLIBRI-GW-WEB-MIB", "koliWebRequestPort"))
)
if mibBuilder.loadTexts:
    koliWebRequestFail.setStatus(
        "current"
    )


# Notifications groups

koliWebNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 3, 4)
)
koliWebNotifications.setObjects(
      *(("KOLIBRI-GW-WEB-MIB", "koliWebServiceStart"),
        ("KOLIBRI-GW-WEB-MIB", "koliWebServiceStop"),
        ("KOLIBRI-GW-WEB-MIB", "koliWebGatewayConnected"),
        ("KOLIBRI-GW-WEB-MIB", "koliWebGatewayDisconnected"),
        ("KOLIBRI-GW-WEB-MIB", "koliWebGenericException"),
        ("KOLIBRI-GW-WEB-MIB", "koliWebConnectFail"),
        ("KOLIBRI-GW-WEB-MIB", "koliWebRequestFail"))
)
if mibBuilder.loadTexts:
    koliWebNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-GW-WEB-MIB",
    **{"koliWebModule": koliWebModule,
       "koliWebTraps": koliWebTraps,
       "koliWebTrap": koliWebTrap,
       "koliWebServiceStart": koliWebServiceStart,
       "koliWebServiceStop": koliWebServiceStop,
       "koliWebGatewayConnected": koliWebGatewayConnected,
       "koliWebGatewayDisconnected": koliWebGatewayDisconnected,
       "koliWebGenericException": koliWebGenericException,
       "koliWebConnectFail": koliWebConnectFail,
       "koliWebRequestFail": koliWebRequestFail,
       "koliWebValue": koliWebValue,
       "koliWebRequestAddress": koliWebRequestAddress,
       "koliWebRequestPort": koliWebRequestPort,
       "koliWebObjects": koliWebObjects,
       "koliWebNotifications": koliWebNotifications}
)
