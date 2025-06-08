# SNMP MIB module (KOLIBRI-DEPLOY-UPDATESERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/rob/MIBs/kolibri_35317/KOLIBRI-DEPLOY-UPDATESERVER-MIB.mib
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

(koliUpdateServer,
 kolibriInstanceName) = mibBuilder.importSymbols(
    "KOLIBRI-MIB",
    "koliUpdateServer",
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

koliUpdateServerModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 100, 1, 0)
)
if mibBuilder.loadTexts:
    koliUpdateServerModule.setRevisions(
        ("2017-04-19 09:00",
         "2017-04-19 08:00",
         "2015-07-17 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_KoliUpdateServerTraps_ObjectIdentity = ObjectIdentity
koliUpdateServerTraps = _KoliUpdateServerTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 100, 1, 1)
)
_KoliUpdateServerTrap_ObjectIdentity = ObjectIdentity
koliUpdateServerTrap = _KoliUpdateServerTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35317, 1, 100, 1, 1, 0)
)

# Managed Objects groups


# Notification objects

koliUpdateServerServiceStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 100, 1, 1, 0, 1)
)
koliUpdateServerServiceStart.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliUpdateServerServiceStart.setStatus(
        "current"
    )

koliUpdateServerServiceStop = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 100, 1, 1, 0, 2)
)
koliUpdateServerServiceStop.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliUpdateServerServiceStop.setStatus(
        "current"
    )

koliUpdateServerGenericException = NotificationType(
    (1, 3, 6, 1, 4, 1, 35317, 1, 100, 1, 1, 0, 7)
)
koliUpdateServerGenericException.setObjects(
    ("KOLIBRI-MIB", "kolibriInstanceName")
)
if mibBuilder.loadTexts:
    koliUpdateServerGenericException.setStatus(
        "current"
    )


# Notifications groups

koliUpdateServerNotifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 35317, 1, 100, 1, 4)
)
koliUpdateServerNotifications.setObjects(
      *(("KOLIBRI-DEPLOY-UPDATESERVER-MIB", "koliUpdateServerServiceStart"),
        ("KOLIBRI-DEPLOY-UPDATESERVER-MIB", "koliUpdateServerServiceStop"),
        ("KOLIBRI-DEPLOY-UPDATESERVER-MIB", "koliUpdateServerGenericException"))
)
if mibBuilder.loadTexts:
    koliUpdateServerNotifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "KOLIBRI-DEPLOY-UPDATESERVER-MIB",
    **{"koliUpdateServerModule": koliUpdateServerModule,
       "koliUpdateServerTraps": koliUpdateServerTraps,
       "koliUpdateServerTrap": koliUpdateServerTrap,
       "koliUpdateServerServiceStart": koliUpdateServerServiceStart,
       "koliUpdateServerServiceStop": koliUpdateServerServiceStop,
       "koliUpdateServerGenericException": koliUpdateServerGenericException,
       "koliUpdateServerNotifications": koliUpdateServerNotifications}
)
