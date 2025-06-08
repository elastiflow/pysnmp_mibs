# SNMP MIB module (KOLIBRI-GW-XML-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-GW-XML-MIB.mib
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

(koliXML,
 kolibriControlAddress,
 kolibriInstanceName) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliXML",
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

koliXMLModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 11, 0)
)
if mibBuilder.loadTexts:
    koliXMLModule.setRevisions(
        ("2017-04-19 09:00",
         "2017-04-19 08:00",
         "2015-07-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliXMLTraps_ObjectIdentity = ObjectIdentity
koliXMLTraps = _KoliXMLTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 11, 1)
)
_KoliXMLTrap_ObjectIdentity = ObjectIdentity
koliXMLTrap = _KoliXMLTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 11, 1, 0)
)

# Managed Objects groups


# Notification objects

koliXMLServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 11, 1, 0, 1)
)
koliXMLServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliXMLServiceStart.setStatus(
        "current"
    )

koliXMLServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 11, 1, 0, 2)
)
koliXMLServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliXMLServiceStop.setStatus(
        "current"
    )

koliXMLGatewayConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 11, 1, 0, 5)
)
koliXMLGatewayConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliXMLGatewayConnected.setStatus(
        "current"
    )

koliXMLGatewayDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 11, 1, 0, 6)
)
koliXMLGatewayDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliXMLGatewayDisconnected.setStatus(
        "current"
    )

koliXMLGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 11, 1, 0, 7)
)
koliXMLGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliXMLGenericException.setStatus(
        "current"
    )


# Notifications groups

koliXMLNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 11, 4)
)
koliXMLNotifications.setObjects(
      *(("KOLIBRI-GW-XML-MIB", "koliXMLServiceStart"),
        ("KOLIBRI-GW-XML-MIB", "koliXMLServiceStop"),
        ("KOLIBRI-GW-XML-MIB", "koliXMLGatewayConnected"),
        ("KOLIBRI-GW-XML-MIB", "koliXMLGatewayDisconnected"),
        ("KOLIBRI-GW-XML-MIB", "koliXMLGenericException"))
)
if mibBuilder.loadTexts:
    koliXMLNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-GW-XML-MIB",
    **{"koliXMLModule": koliXMLModule,
       "koliXMLTraps": koliXMLTraps,
       "koliXMLTrap": koliXMLTrap,
       "koliXMLServiceStart": koliXMLServiceStart,
       "koliXMLServiceStop": koliXMLServiceStop,
       "koliXMLGatewayConnected": koliXMLGatewayConnected,
       "koliXMLGatewayDisconnected": koliXMLGatewayDisconnected,
       "koliXMLGenericException": koliXMLGenericException,
       "koliXMLNotifications": koliXMLNotifications}
)
