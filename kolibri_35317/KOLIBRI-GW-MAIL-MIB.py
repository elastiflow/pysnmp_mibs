# SNMP MIB module (KOLIBRI-GW-MAIL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-GW-MAIL-MIB.mib
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

(koliMail,
 kolibriControlAddress,
 kolibriInstanceName) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliMail",
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

koliMailModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 13, 0)
)
if mibBuilder.loadTexts:
    koliMailModule.setRevisions(
        ("2017-04-19 09:00",
         "2017-04-19 08:00",
         "2015-07-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliMailTraps_ObjectIdentity = ObjectIdentity
koliMailTraps = _KoliMailTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 13, 1)
)
_KoliMailTrap_ObjectIdentity = ObjectIdentity
koliMailTrap = _KoliMailTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 13, 1, 0)
)

# Managed Objects groups


# Notification objects

koliMailServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 13, 1, 0, 1)
)
koliMailServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliMailServiceStart.setStatus(
        "current"
    )

koliMailServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 13, 1, 0, 2)
)
koliMailServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliMailServiceStop.setStatus(
        "current"
    )

koliMailGatewayConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 13, 1, 0, 5)
)
koliMailGatewayConnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliMailGatewayConnected.setStatus(
        "current"
    )

koliMailGatewayDisconnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 13, 1, 0, 6)
)
koliMailGatewayDisconnected.setObjects(
      *(("KOLIBRI-MIB", "kolibriInstanceName"),
        ("KOLIBRI-MIB", "kolibriControlAddress"))
)
if mibBuilder.loadTexts:
    koliMailGatewayDisconnected.setStatus(
        "current"
    )

koliMailGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 13, 1, 0, 7)
)
koliMailGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliMailGenericException.setStatus(
        "current"
    )


# Notifications groups

koliMailNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 3, 13, 4)
)
koliMailNotifications.setObjects(
      *(("KOLIBRI-GW-MAIL-MIB", "koliMailServiceStart"),
        ("KOLIBRI-GW-MAIL-MIB", "koliMailServiceStop"),
        ("KOLIBRI-GW-MAIL-MIB", "koliMailGatewayConnected"),
        ("KOLIBRI-GW-MAIL-MIB", "koliMailGatewayDisconnected"),
        ("KOLIBRI-GW-MAIL-MIB", "koliMailGenericException"))
)
if mibBuilder.loadTexts:
    koliMailNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-GW-MAIL-MIB",
    **{"koliMailModule": koliMailModule,
       "koliMailTraps": koliMailTraps,
       "koliMailTrap": koliMailTrap,
       "koliMailServiceStart": koliMailServiceStart,
       "koliMailServiceStop": koliMailServiceStop,
       "koliMailGatewayConnected": koliMailGatewayConnected,
       "koliMailGatewayDisconnected": koliMailGatewayDisconnected,
       "koliMailGenericException": koliMailGenericException,
       "koliMailNotifications": koliMailNotifications}
)
